# Используем легковесный образ Python
FROM python:3.10-slim

# Рабочая директория
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходники
COPY . .

# Запуск приложения
CMD ["flask", "run", "--host=0.0.0.0"]
