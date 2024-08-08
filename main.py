import os
import subprocess
from datetime import datetime, timedelta

# Настройка
repository_path = 'my-github-drawing-repo'  # Путь к репозиторию
start_date = datetime(2022, 1, 1)  # Дата начала, от которой будем отсчитывать
width, height = 53, 7  # Размер сетки активности (GitHub показывает 53 недели по 7 дней)

# Текст для отображения на графике активности
drawing = [
    "  ###   ###   #   #   ###   ##### ",
    " #   # #   #  ##  #  #   #  #     ",
    "##### #####  # # #  #   #  ####  ",
    "#   # #   #  #  ##  #   #  #     ",
    "#   # #   #  #   #   ###   ##### "
]

# Функция, которая создает коммит с заданной датой
def make_commit(date):
    with open(os.path.join(repository_path, 'README.md'), 'a') as file:
        file.write(f'Commit on {date.isoformat()}\n')
    subprocess.run(['git', 'add', '.'], cwd=repository_path)
    subprocess.run(['git', 'commit', '--date', date.isoformat(), '-m', f'Commit on {date}'], cwd=repository_path)

# Создание пустого репозитория
os.makedirs(repository_path, exist_ok=True)
subprocess.run(['git', 'init'], cwd=repository_path)

# Создание коммитов для каждого символа в тексте
for y in range(len(drawing)):
    for x in range(len(drawing[y])):
        if drawing[y][x] == '#':
            commit_date = start_date + timedelta(weeks=x, days=y)
            make_commit(commit_date)

# Завершение
print("Коммиты завершены. Теперь отправьте изменения в ваш репозиторий на GitHub.")
