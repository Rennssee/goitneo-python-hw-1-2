from datetime import datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    # Отримання поточної дати
    today = datetime.today().date()
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        # Конвертація дати народження
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        # Оцінка дати на цей рік
        if birthday_this_year < today:
            # Змінити на наступний рік
            birthday_this_year = birthday.replace(year=today.year + 1)

        # Порівняння з поточною датою
        delta_days = (birthday_this_year - today).days

        # Визначення дня тижня та зберігання результату
        if delta_days < 7:
            weekday_num = birthday_this_year.weekday()
            # Якщо день народження в суботу або неділю
            if weekday_num == 5 or weekday_num == 6:
                weekday = "Monday"
            else:
                weekday = birthday_this_year.strftime("%A")
            birthdays[weekday].append(name)

    # Виведення результату
    for weekday, names in birthdays.items():
        print(f"{weekday}: {', '.join(names)}")


# Тест
users = [
    {"name": "Vadym Rymar", "birthday": datetime(1996, 10, 28)},
    {"name": "Martha Sereda", "birthday": datetime(1955, 4, 5)},
    {"name": "Mike Peres", "birthday": datetime(2005, 10, 21)},
    {"name": "Mike RESS", "birthday": datetime(2005, 10, 22)},
]
get_birthdays_per_week(users)
