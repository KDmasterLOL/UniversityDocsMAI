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
PATTERN_ENTITY = r"[-+]?([a-zA-Z]|\\[a-zA-Z]+)([_^]([0-9a-zA-Z]|{[a-zA-Z0-9]+})){,2}"
PATTERN_ENTITY_WITH_DIGIT = (
    r"[-+]?([a-zA-Z]|\\[a-zA-Z]+|\d+)([_^]([0-9a-zA-Z]|{[a-zA-Z0-9]+})){,2}"
)
PATTERN_ASSIGN = r"%s(\s?=\s?((%s|\d+))?" % (PATTERN_ENTITY, PATTERN_ENTITY)
PATTERN_PARRENTHESIS = r"\(%s(,\s?%s)*\)" % (
    PATTERN_ENTITY_WITH_DIGIT,
    PATTERN_ENTITY_WITH_DIGIT,
)
print(PATTERN_ASSIGN)
print(PATTERN_PARRENTHESIS)
PATTERNS = {
    "variable": r"[\-+]?([a-zA-Z]([_^]([a-zA-Z0-9]|{[a-zA-Z0-9]+}))?([_^]([a-zA-Z0-9]|{[a-zA-Z0-9]+}))?)",
}
REGEXES = {
    "expression": re.compile(
        r"[\-+]?([a-zA-Z]([_^]([a-zA-Z0-9]|{[a-zA-Z0-9]+}))?([_^]([a-zA-Z0-9]|{[a-zA-Z0-9]+}))?)"
    ),
    "start_equation": re.compile("$[\\a-zA-Z]"),
    "end_equation": re.compile("[\\a-zA-Z}]$"),
    "simple_equation": re.compile(
        r"\s[,.;]?([+\-]?[a-zA-Z]([_^]([0-9a-zA-Z]|{[a-zA-Z0-9]+})){,2})[,.;]?\s"
    ),
    "breaked_word": re.compile("[а-яА-Я]*-$"),
    "has_letter": re.compile("[a-zA-Z]"),
}


class WordProccesor:
    math_characters = ["*", "/", "=", "-", "+", "^"]
    idx_end_equation = -1

    def __init__(self, text="") -> None:
        self.result = []
        self.flags = none
        text = pyperclip.paste()
        #         text = """охватываемых контуром +L-. Каждый ток учитывается столько раз, сколько он охватывается контуром. Ток считается положительным, если его направление связано с направлением обхода правилом правого винта. Ток противоположного направления считается отрицательным.
        # ￼
        # $\sum_{I=1}^N I_i = I_1 + I_2 + I_3 - 0I_4 = I_2$
        # Выражение (29.5) справедливо только для поля в вакууме. Формула (29.3) – постулат, подтвержденный экспериментально."""
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
        if "$" in word:
            if not self.get_flag(EQUATION):
                self.add_flag(EQUATION)
            else:
                self.reset_flag(EQUATION_ENDED)

    def procces(self):
        for paragraph in self.text:
            self.result.append([])
            for idx, word in enumerate(paragraph):
                self.hang_flags(idx, word)
                print(self.get_flag(EQUATION))
                self.result[-1].append(
                    word
                    if self.get_flag(EQUATION)
                    else REGEXES["simple_equation"].sub(r"$\1$", word)
                )

    def get_text(self) -> str:
        return "\n".join([" ".join(paragraph) for paragraph in self.result])

    # def expression_check(paragraph):
    #     is_letter = re.compile("[a-zA-Z]")
    #     is_equation_character = re.compile("[a-zA-Z{}=()_^\\+-]")
    #     equation = 0
    #     for idx,l in enumerate(paragraph):
    #         if l.isspace():
    #             continue
    #         if l == "$" and equation != 1:
    #             equation = 1
    #         else:
    #             equation = 0
    #         if equation == 1:


p = WordProccesor()
p.procces()
print(p.get_text())
pyperclip.copy(p.get_text())
