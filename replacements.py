import re
import pyperclip
LATEX_REPLACEMENTS = {
    r"\alpha": "α",
    r"\rho": "ρ",
    r"\omega": "ω",
    r"\Delta": "Δ",
    r"\Phi": "Ф",
    r"\sum": "∑",
    r"\int": "∫",
    r"\cdot": "·",
    r"\pi": "π",
    r"\tau": "τ",
    r"\mu": "μ",
    r"\varphi": "φ",
    r"\forall": "∀",
    r"\le": "≤",
    r"\ge": "≥",
    r"\xi": "ξ",
    r"\exists": "∃",
    r"\infty": "∞",
    r"\in": "∈",
    r"\pm": "±",
    r"\to": "→",
}
REPLACEMENTS = {
    r">": "&gt;",
    r"<": "&lt;",
}

text = pyperclip.paste()
for source, replacement in REPLACEMENTS.items():
    text = text.replace(source, replacement)
for source, replacement in LATEX_REPLACEMENTS.items():
    text = re.sub("\\" + f"{source}([^A-Za-z])", rf"{replacement}\1", text)
pyperclip.copy(text)

