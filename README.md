# DjangoStripePayment
# Доступ к платежной системе Stripe с использованием Django 

## Задание
### Реализовать Django + Stripe API бэкенд  
### со следующим функционалом и условиями:  
- Django Модель Item с полями (name, description, price)   
- API с двумя методами:  
1. GET /buy/{id}, c помощью которого можно получить Stripe Session Id для  
оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python  
библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...)  
и полученный session.id выдаваться в результате запроса.  
2. GET /item/{id}, c помощью которого можно получить простейшую HTML страницу,  
на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку  
Buy должен происходить запрос на /buy/{id}, получение session_id и далее с  
помощью JS библиотеки Stripe происходить редирект на Checkout форму 
stripe.redirectToCheckout(sessionId=session_id).

Пример реализации можно посмотреть в пунктах 1-3 по ссылке:  
``
https://stripe.com/docs/payments/accept-a-payment?integration=checkout
``

Залить решение на Github, описать запуск в Readme.md.  
Опубликовать свое решение онлайн, предоставив ссылку на решение и доступ к  
админке, чтобы его можно было быстро и легко протестировать. 

### Бонусные задачи: 
- Запуск используя Docker.
- Использование environment variables.
- Просмотр Django Моделей в Django Admin панели.
- Запуск приложения на удаленном сервере, доступном для тестирования, с  
кредами от админки.
- Модель Order, в которой можно объединить несколько Item и сделать платёж в  
Stripe на содержимое Order c общей стоимостью всех Items.
- Модели Discount, Tax, которые можно прикрепить к модели Order и связать с  
соответствующими атрибутами при создании платежа в Stripe - в таком случае они  
корректно отображаются в Stripe Checkout форме. 
- Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и  
в зависимости от валюты выбранного товара предлагать оплату в соответствующей 
валюте.
- Реализовать не Stripe Session, а Stripe Payment Intent.

## Пример

API метод для получения HTML c кнопкой на платежную форму от Stripe для Item с  
id=1: 
``
curl -X GET http://localhost:8000/item/1
``
Результат - HTML c инфой и кнопкой:
``
<html>
  <head>
    <title>Buy Item 1</title>
  </head>
  <body>
    <h1>Item 1</h1>
    <p>Description of Item 1</p>
    <p>1111</p>
    <button id="buy-button">Buy</button>
    <script type="text/javascript">
      var stripe = Stripe('pk_test_a9nwZVa5O7b0xz3lxl318KSU00x1L9ZWsF');
      var buyButton = document.getElementById(buy-button');
      buyButton.addEventListener('click', function() {
        // Create a new Checkout Session using the server-side endpoint 
        // Redirect to Stripe Session Checkout
        fetch('/buy/1', {method: 'GET'})
        .then(response => return response.json())
        .then(session => stripe.redirectToCheckout({ sessionId: session.id }))
      });
    </script>
  </body>
</html>
``

## Стек используемых технологий

 - **Python 3.12+**
 - **Django 5.2+** (включая Django ORM для работы с базой данных)
 - **Django Rest Framework 3.15.2** (для API)
 - **HTML/CSS/JavaScript** (для базового пользовательского интерфейса)
 - **Bootstrap 5** (для стилизации)
 - **SQLite/PostgreSQL** (для хранения данных)
 - **pytils** (Для корректного формирования slug из кириллицы)

## Развертывание проекта.
1. Склонировать репозиторий:
   ```bash
   git clone https://github.com/BalDim1971/DjangoStripePayment.git
   ```
2. Перейти в скачанный каталог:
   ```bash
   cd DjangoStripePayment
   ```
3. Создать виртуальное окружение (при необходимости):
   Для Mac/Linux:
   ```bash
   python3 -m virtual-env -p python3 venv
   source venv/bin/activate
   ```
   Для Windows:
   ```bash
   python3 -m venv venv
   .\venv\Scripts\activate
   ```
4. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```
5. Скопировать файл .env.sample как .env.
6. Для создания DJANGO_SECRET_KEY необходимо: находясь в каталоге 
DjangoStripePayment выполнить следующие действия:
   ```bash
   python manage.py shell
   ```
   Далее в интерактивной консоли выполнить последовательно:
   ```
   from django.core.management import utils
   utils.get_random_secret_key()
   ```
7. Полученный ключ скопировать и вставить в файл .env:
   ```python
   DJANGO_SECRET_KEY='тут_сгенерированный_ключ'
   ```
8. Зарегистрироваться на сайте платежной системы Stripe. Получить публичный и
секретный ключи. Скопировать полученные ключи в файл .env:
   ```python
   STRIPE_PUBLIC='публичный_ключ'
   STRIPE_SECRET='секретный_ключ'
   ```
   Дополнительно, есть параметр STRIPE_URL, содержащий адрес и порт сервера.
По умолчанию, http://localhost:8000
9. Создать и выполнить миграции:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
10. Создать суперпользователя:
   ```bash
   python manage.py createsuperuser
   ```
11. Запустить сервер приложения:
   ```bash
   python manage.py runserver
   ```
