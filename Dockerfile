FROM python:3.11-slim

WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения
COPY ./app ./app

# Открываем порт
EXPOSE 8000

# Команда запуска (обязательно с --host 0.0.0.0)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]