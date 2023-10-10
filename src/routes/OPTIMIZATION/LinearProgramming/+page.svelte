<script>
	import Math from '$lib/components/Math.svelte';
	import Switcher from '$lib/components/Switcher.svelte';

	import book_1 from './docs/SimplexMethodSpecialCases.pdf?url'
</script>


<template lang="pug">
figure
	ol
		ul: a(href="https://www.youtube.com/watch?v=E72DWgKP_1Y") Linear programming introduction
		ul: a(href="https://www.whitman.edu/Documents/Academics/Mathematics/lewis.pdf") Linear Programming: Theory and Applications Catherine Lewis May 11, 2008
		ul: a(href="https://math.mit.edu/~goemans/18310S15/lpnotes310.pdf") 18.310A lecture notes March 17, 2015; Linear programming; Lecturer: Michel Goemans
		ul: a(href="https://www.uky.edu/~dsianita/300/online/LP.pdf") Linear programming
	figcaption: h1 Литература

	p.intro Linear programming is not directly related to computer programming. The term was introduced in the 1950s when computers were few and mostly top secret, and the word programming was a military term that, at that time, referred to plans or schedules for training, logistical supply, or deployment of men. The word linear suggests that feasible plans are restricted by linear constraints (inequalities), and also that the quality of the plan (e.g., costs or duration) is also measured by a linear function of the considered quantities. In a similar spirit, linear programming soon started to be used for planning all kinds of economic activities, such as transport of raw materials and products among factories, sowing various crop plants, or cutting paper rolls into shorter ones in sizes ordered by customers. The phrase “planning with linear constraints” would perhaps better capture this original meaning of linear programming. However, the term linear programming has been well established for many years, and at the same time, it has acquired a considerably broader meaning: Not only does it play a role only in mathematical economy, it appears frequently in computer science and in many other fields.
dl
	dt(lang='en'): dfn Linear program
	dt: dfn Линейная программа 
	dd
		Switcher
			+m({"\\Vec cn": "вектор коэффициентов целевой функции", "\\Vec bm": "вектор свободных членов", "\\Veci xm": "вектор неизвестных"}).block
				| \begin{aligned}
				| \vb c^T\vb x \to \max, i=\overline{1,m}:\sum_{j=1}^n a_{ij}x_j \quad \ge/\le/= \quad b_i,\; \vb x\ge 0 \\
				| \hline
				+LPTASK('\\vb c^T \\eq c_1x_1+c_2x_2+…+c_nx_n',String.raw`b_1\quad\ge/\le/= \quad a_{11}x_1+a_{12}x_2+…+a_{1n}x_n \\b_2 \quad\ge/\le/= \quad a_{21}x_1+a_{22}x_2+…+a_{2n}x_n \\ \vdots \\b_m \quad \ge/\le/= \quad a_{m1}x_1+a_{m2}x_2+…+a_{mn}x_n \\x_1,x_2,…,x_n \ge 0`, true)
				| \end{aligned}
			+m({"\\Vec cn": "вектор коэффициентов целевой функции", "\\Vec bm": "вектор свободных членов", "\\Veci xm": "вектор неизвестных"}).block
				| \begin{aligned}
				| \text{maximize/minimize}\quad \vb c^T\vb x \quad\text{subject to}\quad i=\overline{1,m}:\sum_{j=1}^n a_{ij}x_j \quad \ge/\le/= \quad b_i,\; \vb x\ge 0 \\
				| \hline
				+LPTASK('c_1x_1+c_2x_2+…+c_nx_n',String.raw`b_1\quad\ge/\le/= \quad a_{11}x_1+a_{12}x_2+…+a_{1n}x_n \\ b_2 \quad\ge/\le/= \quad a_{21}x_1+a_{22}x_2+…+a_{2n}x_n \\ \vdots \\ b_m \quad \ge/\le/= \quad a_{m1}x_1+a_{m2}x_2+…+a_{mn}x_n \\ x_1,x_2,…,x_n \ge 0`, true).beauty
				| \end{aligned}
	dt Equational form of a linear program
		a(book="Understanding and Using Linear Programming" chapter="4.1 Equational Form")
	dd
		+m({
			"\\vb c \\in \\R^n, \\vb b \\in \\R^m, \\vb x": "вектора коэффициентов целевой функции, значение ограничений(свободных членов), неизвестных соответсвенно", 
			"A = A_{m\\times n} = (i=\\overline{1,m},j=\\overline{1,n}:a_{ij})": "матрица коэффициентов"
			}).block
			+LPTASK('\\vb c^T \\vb x', String.raw`Ax\eq b \\ \vb x \ge \vec 0`, true)
	dt Ограничение неотрицательности
	dd частичные равенства #[+m Ax=b] и частичные неравенства формы #[+m j=\overline{1,n}:x_j \ge 0 \Leftrightarrow x \ge \vec 0]
		p.warning Although we call this form equational, it contains inequalities as well, and these must not be forgotten!
	dd All variables in the equational form have to satisfy the nonnegativity constraints. In problems encountered in practice we often have nonnegativity constraints automatically, since many quantities, such as the amount of consumed cucumber, cannot be negative.
	dt Transformation of an arbitrary linear program to equational form 
		toggle(target="example")
	example
		+LPTASK('3x_1 - 2x_2',String.raw`2x_1 - x_2 \le 4 \\ x_1 + 3x_2 \ge 5 \\ x_2 \le 0`)
		ol
			li To convert the inequality #[+m 2x_1 − x_2 \le 4] to an equation, introduce a new variable #[+m x_3], together with the nonnegativity constraint #[+m x_3 \ge 0], and replace the considered inequality by the equation #[+m 2x_1 − x_2 + x_3 = 4]. #[mark The auxiliary variable #[+m x_3], which won’t appear anywhere else in the transformed linear program, #[em represents the difference between the right-hand side and the left-hand side of the inequality]]. Such an auxiliary variable is called a #[dfn slack variable].
			li For the next inequality #[+m x_1 + 3x_2 ≥ 5] we first multiply by #[+m −1], which reverses the direction of the inequality. Then we introduce another slack variable x_4 with the nonnegativity constraint x_4 ≥ 0, and we replace the inequality by the equation −x1 − 3x_2 + x_4 = −5.
	dt Добавочные #[en slack] #[+m= s] переменные
	dd переменные добавляемые для превращения неравенств в равенства.
	dd На них также обязательно распространяется ограничение неотрицательности ведь если бы переменная могла бы принимать отрицательные значение то неравенство было бы ложным
		example #[+m x + y \le 10 \Rightarrow x+y+s = 10 \Rightarrow]
	dd #[strong Геометрический смысл] Смещение прямой от исходной позиции. При подставлении #[+m \pm s = -\alpha_1 x_1 - \alpha_2 x_2 - … - \alpha_n x_n + \const] координат точки #[+m () (x_1,x_2,…,x_n)] добавачная переменная равна расстоянию на которое надо сместить прямую #[+m \alpha_1 x_1 + \alpha_2 x_2 + … + \alpha_n x_n = \const] вверх(#[+m= s>0]) или вниз(#[+m= s<0]) чтобы она проходила через точку #[+m () (x_1,x_2,…,x_n)]. 
		example Допустим прямая задана как #[+m \alpha_1 x_1 + \alpha_2 x_2 + … + \alpha_n x_n \le/\ge \const], то приведя данное неравенство к равенству получим #[+m \alpha_1 x_1 + \alpha_2 x_2 + … + \alpha_n x_n \pm s = \const], а изсходя из свойств прямой #[+m x + y \pm s = \const] в декартовой системе координат, таких как при #[+m= s>0] прямая опускается на #[+m= s] единиц, а при #[+m= s<0] наоборот, можно сделать вывод что изменяя значение 
	dt Остаточная #[+m +s]
	dd остаток до предела
	dt Избыточная #[+m -s]
	dd переизбыток после предела
	dt Смешанная #[+m \pm s = s^+ - s^-]
	dd может обозначать как избыток так и остаток

