from aiogram import Router, Bot
from aiogram import types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import (
    FSMContext,
)  # Для отслеживания вопроса, на который отвечает пользователь
from aiogram.fsm.state import State, StatesGroup

from questions import questions

import animals_info
from animals_info import animal_info
from animals_info import animal_images

router = Router()

# Глобальные переменные
animals = animals_info.animals
current_question_index = 0


# Обработчики команд
@router.message(Command("start", "help"))
async def start(msg: Message):
    text = """ Тотемный компас: твой путь к <b>“Клубу друзей”</b>!
Как это работает?\n
<b>Отвечай на вопросы:</b>
1) Выбери ответ, который лучше всего тебе подходит.
2) Не бойся быть честным с собой, ведь твой внутренний зверь ждет, чтобы раскрыться!
<b>Узнай свое тотемное животное:</b>
По результатам викторины ты получишь животное, которое символизирует тебя.
Узнай больше о программе <b>“Клуб друзей” Московского зоопарка</b>, которая позволит тебе:
1) Стать ближе к животным зоопарка.
2) Поддержать зоопарк в заботе о его обитателях.\n
Расскажи своим друзьям о своем тотемном животном и пригласи их пройти викторину!
Делись своими впечатлениями о “Клубе друзей” и зоопарке в социальных сетях!

Начать викторину ➡️ /quiz
    """
    await msg.answer(text, parse_mode="HTML")


@router.message(Command("info"))
async def info(msg: Message, bot: Bot):
    text = """
Основная задача Московского зоопарка с самого начала его существования — сохранение биоразнообразия планеты. 
Когда вы берете под опеку животное, вы помогаете нам в этом благородном деле. 
При нынешних темпах развития цивилизации к 2050 году с лица Земли могут исчезнуть около 10 000 биологических видов. 
Московский зоопарк вместе с другими зоопарками мира делает все возможное, чтобы сохранить их.
В настоящее время опекуны объединились в неформальное сообщество — Клуб друзей Московского зоопарка. 
Программа «Клуб друзей» дает возможность опекунам ощутить свою причастность к делу сохранения природы, 
участвовать в жизни Московского зоопарка и его обитателей, видеть конкретные результаты своей деятельности.\n
Для связи с зоопарком вы можете написать на [zoofriends@moscowzoo.ru](mailto:zoofriends@moscowzoo.ru) 
или позвонить по номеру [+7 (962) 971-38-75](tel:+79629713875)\n
Узнать больше: https://moscowzoo.ru/about/guardianship
    """
    await bot.send_message(msg.chat.id, text=text, parse_mode="Markdown")


@router.message(Command("share"))
async def share_result(msg: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    if "animals" in data:
        result = max(data["animals"], key=data["animals"].get)
        image_url = animal_images.get(result)
        await bot.send_photo(
            msg.chat.id,
            image_url,
            caption="Поделись изображением в социальных сетях - "
            'помоги большему количеству людей узнать о "Клубе друзей" 😉',
        )


# Самый простой способ обратной связи - гугл формы
@router.message(Command("feedback"))
async def get_feedback(msg: Message, bot: Bot):
    form_url = "https://forms.gle/PWUfpSAYvnpTmPYYA"
    text = f"Чтобы оставить отзыв, перейдите по ссылке:\n{form_url}"
    await bot.send_message(msg.chat.id, text)


@router.message(Command("restart"))
async def restart(msg: Message, state: FSMContext, bot: Bot):
    await state.clear()
    await quiz(msg, state, bot)


class QuizState(StatesGroup):
    waiting_for_answer = State()


# Логика викторины
@router.message(Command("quiz"))
async def quiz(msg: Message, state: FSMContext, bot: Bot):
    await state.update_data(
        current_question_index=0, animals={animal: 0 for animal in animals.keys()}
    )
    await send_question(msg.chat.id, state, bot)


async def send_question(chat_id: int, state: FSMContext, bot: Bot):
    data = (
        await state.get_data()
    )  # Словарь, содержащий все сохраненные данные состояния для конкретного пользователя
    current_question_index = data["current_question_index"]
    if current_question_index < len(questions):
        question = questions[current_question_index]
        keyboard_buttons = [
            [types.KeyboardButton(text=option)] for option in question["options"]
        ]
        markup = types.ReplyKeyboardMarkup(
            keyboard=keyboard_buttons, resize_keyboard=True, one_time_keyboard=True
        )
        await bot.send_message(chat_id, question["question"], reply_markup=markup)
        await state.set_state(QuizState.waiting_for_answer)
    else:
        await show_result(chat_id, state, bot)


@router.message(QuizState.waiting_for_answer)
async def handle_answer(msg: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    current_question_index = data["current_question_index"]
    selected_option = msg.text
    question = questions[current_question_index]
    for animal in question["animal_mapping"][selected_option]:
        data["animals"][animal] += 1
    await state.update_data(
        current_question_index=current_question_index + 1, animals=data["animals"]
    )
    await send_question(msg.chat.id, state, bot)


async def show_result(chat_id: int, state: FSMContext, bot: Bot):
    data = await state.get_data()
    result = max(data["animals"], key=data["animals"].get)
    await bot.send_message(
        chat_id, f"Твое тотемное животное - <b>{result}</b>! 🎉", parse_mode="HTML"
    )
    await animal_info(bot, chat_id, result)  # Передаем bot как аргумент
    text = (
        "Пройти викторину заново ➡️ /restart\n"
        'Узнать информацию о "Клубе друзей" ➡️ /info\n'
        "Поделиться результатом ➡️ /share\n"
        "Обратная связь ➡️ /feedback"
    )
    await bot.send_message(chat_id, text)
