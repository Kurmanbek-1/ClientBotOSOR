FROM python:3.10

# Создаем директории и копируем файлы
RUN mkdir -p /opt/osor_client_bot
WORKDIR /opt/osor_client_bot

COPY . /opt/osor_client_bot/

# Создаем отдельную директорию для зависимостей
RUN mkdir -p /opt/osor_client_bot/requirements
COPY requirements.txt /opt/osor_client_bot/requirements/

# Устанавливаем aiogram и другие зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем DNS-серверы
# RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf
# RUN echo "nameserver 8.8.4.4" >> /etc/resolv.conf

# Команда для запуска приложения
# CMD ["python", "/opt/osor_client_bot/main.py"]


