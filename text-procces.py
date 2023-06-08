import pyperclip
import re


def make_definition(words, idx) -> str:
    name_part = "\tspan.name " + " ".join(words[0:idx])
    meaning_part = "\tspan.meaning " + " ".join(words[(idx + 1) :])
    return "\n".join([".definition", name_part, meaning_part])


mark_list = re.compile(
    "(^\(?(([a-zA-Zа-яА-Я]{1})|([\d]+)))[.)]|(^[^a-zA-Zа-яА-Я\n\d()]{1})"
)
types_list = {3: "numbered", 4: "lettered", 5: "dashed"}


def is_marker_of_list(str):
    res = mark_list.match(str)
    return res != None
    groups = res.groups()

    return any([type_list in groups for type_list in types_list])


MAX_LEN_HEADER = 6
result = []
text = pyperclip.paste()
paragraphs = text.split("\n")

for paragraph in paragraphs:
    words = paragraph.split(" ")
    res = []
    is_definition = -1
    if is_marker_of_list(words[0]):
        del words[0]
        res.append("li")
    if len(words) < MAX_LEN_HEADER and words[-1][-1] != ".":
        res = "h1 " + paragraph
    else:
        for idx, word in enumerate(words):
            if word in ["-", "—", "—","–"]:
                is_definition = idx
                break
        if is_definition != -1:
            res.append(make_definition(words.copy(), is_definition))
        else:
            res.append(" ".join(words))
        if is_definition == -1:
            res.insert(0,'p')
    if isinstance(res, list):
        res = " ".join(res)
    result.append(res)
# print(result)
pyperclip.copy("\n".join(result))
