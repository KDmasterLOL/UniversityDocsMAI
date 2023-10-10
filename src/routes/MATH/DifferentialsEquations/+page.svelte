<script>
	import Math from '$lib/components/Math.svelte';
</script>
<template lang="pug">
article: include ./temp
article: include ../tables
h3 Differential Equations
	+source(links=['https://www.mathsisfun.com/calculus/differential-equations.html','https://www.mathsisfun.com/calculus/second-derivative.html','https://www.mathsisfun.com/calculus/differential-equations-solution-guide.html','https://www.mathsisfun.com/algebra/degree-expression.html'])

dl 
	dt: dfn Differential Equation #[+m F(x,y,y',y'',…,y^{(n)}) = F(x,y,\ddv yx,\ddvd 2yx,…,\ddvd {(n)}yx) = 0]
	dd
		p An equation with a function and one or more of its derivatives.
			| #[br]#[em Usage]: Can describe how populations change, how heat moves, how springs vibrate, how radioactive material decays and much more. They are a very natural way to describe many things in the universe.
		p(title="What To Do With Them?") On its own, a Differential Equation is a wonderful way to express something, but is hard to use. So we try to #[em solve] them by turning the Differential Equation into a simpler equation without the differential bits, so we can do calculations, make graphs, predict the future, and so on.
		
		figure
			figcaption
				h1 Why Are Differential Equations Useful?
				p In our world things change, and #[b describing how they change] often ends up as a Differential Equation:
			details
				summary Rabbits!
				img(alt="alt string" src='https://www.mathsisfun.com/calculus/images/rabbits.jpg').no-invert
				p: mark The more rabbits we have the more baby rabbits we get. Then those rabbits grow up and have babies too! #[strong The population will grow faster and faster].
				ul(title="The important parts:")
					li The population #[+m N] at any time #[+m t] - #[+m N(t)]
					li The growth rate - #[+m r]
					li The population's #[+m N] rate of change - #[+m \ddv Nt], Think of it as "how much the population changes as time changes, for any moment in time".
				p Let us imagine the growth rate #[+m r = 0.01] new rabbits per week #[strong for every current rabbit.]. When the population #[+m N = 1000], then the rate of change #[+m \ddv Nt = 1000×0.01 = 10] #[strong new rabbits] per week. #[mark But that is #[strong only true] at a #[em specific time], and #[strong doesn't include that the population is #[em constantly] increasing]. #[strong The bigger the population, the more new rabbits we get!]] When the population #[+m N=2000] we get #[+m 2000×0.01 = 20] new rabbits per week, etc.
				p So it is better to say the rate of change (at any instant) is the growth rate times the population at that instant: #[mark #[+m \ddv Nt = rN]. And that is a #[em Differential Equation], because it has a function #[+m N(t)] and its derivative].#[br]And how powerful mathematics is! That short equation says "the rate of change of the population over time equals the growth rate times the population".
			details
				summary Compound Interest
				img(alt="alt string" src='https://www.mathsisfun.com/money/images/coin-stack-add.jpg').no-invert
				p Money earns interest. The interest can be calculated at fixed times, such as yearly, monthly, etc. and added to the original amount.#[br]This is called #[a(href='https://www.mathsisfun.com/money/compound-interest.html'): dfn compound interest].
				p But when it is compounded #[b continuously] then at any time the interest gets added in proportion to the current value of the loan (or investment).
				p And as the loan grows it earns more interest.
				p Using #[+m t] for time, #[+m r] for the interest rate and #[+m V] for the current value of the loan: #[+m \dd V \dd t = rV]
				p: i And here is a cool thing: it is the same as the equation we got with the Rabbits! It just has different letters. So mathematics shows us these two things behave the same.
				p: b Solving
				p The Differential Equation says it well, but is hard to use.
				p But don't worry, it can be solved (using a special method called #[a(href='https://www.mathsisfun.com/calculus/separation-variables.html') Separation of Variables]) and results in: #[+m V = Pe]
				p Where #[+m P] is the Principal (the original loan), and e is #[a(href='https://www.mathsisfun.com/numbers/e-eulers-number.html') Euler's Number].
				p So a continuously compounded loan of 1,000 for 2 years at an interest rate of 10% becomes: #[+m V = 1000 × eV = 1000 × 1.22140...V = 1,221.40] (to the nearest cent)
				p So Differential Equations are great at describing things, but need to be solved to be useful.
				h4 More Examples of Differential Equations
				h5 The Verhulst Equation
				img(alt="alt string" src='https://www.mathsisfun.com/calculus/images/rabbits.jpg').no-invert
				h5 Example: Rabbits Again!
				p Remember our growth Differential Equation: #[+m \ddv Nt = rN]
				p Well, that growth can't go on forever as they will soon run out of available food.
				p So let's improve it by including:
				ul: li the maximum population that the food can support #[+m k]
				p A guy called Verhulst figured it all out and got this Differential Equation: #[+m \ddv Nt = rN(1−N/k)]
				p: i: b The Verhulst Equation
			details
				summary Simple Harmonic Motion
				dl 
					dt Simple Harmonic Motion
					dd In Physics: A type of periodic motion where the restoring force is directly proportional to the displacement. An example of this is given by a mass on a spring.
				img(alt="alt string" src='https://www.mathsisfun.com/calculus/images/spring-mass.svg').right
				p A spring gets a weight attached to it:
				ul
					li the weight gets pulled down due to gravity
					li as the spring stretches its tension increases
					li the weight slows down
					li then the spring's tension pulls it back up
					li then it falls back down, up and down, again and again
				h1 Describe this with mathematics!
				p #[b The weight] is pulled down by gravity, and we know from #[a(href='https://www.mathsisfun.com/physics/force.html') Newton's Second Law] that force equals mass times acceleration #[+m F=ma] and #[a(href='https://www.mathsisfun.com/measure/metric-acceleration.html') acceleration] is the #[a(href='https://www.mathsisfun.com/calculus/second-derivative.html') second derivative] of position with respect to time, so #[+m F = m \ddvd 2xt]
				p #[b The spring] pulls it back up based on how stretched it is (#[+m k] is the spring's stiffness, and #[+m x] is how stretched it is): #[b F = -kx]
				p The two forces are always equal: #[mark #[+m m \ddvd 2xt = −kx]. We have a differential equation! It has a function #[+m x(t)], and it's second derivative #[+m \ddvd 2xt]]
				figure
					iframe(src='https://www.mathsisfun.com/physics/ispring.html' width="380px" height="400px")
					figcaption We haven't included "damping" (the slowing down of the bounces due to friction), which is a little more complicated, but you can play with it here (press #[b play]):
				p #[b Creating] a differential equation is the first major step. But we also need to #[b solve] it to discover how, for example, the spring bounces up and down over time.
		
		figure
			figcaption: h1 Solving 
			p #[mark We solve it when we discover #[em the function #[+m y] (or set of functions)]]. There are many #[em tricks] to solving Differential Equations #[small if they can be solved].#[br]
				span.intro So how do we exactly solve them? #[small It isn't always easy!] Over the years wise people have worked out #[em special] methods to solve #[em some types] of Differential Equations. So we need to know #[b what type] of Differential Equation it is first. #[small It is like travel: different kinds of transport have solved how to get to certain places. Is it near, so we can just walk? Is there a road so we can take a car? Or is it in another galaxy and we just can't get there yet?] #[strong So let us first #[b classify the Differential] Equation].
