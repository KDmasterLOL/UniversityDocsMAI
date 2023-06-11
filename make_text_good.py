# скоростью \vec v
import pyperclip
import re

mark_list = re.compile(
    "(^\(?(([a-zA-Zа-яА-Я]{1})|([\d]+)))[.)]|(^[^a-zA-Zа-яА-Я\n\d()]{1})"
)
types_list = {3: "numbered", 4: "lettered", 5: "dashed"}


def is_marker_of_list(str):
    res = mark_list.match(str)
    return res != None
    groups = res.groups()

    return any([type_list in groups for type_list in types_list])


(
    none,
    is_equation,
    add_dollar_sign,
    equation_started,
    equation_ended,
    is_breaked_word,
) = [0 << i for i in range(6)]
regexes = {
    "equation": (re.compile("[a-zA-Z=]"), is_equation),
    "part_equation": (re.compile("[-+=0-9&]"), is_equation),
    "breaked_word": (re.compile("[а-яА-Я]*-$"), is_breaked_word),
}
MAX_LEN_HEADER = 6
result = []
flags = none
text = pyperclip.paste()
text.replace("\xa0", " ")
paragraphs = text.split("\n")

index_definition_word = 0


def add_flag(flag):
    flags = flags | flag


def get_flag(flag):
    return (flags & flag) != 0


def reset_flag(flag):
    flags = flags & (~flag)


def hang_flags(word):
    reset_flag(add_dollar_sign | equation_ended)

    if regexes["equation"].match(word):
        if not get_flag(equation_started) and word[0] != '$':
            add_flag(add_dollar_sign)
        add_flag(equation_started)
    elif get_flag(equation_started):
        reset_flag(equation_started)
        add_flag(equation_ended)
        
    # for r, flag in regexes.values():
    #     if r.match(word) != None:
    #         flags = flags | flag


for paragraph in paragraphs:
    if paragraph.isspace():
        continue

    res = []

    words = paragraph.split(" ")
    for idx, word in enumerate(words):
        if word.isspace():
            continue
        hang_flags(word)
        if get_flag(equation_started):
            word = "$" + word

        if word[0] == "$":
            is_equation = 0
        elif word[-1] == "$":
            is_equation = -1
        elif is_equation == -1 and regex_is_equation.search(word) != None:
            is_equation = 1
            word = "$" + word
        elif is_equation == 1:
            if len(words) == idx + 1:
                word = word + "$"
                is_equation = -1
            if regex_is_part_equation.search(word) == None:
                print(res)
                last_word = res[-1]
                if last_word[-1] in [",", "."]:
                    res[-1] = last_word[:-1] + "$" + last_word[-1]
                else:
                    res[-1] = last_word + "$"
                is_equation = -1

        res.append(word)
    result.append(" ".join(res))
print(result)
pyperclip.copy(("\n".join(result)).replace("\xa0", " "))
