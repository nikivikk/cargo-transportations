# cargo-transportations
Инструкция по запуску приложения:

1) Запустить docker desktop

2) docker compose up --build

3) Открыть второй терминал и запустить следующие команды:

4) docker exec -it cargo_transportations_app flask db init

5) docker exec -it cargo_transportations_app flask db migrate

6) docker exec -it cargo_transportations_app flask db upgrade

7) Перейти по первой ссылке в первом терминале

Примеры работы приложения:

1) получить все заказы: http://127.0.0.1:4000/api/v1/orders
2) получить заказ по id: http://127.0.0.1:4000/api/v1/orders/1
3) добавить новый заказ: http://127.0.0.1:4000/api/v1/orders
4) обновить заказ по id: http://127.0.0.1:4000/api/v1/orders/2
5) удалить заказ по id: http://127.0.0.1:4000/api/v1/orders/3
6) пункты 1-5 можно применить и по отношению к водителю, 
заменив orders на drivers
7) получить всех свободных водителей:http://127.0.0.1:4000/api/v1/drivers?free=true
8) получить все завершенные заказы:http://127.0.0.1:4000/api/v1/orders-status?status=завершен
9) получить все завершенные заказы за определенный период времени: http://127.0.0.1:4000/api/v1/orders-status?status=завершен&start-date=2023-10-12&end-date=2023-10-25
10) обновить статус заказа: http://127.0.0.1:4000/api/v1/orders-status/2
11) получить статус заказа: http://127.0.0.1:4000/api/v1/orders-status/2
12) назначить заказ по id водителю: http://127.0.0.1:4000/api/v1/appoint-order/1
13) отчет по выполненным заказам за определенный период времени: http://127.0.0.1:4000/api/v1/make-report?status=завершен&start-date=2023-10-12&end-date=2023-10-25
  