dl
	dt: dfn: abbr(title="Ordinary Differential Equations") ODEs
	dd have #[b a single independent variable] (like #[+m y])
	dt: dfn: abbr(title="Partial Differential Equations") PDEs
	dd have two or more independent variables.
h5 Order and Degree
img(alt="alt string" src='https://www.mathsisfun.com/calculus/images/diff-eq-2.svg')
dl
	dt: dfn Order
	dd The #[b highest derivative]
		ol.example
			li: p #[+m \ddv yx + y = 5x] - It has only the first derivative #[+m \ddv yx], so is #[strong First Order]
			li: p #[+m \ddvd 2yx + xy = \sin(x)] - This has a second derivative #[+m \ddvd 2yx], so is #[strong Order 2]
			li: p #[+m \ddvd 3yx + x\ddv yx + y = e] - This has a third derivative #[+m \ddvd 3yx] which outranks the #[+m \ddv yx], so is #[strong Order 3]
	dt Degree
	dd 
		p The exponent of the highest derivative.
		ol.example 
			li: p #[+m() (\ddv yx)^2 + y = 5x^2] - The highest derivative is just #[+m \ddv yx], and it has an exponent of 2, so this is "Second Degree". #[mark #[small In fact] it is a #[strong First Order Second Degree Ordinary Differential Equation]]
			li: p #[+m \ddvd 3yx + (\ddv yx)^2 + y = 5x^2] - The highest derivative is #[+m \ddvd 3yx], but it has no exponent #[small actually an exponent of 1 which is not shown], so this is "First Degree". #[mark The exponent of 2 on #[+m \ddv yx] does not count, as it is not the highest derivative. So it is a #[b Third Order First Degree Ordinary Differential Equation]]
	p.warning Be careful not to confuse order with degree. Some people use the word order when they mean degree!
h5 Linear
p It is #[b Linear] when the variable (and its derivatives) has no exponent or other function put on it.
p So #[b no] y^2, y^3, \sqrt y, \sin y, \ln y …, #[b just plain y] (or whatever the variable is)
p More formally a #[b Linear Differential Equation] is in the form:
p \ddv yx + P(x)y = Q(x)
h4 Solving
p OK, we have classified our Differential Equation, the next step is solving.
p And we have a #[a(href='https://www.mathsisfun.com/calculus/differential-equations-solution-guide.html') Differential Equations Solution Guide] to help you.
| #[a(href='https://www.mathsisfun.com/calculus/derivatives-introduction.html') Derivatives]#[a(href='https://www.mathsisfun.com/calculus/index.html') Calculus Index]




