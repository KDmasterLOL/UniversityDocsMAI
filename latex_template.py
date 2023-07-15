import math
from itertools import product
from enum import Enum
from functools import partial


def with_index(symbol, r, c):
    if r == math.inf:
        r = r"m"
    if c == math.inf:
        c = r"n"
    return symbol + "_{" + f"{r}{c}" + "}"


def triangle(symbol, r, c):
    if r > c:
        return "0"
    else:
        return with_index(symbol, r, c)


def block(block_type, content):
    block_type = str(block_type)
    block_type = block_type[block_type.index(".") + 1 :]
    make_gate = lambda s: rf"\{s}{'{'+block_type+'}'}"
    return f"{make_gate('begin')}\n{content}\n{make_gate('end')}"


def create_content(symbol="a", size=(4, 4), infinity=False, func=with_index):
    func = partial(func, symbol)
    content = []
    for r in range(1, size[0] + 1):
        buf = []
        for c in range(1, size[1] + 1):
            el = ""
            if infinity:
                if c == r and c == size[1] - 1 and r == size[0] - 1:
                    el = r"\ddots"
                elif c == size[1] - 1:
                    el = "…"
                elif r == size[0] - 1:
                    el = r"\vdots"
                if r == size[0]:
                    r = math.inf
                if c == size[1]:
                    c = math.inf
            if not el:
                el = func(r, c)
            buf.append(el)
        content.append(buf)
    return content


to_matrix = lambda c: " \\\\\n".join(" & ".join(r) for r in c)


BLOCK_TYPES = Enum("BLOCK_TYPES", ["pmatrix"])

print(
    block(
        BLOCK_TYPES.pmatrix,
        to_matrix(create_content(size=(5, 5), func=triangle, infinity=True)),
    )
)
