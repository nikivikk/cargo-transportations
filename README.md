# cargo-transportations
Инструкция по запуску приложения:

1)Запустить docker desktop

2)docker compose up --build

3)docker compose up -d
   
4)docker exec -it cargo_transportations_app flask db init

5)docker exec -it cargo_transportations_app flask db migrate

6)docker exec -it cargo_transportations_app flask db upgrade

7)docker compose up --build --force-recreate

8)Перейти по первой ссылке
