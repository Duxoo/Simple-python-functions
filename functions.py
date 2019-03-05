def fizz_buzz(number: int) -> str:
    if number % 3 == 0 and number % 3 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


# adds comma in the end of the sentence
def correct_sentence(text: str) -> str:
    if text[-1] == ".":
        return text[0].upper() + text[1:]
    else:
        return text[0].upper() + text[1:] + "."


def first_word(text: str) -> str:
    result = ""
    text = text.replace(".", " ").replace(",", " ").lstrip()
    for i in text:
        if i == " ":
            break
        result += i
    return result


# returns a tuple with 3 elements - first, third and second to the last
def easy_unpack(elements: tuple) -> tuple:
    return elements[0], elements[2], elements[-2]


# returns the second index of a symbol in a given text
def second_index(text: str, symbol: str) -> [int, None]:
    try:
        return text.index(symbol, text.index(symbol) + 1)
    except ValueError:
        return None


# returns substring between two given markers
def between_markers(text: str, begin: str, end: str) -> str:
    returning_text = ""
    if text.find(begin) != -1:
        start_index = text.find(begin) + len(begin)
    else:
        start_index = 0
    if text.find(end) != -1:
        end_index = text.find(end)
    else:
        end_index = len(text)
    if start_index > end_index:
        return ""
    while start_index != end_index:
        returning_text += text[start_index]
        start_index += 1
    return returning_text


def difference_min_max(*args):
    if args:
        return max(args) - min(args)
    return 0


# Find Nth power of the element with index N.
def index_power(array: list, n: int) -> int:
    if n < len(array):
        return array[n] ** n
    return -1


# sums even-indexes elements and multiply at the last
def even_indexes_and_multiply_the_last(array):
    sum = 0
    if len(array) == 0:
        return 0
    for x in range(len(array)):
        if x % 2 == 0:
            sum += array[x]
    sum *= array[-1]
    return sum


# sort by abs
def sort_by_abs(numbers_array: tuple) -> list:
    return sorted(numbers_array, key=abs)


# Find a secret message
def find_message(text: str) -> str:
    result = ""
    for x in text:
        if x.isupper():
            result += x
    return result


# Join strings and replace "right" to "left"
def left_join(phrases):
    return ",".join(phrases).replace("right", "left")


# three words in a row
def words_row(words: str) -> bool:
    count = 0
    for x in words.split():
        if x.isalpha():
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False


# multiple all digits in number
def digits_multiple(number: int) -> int:
    result = 1
    for x in str(number):
        if x == '0':
            continue
        result *= int(x)
    return result


# data - dict like {'example' : 100, ...}
def best_stock(data):
    price = 0
    stock_name = ""
    for x in data:
        if data[x] > price:
            price = data[x]
            stock_name = x
    return stock_name


# return dict with words and count of them in text
def popular_words(text: str, words: list) -> dict:
    text = text.lower()
    result = {}
    splited_text = text.split()
    for x in words:
        result[x] = splited_text.count(x)
    return result


# TOP most expensive goods params limit of selection, list of dicts
def bigger_price(limit: int, data: list) -> list:
    return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]
