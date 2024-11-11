# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:3.12.7
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1
# Устанавливает рабочий каталог контейнера — "app"
WORKDIR /app
# Копирует все файлы из нашего локального проекта в контейнер
ADD firenze app/
ADD .env app/
ADD requirements.txt app/
# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
RUN pip install -r app/requirements.txt