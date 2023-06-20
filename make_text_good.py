# скоростью \vec v
import pyperclip
import re

# pyperclip.copy("\n".join(result))

# α -> \alpha
# ρ -> \rho
# ω -> \omega
# Δ -> \Delta
# Ф -> \Phi
# ∑ -> \sum
# · -> \cdot
# π -> \pi
# τ -> \tau
# μ -> \mu
# φ -> \varphi


# -e 's/\s//g' -e 's/#\(.\)->\(\\[a-zA-Z]\+\)/r"\2": "\1",/g'
REPLACEMENTS = {
    r"\alpha": "α",
    r"\rho": "ρ",
    r"\omega": "ω",
    r"\Delta": "Δ",
    r"\Phi": "Ф",
    r"\sum": "∑",
    r"\cdot": "·",
    r"\pi": "π",
    r"\tau": "τ",
    r"\mu": "μ",
    r"\varphi": "φ",
    r">": "&gt;",
    r"<": "&lt;",
    r"\forall": "∀",
    r"\le": "≤",
    r"\ge": "≥",
}

none = 0
(
    EXPRESSION,
    ADD_DOLLAR_SIGN,
    BREAKED_WORD,
    EQUATION,
    EQUATION_ENDED,
) = [1 << i for i in range(5)]

re_clear_text = re.compile("[\xa0￼ ]")
VAR = "[a-zA-Z]"
OPERATOR = r"\\[a-zA-Z]+"
OPERATOR = r"\\[a-zA-Z]+"
CONSTANT = r"\d+"
VAR_CONST = "[0-9a-zA-Z]"


def get_entity_pattern(*args):
    return (
        rf"[-+]?(%s)([_^]({VAR_CONST}|{{{VAR_CONST}+}})){{,2}}(\({VAR_CONST}+(,\s?{VAR_CONST})*\))?"
        % "|".join(args)
    )


PATTERN_VAR = r"[-+]?([a-zA-Z]|\\[a-zA-Z]+)([_^]([0-9a-zA-Z]|{[a-zA-Z0-9]+})){,2}"
PATTERN_VAR_AND_CONSTANT = (
    r"[-+]?([a-zA-Z]|\\[a-zA-Z]+|[0-9]+)([_^]([0-9a-zA-Z]|{[a-zA-Z0-9]+})){,2}"
)
PATTERN_POINTS = r"[A-Z]{2,}"
PATTERN_ENTITY = (
    r"[-+]?([a-zA-Z]|\\[a-zA-Z]+)([_^]([0-9a-zA-Z]|{[a-zA-Z0-9]+})){,2}[^a-zA-Z]"
)
PATTERN_ASSIGN = r"%s\s?=\s?%s" % (
    get_entity_pattern(VAR, OPERATOR),
    get_entity_pattern(VAR, CONSTANT, OPERATOR),
)
PATTERN_PARRENTHESIS = r"\(%s(,\s?%s)*\)" % (
    get_entity_pattern(VAR, CONSTANT, OPERATOR),
    get_entity_pattern(VAR, CONSTANT, OPERATOR),
)

REGEXES = {
    "start_equation": re.compile("$[\\a-zA-Z]"),
    "end_equation": re.compile(r"[\a-zA-Z})]$"),
    "simple_equation": re.compile(
        r"(?P<start>[\s,;:.]?)(%s|%s)(?P<end>[\s,;:.]?)"
        % (PATTERN_POINTS, get_entity_pattern(VAR, OPERATOR))
    ),
    "breaked_word": re.compile("[а-яА-Я]*-$"),
    "has_letter": re.compile("[a-zA-Z]"),
}

# pyperclip.copy(
#     r"[\s,;:.]?(%s|%s)[\s,;:.]?"
#     % (PATTERN_POINTS, get_entity_pattern(VAR, CONSTANT, OPERATOR))
# )


class WordProccesor:
    math_characters = ["*", "/", "=", "-", "+", "^"]
    idx_end_equation = -1

    def __init__(self, text="") -> None:
        self.result = []
        self.flags = none
        text = pyperclip.paste()
        # text = r""""""
        for source, replacement in REPLACEMENTS.items():
            text = text.replace(source, replacement)
        self.text = []
        for paragraph in text.split("\n"):
            paragraph = re_clear_text.sub(" ", paragraph)
            if paragraph.isspace() or not paragraph:
                continue
            buf = []
            for word in paragraph.split(" "):
                if word.isspace() or not word:
                    continue
                buf.append(word)
            self.text.append(buf)
        print(self.text)

    def add_flag(self, flag):
        self.flags = self.flags | flag

    def get_flag(self, flag):
        return (self.flags & flag) != 0

    def reset_flag(self, flag):
        self.flags = self.flags & (~flag)

    def hang_flags(self, idx, word):
        if self.get_flag(EQUATION_ENDED):
            self.reset_flag(EQUATION | EQUATION_ENDED)
        match word.count("$"):
            case 2:
                self.add_flag(EQUATION | EQUATION_ENDED)
            case 1:
                self.add_flag(EQUATION_ENDED if self.get_flag(EQUATION) else EQUATION)

    def procces(self):
        for paragraph in self.text:
            self.result.append([])
            for idx, word in enumerate(paragraph):
                self.hang_flags(idx, word)
                print(self.get_flag(EQUATION))
                self.result[-1].append(
                    word
                    if self.get_flag(EQUATION)
                    else REGEXES["simple_equation"].sub(r"\g<start>$\2$\g<end>", word)
                )

    def get_text(self) -> str:
        return "\n".join([" ".join(paragraph) for paragraph in self.result])


p = WordProccesor()
p.procces()
print(p.get_text())
pyperclip.copy(p.get_text())
