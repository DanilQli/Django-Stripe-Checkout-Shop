# 💳 Django + Stripe Checkout Shop

Простой проект магазина на Django с интеграцией Stripe Checkout, поддержкой заказов, скидок, налогов и мультивалютности.

---

## 📦 Функциональность

- Модель `Item` с полями: `name`, `description`, `price`, `currency`
- API:
  - `GET /item/<id>/` — страница товара с кнопкой "Buy"
  - `GET /buy/<id>/` — создаёт Stripe Checkout Session и редиректит на оплату
  - `GET /order/<id>/` — страница заказа с несколькими товарами
- Модель `Order` с несколькими товарами
- Модель `Discount` (скидка в %)
- Модель `Tax` (налог в %)
- Django Admin для управления моделями
- Поддержка Docker
---

## 🚀 Как запустить локально

### 1. Установка

```bash
git clone https://github.com/DanilQli/django-stripe-shop.git
```

### 2. Создать файл .env в корне проекта
Этот файл будет содержать все секретные ключи и настройки.

⚠️ Никогда не добавляй его в GitHub!

📄 Пример .env файла:
```
SECRET_KEY=django-insecure-замени-на-свой
DEBUG=True

STRIPE_SECRET_KEY_USD=sk_test_ваш_ключ
STRIPE_PUBLISHABLE_KEY_USD=pk_test_ваш_ключ

STRIPE_SECRET_KEY_EUR=sk_test_евро_ключ
STRIPE_PUBLISHABLE_KEY_EUR=pk_test_евро_ключ

DEFAULT_CURRENCY=usd
```

### 3. Создание БД и суперпользователя
```
python manage.py migrate
python manage.py createsuperuser
```
### 4. Запуск сервера
```
python manage.py runserver
```
🌐 Интерфейсы

http://127.0.0.1:8000/item/1/ — покупка товара
http://127.0.0.1:8000/order/1/ — покупка заказа
http://127.0.0.1:8000/admin — админка

🐳 Альтернатива: Docker
```
docker-compose up --build
```

🔐 Безопасность ключей
- Все ключи и секреты вынесены в .env
- Используется библиотека python-decouple для безопасного доступа
- .env добавлен в .gitignore (не попадает в Git)

📡 Демо
- 🛒 Товар: https://yourusername.pythonanywhere.com/item/1
- 📦 Заказ: https://yourusername.pythonanywhere.com/order/1
- 🔐 Admin: https://yourusername.pythonanywhere.com/admin
- - Логин: danil
- - Пароль: 111

🧠 Бонусные фичи
- ✅ Order с несколькими товарами
- ✅ Скидки (Discount)
- ✅ Налоги (Tax)
- ✅ Валюты: USD и EUR
- ✅ Stripe Checkout
- ✅ Docker
- ✅ Админка
- ✅ Поддержка PaymentIntent (опционально)

🧾 Примеры API

GET /item/1
- Возвращает страницу товара с кнопкой "Buy"

GET /buy/1
- Возвращает Stripe Session и редиректит на оплату