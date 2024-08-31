
questions = [
    {
        'question': 'Как бы вы себя описали?',
        'options': ['Мудрый', 'Грациозный', 'Индивидуальный', 'Добрый', 'Нелюдимый красавчик', 'Общительный'],
        'animal_mapping': {
            'Мудрый': ['Южноафриканский жираф'], 'Грациозный': ['Снежный барс'], 'Индивидуальный': ['Морж'],
            'Добрый': ['Двугорбый верблюд'], 'Нелюдимый красавчик': ['Мохноногий сыч'], 'Общительный': ['Папуанский пингвин']
        }
    },
    {
        'question': 'Вы предпочитаете одиночество или компанию единомышленников?',
        'options': ['Одиночество', 'Компания'],
        'animal_mapping': {
            'Одиночество': ['Снежный барс', 'Мохноногий сыч'],
            'Компания': ['Южноафриканский жираф', 'Морж', 'Двугорбый верблюд', 'Папуанский пингвин']
        }
    },
    {
        'question': 'Вы предпочитаете отдых на море или на суше?',
        'options': ['На море', 'На суше'],
        'animal_mapping': {
            'На море': ['Морж', 'Папуанский пингвин'],
            'На суше': ['Снежный барс', 'Мохноногий сыч', 'Южноафриканский жираф', 'Двугорбый верблюд']
        }
    },
    {
        'question': 'Как бы вы предпочли провести свой выходной?',
        'options': ['Поход в музей', 'Сеанс медитации', 'Концерт любимой группы',
                    'Бассейн и спа-процедуры', 'Собрание экоактивистов', 'Спортзал'],
        'animal_mapping': {
            'Поход в музей': ['Южноафриканский жираф'], 'Сеанс медитации': ['Двугорбый верблюд'],
            'Концерт любимой группы': ['Мохноногий сыч'], 'Бассейн и спа-процедуры': ['Морж'],
            'Собрание экоактивистов': ['Папуанский пингвин'], 'Спортзал': ['Снежный барс']
        }
    },
    {
        'question': 'В какое время суток вы ощущаете себя наиболее продуктивным?',
        'options': ['День', 'Ночь'],
        'animal_mapping': {
            'День': ['Южноафриканский жираф', 'Морж', 'Двугорбый верблюд', 'Папуанский пингвин'],
            'Ночь': ['Снежный барс', 'Мохноногий сыч']
        }
    },
    {
        'question': 'Представьте себя животным. Какой способ передвижения вы бы выбрали?',
        'options': ['Летать', 'Плавать', 'Ходить'],
        'animal_mapping': {
            'Летать': ['Мохноногий сыч'],
            'Плавать': ['Морж', 'Папуанский пингвин'],
            'Ходить': ['Южноафриканский жираф', 'Двугорбый верблюд', 'Снежный барс']
        }
    },
    {
        'question': 'Какой климат для вас комфортнее?',
        'options': ['Жаркий', 'Умеренный', 'Холодный'],
        'animal_mapping': {
            'Жаркий': ['Южноафриканский жираф', 'Двугорбый верблюд'],
            'Умеренный': ['Мохноногий сыч'],
            'Холодный': ['Морж', 'Папуанский пингвин', 'Снежный барс']
        }
    },
    {
        'question': 'Прийдя в ресторан, вы скорее закажете:',
        'options': ['Средиземноморский салат из свежих овощей', 'Сочное каре ягненка', 'Стейк лосося, запеченный с помидорами черри'],
        'animal_mapping': {
            'Средиземноморский салат из свежих овощей': ['Южноафриканский жираф', 'Двугорбый верблюд'],
            'Сочное каре ягненка': ['Мохноногий сыч',   'Снежный барс'],
            'Стейк лосося, запеченный с помидорами черри': ['Морж', 'Папуанский пингвин', ]
        }
    },
    {
        'question': ' Выберете цитату, олицетворяющую вас:',
        'options': ['Единственное, что мешает мне учиться, — это полученное мной образование.',
                    'Я не против побыть один. Я просто не хочу быть частью толпы.',
                    'Самый важный вид свободы — быть тем, кто ты есть на самом деле.',
                    'Прекраснейшая музыка души — это доброта.',
                    'Красота в глазах смотрящего.',
                    'Ничего не принимайте близко к сердцу. Немногое на свете  долго бывает важным.'],
        'animal_mapping': {
            'Единственное, что мешает мне учиться, — это полученное мной образование.': ['Южноафриканский жираф'],
            'Я не против побыть один. Я просто не хочу быть частью толпы.': ['Снежный барс'],
            'Самый важный вид свободы — быть тем, кто ты есть на самом деле.': ['Морж'],
            'Прекраснейшая музыка души — это доброта.': ['Двугорбый верблюд'],
            'Красота в глазах смотрящего.': ['Мохноногий сыч'],
            'Ничего не принимайте близко к сердцу. Немногое на свете  долго бывает важным.': ['Папуанский пингвин']
        }
    },
    {
        'question': 'Какой жанр чаще всего играет у вас в наушниках?',
        'options': ['Инди', 'Классика', 'Джаз', 'Блюз', 'Поп-музыка', 'Рок'],
        'animal_mapping': {
            'Инди': ['Южноафриканский жираф'], 'Классика': ['Снежный барс'], 'Джаз': ['Морж'],
            'Блюз': ['Двугорбый верблюд'], 'Поп-музыка': ['Мохноногий сыч'], 'Рок': ['Папуанский пингвин']
        }
    }
]
