## Cоздание  [docker image](./dz-1) с http сервером nginx.
1. Запустить терминал из папки с [Dockerfile](./dz-1).
2. Создать image образ c именем "my_nginx", используя команду:```docker build -t my_nginx .```
3. Создать докер контейнер с именем "world" и заменить страницу приветствия nginx, используя мэппинг томов: ```docker run --name world -p 80:80 -v ${PWD}:/usr/share/nginx/html my_nginx```.

## Создание [контейнера](./dz-2) REST API сервера.
1. Запустить терминал из папки с [Dockerfile](./dz-2).
2. Создать image образ c именем "rest_api", используя команду:```docker build -t rest_api .``` .
3. Создать докер контейнер с именем "CRUD" используя команду: ```docker run --name CRUD -d -p  8080:8080 rest_api```
4. Для проверки в браузере используйте [адрес localhost c портом 8080](http://localhost:8080/admin/login/?next=/admin/) 