h2 Виды решений ЗЛП
	dl
		dt #[abbr(term="Вырожденное решение") ВР]
		dd БР содержащее базисную переменную равную нулю

section.example
	h2 Examples
	ol
		li
			+m.block
				+LPTASK('x+y',String.raw`10x-2y \le 2 \\ x+2y\le 2`,true)
				| \Longrightarrow
				+LPTASK('x+y+0s_1+0s_2',String.raw`10x-2y+s_1 \eq 2 \\ x+2y+s_2 = 2`,true)
				| \Longrightarrow
				+LPTASK('x+y+0s_1+0s_2',String.raw`s_1 \eq 2-10x+2y \\ s_2 \eq 2-x-2y`,true)
				| \Longrightarrow
				+LPTASK(String.raw`x+y\eq 0.2+0\eq0.2`,String.raw`x\eq\underbrace{0.2+0.2y-0.1s_1}_{(2+2y-s_1)/10} \Leftarrow 10x = 2+2y-s_1 \\ s_2 =1.8-2.2y-0.1s_1=2-\overbrace{(0.2+0.2y-0.1s_1)}^x-2y`,true)
				| \Longrightarrow
				+LPTASK('x+y+0s_1+0s_2',String.raw`x\eq 0.2+0.2\overbrace{(\frac{18}{22}-\frac{1}{22}s_1-\frac{10}{22}s_2)}^{y}-0.1s_1 \\ y=\underbrace{\frac{18}{22}-\frac{1}{22}s_1-\frac{10}{22}s_2}_{(1.8-0.1s_1-s_2)/2.2} \Leftarrow 2.2y=1.8-0.1s_1-s_2`,true)
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


