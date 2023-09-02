# Objective: make table with letters
import types


def table(letter, size=5, before=2, after=1):
    def to_list(val) -> list:
        if not isinstance(val, list):
            return [val, val]
        return val

    before = to_list(before)
    after = to_list(after)
    size = to_list(size)

    # before and collapse (…) element and that after in table example: a_1 a_2 … a_4 a_5
    count = [before[0] + after[0] + 1, before[1] + after[1] + 1]

    def get_pos(pos):
        result = []
        for idx, val in enumerate(pos):
            if val > collapse_point[idx]:
                if isinstance(size[0], str):
                    buf = ""
                    if count[idx] - val == 0:
                        buf = size[idx]
                    else:
                        buf = f"{size[idx]}-{count[idx] - val}" + (
                            ", " if idx == 0 else ""
                        )
                    result.append(buf)
                else:
                    result.append(size[idx] - count[idx] + val)
            else:
                result.append(val)
        return result

    # if isinstance(size[0], str):
    #     get_pos = lambda l: [
    #         (f"{size[idx]}-{count[idx] + val}" if val > collapse_point[idx] else val)
    #         for (idx, val) in enumerate(l)
    #     ]
    # else:
    #     get_pos = lambda l: [
    #         (size[idx] - count[idx] + val if val > collapse_point[idx] else val)
    #         for (idx, val) in enumerate(l)
    #     ]

    collapse_point = [before[0] + 1, before[1] + 1]

    result = []
    # In cycles offset by one
    for row in range(1, count[0] + 1):
        result.append([])
        for col in range(1, count[1] + 1):
            is_collapse = [
                val == collapse_point[idx] for (idx, val) in enumerate([row, col])
            ]
            buf = ""
            if all(is_collapse):
                buf = r"\ddots"
            elif is_collapse[0]:
                buf = r"\vdots"
            elif is_collapse[1]:
                buf = "…"
            else:
                pos = get_pos([row, col])
                buf = "a_{%s%s}" % (pos[0], pos[1])
            result[-1].append(buf)
    return result


to_matrix = lambda ll: " \\\\ \n".join(" & ".join(l) for l in ll)


def wrap(content, block_name, wrapped="$$"):
    return (
        wrapped
        + "\n".join(
            [r"\begin{%s}" % block_name, to_matrix(content), r"\end{%s}" % block_name]
        )
        + wrapped
    )


MATRIX = "pmatrix"
DETERMINANT = "vmatrix"
print(wrap(table("a", size=["m", "n"], after=1), MATRIX, wrapped=""))
