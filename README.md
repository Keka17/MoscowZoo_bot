# Telegram-бот "Тотемный компас" для Московского Зоопарка #

Бот «Тотемный компас» предназначен для пользователей Telegram, которые хотят определить своё тотемное животное, а также узнать больше о программе __«Клуб друзей»__ Московского зоопарка.

**Функции**:
* Проведение викторины для определения тотемного животного
* Предоставление информации о "Клубе друзей" Московского зоопарка
* Возможность поделиться результатом викторины
* Обратная связь через _Google Forms_


**Технологии**:
* _Python 3.10+_
* _Aiogram_ (_Telegram Bot API_)
* _FSM_ (_Finite State Machine_): для управления состояниями пользователей
* _python-dotenv_:для хранения токена


**Команды бота**:
* `/start, /help` - запуск бота и объяснение его работы
* `/quiz` - начать викторину по определению тотемного животного
* `/restart` - перезапуск викторины
* `/info` - получить информацию о "Клубе друзей" и Московском зоопарке
* `/share` - поделиться результатом викторины
* `/feedback` - оставить отзыв через Google Forms


**Установка и запуск**:

1. Откройте терминал и выполните команду:

   ```bash
   git clone https://github.com/Keka17/MoscowZoo_bot.git
   
   cd MoscowZoo_bot
   ```
2. Создание виртуального окружения:
   
   ```bash
   
   python -m venv venv\
   
   source venv/bin/activate   # Для Linux и macOS\
   
   venv\Scripts\activate   # Для Windows
   ```
3. Установите зависимости:
   
   ```bash
   pip install -r requirements.txt
   ```
4. Настройка переменных окружения:
   
     Создайте файл `.env`, добавив в него токен бота (`TOKEN=your_token`), который необходимо предварительно получить через __@BotFather__.

5. Запуск бота:
   
   ```bash
   python main.py
   ```

## Запуск через Docker

1. Клонирование репозитория
   
   ```bash
   git clone https://github.com/Keka17/MoscowZoo_bot.git
   cd MoscowZoo_bot
   ```
2. Настройка переменных окружения
   
   Создайте файл `.env`, добавив в него токен бота (`TOKEN=your_token`), , который необходимо предварительно получить через __@BotFather__.

3. Сборка контейнера
   
   ```bash
   docker build -t totem-bot .
   ```

4. Запуск контейнера

   ```bash
   docker run -d --name totem-bot --restart unless-stopped --env-file .env totem-bot
   ```
   
## Демонстрация работы бота


https://github.com/user-attachments/assets/bbecbd3f-5e07-47ff-878b-3c56ec35f0d5