section 
	h3 Решение линейного неоднородного дифференциального уравнения первого порядка: #[+m y' + p(x) y = q(x)]
		+source(links=['https://1cov-edu.ru/differentsialnye-uravneniya/pervogo-poryadka/linejnye/metod-bernulli/'])
	ul
		li #[a(href='https://1cov-edu.ru/differentsialnye-uravneniya/pervogo-poryadka/linejnye/') метод интегрирующего множителя];
		li #[a(href='https://1cov-edu.ru/differentsialnye-uravneniya/pervogo-poryadka/linejnye/metod-lagranzha/') метод вариации постоянной (Лагранжа)].
	dl
		dt: dfn Метод Бернулли
		dt: dfn Метод введения двух функций
		dd 
			ol 
				li Ищем решение исходного уравнения в виде произведения двух функций: #[+m u=u(x), v=v(x):y = u\cdot v]. 
				li Дифференцируем: #[+m y' = u' · v + u · v']. 
				li Подставляем в исходное уравнение: #[+m u'v + uv' + p(x) uv = q(x)]
				li Выносим #[+m u] за скобки: #[+m u' v + u (v' + p(x)v) = q(x)] 
				li В качестве #[+m v] возьмем любое, отличное от нуля, решение уравнения: #[+m v' + p(x)v = 0] 
				li Это уравнение с разделяющимися переменными. #[+m \ddv vx + p(x) v = 0] 
				li Разделяем переменные. Умножаем обе части уравнения на #[+m \dd x] и делим на #[+m v]: #[+m \frac{\dd v}v + p(x) \dd x = 0] 
				li Интегрируем: #[+m \int \frac{\dd v}v + \int p(x)\dd x = C] 
				li Постоянную #[+m C] возьмем равной нулю, поскольку нам нужно любое, отличное от нуля, решение: #[+m \int \frac{\dd v}v = \ln |v| = -\int p(x)\dd x]
				li Потенцируем и опускаем знак модуля (Знак модуля сводится к умножению на постоянную ±1): #[+m v = e^{-\int p(x)\dd x}] 
				li Подставим в #[+m u' v + u (v' + p(x)v) = q(x)] учитывая, что согласно #[+m v' + p(x)v = 0], выражение в скобках равно нулю: #[+m \ddv udx \cdot e^{-\int p(x)\dd x} = q(x)] Отсюда #[+m \frac{du}{dx} = q(x), e^{\int p(x)\dd x}] 
				li Интегрируем #[+m u = \int q(x) e^{\int p(x)\dd x}\dd x + C] 
				li Окончательно находим: #[+m y = uv = \left(\int q(x) e^{\int p(x)\dd x} \dd x + C \right) \cdot e^{-\int p(x)\dd x} = C \cdot e^{-\int p(x)\dd x} + e^{-\int p(x) \dd x} \int q(x) e^{\int p(x)\dd x} \dd x]
		details.example
			summary #[+m xy' + 3y = x^2]
			ol
				li Делаем подстановку: #[+m y = u(x)\cdot v(x)]. 
				li Дифференцируем: #[+m y' = u' · v + u · v'] 
				li Подставляем в исходное уравнение: #[+m x( u' v + u v' ) + 3 u v = x^2] 
				li Выносим u за скобки: #[b (3)] #[+m x u' v + u ( xv' + 3v) = x^2] 
				li В качестве v возьмем любое, отличное от нуля, решение уравнения: #[b (4)] #[+m xv' + 3v = 0]. 
				li Это уравнение с разделяющимися переменными, #[+m x \frac{dv}{dx} + 3v = 0]. 
				li Разделяем переменные. Умножаем обе части уравнения на dx и делим на xv: #[+m \frac{dv}{v} + 3\frac{dx}x = 0] 
				li Интегрируем: #[+m \int \frac{dv}{v} + 3 \int \frac{dx}x = C] 
				li Постоянную C возьмем равной нулю, поскольку нам нужно любое, отличное от нуля, решение. По #[a(href='https://1cov-edu.ru/mat_analiz/integrali/tablitsa/') таблице интегралов], находим: #[+m \int \frac{dv}{v} = \ln|v| = - 3 \int \frac{dx}x = - 3 \ln|x|] Или #[+m \ln|v| = - 3 \ln|x|] 
				li Потенцируем и опускаем знаки модуля (Знак модуля сводится к умножению на постоянную ±1). #[+m v = x^{-3}] 
				li Подставим в (3) учитывая, что согласно (4), выражение в скобках равно нулю: #[+m x \frac{du}{dx} x^{-3} = x^2] 
				li Отсюда #[+m \frac{du}{dx} = x^4] 
				li Интегрируем, применяя формулу #[+m \int x^n\dd x = \frac 1{n+1} x^{n+1}]: #[+m u = \int x^4\dd x = \frac 1{4+1} x^{4+1} + C =]#[+m \frac 15 x^5 + C]. 
				li Окончательно находим: #[+m y = uv = \left( \frac 15 x^5 + C \right) x^{-3} =]#[+m C x^{-3} + \frac 15 x^2].
				li Ответ: Общее решение уравнения: #[+m y = \frac{C}{x^3} + \frac 15 x^2]
</template>