section
	h3 Graphical Method of Solving Linear Programming Problems
		+source(links=['https://www.toppr.com/guides/maths/linear-programming/graphical-method-of-solving-a-linear-programming-problem/'])
	dl
		dt Graphical Method
		dd 
			p.intro #[em In principle] this method works for almost all different types of problems but #[strong apllied mostly for problems with 2 decision variables] and in rare cases with 3.
			p We will first discuss the steps of the #[a(href='https://www.toppr.com/guides/maths/polynomials/value-of-polynomial-and-division-algorithm/') algorithm]:
			ol
				li
					p #[strong Formulate the LP problem]
				li
					p #[strong Construct a graph and plot the constraint lines]. The graph must be constructed in #[+m n\text{ dimensions} = \text{number of decision variables}], #[strong this should give you an idea about the complexity of this step if the number of decision variables increases]. One must know that one cannot imagine more than 3-dimensions anyway! The constraint lines can be constructed by joining the horizontal and vertical intercepts found from each constraint equation.
				li
					p #[strong Determine the valid side of each constraint line]. This is used to determine the domain of the available space, which can result in a feasible solution. How to check? A simple method is to put the coordinates of the origin (0,0) in the problem and determine whether the objective function takes on a physical solution or not. If yes, then the side of the constraint lines on which the origin lies is the valid side. Otherwise it lies on the opposite one.
				li
					p #[strong Identify the feasible solution region]. The #[dfn feasible solution region] on the graph is the one which is satisfied by all the constraints #[eg the intersection of the valid regions of each constraint line]. Choosing any point in this area would result in a valid solution for our objective function.
				li
					p #[strong Plot the objective function on the graph]. It will clearly be a straight line since we are dealing with linear equations here. One must be sure to draw it differently from the constraint lines to avoid confusion. Choose the constant value in the equation of the objective function randomly, just to make it clearly distinguishable.
				li Find the optimum point
					p(title="Optimum Points") An optimum point always lies on one of the corners of the feasible region. How to find it? Place a ruler on the graph sheet, parallel to the objective function. Be sure to keep the orientation of this ruler fixed in space. We only need the direction of the straight line of the objective function. Now begin from the far corner of the #[a(href='https://www.toppr.com/guides/maths/smart-charts/bar-graph/') graph] and tend to slide it towards the origin.
					ul
						li If the goal is to minimize the objective function, find the point of contact of the ruler with the feasible region, which is the closest to the origin. This is the optimum point for minimizing the function.
						li If the goal is to maximize the objective function, find the point of contact of the ruler with the feasible region, which is the farthest from the origin. This is the optimum point for maximizing the function.
					figure
						iframe(src="https://d1whtlypfis84e.cloudfront.net/guides/wp-content/uploads/2020/04/12164453/Linear-Programming-Page-21.pdf")
						figcaption: h1 Linear Programming Problem Cheat Sheet
				li Calculate the coordinates of the optimum point.
					p This is the last step of the process. Once you locate the optimum point, you’ll need to find its coordinates. This can be done by drawing two perpendicular lines from the point onto the coordinate axes and noting down the coordinates.
					p Otherwise, you may proceed algebraically also if the optimum point is at the intersection of two constraint lines and find it by solving a set of simultaneous linear equations. The Optimum Point gives you the values of the decision #[a(href='https://www.toppr.com/guides/business-economics-cs/mathematics-of-finance-and-elementary-probability/random-variables/') variables] necessary to optimize the objective function.
					p To find out the optimized objective function, one can simply put in the values of these parameters in the equation of the objective function. You have found your solution! Worried about the execution of this seemingly long algorithm? Check out a solved example below!
	h4 Solved Examples for You
	p: strong Question 1: A health-conscious family wants to have a very well controlled vitamin C-rich mixed fruit-breakfast which is a good source of dietary fibre as well; in the form of 5 fruit servings per day. They choose apples and bananas as their target fruits, which can be purchased from an online vendor in bulk at a reasonable price.
	p: strong Bananas cost 30 rupees per dozen (6 servings) and apples cost 80 rupees per kg (8 servings). Given: 1 banana contains 8.8 mg of Vitamin C and 100-125 g of apples i.e. 1 serving contains 5.2 mg of Vitamin C.
	p: strong Every person of the family would like to have at least 20 mg of Vitamin C daily but would like to keep the intake under 60 mg. How much fruit servings would the family have to consume on a daily basis per person to minimize their cost?
	p #[strong Answer :] We begin step-wise with the formulation of the problem first. The constraint variables – ‘x’ = number of banana servings taken and ‘y’ = number of servings of apples taken. Let us find out the objective function now.
	ul
		li Cost of a banana serving = 30/6 rupees = 5 rupees. Thus, the cost of ‘x’ banana servings = 5x rupees
		li Cost of an apple serving = 80/8 rupees = 10 rupees. Thus the cost of ‘y’ apple servings = 10y rupees
	p Total Cost C = 5x + 10y
	p Constraints: x ≥ 0; y ≥ 0 (non-negative number of servings)
	p Total Vitamin C intake: 8.8x + 5.2y ≥ 20 (1) 8.8x + 5.2y ≤ 60 (2)
	h5 us plot a graph with the constraint equations-
	p To check for the validity of the equations, put x=0, y=0 in (1). Clearly, it doesn’t satisfy the inequality. Therefore, we must choose the side opposite to the origin as our valid region. Similarly, the side towards origin is the valid region for equation 2)
	p Feasible Region: As per the analysis above, the feasible region for this problem would be the one in between the red and blue #[a(href='https://www.toppr.com/guides/maths/straight-lines/basics-of-straight-lines/') lines] in the graph! For the #[a(href='https://www.toppr.com/guides/business-studies/directing/elements-of-directing/') direction] of the objective function; let us plot 5x+10y = 50.
	p Now take a ruler and place it on the straight line of the objective function. Start sliding it from the left end of the graph. What do we want here? We want the minimum value of the cost i.e. the minimum value of the optimum function C. Thus we should slide the ruler in such a way that a point is reached, which:
	p 1) lies in the feasible region 2) is closer to the origin as compared to the other points
	p This would be our Optimum Point. I’ve marked it as P in the graph. It is the one which you will get at the extreme right side of the feasible region here. I’ve also shown the position in which your ruler needs to be to get this point by the line in green.
	p Now we must calculate the coordinates of this point. To do this, just solve the simultaneous pair of linear equations:
	p #[em y = 0]#[em 8.8x + 5.2y = 20]
	p We’ll get the coordinates of ‘P’ as (2.27, 0). This implies that the family must consume 2.27 bananas and 0 apples to minimize their cost and function according to their diet plan.
	p: strong Question 2: What is the purpose of a graphical method?
	p #[strong Answer:] We use a graphical method of linear programming for solving the problems by finding out the maximum or lowermost point of the intersection on a graph between the objective function line and the feasible region.
	p: strong Question 3: How do you solve the LPP with the help of a graphical method?
	p #[strong Answer:] We can solve the LPP with the graphical method by following these steps:
	p #[strong 1st Step:] First of all, formulate the LP problem.
	p #[strong 2nd Step:] Then, make a graph and plot the constraint lines over there.
	p #[strong 3rd Step:] Determine the valid part of each constraint line.
	p #[strong 4th Step:] Recognize the possible solution area.
	p #[strong 5thStep:] Place the objective function in the graph.
	p #[strong 6th Step:] Finally, find out the optimum point.
	p: strong Question 4: Define the graphical method for the simultaneous equations?
	p #[strong Answer:] For graphically solving a pair of simultaneous equations, firstly we have to draw a graph of both the equations simultaneously. We have 2 straight lines crossing each other at a common point which provides the solution of this pair of equations.
	p: strong Question 5: What is a graphical interpretation?
	p #[strong Answer:] A graphical interpretation proposes a number of valuable problem-solving methods. For example, finding the greatest value of a nonstop differentiable function ‘f(x)’ defined in some interval ‘an ≤ x ≤ b’.
	| Share with friends


