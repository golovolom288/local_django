# Пульт охраны банка
- Данный проект позволяет следить за посетителями банка и продолжительностью их посещений

## Как установить
- В проекте есть 8 переменных окружения: 
```
ENGINE, HOST, PORT, NAME, USER, PASSWORD, SECRET_KEY, DEBUG
```
Каждая из них является настройкой для запуска сайта:
- ENGINE определяет тип базы данных.
- HOST определяет адрес хоста сервера где будет запущен сайт
- PORT определяет порт подключения пользователей на сайт
- NAME определяет имя базы данных
- USER ник пользователя базой данных
- PASSWORD пароль пользователя базой данных
- SECRET_KEY определяет секретный ключ сайта
- DEBUG режим отладки


Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

- pip install -r requirements.txt

После чего вы сможете запустить сайт с помощью команды.
```
python manage.py runserver 0.0.0.0:8000
```
### Цель проекта
- Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.[README.md](..%2F..%2Fspace_images%2FREADME.md)[README.md](..%2F..%2Fspace_images%2FREADME.md)