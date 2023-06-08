# скоростью \vec v
import pyperclip
import re

mark_list = re.compile(
    "(^\(?(([a-zA-Zа-яА-Я]{1})|([\d]+)))[.)]|(^[^a-zA-Zа-яА-Я\n\d()]{1})"
)
types_list = {3: "numbered", 4: "lettered", 5: "dashed"}
regex_is_equation = re.compile("[a-zA-Z=]")
regex_is_part_equation = re.compile("[-+=0-9&]")
regex_is_empty_line = re.compile("^\s*$")

def is_marker_of_list(str):
    res = mark_list.match(str)
    return res != None
    groups = res.groups()

    return any([type_list in groups for type_list in types_list])


MAX_LEN_HEADER = 6
result = []
text = pyperclip.paste()
paragraphs = text.split("\n")

is_equation = -1
for paragraph in paragraphs:
    words = paragraph.split(" ")
    res = []
    is_definition = -1
    if is_equation == 1:
        is_equation = -1
    if regex_is_empty_line.match(paragraph) != None:
        continue
    for idx, word in enumerate(words):
        if regex_is_empty_line.match(word) != None:
            continue
        # print(words)
        print(word)
        if word[0] == "$":
            is_equation = 0
        elif word[-1] == "$":
            is_equation = -1
        elif is_equation == -1 and regex_is_equation.search(word) != None:
            is_equation = 1
            word = "$" + word
        elif is_equation == 1:
            if len(words) == idx+1:
                word = word+'$'
                is_equation = -1
            if regex_is_part_equation.search(word) == None:
                print(res)
                last_word = res[-1]
                if last_word[-1] in [',','.']:
                    res[-1] = last_word[:-1]+'$'+last_word[-1]
                else:
                    res[-1] = last_word+'$'
                is_equation = -1
                
        res.append(word)
    result.append(" ".join(res))
print(result)
pyperclip.copy("\n".join(result))
