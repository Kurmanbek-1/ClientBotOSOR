# Используем официальный образ Python
FROM python:3.10

# Устанавливаем зависимости
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем файлы в контейнер
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Запускаем бота
CMD ["python", "main.py"]
