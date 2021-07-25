# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:3.9
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1
# Устанавливает рабочий каталог контейнера — "for_sibdev"
WORKDIR /for_sibdev
# Копирует все файлы из нашего локального проекта в контейнер
ADD . /for_sibdev
# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
RUN pip install -r requirements.txt