from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    for x in elements:
        if elements.count(x) != len(elements):
            return False
    return True


def is_password_strong(data: str) -> bool:
    if len(data) >= 10:
        upper = digit = lower = False
        for x in data:
            if x.isupper():
                upper = True
            elif x.islower():
                lower = True
            elif x.isdigit():
                digit = True
        if upper and lower and digit:
            return True
    return False


def frequentest_letter(text: str) -> str:
    result = {}
    lower_text = text.lower()
    for x in lower_text:
        if x.isalpha():
            result[x] = lower_text.count(x)
    result = sorted(result.items(), key=lambda x:( -x[1], x[0]))
    print(result)
    return result[0][0]


def time_converter(time):
    day_time = " p.m."
    hours = time[0] + time[1]
    if int(hours) < 12:
        day_time = " a.m."
        if int(hours) == 00:
            hours = 12
    elif int(hours) == 12:
        pass
    else:
        hours = int(hours) - 12
    hours = str(hours)
    if int(hours) < 10 and day_time == " a.m.":
        hours = hours[1]
    return hours + ":" + time[3] + time[4] + day_time


def non_unique_elements(data: list) -> list:
    result = []
    for x in data:
        if data.count(x) > 1:
            result.append(x)
    return result


def sort_array_by_element_frequency(items):
    frequency_count = {}
    result = []
    for x in items:
        frequency_count[x] = items.count(x)
    frequency_count = sorted(frequency_count.items(), key=lambda x: -x[1])
    for x in frequency_count:
        for y in range(x[1]):
            result.append(x[0])
    return result


def flat_list(array):
    result = []
    for x in array:
        if isinstance(x, list):
            result += flat_list(x)
        else:
            result.append(x)
    return result


def long_repeat(line):
    if line == "":
        return 0
    count = maximum = 1
    current = ""
    for x in line:
        if x == current:
            count += 1
        else:
            count = 1
            current = x
        maximum = max(count, maximum)
    return maximum


def sun_angle(time):
    minutes = int(time[:2]) * 60 + int(time[3:])
    if minutes < 360 or minutes > 1080:
        return "I don't see the sun!"
    return (minutes - 360) / 4


# The bird converts words by two rules:
# - after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
# - after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
def translate(phrase):
    vowels = "aeiouy"
    result = ""
    x = 0
    while x < len(phrase):
        if vowels.find(phrase[x]) != -1:
            result += phrase[x]
            x += 3
        elif phrase[x] == " ":
            result += phrase[x]
            x += 1
        else:
            result += phrase[x]
            x += 2
    return result


# You are given a set of square coordinates where we have placed white pawns.
# You should count how many pawns are safe.
def safe_pawns(pawns: set) -> int:
    rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    columns = [1, 2, 3, 4, 5, 6, 7, 8]
    counter = 0
    for x in pawns:
        if int(x[1]) == 1:
            continue
        if x[0] == "h":
            position1 = "empty"
        else:
            position1 = rows[rows.index(x[0]) + 1] + str(columns[columns.index(int(x[1])) - 1])
        if x[0] == "a":
            position2 = "empty"
        else:
            position2 = rows[rows.index(x[0]) - 1] + str(columns[columns.index(int(x[1])) - 1])
        if position1 in pawns or position2 in pawns:
            counter += 1
    return counter


def tic_tac_toe(field: List[str]) -> str:
    rotated_filed = list(zip(*field))
    for line in rotated_filed:
        if line[0] != "." and line[0] == line[1] == line[2]:
            return line[0]
    for line in field:
        if line[0] != "." and line[0] == line[1] == line[2]:
            return line[0]
    if (field[0][0] == field[1][1] == field[2][2] != ".") or (field[0][2] == field[1][1] == field[2][0] != "."):
        return field[1][1]
    else:
        return "D"


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True


class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.attack = 7


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health = unit_2.health - unit_1.attack
        unit_1.health = unit_1.health - unit_2.attack
        if unit_2.health <= 0:
            unit_2.is_alive = False
            return True
        if unit_1.health <= 0:
            unit_1.is_alive = False
            return False