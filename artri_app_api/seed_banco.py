import csv
import os
from datetime import timedelta

import django

# Configura o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'artri_app_api.settings')
django.setup()

from django.utils import timezone

from src.models import DailyPainReport, Exercise, Training, TrainingExercise, User

# Mapeamento para todas as possíveis variações que você pode digitar na planilha
DIFFICULTY_MAP = {
    'FÁCIL': 'Easy', 'FACIL': 'Easy', 'INICIANTE': 'Easy',
    'MÉDIO': 'Medium', 'MEDIO': 'Medium', 'INTERMEDIÁRIO': 'Medium', 'INTERMEDIARIO': 'Medium',
    'DIFÍCIL': 'Hard', 'DIFICIL': 'Hard', 'AVANÇADO': 'Hard', 'AVANCADO': 'Hard'
}

# Mapeia a última parte do nome do Treino (ex.: "EXERCÍCIO PERSONALIDADO - INICIANTE - PERNAS")
# para a category usada no fluxo de exercícios personalizados.
CATEGORY_MAP = {
    'AQUECIMENTO': 'warmup',
    'BRAÇOS': 'arms', 'BRACOS': 'arms',
    'PERNAS': 'legs',
    'TRONCO': 'trunk',
    'ALONGAMENTO': 'stretching',
}


def derive_category(treino_name, ex_name):
    """Retorna a category do exercício personalizado, ou None para os treinos
    pré-determinados (Mãos/Pés/relaxamento). A MOBILIDADE, que no CSV é uma
    categoria única, é dividida em perna/braços/tronco pelo nome do exercício."""
    treino = treino_name.upper()
    if 'PERSONAL' not in treino:
        return None

    part = treino.split(' - ')[-1].strip()
    if part in CATEGORY_MAP:
        return CATEGORY_MAP[part]

    if part == 'MOBILIDADE':
        name = ex_name.lower()
        if 'tronco' in name or 'gato' in name:
            return 'mobility_trunk'
        if 'braço' in name or 'ombro' in name or 'punho' in name:
            return 'mobility_arms'
        return 'mobility_legs'

    return None


def reset_and_seed(csv_path):
    print("⚠️  ATENÇÃO: Apagando todos os Treinos e Exercícios antigos do banco...")
    Training.objects.all().delete()
    Exercise.objects.all().delete()
    # O TrainingExercise é apagado automaticamente pelo Django (efeito Cascata)
    print("✅ Banco limpo com sucesso!\n")

    print(f"📖 Lendo o arquivo {csv_path} e recriando os dados...")

    # Dicionário para controlar a ordem dos exercícios dentro de cada treino
    training_order = {}
    exercicios_processados = 0

    with open(csv_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        # Limpa os cabeçalhos para evitar erros com espaços invisíveis
        reader.fieldnames = [str(field).strip() for field in reader.fieldnames if field]

        for row in reader:
            clean_row = {str(k).strip(): str(v).strip() for k, v in row.items() if k is not None}

            ex_name = clean_row.get('Nome do exercício')
            if not ex_name:
                continue  # Pula linhas vazias

            sets = clean_row.get('Séries e Repetições', '')
            rest = clean_row.get('Descanso', '')
            obs = clean_row.get('Instruções/Observações', '')
            link = clean_row.get('Link do vídeo', '')
            diff_pt = clean_row.get('Dificuldade', 'Fácil').upper()
            treino_name = clean_row.get('Treino', 'Treino Geral')

            # Limpa links incorretos copiados do Excel
            if 'Mesmo' in link or 'Mesmo' in obs:
                link = ''

            db_diff = DIFFICULTY_MAP.get(diff_pt, 'Easy')
            category = derive_category(treino_name, ex_name)

            # 1. Cria o Exercício (usamos get_or_create para não duplicar no banco
            # caso o mesmo exercício exato seja usado em treinos diferentes).
            # A category entra na chave para que um exercício personalizado não
            # se funda com um exercício de Mãos/Pés de mesmo nome/dificuldade.
            exercise, _ = Exercise.objects.get_or_create(
                name=ex_name,
                difficulty=db_diff,
                category=category,
                defaults={
                    'sets_reps': sets,
                    'rest_time': rest,
                    'description': obs,
                    'tutorial_link': link
                }
            )
            exercicios_processados += 1

            # 2. Cria ou pega o Treino
            training, _ = Training.objects.get_or_create(
                name=treino_name,
                defaults={
                    'difficulty': db_diff,
                    'description': f'Exercícios focados em: {treino_name.title()}'
                }
            )

            # 3. Inicializa o contador de ordem para este treino (se for a primeira vez)
            if treino_name not in training_order:
                training_order[treino_name] = 0

            # 4. Vincula o Exercício ao Treino mantendo a ordem exata da planilha (0, 1, 2...)
            TrainingExercise.objects.create(
                training=training,
                exercise=exercise,
                order=training_order[treino_name]
            )

            training_order[treino_name] += 1

    print("\n🎉 Sucesso! Processo concluído.")
    print(f"🏋️  Total de exercícios mapeados: {exercicios_processados}")
    print(f"📋 Treinos criados ({len(training_order)}):")
    for t_name, count in training_order.items():
        print(f"   - {t_name}: {count} exercícios vinculados ordenadamente.")


def seed_daily_pain_reports(username):
    user = User.objects.get(username=username)

    print(f"\n🩹 Recriando histórico de dor de exemplo para '{username}'...")
    DailyPainReport.objects.filter(user=user).delete()

    sample_entries = [
        (6, 'Joelho', 6),
        (5, 'Ombro', 4),
        (4, 'Coluna', 7),
        (3, 'Joelho', 5),
        (2, 'Tornozelo', 3),
        (1, 'Ombro', 6),
        (0, 'Coluna', 8),
    ]

    now = timezone.now()
    for days_ago, location, level in sample_entries:
        moment = now - timedelta(days=days_ago)
        report = DailyPainReport.objects.create(
            user=user,
            date=moment.date(),
            pain_level=level,
            pain_location=location,
        )
        DailyPainReport.objects.filter(pk=report.pk).update(created_at=moment)

    print(f"✅ {len(sample_entries)} registros de dor criados para '{username}'.")


if __name__ == '__main__':
    # Coloque o nome exato do seu arquivo CSV atual
    reset_and_seed('Exercícios ArtriApp - Exercícios ArtriApp - Exercícios.csv')
    seed_daily_pain_reports('taichi1')
