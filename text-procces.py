import pyperclip
import re


def make_definition(words, idx) -> str:
    name_part = "\tdt " + " ".join(words[0:idx])
    meaning_part = "\tdd " + " ".join(words[(idx + 1) :])
    return "\n".join(["dl", name_part, meaning_part])


mark_list = re.compile(
    "(^\(?(([a-zA-Zа-яА-Я]{1})|([\d]+)))[.)]|(^[^a-zA-Zа-яА-Я\n\d()]{1})"
)
types_list = {3: "numbered", 4: "lettered", 5: "dashed"}


def is_marker_of_list(str):
    res = mark_list.match(str)
    return res != None
    groups = res.groups()

    return any([type_list in groups for type_list in types_list])


def hung_flags(string, idx=None):
    global flags
    global definition_index
    if idx == None:
        reset_flag(DEFINITION | SEVERAL_DOTS | HEADER)
        if len(string.split(" ")) <= MAX_LEN_HEADER and string[-1] != ".":
            add_flag(HEADER)
    elif len(string) != 0:
        if string[-1] == ".":
            add_flag(SEVERAL_DOTS)
        if string in ["-", "—", "—", "–"] and not get_flag(SEVERAL_DOTS):
            add_flag(DEFINITION)
            definition_index = idx


def add_flag(flag):
    global flags

    flags = flags | flag


def get_flag(flag):
    global flags

    return (flags & flag) != 0


def reset_flag(flag):
    global flags

    flags = flags & (~flag)


MAX_LEN_HEADER = 6
NONE = 0
(DEFINITION, HEADER, SEVERAL_DOTS) = [1 << i for i in range(3)]
definition_index = 0
regexes = {}
flags = NONE
result = []
text = pyperclip.paste()
paragraphs = text.split("\n")

for paragraph in paragraphs:
    words = paragraph.split(" ")
    res = []
    hung_flags(paragraph)
    # if is_marker_of_list(words[0]):
    #     del words[0]
    #     res.append("li")
    if get_flag(HEADER):
        res = "h1 " + paragraph
    else:
        for idx, word in enumerate(words):
            hung_flags(word, idx)
        if get_flag(DEFINITION):
            res.append(make_definition(words.copy(), definition_index))
        else:
            res.insert(0, "p")
            res.append(" ".join(words))
    if isinstance(res, list):
        res = " ".join(res)
    result.append(res)
print(result)
pyperclip.copy("\n".join(result))
