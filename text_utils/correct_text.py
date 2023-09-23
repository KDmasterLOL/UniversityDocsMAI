import re

text = ""
with open("text_utils/plain_text/МЕТОДЫ_ОДНОМЕРНОЙ_ОПТИМИЗАЦИИ", "r") as file:
    text = "".join(file.readlines())
reg_matches = {"simple_function": "[a-zA-Z](?:(_|^)[a-zA-Z]){,2}\([a-zA-Z]\)"}
repeated_pattern = lambda pattern, separator=",": "(((?:%s )?%s)+)" % (
    separator,
    pattern,
)
wrap_in_math = lambda pattern: (
    (
        "(?P<left>[а-яА-Я](?:[., ]+))(?P<center>%s)(?P<right>([., ]+[а-яА-Я]))"
        % pattern,
        "\g<left>#[+m \g<center>]\g<right>",
    )
)

regexes = [
    (r"^\d{1,2}$", ""),
    (r"^\s*$\n?", ""),
    (r"(?<!\.)\n(?=[а-я])", ""),
    (r"(?<=\))\s(?=,)", ""),
    (r"(?<=[Hg])\s?(?=[kj])", "_"),
    (r"(([Hgf](_[jk])?))\s*(?=([^)]+))", r"\1"),
    (r"(?<=[fD])\s+(?=\(\w\))", r""),
    (r"(?<=\w)\s*\s*(?=1, 2,...,\w)", r" = "),
    (
        r"(?<=[а-я])([.,\s]+)((?:\w\(\w\))(?:, \w\(\w\))*)([.,\s]+)(?=[,.\s]*[а-я])",
        r"\1#[+m \2]\3",
    ),
]

for rege in regexes:
    text = re.sub(rege[0], rege[1], text, flags=re.M)
print(text)
with open("text_utils/result.txt", "w") as file:
    file.write(text)
