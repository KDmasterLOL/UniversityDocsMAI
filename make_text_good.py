# скоростью \vec v
import pyperclip
import re

# pyperclip.copy("\n".join(result))

none = 0
(
    EXPRESSION,
    ADD_DOLLAR_SIGN,
    BREAKED_WORD,
) = [1 << i for i in range(3)]

re_clear_text = re.compile("[\xa0￼ ]")

REGEXES = {
    "expression": re.compile(
        "[-+]?([a-zA-Z]([_^]([a-zA-Z0-9]|{[a-zA-Z0-9]+}))?([_^]([a-zA-Z0-9]|{[a-zA-Z0-9]+}))?)"
    ),
    "start_equation": re.compile("$[\\a-zA-Z]"),
    "end_equation": re.compile("[\\a-zA-Z}]$"),
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
        text = r"""3.1.3. Законы постоянного тока http://edu.tltsu.ru/er/book_view.php?book_id=2752&page_id=31150
1) Закон Ома $I=\frac UR$ –  сила тока, текущего по проводнику, пропорциональна напряжению на концах проводника и обратно пропорциональна его сопротивлению. Экспериментальный закон. Соотношение $I=\frac UR$ иначе называют законом Ома в интегральной форме записи. Это соотношение можно распространить на отдельные участки и всю замкнутую электрическую цепь, учитывая формулы (10), (11), (12) и внутреннее сопротивление источника тока r. При этом получим частные случаи закона Ома:
а) неоднородный участок цепи: $I = \frac{\qty(\varphi_1\varphi_2)+\EMF}{R+r}$ - обобщённым закон Ома в интегральной форме записи
б) однородный участок цепи: $I = \frac{\qty(\varphi_1\varphi_2)+\EMF}{R}$ 
в) цепь замкнута:$I=\frac{\EMF}{R+r}$
Электрическое сопротивление $R$ [Ом] - характеристика противодействия проводника электрическому току и зависит от формы, размеров и материала проводника. Измеряется сопротивление $R$ в омах
Для однородного цилиндрического проводника длиной $l$ и поперечным сечением $S$:$R=\rho \frac lS$, где ρ – удельное сопротивление проводника. Оно зависит от материала проводника и условий протекания тока, в частности, от температуры. Для большинства металлов при температурах, близких к комнатной, удельное сопротивление изменяется пропорционально температуре T: $\rho = \rho_0 \alpha T$, где ρ0 – удельное сопротивление проводника при 0ºС (T = 273 К). Удельное сопротивление ρ измеряется в ом-метрах [Ом·м].
Закон Ома в дифференциальной форме записи можно получить, если рассмотреть бесконечно малый участок проводника длиной dl и поперечным сечением dS.
￼
К выводу закона Ома в дифференциальной форме записи
Сопротивление этого участка: $R=\rho \frac lS$. Напряжение на концах проводника $dU$, совпадающее с разностью потенциалов, связано с напряжённостью $E$ электрического поля соотношением: $dU=Edl$
Через сечение dS течёт ток, плотность которого согласно соотношению (4): $j=\frac{dI}{dS}$
Подставляя значения R и U по формулам (19) и (20) в закон Ома (13), получаем: $dI=\frac {dU}{R}=\frac{E\dd{l}\dd{S}}{\rho \dd{l}}=\frac{E\ddS}{\rho}$, откуда: $\dv{l}{S}=\frac {E}{\rho}$, или, с учётом соотношения (21), $j=\frac{E}{\rho}=\sigma E$, где $\sigma = \frac{1}{\rho}$  – удельная проводимость проводника.
Учитывая, что направления $\vec j$ и $\vec E$ совпадают, соотношение (22) можно записать в векторном виде: $\vec j = \frac{\vec E}{\rho} = \sigma \vec E$
Это и есть дифференциальная форма записи закона Ома для однородного участка проводника. На неоднородном участке, кроме электростатического поля с напряжённостью $\vec E$, действует поле сторонних сил, напряжённость которого – $\vec E_{\text{стор}}$; в этом случае: $\vec j = \frac{\vec E+\vec E_{\text{стор}}}{\rho} = \sigma \qty(\vec E+\vec E_{\text{стор}})$
Закон Ома в дифференциальной форме записи для неоднородного участка проводника $\vec j = \frac{\vec E+\vec E_{\text{стор}}}{\rho} = \sigma \qty(\vec E+\vec E_{\text{стор}})$
2) Закон Джоуля-Ленца характеризует тепловое действие тока. При протекании электрического тока проводник нагревается, при этом выделяется количество теплоты $Q_T$, определяемое соотношениями: $Q_m=IUt=I^2Rt=\frac{U^2}{R}t$
3) Правила Кирхгофа значительно упрощают расчёт разветвлённых электрических цепей. Пример такой цепи показан на рис"""
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
        pass
    def procces(self):
        for paragraph in self.text:
            self.result.append([])
            for idx, word in enumerate(paragraph):
                self.hang_flags(idx, word)
                self.result[-1].append(word)

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
# pyperclip.copy(p.get_text())
