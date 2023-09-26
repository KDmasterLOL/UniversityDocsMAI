import os
import re
import copy


def process_files(function):
    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk("./src/lib/pug/articles/MATH/OPTIMIZATION"):
        path = root.split(os.sep)
        for file in files:
            if file.endswith(".pug"):
                print(root + "/" + file)
                with open(root + "/" + file, "r") as f:
                    text = "".join(f.readlines())
                text = function(text)
                with open(root + "/" + file, "w") as f:
                    f.write(text)


# If you not sure not CHANGE!! DANGER
def function(text):
    orig = copy.copy(text)
    for entry in re.finditer(r"#\[\+m", orig):
        was_open = False
        pos = entry.end()
        result = None
        while result == None:
            if orig[pos] == "[":
                was_open = True
            elif orig[pos] == "]":
                if was_open:
                    was_open = False
                else:
                    buff = orig[entry.end() : pos].strip()
                    if "]" in buff:
                        buff = "= String.raw`%s`" % buff
                    result = entry[0] + buff + orig[pos]
            pos += 1
        text = text.replace(
            orig[entry.start() : pos], re.sub(r" {2,}", " ", result.replace("\n", " "))
        )
    return text


def test():
    text = r"""h1 Симплекс метод
    dl
        dt Symplex method
        toggle(target="example")
        dd In the method first express each linear program in the form of a simplex tableau.
        example
            p
                | Task: #[+m \begin{align} x_1 + x_2 \to \max \\ -x_1 + x_2 \le 1 \\ x_1  \le 3 \\ x_2 \le 2 \\ x_1,x_2 \ge 0 \end{align}]. The variables are nonnegative, but the inequalities have to be replaced by equations, by introducing slack variables.#[br]The equational form is
                +m \begin{align} x_1 + x_2 \\ -x_1 + x_2 + x_3 = 1 \\ x_1 + x_4 = 3 \\ x_2 + x_5 = 2 \\ x_1,x_2,…,x_5 \ge 0 \end{align}
                | with the matrix 
                +m A = \begin{pmatrix} -1 & 1 & 1 & 0 & 0 \\ 1 & 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 & 1 \end{pmatrix}
            p First express linear program in the form of a simplex tableau. In our case begin with the tableau #[+m \begin{array}{ccc} x_3& = 1 + x_1 - x_2 \\ x_4& = 3 - x_1 \\ x_5& = 2 - x_2 \\ \hline z& = x_1+x_2 \end{array}]. The first three rows consist of the equations of the linear program, in which the slack variables have been carried over to the left-hand side and the remaining terms are on the right-hand side. The last row, separated by a line, contains a new variable z, which expresses the objective function. Each simplex tableau is associated with a certain basic feasible solution. In our case we #[mark substitute #[+m 0] for the variables #[+m x_1, x_2] from the right-hand side, and without calculation see that #[+m x_3 = 1, x_4 = 3, x_5 = 2]]. This #[strong feasible solution] is basic with #[+m B = \{3, 4, 5\}] variables indeces. #[note #[+m A_B] is the identity matrix]. The variables #[+m x_3, x_4, x_5] from the left-hand side are basic and the variables #[+m x_1, x_2] from the right-hand side are nonbasic. The value of the objective function #[+m z = 0] corresponding to this basic feasible solution can be read off from the last row of the tableau. 
            p From the initial simplex tableau we will construct a sequence of tableaus of a similar form, by gradually rewriting them according to certain rules. Each tableau will contain the same information about the linear program, only written differently. The procedure terminates with a tableau that represents the information so that the desired optimal solution can be read off directly. 
            p Let us go to the first step. We try to increase the value of the objective function by increasing one of the nonbasic variables #[+m x_1] or #[+m x_2]. In the tableau observe that #[mark increasing the value of #[+m x_1] (i.e. making #[+m x_1] positive) increases the value of #[+m z]]. #[em The same is true for #[+m x_2], because both variables have positive coefficients in the #[+m z]-row of the tableau]. We can choose either #[+m x_1] or #[+m x_2]. Decide #[em (arbitrarily)] increase #[+m x_2], while #[+m x_1] will stay 0.#[br]#[strong How much can we increase #[+m x_2]?] To maintain feasibility, we have to be careful not to let any of the basic variables #[+m x_3, x_4, x_5] go #[em below zero]. This means that the equations determining #[+m x_3, x_4, x_5] may limit the increment of #[+m x_2].#[br]Let us consider the #[strong first equation] #[+m x_3 = 1 + x_1 − x_2]. Together with the implicit constraint #[+m x_3 ≥ 0] it #[mark lets us increase #[+m x_2] up to the value #[+m x_2 = 1]] (while keeping #[+m x_1 = 0]). The #[strong second equation] #[+m x_4 = 3 − x_1] does not limit the increment of #[+m x_2] at all, and the #[strong third equation] #[+m x_5 = 2 − x_2] allows for an increase of #[+m x_2] up to #[+m x_2 = 2] before #[+m x_5] gets negative. The most stringent restriction thus follows from the first equation.
            p.
                We increase #[+m x_2] as much as we can, obtaining #[+m x_2 = 1] and #[+m x_3 = 0]. From the remaining equations of the tableau we get the values of the other variables:
                #[+m \begin{align} x_4 =3−x_1=3 \\ x_5 =2−x_2=1\end{align} ]. In this new feasible solution #[+m x_3] became zero and #[+m x_2] nonzero. Quite naturally we thus transfer #[+m x_3] to the right-hand side, where the nonbasic variables live, and #[+m x_2] to the left-hand side, where the basic variables reside. We do it by means of the most stringent equation #[+m x_3 = 1 + x_1 − x_2], from which we express #[+m x_2 = 1 + x_1 − x_3].
                We substitute the right-hand side for #[+m x_2] into the remaining equations, and
                we arrive at a new tableau: #[+m \begin{array}{ccc} x_2 &= 1 + x_1 − x_3 \\ x_4 &= 3 − x_1 \\ x_5 &= 1 − x_1 +x_3 \\ \hline z &= 1 + 2x_1 − x_3 \end{array}]
                Here #[+m B = \{2,4,5\}], which corresponds to the basic feasible solution #[+m x = (0, 1, 0, 3, 1)] with the value of the objective function #[+m z = 1].#[br]This process of rewriting one simplex tableau into another is called a #[dfn pivot step]. In each pivot step some nonbasic variable, in our case #[+m x_2], enters the basis, while some basic variable, in our case #[+m x_3], leaves the basis.#[br]In the new tableau we can further increase the value of the objective function by increasing #[+m x_1], while increasing #[+m x_3] would lead to a smaller #[+m z]-value. The first equation does not restrict the increment of #[+m x_1] in any way, from the second one we get #[+m x_1 ≤ 3], and from the third one #[+m x_1 ≤ 1], so the strictest limitation is implied by the third equation. Similarly as in the previous step, we express #[+m x_1] from it and we substitute this expression into the remaining equations. Thereby #[+m x_1] enters the basis and moves to the left-hand side, and #[+m x_5] leaves the basis and migrates to the right-hand side.#[br]The tableau we obtain is 
                #[+m \begin{array}{ccc} x_1 = 1 + x_3 − x_5 \\ x_2 = 2 − x_5 \\ x_4 = 2 − x_3 + x_5 \\ \hline z = 3 + x_3 − 2x_5 \end{array}] with #[+m B = \{1,2,4\}], basic feasible solution #[+m x = (1,2,0,2,0)], and #[+m z = 3]. After one more pivot step, in which #[+m x_3] enters the basis and #[+m x_4] leaves it, we arrive at the tableau
                #[+m \begin{array}{ccc} x_1 =3 − x_4 \\ x_2 = 2 − x_5 \\ x_3 =2−x_4 +x_5 \\ \hline z = 5 − x_4 − x_5 \end{array}] with basis #[+m {1, 2, 3}], basic feasible solution #[+m x = (3, 2, 2, 0, 0)], and #[+m z = 5]. In this tableau, no nonbasic variable can be increased without making the objective function value smaller, so we are stuck. Luckily, this also means that we have already found an optimal solution! Why?#[br]Let us consider an arbitrary feasible solution #[+m \tilde x  = (\tilde{x_1},…,\tilde{x_5})] of our linear program, with the objective function attaining some value #[+m \tilde z]. Now #[+m \tilde x] and #[+m z] satisfy all equations in the final tableau, which was obtained from the original equations of the linear program by equivalent transformations. Hence we necessarily have #[+m \tilde z = 5 − \tilde {x_4} − \tilde {x_5}].#[br]Together with the nonnegativity constraints #[+m x_4,x_5 ≥ 0] this implies #[+m z ≤ 5]. The tableau even delivers a #[em proof] that #[+m x = (3, 2, 2, 0, 0)] is the only optimal solution: #[mark If #[+m z = 5], then #[+m x_4 = x_5 = 0], and this determines the values of the remaining variables #[strong uniquely]].



    h4 Exception Handling
    h5 Infeasibility
    intro In order that the simplex method be able to start at all, we need a feasible basis. #[note In linear programs of the #[strong form] #[+m \vb c^T\vb x \to \max] subject to #[+m A \vb x ≤ b] and #[+m \vb x ≥ 0] with #[+m \vb b ≥ 0] we get free feasible basis. Indeed, the indices of the slack variables introduced in the transformation to equational form can serve as a feasible basis.]#[br]#[small However, in general, finding any feasible solution of a linear program is equally as difficult as finding an optimal solution]. Computing the initial feasible basis can be done by the simplex method itself, if we apply it to a suitable auxiliary problem.
        toggle(target="example")
    example
        p Task: linear program in equational form #[+m \begin{aligned} x_1 + 2x_2 \to \max\\ x_1+3x_2+x_3=4 \\ 2x_2 +x_3 =2\\ x_1,x_2,x_3 ≥0 \end{aligned}]
        ol
            li Produce a feasible solution starting with #[+m() (x_1, x_2, x_3) = (0, 0, 0)]. This vector is #[em nonnegative], but of course it is #[strong not feasible], since it does not satisfy the equations of the linear program. 
            li Introduce auxiliary variables #[+m x_4] and #[+m x_5] as “corrections” of infeasibility: #[+m x_4 =4−x_1−3x_2−x_3] expresses by how much the original variables #[+m x_1, x_2, x_3] fail to satisfy the first equation, and #[+m x_5 = 2 − 2x_2 − x_3] plays a similar role for the second equation. #[mark If we managed to find nonnegative values of #[+m x_1,x_2,x_3] for which both of these corrections come out as zeros, we would have a feasible solution of the considered linear program].
            li The task of finding nonnegative #[+m x_1, x_2, x_3] with zero corrections can be captured by a linear program: #[+m \begin{aligned} − x_4 − x_5 \to \max\\ x_1 +3x_2 + x_3 +x_4 =4 \\ 2x_2 + x_3 + x_5 = 2\\ x_1,x_2,...,x_5 ≥ 0 \end{aligned}]
            li The optimal value of the objective function #[+m −x_4 − x_5] is 0 exactly if there exist values of #[+m x_1,x_2,x_3] with zero corrections, i.e., a feasible solution of the original linear program. This is the #[strong right auxiliary linear program]. The variables #[+m x_4] and #[+m x_5] form a feasible basis, with the basic feasible solution #[+m() (0,0,0,4,2)]. #[small Here we use that the right-hand sides, 4 and 2, are nonnegative, but since we deal with equations, this can always be achieved by sign changes]. Once we express the objective function using the nonbasic variables, that is, in the form #[+m z = −6 + x_1 + 5x_2 + 2x_3], we can start the simplex method on the auxiliary linear program.
            li The auxiliary linear program is surely bounded, since the objective function cannot be positive. The simplex method thus computes a basic feasible solution that is optimal. As training the reader can check that if we let #[+m x_1] enter the basis in the first pivot step and #[+m x_3] in the second, the final simplex tableau comes out as #[+m x_1 = 2 − x_2 − x_4 + x_5 x_3 = 2 − 2x_2 − x_5 z = − x_4 − x_5].
            li The corresponding optimal solution #[+m() (2, 0, 2, 0, 0)] yields a basic feasible solution of the original linear program: #[+m() (x_1 , x_2 , x_3 ) = (2, 0, 2)]. The initial simplex tableau for the original linear program can even be obtained from the final tableau of the auxiliary linear program, by leaving out the columns of the auxiliary variables #[+m x_4] and #[+m x_5], and by changing the objective function back to the original one, expressed in terms of the nonbasic variables: #[+m \begin{aligned}x_1 =2− x_2 \\ x_3 =2−2x2 \\ \hline z = 2 + x_2 \end{aligned}]. #[small Starting from this tableau, a single pivot step already reaches the optimum].










    dl
        dt #[abbr(term="Условие допустимости") УД]
        dd в задаче максимизации отсутствие отрицательных коэффициентов в ЦФ, а в задаче минимизации отсутствие положительных

    h2 Особые случаи применения
    dl
        dt Вырожденность
            toggle(target="example")
        dd оптимальное решение - вырожденое. В ходе выполнения симплекс-метода проверка УД может привести к неоднозначному выбору исключаемой переменной, то есть #[+m \theta] нескольких ограничений будут одинаковы. И на следующей итерации одна или несколько базисных переменных примут нулевое значение. Тогда новое решение будет вырожденным. зам В вырожденном решении нет никакой опасности, за исключением небольших теоретических неудобств. С практической точки зрения вырожденность объясняется тем, что в исходной задаче присутствует по крайней мере одно избыточное ограничение
        example
            .
                #[+m z=3x_1+9x_2 \rightarrow \max \\ \begin{cases} x_1+4x_2 \le 8 \\ x_1+2x_2 \le 4 \\ x_1,x_2 \ge 0 \end{cases}]
                #[img.invert(src="Симплекс-таблица с оптимальным вырожденным решением.webp")]
                На начальной итерации в качестве исключаемой можно выбрать как переменную #[+m x_3], так и #[+m х_4],. Если оставить в базисе переменную #[+m x_4] на следующей итерации она примет значение 0, т.е. получим вырожденное базисное решение. Оптимальное решение получается на следующей итерации.
                Что же практически приводит к вырожденности решения? В графическом представлении решении этой задачи. Точка оптимума #[+m x_1=0, x_2=2] - пересечение трех прямых. Поскольку данная задача двухмерна, эта точка переопределена (на плоскости для определения точки достаточно двух прямых), и, следовательно, одно из ограничений избыточно.
                #[img.invert(src="Пример графического оптимального вырожненого решения.webp")]
                На практике информация о том, что некоторые ресурсы недефицитны, может быть полезной при интерпретации результатов решения задачи. Эти сведения также могут помочь выявить неточности и ошибки в постановке исходной задачи. К сожалению, не существует способов определить избыточное ограничение непосредственно из данных симплекс-таблиц.
                С вычислительной и теоретической точек зрения вырожденность может привести к: 
                1. В процессе вычислений может возникнуть зацикливание. Если в приведенной выше таблице сравнить первую и вторую итерации, то можно заметить, что значение ЦФ не изменилось (#[+m z= 18]). Поэтому может возникнуть ситуация, когда при реализации симплекс-метода некоторая последовательность будет повторяться, не изменяя значения целевой функции и не приводя к завершению вычислительного процесса. Существуют методы, предотвращающие зацикливание, однако они значительно замедляют процесс вычислений. Поэтому в большинстве программ, реализующих симплекс-метод, отсутствуют специальные средства защиты от зацикливания, тем более, что вероятность зацикливания очень мала.
                2. Во-вторых, последствие вырожденности решения можно обнаружить, сравнивая первую и вторую итерации в приведенной выше таблице. Хотя в этих итерациях состав базисных и небазисных переменных различен, значения всех переменных и значение целевой функции не изменяются:
                #[+m x_1 = 0, x_2 = 2, x_3= 0, x_4 = 0, z= 18]
                Можно ли, несмотря на то, что оптимальное решение не достигнуто, остановить вычисления на первой итерации (когда впервые обнаруживается вырожденность)? Ответ отрицательный, так как решение может быть только временно вырожденным.
            dt Связывающее неравенство
            dd неравенство которое в точке оптимума выполняется как точное равенство
            dt Альтернативные оптимальные решения
            dd доступен диапазон оптимальных решений. #[i На примере графического метода] Возникает когда прямая ЦФ параллельна прямой, соответствующей связывающему неравенству, ЦФ принимает одно и тоже оптимальное значение на некотором множестве точек границы пространства решений, то есть имеет альтернативные оптимальные решения. Следующий пример показывает, что таких решений(если они существуют) бесконечное множество. Этот пример также проиллюстрирует практическую значимость альтернативных решений.
            details
                summary.example
                div
                    img(src="Альтернативные решения на графике.webp" alt="" srcset="")
                    p множество альтернативных оптимальных решений - следствие того, что прямая ЦФ параллельна прямой, соответствующей связывающему ограничению
                    img(src="Альтернативные решения таблица.webp")

    example
        +m.block.
            \begin{aligned}
            z = x+y \\
            \begin{cases}
            10x-2y\le 2 \\
            x+2y\le 2
            \end{cases}
            \end{aligned}

            \Longrightarrow

            \begin{aligned}
            z = x+y+0s_1+0s_2 \\
            \begin{cases}
            10x-2y+s_1 = 2 \\
            x+2y+s_2 = 2
            \end{cases}
            \end{aligned}

            \Longrightarrow

            \begin{aligned}
            z = x+y+0s_1+0s_2 \\
            \begin{cases}
            s_1 = 2-10x+2y \\
            s_2 = 2-x-2y
            \end{cases}
            \end{aligned}

            \Longrightarrow

            \begin{aligned}
            z = x+y=0.2+0=0.2 \\
            \begin{cases}
            x=\underbrace{0.2+0.2y-0.1s_1}_{(2+2y-s_1)/10} \Leftarrow 10x = 2+2y-s_1 \\
            s_2 =1.8-2.2y-0.1s_1=2-\overbrace{(0.2+0.2y-0.1s_1)}^x-2y
            \end{cases}
            \end{aligned}

            \Longrightarrow

            \begin{aligned}
            z = x+y+0s_1+0s_2 \\
            \begin{cases}
            x=0.2+0.2\overbrace{(\frac{18}{22}-\frac{1}{22}s_1-\frac{10}{22}s_2)}^{y}-0.1s_1 \\
            y=\underbrace{\frac{18}{22}-\frac{1}{22}s_1-\frac{10}{22}s_2}_{(1.8-0.1s_1-s_2)/2.2} \Leftarrow 2.2y=1.8-0.1s_1-s_2
            \end{cases}
            \end{aligned}
        +m.block.
            \begin{array}{cccc|c}
            1 & 1 & 0 & 0 & z \\
            \hline
            10 & -2 & 1 & 0 & 2 \\
            1 & 2 & 0 & 1 & 2
            \end{array}
            \Longrightarrow
            \begin{array}{cccc|c}
            1 & 1 & 0 & 0 & z \\
            \hline
            10 & -2 & 1 & 0 & 2 \\
            1 & 2 & 0 & 1 & 2
            \end{array}
    h2 FAQ
    mixin question(question)
        li 
            strong=question+'?'
            block
    ol
        +question("Зачем нужны ограничения если оптимальное решение только на вершинах многоугольника") Чтобы найти этот многоугольник!! Привести пример сложной системы графиков где точка (0,0) не является допустимым решением и сделать подводку к нахождению начального базисного решения 
        +question("Как происходит перемещение из точки в точку с помощью введения в базис переменных") 
        li Доказательство того что уменьшив или увеличив на какое-то число, то просто ее пересечения с осями сместятся на это число, а не в конец перпендикулярного этой прямой вектора с длинной этого числа. Это можно логически доказать как если бы у нас было уравнение состоящее из целых чисел #[+m x,y,s\in Z:x+y+s=\const], то если бы добавочная переменная 
        li Переводя какую-либо переменную в базис #[+m \begin{cases}s_1=\const_1+ \alpha_1 x+\beta_1 y\\ s_2=\const_2+ \alpha_2 x+\beta_2 y \end{cases} \Rightarrow \begin{cases}x=(\const_1+\beta_1 y - s_1)/\alpha_1\\ s_2=\const_2+ \alpha_2 (\const_1+\beta_1 y - s_1)/\alpha_1+\beta_2 y \end{cases}] мы двигаем второй график на величину #[+m \frac{\alpha_2\const_1}{\alpha_1}] и в случае если бы графиком было #[+m m], то все бы они также подвинулись на эту величину, #[mark то есть: #[strong вводя переменную в базис все ограничения двигуются из исходной точки в направлении оси представляющей переменную на величину ] #[+m \frac{\alpha_2\const_1}{\alpha_1}]]
        li В уравнение #[+m \alpha_1x_1+\alpha_2x_2+…+\alpha_nx_n + s = \const] каждая единица #[+m s] смещает график на #[+m \pm \frac{s}{\const}] это следует из #[+m p\in [1,n],i=\overline{1,n},\forall i\ne p,x_i = 0: \alpha_1x_1+\alpha_2x_2+…+\alpha_2x_2+…+\alpha_nx_n + s = \const \Leftrightarrow \alpha_10+\alpha_20+…+\alpha_px_p+…+\alpha_n0 + s = \alpha_px_p + s = \const \Rightarrow x_p = \frac{\const-s}{\alpha_p} =\frac{\const}{\alpha_p}-\frac{s}{\alpha_p}], то есть чтобы пересечение по оси #[+m x_p] было в точке ноль нужно обнулить чтобы выполнялось равенство #[+m \frac{\const}{\alpha_p}=\frac{s}{\alpha_p}], которое выполняется только при #[+m \const = s]
        li 
            p Сколько прямых столько и выбор на сколько сместиться по оси, то есть например если мы выбираем на сколько сместится по оси #[+m x], то у нас стоит выбор между количеством точек равным количеству прямых ограничений, так как они все пересекаются с этой осью #[small если они не паралельны ей] #[+m \begin{cases}\alpha_1x_1+…\\\alpha_2x_2+…\\\vdots\\\alpha_mx_m+…\end{cases}]





    hgroup 
        h5 There is no initial basis in the Simplex tableau 
            a(book="Linear Programming: Theory and Applications Catherine Lewis May 11, 2008" chapter="8. What if there is no initial basis in the Simplex tableau?")
        intro What does one do when the initial tableau contains no starting basis? That is, what happens if the initial tableau (for a program where  is ) does not contain all the columns of an  identity matrix?
    p This problem occurs when the constraints are in either equality or “greater than or equal to” form. In the case of an equality constraint, one cannot add a slack or an excess variable and therefore there will be no initial basic variable in that row. In the case of a “greater than or equal to” constraint, one must add an excess variable, which gives a −1 in that row instead of a +1. #[small Simply multiplying through that row by −1 would not solve the problem, for then the right-hand-side variable would be negative].#[br]#[em There are two main methods to dealing with this problem]: the #[dfn Two-Phase Method] and the #[dfn Big-M Method]. Both of these methods involve adding #[dfn artificial] variables that start out as basic variables but #[mark #[strong must] eventually equal zero in order for the original problem to be feasible].
    h6 The Two-Phase Method
    ol In summary, the Two-Phase Method can be completed using the following steps:
        toggle(target="example")
        li If there is no basis in the original tableau, add artificial variables to rows in which there are no slack variables.
        li Set up a new objective function that minimizes these slack variables.
        li Modify the tableau so that the Row 0 coefficients of the artificial variables are zero.
        li Complete the Simplex algorithm as usual for a minimization problem.
        li At optimality, the artificial variables should be nonbasic variables, or basic variables equal to zero. If not, the original problem was infeasible.
        li After reaching optimality, delete all rows associated with artificial variables. Also, replace the artificial objective function with the original objective function. This is the start of Phase II.
        li Modify the tableau so that the Row 0 coefficients of the basic variables are zero.
        li Proceed with the Simplex algorithm as usual. The optimal solution to this tableau will be the optimal solution to the original problem.
    example
        p.
            Consider the following problem:
            #[+m \begin{aligned} \text{Maximize} \quad &  z=2x_1 − x_2 + x_3 \\ \text{subject to} \quad & 2x_1 + x_2 − 2x_3 ≤ 8 \\ & 4x_1−x_2+2x_3 = 2 \\ & 2x_1+3x_2−x_3 ≥ 4 \\ & x_1,x_2,x_3 ≥ 0 \\ \end{aligned}]
        ol
            li: .step
                p To put this in standard form, all constraints must become equalities. Adding a slack variable, #[+m s_1], to the first constraint and subtracting an excess variable #[+m e_3] from the third constraint gives the initial Simplex tableau. 
                .
                    #[+m \begin{array}{c|ccccc|c}
                    1 & -2 & 1 & -1 & 0 & 0 & 0 \\ 
                    \hline
                    0 & 2 & 1 & -2 & 0 & 1 & 8 \\ 
                    0 & 4 & -1 & 2 & 0 & 0 & 2 \\ 
                    0 & 2 & 3 & -1 & -1 & 0 & 4
                    \end{array}]
            li: .step"""
    print(function(text))


process_files(function)

# test()