article
	h1 Симплекс метод
	dl
		dt #[abbr(term="Условие допустимости") УД]
		dd В задаче максимизации отсутствие отрицательных коэффициентов в ЦФ, а в задаче минимизации отсутствие положительных
		dt Symplex method
		dd 
			p.intro In the method first express each linear program in the form of a simplex tableau.
			details
				summary #[+LPTASK('x_1 + x_2',String.raw`-x_1 + x_2 \le 1 \\ x_1 \le 3 \\ x_2 \le 2 \\ x_1,x_2 \ge 0`).block]
				p The variables are nonnegative, but the inequalities have to be replaced by equations, by introducing slack variables.#[br]The equational form is #[+LPTASK('x_1 + x_2 + 0x_3 + 0x_4 + 0x_5',String.raw`-x_1 + x_2 + x_3 = 1 \\ x_1 + x_4 = 3 \\ x_2 + x_5 = 2 \\ x_1,x_2,…,x_5 \ge 0`)] with the matrix #[+m A = \begin{pmatrix} -1 & 1 & 1 & 0 & 0 \\ 1 & 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 & 1 \end{pmatrix}]
				p First express linear program in the form of a simplex tableau. In our case begin with the tableau #[+m \begin{array}{ccc} x_3& = 1 + x_1 - x_2 \\ x_4& = 3 - x_1 \\ x_5& = 2 - x_2 \\ \hline z& = x_1+x_2 \end{array}]. The first three rows consist of the equations of the linear program, in which the slack variables have been carried over to the left-hand side and the remaining terms are on the right-hand side. The last row, separated by a line, contains a new variable z, which expresses the objective function. Each simplex tableau is associated with a certain basic feasible solution. In our case we #[mark substitute #[+m 0] for the variables #[+m x_1, x_2] from the right-hand side, and without calculation see that #[+m x_3 = 1, x_4 = 3, x_5 = 2]]. This #[strong feasible solution] is basic with #[+m B = \{3, 4, 5\}] variables indeces. #[note #[+m A_B] is the identity matrix]. The variables #[+m x_3, x_4, x_5] from the left-hand side are basic and the variables #[+m x_1, x_2] from the right-hand side are nonbasic. The value of the objective function #[+m z = 0] corresponding to this basic feasible solution can be read off from the last row of the tableau. 
				p From the initial simplex tableau we will construct a sequence of tableaus of a similar form, by gradually rewriting them according to certain rules. Each tableau will contain the same information about the linear program, only written differently. The procedure terminates with a tableau that represents the information so that the desired optimal solution can be read off directly. 
				p Let us go to the first step. We try to increase the value of the objective function by increasing one of the nonbasic variables #[+m x_1] or #[+m x_2]. In the tableau observe that #[mark increasing the value of #[+m x_1] (i.e. making #[+m x_1] positive) increases the value of #[+m z]]. #[em The same is true for #[+m x_2], because both variables have positive coefficients in the #[+m z]-row of the tableau]. We can choose either #[+m x_1] or #[+m x_2]. Decide #[em (arbitrarily)] increase #[+m x_2], while #[+m x_1] will stay 0.#[br]#[strong How much can we increase #[+m x_2]?] To maintain feasibility, we have to be careful not to let any of the basic variables #[+m x_3, x_4, x_5] go #[em below zero]. This means that the equations determining #[+m x_3, x_4, x_5] may limit the increment of #[+m x_2].#[br]Let us consider the #[strong first equation] #[+m x_3 = 1 + x_1 − x_2]. Together with the implicit constraint #[+m x_3 ≥ 0] it #[mark lets us increase #[+m x_2] up to the value #[+m x_2 = 1]] (while keeping #[+m x_1 = 0]). The #[strong second equation] #[+m x_4 = 3 − x_1] does not limit the increment of #[+m x_2] at all, and the #[strong third equation] #[+m x_5 = 2 − x_2] allows for an increase of #[+m x_2] up to #[+m x_2 = 2] before #[+m x_5] gets negative. The most stringent restriction thus follows from the first equation.
				p.
					We increase #[+m x_2] as much as we can, obtaining #[+m x_2 = 1] and #[+m x_3 = 0]. From the remaining equations of the tableau we get the values of the other variables:
					#[+m \begin{aligned} x_4 =3−x_1=3 \\ x_5 =2−x_2=1\end{aligned}]. In this new feasible solution #[+m x_3] became zero and #[+m x_2] nonzero. Quite naturally we thus transfer #[+m x_3] to the right-hand side, where the nonbasic variables live, and #[+m x_2] to the left-hand side, where the basic variables reside. We do it by means of the most stringent equation #[+m x_3 = 1 + x_1 − x_2], from which we express #[+m x_2 = 1 + x_1 − x_3].
					We substitute the right-hand side for #[+m x_2] into the remaining equations, and
					we arrive at a new tableau: #[+m \begin{array}{ccc} x_2 &= 1 + x_1 − x_3 \\ x_4 &= 3 − x_1 \\ x_5 &= 1 − x_1 +x_3 \\ \hline z &= 1 + 2x_1 − x_3 \end{array}]
					Here #[+m B = \{2,4,5\}], which corresponds to the basic feasible solution #[+m x = (0, 1, 0, 3, 1)] with the value of the objective function #[+m z = 1].#[br]This process of rewriting one simplex tableau into another is called a #[dfn pivot step]. In each pivot step some nonbasic variable, in our case #[+m x_2], enters the basis, while some basic variable, in our case #[+m x_3], leaves the basis.#[br]In the new tableau we can further increase the value of the objective function by increasing #[+m x_1], while increasing #[+m x_3] would lead to a smaller #[+m z]-value. The first equation does not restrict the increment of #[+m x_1] in any way, from the second one we get #[+m x_1 ≤ 3], and from the third one #[+m x_1 ≤ 1], so the strictest limitation is implied by the third equation. Similarly as in the previous step, we express #[+m x_1] from it and we substitute this expression into the remaining equations. Thereby #[+m x_1] enters the basis and moves to the left-hand side, and #[+m x_5] leaves the basis and migrates to the right-hand side.#[br]The tableau we obtain is 
					#[+m \begin{array}{ccc} x_1 = 1 + x_3 − x_5 \\ x_2 = 2 − x_5 \\ x_4 = 2 − x_3 + x_5 \\ \hline z = 3 + x_3 − 2x_5 \end{array}] with #[+m B = \{1,2,4\}], basic feasible solution #[+m x = (1,2,0,2,0)], and #[+m z = 3]. After one more pivot step, in which #[+m x_3] enters the basis and #[+m x_4] leaves it, we arrive at the tableau
					#[+m \begin{array}{ccc} x_1 =3 − x_4 \\ x_2 = 2 − x_5 \\ x_3 =2−x_4 +x_5 \\ \hline z = 5 − x_4 − x_5 \end{array}] with basis #[+m {1, 2, 3}], basic feasible solution #[+m x = (3, 2, 2, 0, 0)], and #[+m z = 5]. In this tableau, no nonbasic variable can be increased without making the objective function value smaller, so we are stuck. Luckily, this also means that we have already found an optimal solution! Why?#[br]Let us consider an arbitrary feasible solution #[+m \tilde x = (\tilde{x_1},…,\tilde{x_5})] of our linear program, with the objective function attaining some value #[+m \tilde z]. Now #[+m \tilde x] and #[+m z] satisfy all equations in the final tableau, which was obtained from the original equations of the linear program by equivalent transformations. Hence we necessarily have #[+m \tilde z = 5 − \tilde {x_4} − \tilde {x_5}].#[br]Together with the nonnegativity constraints #[+m x_4,x_5 ≥ 0] this implies #[+m z ≤ 5]. The tableau even delivers a #[em proof] that #[+m x = (3, 2, 2, 0, 0)] is the only optimal solution: #[mark If #[+m z = 5], then #[+m x_4 = x_5 = 0], and this determines the values of the remaining variables #[strong uniquely]].
	section
		hgroup
			h4 Special cases or Exception Handling
			+source(links=['https://www.ques10.com/p/7790/special-cases-in-lpp/'])
		dl
			dt Infeasibility
			dd
				p.intro In order that the simplex method be able to start at all, we need a feasible basis. #[note In linear programs of the #[strong form] #[+m \vb c^T\vb x \to \max] subject to #[+m A \vb x ≤ b] and #[+m \vb x ≥ 0] with #[+m \vb b ≥ 0] we get free feasible basis. Indeed, the indices of the slack variables introduced in the transformation to equational form can serve as a feasible basis.]#[br]#[small However, in general, finding any feasible solution of a linear program is equally as difficult as finding an optimal solution]. Computing the initial feasible basis can be done by the simplex method itself, if we apply it to a suitable auxiliary problem.
				p This occurs when the entire iteration has ended, but an artificial variable is still present in the base. Such a solution is a false solution.
				details.example
					summary: +LPTASK('x_1 + 2x_2',String.raw`x_1+3x_2+x_3\eq4 \\ 2x_2+x_3=2\\ x_1,x_2,x_3 ≥0`)
					ol
						li Produce a feasible solution starting with #[+m() (x_1, x_2, x_3) = (0, 0, 0)]. This vector is #[em nonnegative], but of course it is #[strong not feasible], since it does not satisfy the equations of the linear program. 
						li Introduce auxiliary variables #[+m x_4] and #[+m x_5] as “corrections” of infeasibility: #[+m x_4 =4−x_1−3x_2−x_3] expresses by how much the original variables #[+m x_1, x_2, x_3] fail to satisfy the first equation, and #[+m x_5 = 2 − 2x_2 − x_3] plays a similar role for the second equation. #[mark If we managed to find nonnegative values of #[+m x_1,x_2,x_3] for which both of these corrections come out as zeros, we would have a feasible solution of the considered linear program].
						li The task of finding nonnegative #[+m x_1, x_2, x_3] with zero corrections can be captured by a linear program: #[+m \begin{aligned} − x_4 − x_5 \to \max\\ x_1 +3x_2 + x_3 +x_4 =4 \\ 2x_2 + x_3 + x_5 = 2\\ x_1,x_2,...,x_5 ≥ 0 \end{aligned}]
						li The optimal value of the objective function #[+m −x_4 − x_5] is 0 exactly if there exist values of #[+m x_1,x_2,x_3] with zero corrections, i.e., a feasible solution of the original linear program. This is the #[strong right auxiliary linear program]. The variables #[+m x_4] and #[+m x_5] form a feasible basis, with the basic feasible solution #[+m () (0,0,0,4,2)]. #[small Here we use that the right-hand sides, 4 and 2, are nonnegative, but since we deal with equations, this can always be achieved by sign changes]. Once we express the objective function using the nonbasic variables, that is, in the form #[+m z = −6 + x_1 + 5x_2 + 2x_3], we can start the simplex method on the auxiliary linear program.
						li The auxiliary linear program is surely bounded, since the objective function cannot be positive. The simplex method thus computes a basic feasible solution that is optimal. As training the reader can check that if we let #[+m x_1] enter the basis in the first pivot step and #[+m x_3] in the second, the final simplex tableau comes out as #[+m x_1 = 2 − x_2 − x_4 + x_5 x_3 = 2 − 2x_2 − x_5 z = − x_4 − x_5].
						li The corresponding optimal solution #[+m () (2, 0, 2, 0, 0)] yields a basic feasible solution of the original linear program: #[+m () (x_1 , x_2 , x_3 ) = (2, 0, 2)]. The initial simplex tableau for the original linear program can even be obtained from the final tableau of the auxiliary linear program, by leaving out the columns of the auxiliary variables #[+m x_4] and #[+m x_5], and by changing the objective function back to the original one, expressed in terms of the nonbasic variables: #[+m \begin{aligned}x_1 =2− x_2 \\ x_3 =2−2x_2 \\ \hline z = 2 + x_2 \end{aligned}]. #[small Starting from this tableau, a single pivot step already reaches the optimum].
			dt: dfn Degeneracy
			dt: dfn Вырожденность
			dd 
				p В ходе выполнения симплекс-метода проверка УД может привести к неоднозначному выбору исключаемой переменной, то есть #[+m \theta] нескольких ограничений будут одинаковы. И на следующей итерации одна или несколько базисных переменных примут нулевое значение. Тогда новое решение будет вырожденным. зам В вырожденном решении нет никакой опасности, за исключением небольших теоретических неудобств. С практической точки зрения вырожденность объясняется тем, что в исходной задаче присутствует по крайней мере одно избыточное ограничение
				p Occurs when #[strong one or more of the variables in the base have zero value in the RHS column, or during any stage in the iteration, when there is a tie in the #[+m \theta] values of two rows].
				details
					summary: +LPTASK('3x_1+9x_2',String.raw`x_1+4x_2 \le 8 \\ x_1+2x_2 \le 4 \\ x_1,x_2 \ge 0`)
					img(src="./Симплекс-таблица с оптимальным вырожденным решением.png")
					p На начальной итерации в качестве исключаемой можно выбрать как переменную #[+m x_3], так и #[+m х_4],. Если оставить в базисе переменную #[+m x_4] на следующей итерации она примет значение 0, т.е. получим вырожденное базисное решение. Оптимальное решение получается на следующей итерации.
					p Что же практически приводит к вырожденности решения? В графическом представлении решении этой задачи. Точка оптимума #[+m x_1=0, x_2=2] - пересечение трех прямых. Поскольку данная задача двухмерна, эта точка переопределена (на плоскости для определения точки достаточно двух прямых), и, следовательно, одно из ограничений избыточно.
					img(src="./Пример графического оптимального вырожненого решения.png")
					p На практике информация о том, что некоторые ресурсы недефицитны, может быть полезной при интерпретации результатов решения задачи. Эти сведения также могут помочь выявить неточности и ошибки в постановке исходной задачи. К сожалению, не существует способов определить избыточное ограничение непосредственно из данных симплекс-таблиц.
					p С вычислительной и теоретической точек зрения вырожденность может привести к: 
					ol
						li В процессе вычислений может возникнуть зацикливание. Если в приведенной выше таблице сравнить первую и вторую итерации, то можно заметить, что значение ЦФ не изменилось (#[+m z= 18]). Поэтому может возникнуть ситуация, когда при реализации симплекс-метода некоторая последовательность будет повторяться, не изменяя значения целевой функции и не приводя к завершению вычислительного процесса. Существуют методы, предотвращающие зацикливание, однако они значительно замедляют процесс вычислений. Поэтому в большинстве программ, реализующих симплекс-метод, отсутствуют специальные средства защиты от зацикливания, тем более, что вероятность зацикливания очень мала.
						li Во-вторых, последствие вырожденности решения можно обнаружить, сравнивая первую и вторую итерации в приведенной выше таблице. Хотя в этих итерациях состав базисных и небазисных переменных различен, значения всех переменных и значение целевой функции не изменяются:
					p #[+m x_1 = 0, x_2 = 2, x_3= 0, x_4 = 0, z= 18]
					p Можно ли, несмотря на то, что оптимальное решение не достигнуто, остановить вычисления на первой итерации (когда впервые обнаруживается вырожденность)? Ответ отрицательный, так как решение может быть только временно вырожденным.
			dt: dfn Связывающее неравенство
			dd неравенство которое в точке оптимума выполняется как точное равенство
			dt(lang="en"): dfn Alternate optimum
			dt: dfn Альтернативные оптимальные решения
			dd 
				p #[strong If a non-basic variable has #[+m C_j-Z_j] value as zero, there exists an alternate optimum solution]. 
				img(src="./Альтернативные решения таблица.png")
			dd 
				p Graphically, if the objective function is parallel to a binding constraint, then the same optimal value is obtained at more than one corner points.
				p доступен диапазон оптимальных решений. #[i На примере графического метода] Возникает когда прямая ЦФ параллельна прямой, соответствующей связывающему неравенству, ЦФ принимает одно и тоже оптимальное значение на некотором множестве точек границы пространства решений, то есть имеет альтернативные оптимальные решения. Следующий пример показывает, что таких решений(если они существуют) бесконечное множество. Этот пример также проиллюстрирует практическую значимость альтернативных решений.
				img(src="./Альтернативные решения на графике.png")
				p множество альтернативных оптимальных решений - следствие того, что прямая ЦФ параллельна прямой, соответствующей связывающему ограничению
			dt: dfn Unbounded solution
			dd An unbounded solution occurs when it is not possible to select the variable which should leave the base. This happens when there is no non-negative #[+m \theta] value. In such a case, the value of the entering variable can be increased indefinitely, without violating any constraint. So the solution space in the graph is said to be unbounded.
			dt: dfn Unrestricted(Unconstrained) variable
			dd Some variables may be encountered where they can take any value, positive or negative. To take care of such variables, they are substituted with 2 other variables, that themselves are non-negative, but whose difference may be negative.



		










section
	h2 FAQ

	dl
		dt Зачем нужны ограничения если оптимальное решение только на вершинах многоугольника 
		dd Чтобы найти этот многоугольник!! Привести пример сложной системы графиков где точка (0,0) не является допустимым решением и сделать подводку к нахождению начального базисного решения 
		dt Как происходит перемещение из точки в точку с помощью введения в базис переменных
		dd 
			p Доказательство того что уменьшив или увеличив на какое-то число, то просто ее пересечения с осями сместятся на это число, а не в конец перпендикулярного этой прямой вектора с длинной этого числа. Это можно логически доказать как если бы у нас было уравнение состоящее из целых чисел #[+m x,y,s\in Z:x+y+s=\const], то если бы добавочная переменная 
			p Переводя какую-либо переменную в базис #[+m \begin{cases}s_1=\const_1+ \alpha_1 x+\beta_1 y\\ s_2=\const_2+ \alpha_2 x+\beta_2 y \end{cases} \Rightarrow \begin{cases}x=(\const_1+\beta_1 y - s_1)/\alpha_1\\ s_2=\const_2+ \alpha_2 (\const_1+\beta_1 y - s_1)/\alpha_1+\beta_2 y \end{cases}] мы двигаем второй график на величину #[+m \frac{\alpha_2\const_1}{\alpha_1}] и в случае если бы графиком было #[+m m], то все бы они также подвинулись на эту величину, #[mark то есть: #[strong вводя переменную в базис все ограничения двигуются из исходной точки в направлении оси представляющей переменную на величину ] #[+m \frac{\alpha_2\const_1}{\alpha_1}]]
			p В уравнение #[+m \alpha_1x_1+\alpha_2x_2+…+\alpha_nx_n + s = \const] каждая единица #[+m= s] смещает график на #[+m \pm \frac{s}{\const}] это следует из #[+m= String.raw`p\in [1,n],i=\overline{1,n},\forall i\ne p,x_i = 0: \alpha_1x_1+\alpha_2x_2+…+\alpha_2x_2+…+\alpha_nx_n + s = \const \Leftrightarrow \alpha_10+\alpha_20+…+\alpha_px_p+…+\alpha_n0 + s = \alpha_px_p + s = \const \Rightarrow x_p = \frac{\const-s}{\alpha_p} =\frac{\const}{\alpha_p}-\frac{s}{\alpha_p}`], то есть чтобы пересечение по оси #[+m x_p] было в точке ноль нужно обнулить чтобы выполнялось равенство #[+m \frac{\const}{\alpha_p}=\frac{s}{\alpha_p}], которое выполняется только при #[+m \const = s]
			p Сколько прямых столько и выбор на сколько сместиться по оси, то есть например если мы выбираем на сколько сместится по оси #[+m x], то у нас стоит выбор между количеством точек равным количеству прямых ограничений, так как они все пересекаются с этой осью #[small если они не паралельны ей] #[+m \begin{cases}\alpha_1x_1+…\\\alpha_2x_2+…\\\vdots\\\alpha_mx_m+…\end{cases}]




section
	hgroup 
		h5 There is no initial basis in the Simplex tableau 
		a(book="Linear Programming: Theory and Applications Catherine Lewis May 11, 2008" chapter="8. What if there is no initial basis in the Simplex tableau?")
		p.intro What does one do when the initial tableau contains no starting basis?
	p(title="Причины") This problem occurs when the constraints are in either equality or “greater than or equal to” form. In the case of an equality constraint, one cannot add a slack or an excess variable and therefore there will be no initial basic variable in that row. In the case of a “greater than or equal to” constraint, one must add an excess variable, which gives a −1 in that row instead of a +1. #[small Simply multiplying through that row by −1 would not solve the problem, for then the right-hand-side variable would be negative].#[br]#[em There are two main methods to dealing with this problem]: the #[dfn Two-Phase Method] and the #[dfn Big-M Method]. Both of these methods involve adding #[dfn artificial] variables that start out as basic variables but #[mark #[strong must] eventually equal zero in order for the original problem to be feasible].
	dl
		dt: dfn Two-Phase Method
		dd
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
			section.example
				p.
					Consider the following problem:
					#[+m \begin{aligned} \text{Maximize} \quad & z=2x_1 − x_2 + x_3 \\ \text{subject to} \quad & 2x_1 + x_2 − 2x_3 ≤ 8 \\ & 4x_1−x_2+2x_3 = 2 \\ & 2x_1+3x_2−x_3 ≥ 4 \\ & x_1,x_2,x_3 ≥ 0 \\ \end{aligned}]
				ol
					li
						p To put this in standard form, all constraints must become equalities. Adding a slack variable, #[+m= s_1], to the first constraint and subtracting an excess variable #[+m e_3] from the third constraint gives the initial Simplex tableau. 
						+m.right \begin{array}{c|ccccc|c} 1 & -2 & 1 & -1 & 0 & 0 & 0 \\ \hline 0 & 2 & 1 & -2 & 0 & 1 & 8 \\ 0 & 4 & -1 & 2 & 0 & 0 & 2 \\ 0 & 2 & 3 & -1 & -1 & 0 & 4 \end{array}
					li
						p #[strong There is no initial basis in this tableau]. To correct this, add two more variables, called #[dfn artificial variables] #[+m a_1] and #[+m a_3], to constraints two and three. This step alone however, will not solve the problem since these two extra variables cannot be in the final basis. Therefore, in addition to adding two artificial variables, the initial objective function must be altered as well. To ensure that #[+m a_1] and #[+m a_3] are not in the final basis, the initial objective function must become “minimize #[+m z = -a_1 − a_3]”. 
						+m.right \begin{array}{c|ccccccc|c} 1 & 0 & 0 & 0 & 0 & 0 & -1 & -1 & 0 \\ \hline 0 & 2 & 1 & -2 & 0 & 1 & 0 & 0 & 8 \\ 0 & 4 & -1 & 2 & 0 & 0 & 1 & 0 & 2 \\ 0 & 2 & 3 & -1 & -1 & 0 & 0 & 1 & 4 \end{array}
					li
						p The last step before performing the Simplex algorithm as usual, is to add rows 2 and 3 to Row 0. The tableau in Table 5 is better because #[+m I_3] is in the body of the tableau. This tableau is the initial tableau for Phase I of the Two Phase Method. 
						+m.right \begin{array}{c|ccccccc|c} 1 & 6 & 2 & 1 & -1 & 0 & 0 & 0 & 6 \\ \hline 0 & 2 & 1 & -2 & 0 & 1 & 0 & 0 & 8 \\ 0 & 4 & -1 & 2 & 0 & 0 & 1 & 0 & 2 \\ 0 & 2 & 3 & -1 & -1 & 0 & 0 & 1 & 4 \end{array}
					li
						p Phase I will be complete when this tableau is optimal. To get this tableau to optimality takes two steps. In new tableau the variables #[+m a_1] and #[+m a_3] are zero and the variables #[+m x_1], #[+m x_2] and #[+m= s_1] are basic.
						+m.right \begin{array}{c|ccccccc|c} 1 & 0 & 0 & .6 & -.3 & 0 & -.8 & -1.4 & .8 \\ \hline 0 & 0 & 0 & -2.6 & .2 & 1 & -.25 & .2 & 6.4 \\ 0 & 1 & 0 & .3 & -.1 & 0 & .2 & .10 & .8 \\ 0 & 0 & 1 & -.8 & -.4 & 0 & -.2 & .4 & 1.2 \end{array}
					li
						p For #[strong Phase II], replace the current objective function with the objective function from the original problem and make all entries of Row 0 in the column of a basic variable equal to zero. Also, delete all columns associated with artificial variables. After that, proceed with the Simplex algorithm until optimality is reached. The first tableau for Phase II is shown in the first part of tableau. After multiplying Row 2 by two, Row 3 by negative one, and adding both of the resultant rows to Row 0, the tableau becomes like the second part of Table 7. After obtaining this tableau, proceed with the Simplex algorithm as usual. Remember, now the objective function must be maximized. The solution to this phase is the solution to the original problem.
						+m.
							\begin{array}{c|ccccc|c}
							1 & -2 & 1 & -1 & 0 & 0 & 0 \\ 
							\hline
							0 & 0 & 0 & -2.6 & .2 & 1 & 6.4 \\ 
							0 & 1 & 0 & .3 & -.1 & 0 & .8 \\ 
							0 & 0 & 1 & -.8 & -.4 & 0 & 1.2 \\
							\\
							\\
							1 & 0 & 0 & .4 & .2 & 0 & .4 \\ 
							\hline
							0 & 0 & 0 & -2.6 & .2 & 1 & 6.4 \\ 
							0 & 1 & 0 & .3 & -.1 & 0 & .8 \\ 
							0 & 0 & 1 & -.8 & -.4 & 0 & 1.2
							\end{array}


		dt: dfn Big-M Method
		dd
			details
				summary #[+LPTASK('x_1 − 2x_2',String.raw`x_1+x_2 ≥ 2 \\ −x_1+x_2 ≥ 1 \\ x_2 ≤ 3 \\ x_1,x_2 ≥ 0`)] Wouldn’t it be nice to be able to solve this problem with artificial variables, but without having to complete two phases? Well, the Big-M method makes that possible.
				ol
					li: +LPTABLE([[1, -1, 2, 0, 0, 0, 0],[0, 1, 1, -1, 0, 0, 2],[0, -1, 1, 0, -1, 0, 1],[0, 0, 1, 0, 0, 1, 3]])
					li: +LPTABLE([[1, -1, 2, 0, 0, 0, 0, 0, 0],[0, 1, 1, -1, 0, 0, 1, 0, 2],[	0, -1, 1, 0, -1, 0, 0, 1, 1],[	0, 0, 1, 0, 0, 1, 0, 0, 3]])
					li: +LPTABLE([[1, -1, 2, 0, 0, 0, '-M', '-M', 0],[0, 1, 1, -1, 0, 0, 1, 0, 2],[	0, -1, 1, 0, -1, 0, 0, 1, 1],[	0, 0, 1, 0, 0, 1, 0, 0, 3 ]])
					li: +LPTABLE([[1, -1, '2+2M', '-M', '-M', 0, 0, 0, '3M'],[0, 1, 1, -1, 0, 0, 1, 0, 2],[	0, -1, 1, 0, -1, 0, 0, 1, 1],[	0, 0, 1, 0, 0, 1, 0, 0, 3 ]])
					li: +LPTABLE([[1, '1+2M', 0, '-M', '2+M', 0, 0, '-2-2M', '-2+M'],[0, 2, 0, -1, 1, 0, 1, -1, 1],[	0, -1, 1, 0, -1, 0, 0, 1, 1],[	0, 1, 0, 0, 1, 1, 0, -1, 2 ]])
					li: +LPTABLE([[1, -1, 0, 0, 0, -2, '-M', '-M', -6],[0, 1, 0, 0, 1, 1, 0, -1, 2],[	0, 0, 1, 0, 0, 1, 0, 0, 3],[	0, -1, 0, 1, 0, 1, -1, 0, 1 ]])
				p First, the initial tableau of this problem is shown in Table 6. After adding artificial variables #[+m a_1] and #[+m a_2] to rows 1 and 2, the tableau becomes the tableau in the first part of Table 8. Since the artificial variables must go to zero at optimality, there must be a way to force them to do so. By adding Ma_1 +Ma_2 to the objective function, where #[+m M] is a really big number (near infinity!, it is clear that this minimization problem will be optimal when #[+m a_1] and #[+m a_2] are zero. For a maximization problem, adding −Ma_1 − Ma_2 to the objective function produces the same effect. This step is shown in the second part of Table 9.
				p Next, the coefficients in Row 0 must be modified so that they are zero for all basic variables. Therefore, multiply rows 1 and 2 by #[+m M] and add them to Row 0. The resulting tableau is shown in the third part of Table 9.
				p The most positive coefficient in Row 0 is 2 + 2M . Therefore, this column is selected for a pivot and the ratio test is performed as usual. Row 2 wins the ratio test and the next tableau is shown in the fourth part of Table 9. The term 1 + 2M is the most positive so that column is the pivot column. This part of the Big-M Method is just like performing the Simplex Method as usual, except with a variable #[+m M] floating around. This particular problem continues for a few more steps (two more pivots to be exact) before reaching optimality. The optimal tableau is shown in the fifth part of Table 9, where the solution is x_2 =3, x_3 =1, x_4 =2andz=−6.
				p In this tableau, there is no #[+m M] in the objective function value. Also, none of the artificial variables are basic variables. If an artificial variable were a basic variable in the optimal tableau, this would indicate that the the original problem was infeasible. If there were an #[+m M] in the objective function value, this would indicate that the original problem was unbounded.
				p In summary, the Big-M Method can be completed using the following steps:
				ol
					li If there is no basis in the original tableau, add artificial variables to rows in which there are no slack variables.
					li Depending on whether the problem is minimization or maximization, add or subtract Mxa to the objective function where #[+m M] is a really big number and xa is a vector of the artificial variables.
					li Modify the tableau so that the Row 0 coefficients of the artificial variables are zero.
					li Complete the Simplex algorithm as usual.
					li At optimality, the artificial variables should be nonbasic variables and the objective function value should be finite.






	figure
		iframe(src="http://www.lokminglui.com/lpch4.pdf" width="80%" height="40vw" frameborder="0") 
		figcaption: h1 Special methods
	figure
		iframe(src="{book_1}", frameborder="0" width="80%" height="40vh")
		figcaption: h1 Simplex Method Special Cases
	h3 SPECIAL CASES IN APPLYING SIMPLEX METHODS
		+source(links=['http://www.lokminglui.com/lpch4.pdf'])
	//- dl
		dt: dfn No Feasible Solutions
		dd
			p In terms of the methods of artificial variable techniques, the solution at optimality could include one or more artificial variables at a positive level #[eg as a non-zero basic variable]. In such a case the corresponding constraint is violated and the artificial variable cannot be driven out of the basis. The feasible region is thus empty.
			details.example
				summary Example
				p Consider the following linear programming problem.#[+LPTASK('2x_1+x_2',String.raw`x_1 + x_2 ≥ 2 \\ x_1 + x_2 ≤ 1 \\ x_1, x_2 ≥ 0`)]
				p Using a surplus variable #[+m x_3], an artificial variable #[+m x_4] and a slack variable #[+m x_5], the augmented system is #[+m \begin{aligned}x_1 + x_2 - x_3 + x_4&=2 \\ x_1 + x_2 + x_5&=1 \\ z - 2x_1 - x_2 + Mx_4&=0\end{aligned}]
				p Now the columns corresponding to x_4 and x_5 form an identity matrix. In tableau form, we have
				table
					tr
						td #[+m x_1]
						td #[+m x_2]
						td #[+m x_3]
						td #[+m x_4]
						td #[+m x_5]
						td #[+m \mathbb{B}]
					tr
						td #[+m x_4]
						td -1
						td 1
						td -1
						td 1
						td 0
						td 2
					tr
						td #[+m x_5]
						td 1
						td 1
						td 0
						td 0
						td 1
						td 1
					tr
						td #[+m z]
						td -2
						td -1
						td 0
						td #[+m M]
						td 0
						td 0
				p After elimination of the M in the x_4 column, we have the initial tableau:
				table
					tr
						td #[+m x_1]
						td #[+m x_2]
						td #[+m x_3]
						td #[+m x_4]
						td #[+m x_5]
						td #[+m \mathbb{B}]
					tr
						td #[+m x_4]
						td -1
						td 1
						td -1
						td 1
						td 0
						td 2
					tr
						td #[+m x_5]
						td 1
						td 1
						td 0
						td 0
						td 1
						td 1
					tr
						td #[+m z]
						td -2
						td -1
						td 0
						td #[+m M]
						td 0
						td 0
				table
					tr
						td
							p 1
							p 1
						td
							p 1
							p 1�-
						td
							p 1
							p 0
						td
							p 1
							p 0
						td
							p 0
							p 1
						td
							p 2
							p 1
					tr
						td: p 2 + M
						td: p 1 M
						td: p M
						td: p 0
						td: p 0
						td: p 2M
					p
						p x_4 x_5 x_0
						p 1
						p x + x=2
						p 1 2
						p x +x=1
						p 1 2
						p
							p 3.5
							p 3
							p 2.5
							p 2
							p 1.5
							p 1
							p 0.5
							p 0
							p 0.5
							p 1
							p 2 1.5 1 0.5 0 0.5 1 1.5 2 2.5 3
							h5 Figure 4.1. #[i No Feasible Region]
							table
								tr
									td
										p 2
										p 1
									td
										p 0
										p 1
									td
										p 1
										p 0
									td
										p 1
										p 0
									td
										p 1
										p 1
									td
										p 1
										p 1
								tr
									td: p 1 + 2M
									td: p 0
									td: p M
									td: p 0
									td: p 1 + M
									td: p 1 M
							p x_1 x_2 x_3 x_4 x_5 b
							p x_4 x_2 x_0
							p Since M is a very large number, 1+2M is positive. Hence all entries in the x_0 row are nonnegative. Thus we have reached an optimal point. However, we see that the artificial variable x_4 =1, which is not zero. That means that the solution just found is not a solution to our original problem. Indeed the #[b x]that satisfies A#[b x]+ I#[b x]a =#[b b]with #[b x]a /=0 is not a solution to A#[b x]=#[b b]. Figure 4.1 shows that the feasible region to the problem is empty.
		//- li
			h4 Unbounded Solutions
			p Theorem 4.1. Consider an LPP in feasible canonical form. If in the simplex tableau, there exists a nonbasic variable xj such that yij ≤ 0 for all i =1, 2, · · · , m, i.e. all entries in the xj column are non positive, then the feasible region is unbounded. If moreover that zj cj < 0, then there exists a feasible solution with at most m + 1 variables nonzero and the corresponding value of the objective function can be set arbitrarily large.
			p #[i Proof.]Let #[b x]B be the current BFS with B#[b x]B =#[b b]. Let the columns of B be denoted by #[b b]i. Then we have
			p m
			p
				p BxB =Σ xBi bi =b.
				p i=1
				p
					p 4.2. Unbounded Solutions 3
					p Let #[b a]j be the column of A that corresponds to the variable xj. By (#[b ??]), we have
					p Hence for all θ > 0, we have
					p aj =Byj =Σ yijbi.
					p m
					p
						p i=1
						p m
						p
							p b =Σ xBi bi θaj + θaj
							p i=1
							p m m
							p =Σ xBi bi θ Σ yijbi + θaj
							p i=1 m
							p i=1
							p =Σ(xBi θyij)#[b b]i + θ#[b a]j .
							p i=1





</template>