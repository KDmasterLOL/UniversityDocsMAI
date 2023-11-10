<script>
	import { Math } from "docs-lib";
</script>
<svelte:head>
	<title>Theory of propability</title>
</svelte:head>
<template lang="pug">
include temp
- function fac(n) {return (n<2)?1:fac(n-1)*n}
mixin Bernuli(n,m,p)
	-
		q = 1-p
		result = fac(n)/(fac(m)*fac(n-m))*Math.pow(p,m)*Math.pow(q,n-m)
		output = `P_{${n}}(${m}) = C_{${n}}^{${m}}p^{${m}}q^{${n-m}}=\\frac{${n}!}{${m}!${n-m}!} ${p}^{${m}}${q}^{${n-m}} = ${result}`
	| #{output}
mixin sum(vari, from,to, str)
	-
		let output = `\\sum_{${vari} = ${from}}^{${to}} ${str} = `
		let reg = new RegExp(String.raw`(?<=\W)${vari}(?=\W)`, "g")
		output += Array.from({length: to-from+1}, (_,i)=> str.replace(reg,from+i)).join('+')
	| #{output} 
mixin table(object)
	table
		each key in Object.keys(object)
			tr
				th: +m= key
				each val in object[key]
					td= val

figure
	ol
		li: a(href="https://www.probabilitycourse.com/preface.php") Probability course
	figcaption Literature
article: include probability
section
	hgroup
		h3 Random Variables: Mean, Variance and Standard Deviation
		+source(links=['https://www.mathsisfun.com/data/random-variables-mean-variance.html'])
	dl
		dt: dfn Random Variable 
		dd 
			p A variable whose possible values are numerical outcomes of a random experiment or a set of #[b possible values] from a random experiment. Can be either Discrete(certain values #[span.example 1,2,3,4,5]) or Continuous(any value within a range #[span.example such as a person's height])
			details.example
				summary Tossing a coin: we could get Heads or Tails
				p Let's give them the values #[b Heads=0] and #[b Tails=1] and we have a Random Variable "X":
				figure
					img(src='https://www.mathsisfun.com/data/images/random-variable-1.svg')
					figcaption Experiment - like tossing a coin. Values #[+m 1, 2] matched to each event. The #[b set of values] is a #[b Random Variable]
		dt(lang="en"): dfn Expected Value
		dt(lang="en"): dfn Mean
		dt: dfn Математическое ожидание
		dd
			+m({'p': 'probability of every random value'}).block \mu = M(X) = \sum_{i=0}^n x_ip_i
			p When we know the probability #[+m p] of every value #[+m X] we can calculate the Expected Value of #[+m X]
			details.example
				summary Tossing a single #[b unfair] die
				img(src='https://www.mathsisfun.com/data/images/die.jpg').no-invert
				p Imagine a #[b weighted] die (cheating!) so we have these probabilities:
				+table({'x': [1, 2, 3, 4, 5, 6],'p': [0.1, 0.1, 0.1, 0.1, 0.1, 0.5], 'xp': [0.1, 0.2, 0.3, 0.4, 0.5, 3]})
				+m.block \mu = \sum_{i=0}^n x_ip_i = 0.1+0.2+0.3+0.4+0.5+3 = 4.5
				p.note This is a weighted mean: values with higher probability have higher contribution to the mean.
		dt: dfn Variance
		dd
			+m.block Var(X) = \mu(X^2) - \mu(X)^2 = \sum_{i=0}^n x_i^2p_i − (\sum_{i=0}^n x_ip_i)^2
			details.example
				summary Tossing a single #[b unfair] die
				img(src='https://www.mathsisfun.com/data/images/die.jpg')
				p Imagine a #[b weighted] die (cheating!) so we have these probabilities:
				+table({'x': [ 1, 2, 3, 4, 5, 6], 'p': [0.1, 0.1, 0.1, 0.1, 0.1, 0.5], 'x^2p': [ 0.1, 0.4, 0.9, 1.6, 2.5, 18]})
				+m.block \sum_{i=0}^n x_i^2p_i = 0.1+0.4+0.9+1.6+2.5+18 = 23.5 \\ Var(X) = \sum_{i=0}^n x_i^2p_i − (\sum_{i=0}^n x_ip_i)^2 = 23.5 - 4.5 = 3.25
		dt: dfn Standard Deviation
		dd
			+m.block σ = \sqrt{Var(X)}
			details.example
				summary Tossing a single #[b unfair] die
				img(src='https://www.mathsisfun.com/data/images/die.jpg')
				p Imagine a #[b weighted] die (cheating!) so we have these probabilities:
				table
					tr #[th: +m x] #[td 1] #[td 2] #[td 3] #[td 4] #[td 5] #[td 6]
					tr #[th: +m p] #[td 0.1] #[td 0.1] #[td 0.1] #[td 0.1] #[td 0.1] #[td 0.5]
					tr #[th: +m x^2p] #[td 0.1] #[td 0.4] #[td 0.9] #[td 1.6] #[td 2.5] #[td 18]
				+m σ = \sqrt{Var(X)} = \sqrt {3.25} = 1.803...
	details
		summary
			p You plan to open a new McDougals Fried Chicken, and found these stats for similar restaurants:
			table
				tr #[th Percent] #[th Year's Earnings]
				tr #[td 20%] #[td $50,000 Loss]
				tr #[td 30%] #[td $0]
				tr #[td 40%] #[td $50,000 Profit]
				tr #[td 10%] #[td $150,000 Profit]
			p Using that as #[b probabilities] for your new restaurant's profit, what is the Expected Value and Standard Deviation?
		p The Random Variable is #[+m X = \text{possible profit}]
		table
			tr #[th: +m p_i] #[th: +m x_i] #[th: +m xp] #[th: +m x^2p]
			tr #[td 0.2] #[td -50] #[td -10] #[td 500]
			tr #[td 0.3] #[td 0] #[td 0] #[td 0]
			tr #[td 0.4] #[td 50] #[td 20] #[td 1000]
			tr #[td 0.1] #[td 150] #[td 15] #[td 2250]
		+m.block \mu = \sum_{i=0}^n x_ip_i = 25 \\ Var(X) = \sum_{i=0}^n x_i^2p_i − \mu^2 = 3750 − 25 = 3750 − 625 = 3125 \\ σ = \sqrt{3125} = 56 \text{ Rounded to nearest whole number}
		p But remember these are in thousands of dollars, so:
		ul
			li \mu = $25,000
			li σ = $56,000
		p So you might expect to make $25,000, but with a very wide deviation possible.
		p Let's try that again, but with a much higher probability for $50,000: Now with different probabilities (the $50,000 value has a high probability of #[b 0.7] now):
		table
			tr #[th Probability p] #[th Earnings ($'000s) x] #[th xp] #[th xp]
			tr #[td 0.1] #[td -50] #[td -5] #[td 250]
			tr #[td 0.1] #[td 0] #[td 0] #[td 0]
			tr #[td 0.7] #[td 50] #[td 35] #[td 1750]
			tr #[td 0.1] #[td 150] #[td 15] #[td 2250]
			tr
				td Σp = 1
				td Sums:
		//- 		td \sum_{i=0}^n x_ip_i = 45
		//- 		td \sum_{i=0}^n x_ip_i = 4250
		//- p \mu = \sum_{i=0}^n x_ip_i = #[b 45]
		//- p Var(X) = \sum_{i=0}^n x_ip_i − \mu = 4250 − 45 = 4250 − 2025 = #[b 2225]
		p σ = √2225 = #[b 47] (to nearest whole number)
		p In thousands of dollars:
		ul #[li \mu = $45,000] #[li σ = $47,000]
		p The mean is now much closer to the most probable value.
		p And the standard deviation is a little smaller (showing that the values are more central.)


hgroup
	h1 BB
	+source(links=['https://www.berdov.com/works/teorver/bernoulli_scheme/', 'https://byjus.com/normal-distribution-formula/'])
dl
	dt: dfn Схема Бернулли
	dd.intro
		p Задачи, которые решаются по схеме Бернулли, чрезвычайно разнообразны: от простеньких #[span.example найдите вероятность, что стрелок попадет 1 раз из 10] до весьма суровых #[span.example задачи на проценты или игральные карты]. В реальности эта схема часто применяется для решения задач, связанных с контролем качества продукции и надежности различных механизмов, все характеристики которых должны быть известны до начала работы.
	dd 
		p Когда производится #[+m n] однотипных независимых опытов, в каждом из которых может появиться интересующее нас событие #[+m A], причем известна вероятность этого события #[+m P(A) = p]. Требуется определить вероятность того, что при проведении #[+m n] испытаний событие #[+m A] появится ровно #[+m k] раз.
		p Поскольку речь идет о независимых испытаниях, и в каждом опыте вероятность события #[+m A] одинакова, возможны лишь два исхода:
		ol
			li #[+m A] — появление события #[+m A] с вероятностью #[+m p];
			li #[+m \overline A] — событие #[+m A] не появилось с вероятностью #[+m q = 1 − p].
		p Важнейшее условие, без которого схема Бернулли теряет смысл — это постоянство. Сколько бы опытов мы ни проводили, нас интересует одно и то же событие #[+m A], которое возникает с одной и той же вероятностью #[+m p]. #[mark далеко не все задачи сводятся к постоянным условиям #[span.example вынимание разноцветных шаров из ящика, не является опытом с постоянными условиями, так как при вынимании очередного шара — соотношение цветов в ящике изменияется, следовательно, и вероятностей]].
		p Если же условия постоянны, можно точно определить вероятность того, что событие #[+m A] произойдет ровно k раз из n возможных. Сформулируем этот факт в виде теоремы:
	dt: dfn Теорема Бернулли
	dd
		p Пусть вероятность появления события #[+m A] в каждом опыте постоянна и равна #[+m р]. Тогда вероятность того, что в n независимых испытаниях событие #[+m A] появится ровно k раз, рассчитывается по #[dfn формуле Бернулли]: #[+m({'C^k_n': 'число сочетаний'}) q = 1 − p:P_n(k) = C^k_n p^kq^{n-k}] #[small задачи, приведенные ниже, вполне решаются без использования этой формулы. Например, можно применить формулы сложения вероятностей. Однако объем вычислений будет просто нереальным].
		ol.example
			li: details.example
				summary Определить вероятность того, что в партии из десяти выпущенных на данном станке деталей ровно #[+m k = 0, 1, 10] будут без брака. Вероятность выпуска бракованного изделия на станке равна 0,2.
				ul
					li нас интересует событие #[+m A] выпуска изделий без брака, которое случается каждый раз с вероятностью #[+m p = 1 − 0.2 = 0.8]. 
					li Нужно определить вероятность того, что это событие произойдет #[+m k] раз. 
					li Событию #[+m A] противопоставляется событие #[+m \overline A], т.е. выпуск бракованного изделия.
				p #[mark Таким образом, имеем: #[+m n = 10; p = 0.8; q = 0.2]]. Находим вероятность того, что в партии все детали бракованные #[+m k = 0], что только одна деталь без брака #[+m k = 1], и что бракованных деталей нет вообще #[+m k = 10]:
				+m.block.solution \begin{aligned}k=0:#[+Bernuli(10,0,0.5)] \\ k=1:#[+Bernuli(10,1,0.5)] \\ k=10:#[+Bernuli(10,10,0.5)]\end{aligned}
			li: details.example
				summary Монету бросают 6 раз. Выпадение герба и решки равновероятно. Найти вероятность того, что:
					ol
						li герб выпадет три раза
						li герб выпадет один раз
						li герб выпадет не менее двух раз
				ul 
					li Нас интересует событие #[+m A], когда выпадает герб. Вероятность этого события равна #[+m p = 0.5]. 
					li Событию #[+m A] противопоставляется событие #[+m \overline A], когда выпадает решка, что случается с вероятностью #[+m q = 1 − 0.5 = 0.5]. 
					li Нужно определить вероятность того, что герб выпадет #[+m k] раз.
				p #[mark Таким образом, имеем: #[+m n = 6; p = 0.5; q = 0.5]]. Для того чтобы определить вероятность того, что герб выпал три или один раз достаточно просто подставить значения в формулу Бернулли. 
					| #[br]#[strong Но как определить, с какой вероятностью герб выпадет не менее двух раз?] Основная загвоздка — во фразе #[em не менее]. Это значит что #[mark нас устроит любое #[+m k], кроме 0 и 1, иначе надо найти значение суммы #[strong: +m X = #[+sum("k",2,6,"P(k)")]] = 1 − P(0) − P(1)], то есть также достаточно из всех возможных вариантов «вырезать» те, когда герб выпал 1 раз #[+m k = 1] или не выпал вообще #[+m k = 0]. Поскольку P(1) нам уже известно, осталось найти P(0):
				+m.block.solution \begin{aligned}k=1:#[+Bernuli(6,1,0.5)] \\ k=3:#[+Bernuli(6,3,0.5)] \\ k=0:#[+Bernuli(6,0,0.5)] \\ k\ge 2: X =  1 − P(0) − P(1)\end{aligned}
			li: details
				summary Вероятность того, что телевизор имеет скрытые дефекты, равна 0,2. На склад поступило 20 телевизоров. Какое событие вероятнее: что в этой партии имеется два телевизора со скрытыми дефектами или три?
				p Интересующее событие #[+m A] — наличие скрытого дефекта. Всего телевизоров n = 20, вероятность скрытого дефекта p = 0,2. Соответственно, вероятность получить телевизор без скрытого дефекта равна q = 1 − 0,2 = 0,8.
				p Получаем стартовые условия для схемы Бернулли: n = 20; p = 0,2; q = 0,8.
				p Найдем вероятность получить два «дефектных» телевизора (k = 2) и три (k = 3):
				p Очевидно, P(3) > P(2), т.е. вероятность получить три телевизора со скрытыми дефектами больше вероятности получить только два таких телевизора. Причем, разница неслабая.
				p Небольшое замечание по поводу факториалов. Многие испытывают смутное ощущение дискомфорта, когда видят запись «0!» (читается «ноль факториал»). Так вот, 0! = 1 по определению.
				p P. S. А самая большая вероятность в последней задаче — это получить четыре телевизора со скрытыми дефектами. Подсчитайте сами — и убедитесь.

//- section
	hgroup
		h1 Theory of propability
		+source(links=['https://cdto.wiki/', 'https://www.cuemath.com/data/probability-theory/', 'https://www.cuemath.com/data/sample-space/', 'https://otvet.mail.ru/question/69280712'])
	dl
		dt: dfn Априорная(доопытная)
		dd То есть мы предполагаем о результатах некоторого эксперимента, судим о вероятности тех или иных событий, не зная результатов эксперимента, до его проведения #[span.example По формуле полной вероятности мы догадываемся о результате какого-либо события, имея на руках лишь вероятности тех или иных факторов, способствующих данному событию. То есть, априорных факторов].
		dt: dfn Апостериорная(послеопытная)
		dd То есть после того, как мы провели эксперимент, ситуация более менее прояснилась, изменились вероятности тех или иных событий, была получена новая информация, исходя из которой мы можем судить о результатах эксперимента более чётко #[span.example Формула Байеса позволяет менять местами причину со следствием и перерасчитывать вероятности факторов, становящихся уже апостериорными]. 
			details.example
				summary Вероятность того. что студент на экзамене попадёт к первому преподавателю, равна 0,6, ко второму - 0,3, к третьему 0,1. Вероятность получить "отлично" у первого преподавателя равна 0,2, у второго - 0,4, у третьего 0,6. Найти вероятность того, что студент получит "отлично" на экзамене. 
				ol
					li
						ol(title="Расмотрим пример") 
							li события, состоящие в том, что студент попадёт к первому, второму и третьему преподавателям соответственно, являются взаимоисключающими (т. е. студент не может попасть сразу к двум преподавателям) , а также образующими полную группу событий, (т. е. , студент обязательно попадёт хотя бы к одному из преподавателей) . Также какими-то способами стала известна вероятность получить пятёрку у каждого преподавателя. Во-первых, мы не знаем, к какому именно преподавателю попадёт студент, 
							li не знаем, получит ли он 5, если попадёт к кому-нибудь из них. Всё это - априорные сведения. Исходя из них, мы оцениваем возможность получения пятёрки вообще. Делаем это по формуле полной вероятности. . Нам известны условные вероятности - вероятности получения студентом пятёрки, при условии, что он попадёт к 1-му, 2-му и 3-му преподавателям соответственно, а также вероятности наступления этих условий. Полная вероятность рассчитывается как сумма произведений условных вероятностей на вероятности соответствующих условий, т. е. в данном случае она равна 0,2*0,6 + 0,4*0,3 + 0,6*0,1 = 0.12 + 0,12 + 0,06 = 0,3. Это и есть вероятность получения студентом пятёрки, если он попадёт к случайному, неизвестному заранее преподавателю. 
					.
						Рассмотрим теперь апостериорные вероятности. Пример. По результатам экзамена (см. предыдущий пример) , стало известно, что студент получил оценку "отлично". Найти вероятность того, что студент побывал: 
						а) у первого преродавателя 
						б) у второго преподавателя 
						в) у третьего преподавателя 
						То есть здесь, зная конкретный результат эксперимента, мы перерасчиываем вероятности беседы студента с конкретным преподавателем, находим апостериорные вероятности. Делаем это по формуле Байеса. Она говорит о том, что апостериорная вероятность гипотезы (в данном случае, вероятность того, что студент побывал у, скажем, 1-го преподавателя) равна априорной вероятности той же гипотезы (вероятности того, что студент до экзамена попадёт к 1-му преподавателю) , умноженной на вероятность события (получения пятёрки у данного преподавателя) , делённой на полную вероятность (вероятность получения пятёрки у случайного преподавателя, см. предыдущий пример) . 
						То есть в этом случае соответствующие вероятности равны 
						а) Р = 0,6*0,2/0,3 = 0,4 
						б) Р = 0,3*0,4/0,3 = 0,4 
						в) Р = 0,1*0,6/0,3 = 0,2 
						То есть апостериорные вероятности (послеопытные) в этом случае равны - вероятность того, что студент после экзамена, получив 5, побывал у 1-го преподавателя равна 40%, у второго - 40% и у третьего - 20% 
						Априорные же вероятности (доопытные) равны - вероятность того, что студент до экзамена попадёт к 1-му преподавателю равна 60%, ко 2-му - 30% и к 3-му - 10%. 
						Вот, что такое априорные и апостериорные вероятности событий. Думаю, что всё понятно. 
		dt: dfn Априорное распределение вероятностей неопределенной величины #[+m p]
		dd Выражает предположения о #[+m p] до учета экспериментальных данных #[span.example При #[+m p] — доля избирателей, готовых голосовать за определенного кандидата, априорным распределением будет предположение о #[+m p] до учета результатов опросов или выборов]. Противопоставляется апостериорной вероятности, условной вероятности случайного события при условии того, что известны апостериорные данные, т. е. полученные после опыта
		dt: dfn Probability theory
		dd A branch of mathematics that investigates the probabilities associated with a random phenomenon. A random phenomenon can have several outcomes. Probability theory describes the chance of occurrence of a particular outcome by using certain formal concepts. Probability theory makes use of some fundamentals such as sample space, probability distributions, random variables, etc. to find the likelihood of occurrence of an event. In this article, we will take a look at the definition, basics, formulas, examples, and applications of probability theory.
			ul.note
				li Probability theory is a branch of mathematics that deals with the probabilities of random events.
				li The concept of probability in probability theory gives the measure of the likelihood of occurrence of an event.
				li The probability value will always lie between 0 and 1.
				li In probability theory, all the possible outcomes of a random experiment give the sample space.
				li Probability theory uses important concepts such as random variables, and cumulative distribution functions to model a random event and determine various associated probabilities.
		dd Makes the use of random variables and probability distributions to assess uncertain situations mathematically. In probability theory, the concept of #[a(href='https://www.cuemath.com/data/probability/') probability] is used to assign a numerical description to the likelihood of occurrence of an event. Probability can be defined as the number of favorable outcomes divided by the total number of possible outcomes of an event
		dd A field of mathematics and statistics that is concerned with finding the probabilities associated with random events. There are two main approaches available to study probability theory. These are theoretical probability and experimental probability. Theoretical probability is determined on the basis of logical reasoning without conducting experiments. In contrast, #[a(href='https://www.cuemath.com/data/experimental-probability/') experimental probability] is determined on the basis of historic data by performing repeated experiments.
		dd.example Suppose the probability of obtaining a number 4 on rolling a fair dice needs to be established. The number of favorable outcomes is 1. The possible outcomes of the dice are {1, 2, 3, 4, 5, 6}. This implies that there are a total of 6 outcomes. Thus, the probability of obtaining 4 on a dice roll, using probability theory, can be computed as #[+m \frac 16 = 0.167].
		dt: dfn Random Experiment
		dd Can be defined as a trial that is repeated multiple times in order to get a well-defined set of possible outcomes #[span.example Tossing a coin].
		dt: dfn Sample Space
		dd Can be defined as the set of all possible outcomes that result from conducting a random experiment. For example, the sample space of tossing a fair coin is {heads, tails}.
		dt: dfn Event
		dd A set of outcomes of an experiment that forms a subset of the sample space. The types of events are given as follows:
			ul
				li #[a(href='https://www.cuemath.com/data/independent-events/') Independent events]: Events that are not affected by other events are independent events.
				li Dependent events: Events that are affected by other events are known as dependent events.
				li Mutually exclusive events: Events that cannot take place at the same time are mutually exclusive events.
				li Equally likely events: Two or more events that have the same chance of occurring are known as equally likely events.
				li Exhaustive events: An exhaustive event is one that is equal to the sample space of an experiment.
		dt: dfn Random Variable
		dd In probability theory, a random variable can be defined as a variable that assumes the value of all possible outcomes of an experiment. There are two types of random variables as given below.
		dt: dfn Discrete Random Variable 
			a(href='https://www.cuemath.com/algebra/discrete-random-variable/')
		dd Can take an exact countable value such as 0, 1, 2... It can be described by the cumulative distribution function and the probability mass function.
		dt: dfn Continuous Random Variable
		dd A variable that can take on an infinite number of values. The cumulative distribution function and probability density function are used to define the characteristics of this variable.
		dt: dfn Probability
		dd The numerical likelihood of occurrence of an event. The probability of an event taking place will always lie between 0 and 1. This is because the number of desired outcomes can never exceed the total number of outcomes of an event. Theoretical probability and empirical probability are used in probability theory to measure the chance of an event taking place.
			img(alt="alt string" src='https://d138zd1ktt9iqe.cloudfront.net/media/seo_landing_files/probability-theory-formula-1639571790.png')
		dt: dfn Conditional Probability
			a(href='https://www.cuemath.com/conditional-probability-formula/')
		dd When the likelihood of occurrence of an event needs to be determined given that another event has already taken place. It is denoted as P(A | B). This represents the conditional probability of event A given that event B has already occurred.
		dt: dfn Expectation of a random variable #[+m X]
			a(href='https://www.cuemath.com/expected-value-formula/')
		dd The #[a(href='https://www.cuemath.com/data/average/') average] value of the outcomes of an experiment when it is conducted multiple times. It is denoted as E[X]. It is also known as the #[a(href='https://www.cuemath.com/data/mean/') mean] of the random variable.
		dt: dfn Variance #[+m Var[X]]
			a(href='https://www.cuemath.com/data/variance/')
		dd The measure of dispersion that shows how the distribution of a random variable varies with respect to the mean. It can be defined as the average of the squared differences from the mean of the random variable.
		dt: dfn Probability Theory Distribution Function
		dd #[a(href='https://www.cuemath.com/data/probability-distribution/') Probability distribution] or cumulative distribution function is a function that models all the possible values of an experiment along with their probabilities using a random variable. Bernoulli distribution, #[a(href='https://www.cuemath.com/algebra/binomial-distribution/') binomial distribution], are some examples of discrete probability distributions in probability theory. #[a(href='https://www.cuemath.com/normal-distribution-formula/') Normal distribution] is an example of a continuous probability distribution.
		dt: dfn Probability Mass Function
		dd The probability that a discrete random variable will be exactly equal to a specific value.
		dt: dfn Probability Density Function
		dd #[a(href='https://www.cuemath.com/data/probability-density-function/') Probability density function] is the probability that a continuous random variable will take on a set of possible values.
	h4 Probability Theory Formulas
	p There are many formulas in probability theory that help in calculating the various probabilities associated with events. The most important probability theory formulas are listed below.
	ul
		li Theoretical probability: Number of favorable outcomes / Number of possible outcomes.
		li #[a(href='https://www.cuemath.com/empirical-probability-formula/') Empirical probability]: Number of times an event occurs / Total number of trials.
		li Addition Rule: #[+m P(A ∪ B) = P(A) + P(B) - P(A∩B)], where A and B are events.
		li Complementary Rule: #[+m P(A') = 1 - P(A). P(A')] denotes the probability of an event not happening.
		li Independent events: #[+m P(A∩B) = P(A) ⋅ P(B)]
		li Conditional probability: #[+m P(A | B) = P(A∩B) / P(B)]
		li Bayes' Theorem: #[+m P(A | B) = P(B | A) ⋅ P(A) / P(B)]
		li Probability mass function: #[+m f(x) = P(X = x)]
		li Probability density function: #[+m p(x) = p(x) = (\frac{\mathrm{d} F(x)}{\mathrm{d} x}) = F'(x)], where #[+m F(x)] is the cumulative distribution function.
		li Expectation of a continuous random variable: #[+m() (\int xf(x)dx)], where #[+m f(x)] is the pdf.
		li Expectation of a discrete random variable: #[+m() (\sum xp(x))], where #[+m p(x)] is the pmf.
		li Variance: #[+m Var(X) = E[X] - (E[X])]
	h4 Applications of Probability Theory
	p Probability theory is used in every field to assess the risk associated with a particular decision. Some of the important applications of probability theory are listed below:
	ul
		li In the finance industry, probability theory is used to create mathematical models of the stock market to predict future trends. This helps investors to invest in the least risky asset which gives the best returns.
		li The consumer industry uses probability theory to reduce the probability of failure in a product's design.
		li Casinos use probability theory to design a game of chance so as to make profits.
	p: strong Related Articles:
	ul
		li: a(href='https://www.cuemath.com/data/probability-rules/') Probability Rules
		li: a(href='https://www.cuemath.com/data/probability-and-statistics/') Probability and Statistics
		li: a(href='https://www.cuemath.com/geometric-distribution-formula/') Geometric Distribution

	ol.example
		li 
			p When two dice are rolled what is the probability of getting a sum of 8? #[strong Solution:] When two dice are rolled there are 36 possible outcomes. To get the sum as 8 there are 5 favorable outcomes. #[+m [(2, 6), (6, 2), (3, 5), (5, 3), (4, 4)]]. Using probability theory formulas, #[+m \text{Probability} = \frac {\text{Number of favorable outcomes}}{\text{total number of possible outcomes}} = \frac {5}{36}]
			img(alt="alt string" src='https://d138zd1ktt9iqe.cloudfront.net/media/seo_landing_files/probability-theory-example-1639628394.png')
			p #[strong Answer:] The probability of getting the sum as 8 when two dice are rolled is 5 / 36.
		li
			p What is the probability of drawing a queen from a deck of cards? #[strong Solution:] A deck of cards has 4 suits. Each suit consists of 13 cards. Thus, #[+m \text{the total number of possible outcomes} = 4\times 13 = 52] There can be 4 queens, one belonging to each suit. Hence, the number of favorable outcomes = 4. The #[a(href='https://www.cuemath.com/data/card-probability/') card probability] = 4 / 52 = 1 / 13 #[strong Answer:] The probability of getting a queen from a deck of cards is 1 / 13
		li Out of 10 people, 3 bought pencils, 5 bought notebooks and 2 got both pencils and notebooks. If a customer bought a notebook what is the probability that she also bought a pencil.#[strong Solution:] Using the concept of conditional probability in probability theory, #[+m P(A | B) = P(A∩B) / P(B)]. Let A be the event of people buying pencils and B be the event people of buying notebooks. P(A) = 3 / 10 = 0.3 P(B) = 5 / 10 = 0.5 P(A∩B) = 2 / 10 = 0.2 Substituting the values in the given formula, P(A | B) = 0.2 / 0.5 = 0.4#[strong Answer:] The probability that a customer bought a pencil given that she bought a notebook is 0.4.
	h4 FAQs on Probability Theory
	h5 What is the Concept of Probability Theory?
	p Probability theory is a branch of mathematics that deals with the likelihood of occurrence of a random event. It encompasses several formal concepts related to probability such as random variables, probability theory distribution, expectation, etc.
	h5 What are the Two Types of Probabilities in Probability Theory?
	p The two types of probabilities in probability theory are theoretical probability and experimental probability. Theoretical probability gives the probability of what is expected to happen without conducting any experiments. Experimental probability uses repeated experiments to give the probability of an event taking place.
	figure
		ul
			li Independent events: P(A∩B) = P(A) ⋅ P(B)
			li Conditional probability: P(A | B) = P(A∩B) / P(B)
			li Bayes' Theorem: P(A | B) = P(B | A) ⋅ P(A) / P(B)
			li Theoretical probability: Number of favorable outcomes / Number of possible outcomes.
		figcaption: h1 The main probability theory formulas
	h5 Why is Probability Theory Used in Statistics?
	p Probability theory is useful in making predictions that form an important part of research. Further analysis of situations is made using statistical tools. Thus, #[a(href='https://www.cuemath.com/data/statistics/') statistics] is dependent on probability theory to draw sound conclusions.
	h5 Can the Value of Probability Be Negative According to Probability Theory?
	p According to probability theory, the value of any probability lies between 0 and 1. 0 implies that an event does not happen and 1 denotes that the event takes place. Thus, probability cannot be negative.
	h5 What is a Random Variable in Probability Theory?
	p A #[a(href='https://www.cuemath.com/data/random-variable/') random variable] in probability theory can be defined as a variable that is used to model the probabilities of all possible outcomes of an event. A random variable can be either continuous or discrete.
	h5 What are the Applications of Probability Theory?
	p Probability theory has applications in almost all industrial fields. It is used to gauge and analyze the risk associated with an event and helps to make robust decisions.
section
	hgroup 
		h4 Распределение случайных величин
		+source(links=['https://www.matburo.ru/tv_spr_sub.php?p=3','https://www.scribbr.com/statistics/poisson-distribution/'])
	h5 Распределение дискретных случайных величин
	dl 
		dt: dfn Биномиальное распределение
		dd
			p Пусть дискретная случайная величина #[+m X] - количество "успехов" в последовательности из #[+m n] независимых случайных экспериментов, таких что вероятность "успеха" в каждом из них равна #[+m p] ("неуспеха" - #[+m q=1-p]).
			+m.block.
				X = \quad
				\begin{array}{c|c}
				x_k & 0 & 1 & … & k & … & n \\ \hline
				p_k & q^n & np q^{n-1} & … & C_n^k p^k q^{n-k} & … & p^n
				\end{array}
			p Здесь вероятности находятся по формуле Бернулли: #[+m P(X=k) = C_n^k p^k (1-p)^{n-k} = C_n^k p^k q^{n-k}, k=0,1,2,...,n] 
			p Числовые характеристики биномиального распределения: #[+m M(X)=np, \quad D(X)=npq, \sigma(X)=\sqrt{npq}] 
			figure.example
				img(src='https://www.matburo.ru/tv/tvformul/image153.jpg')
				figcaption многоугольники распределения для #[+m n=5] и различных вероятностей
		dt(lang="en"): dfn Poisson distribution
		dt: dfn Пуассоновское распределение
		dd 
			+m({'k': 'the number of times an event occurs', '\\lambda': 'the average number of times an event occurs within given period of time or space or mean'}).block P(X=k) = \frac {e^{-\lambda}\lambda^k}{k!} \\ \mu = \operatorname{Var} = \lambda
			p моделирует случайную величину, представляющую собой число событий, произошедших за фиксированное время, при условии, что данные события происходят с некоторой фиксированной средней интенсивностью и независимо друг от друга.
			p.note При условии #[+m p\to 0], #[+m n \to \infty], #[+m np \to \lambda = const] закон распределения Пуассона является предельным случаем биномиального закона. Так как при этом вероятность #[+m p] события #[+m A] в каждом испытании мала, то закон распределения Пуассона называют часто законом редких явлений.
			figure
				+m.block.
					X = \quad
					\begin{array}{c|c}
					x_k & 0 & 1 & ... & k & ... \\ \hline
					p_k & e^{-\lambda} & \lambda e^{-\lambda} & ... & \frac{\lambda^k}{k!}\cdot e^{-\lambda} & ...
					\end{array}
				figcaption Ряд распределения
			p Gives the probability of an event #[span.example from disease cases to customer purchases to meteor strikes, Text messages per hour, Male grizzly bears per hectare, Machine malfunctions per year, Website visitors per month, Influenza cases per year] happening a certain number of times #[+m k] within a given interval of time or space #[span.example 10 days or 5 square inches]. #[mark Has only one parameter λ #[eg the only thing needed to calculate the probability of an event occurring a certain number of times]].
			p In general it appropriate for #[dfn count data]. Count data is composed of observations that are non-negative integers (i.e., numbers that are used for counting, such as 0, 1, 2, 3, 4, and so on).
			ol(title="You can use it if")
				li Individual events happen at random and independently. That is, the probability of one event doesn’t affect the probability of another event.
				li You know the constant mean number #[+m \lambda = \const] of events occurring within a given interval of time or space.
			details
				summary Horse kick deaths
				p.history One of the first applications of the Poisson distribution was by statistician Ladislaus Bortkiewicz. In the late 1800s, he investigated accidental deaths by horse kick of soldiers in the Prussian army. He analyzed 20 years of data for 10 army corps, equivalent to 200 years of observations of one corps.
				figure
					img(src='https://www.scribbr.nl/wp-content/uploads/2022/08/Poisson-distribution-Ladislaus-Bortkiewicz.webp')
					figcaption histogram shows simulated data that are similar to what Bortkiewicz observed
				p He found that a mean of 0.61 soldiers per corps died from horse kicks each year. However, most years, no soldiers died from horse kicks. On the other end of the spectrum, one tragic year there were four soldiers in the same corps who died from horse kicks.
				ul
					li event - death by horse kick
					li time interval - one year
					li The mean number of events per time interval #[+m \lambda = 0.61]
					li The number of deaths by horse kick in a specific year is #[em k]
				p The army corps that Bortkiewicz observed were a sample of the population of all Prussian army corps. Because of the random nature of sampling, samples rarely follow a probability distribution perfectly. The deaths by horse kick in the sample approximately follow a Poisson distribution, so we can reasonably infer that the population follows a Poisson distribution.
				p An average of 0.61 soldiers died by horse kicks per year in each Prussian army corps. You want to calculate the probability that exactly two soldiers died in the VII Army Corps in 1898, assuming that the number of horse kick deaths per year follows a Poisson distribution.
				p The specific army corps (VII Army Corps) and year (1898) don’t matter because the probability is constant.
				+m.block.
					\begin{aligned}
					k = 2 \text{ deaths by horse kick}\\ \lambda = 0.61 \text{ deaths by horse kick per year}
					\end{aligned}:
					P(X=2) = \frac {e^{-0.61}0.61^2}{2!} = 0.101
				p The probability that exactly two soldiers died in the VII Army Corps in 1898 is 0.101.
			details.example
				summary Graph visualisation and special cases
				figure
					img(src='https://www.scribbr.nl/wp-content/uploads/2022/08/Poisson-distribution-graph.webp')
					figcaption The graph of Poisson distributions with different values of λ.
				figure
					img(src='https://www.scribbr.nl/wp-content/uploads/2022/08/Poisson-distribution-right-skewed.webp')
					figcaption When λ is low, the distribution is much longer on the right side of its peak than its left (i.e., it is strongly right-skewed).
				figure
					img(src='https://www.scribbr.nl/wp-content/uploads/2022/08/Poisson-distribution-normal.webp')
					figcaption As λ increases, the distribution looks more and more similar to a normal distribution. In fact, when λ is 10 or greater, a normal distribution is a good approximation of the Poisson distribution.
				p When the mean of a Poisson distribution is large (>10), it can be approximated by a normal distribution.
				figure
					img(src='https://www.matburo.ru/tv/tvformul/image174.jpg')
					figcaption Разные многоугольники распределения при #[+m \lambda = 1; 4; 10].
		dt: dfn Геометрическое распределение
		dd
			p Пусть происходит серия независимых испытаний, в каждом из которых событие может появится с одной и той же вероятностью #[+m p], а вероятность не возникновение этого события #[+m q=1-p]. А #[+m X] случайная величина  - количество испытаний до #[strong первого] появления события. То эта случайная величина имеет геометрическое распределение вероятностей.
			p Формула для вероятностей: #[+m P(X=k) = q^k \cdot p, k=0,1,2,...,n,...] 
			p Ряд распределения геометрического закона:
			+m.block.
				X = \quad
				\begin{array}{c|c}
				x_k & 0 & 1 & 2 & ... & k & ... \\ \hline
				p_k & p & q\cdot p & q^2 \cdot p & ... & q^k \cdot p & ...
				\end{array}
			p Числовые характеристики: #[+m M(X)=\frac{q}{p}, \quad D(X)=\frac{q}{p^2}] 
		dt: dfn Гипергеометрическое распределение
		dd
			p Из урны, в которой находятся #[+m N] шаров (#[+m K] белых и #[+m N-K] чёрных шаров), наудачу и без возвращения вынимают #[+m n] шаров (#[+m n \le N]). Найти закон распределения случайной величины #[+m X] - равной числу белых шаров среди выбранных.
			p Случайная величина #[+m X] может принимать целые значения от #[+m 0] до #[+m K] (если #[+m n \lt K], то до #[+m n]). Вероятности вычисляются по формуле: #[+m P(X=k)=\frac{C_K^k \cdot C_{N-K}^{n-k}}{C_N^n}, \quad 0\le k \le K].
			p Числовые характеристики: #[+m M(X)=\frac{K}{N}\cdot n, \quad D(X)=\frac{K}{N}\cdot n \cdot \frac{N-n}{N} \cdot \frac{N-K}{N-1}] 
	h4 Непрерывные случайные величины
	dl
		dt: dfn Экспоненциальное распределение
		dt: dfn Показательное распределение
		dd
			+m.block \lambda > 0: f(x) = \begin{cases} 0, x \lt 0 \\ \lambda e^{-\lambda x},x\ge 0 \end{cases}
			p абсолютно непрерывное распределение, моделирующее время между двумя последовательными свершениями одного и того же события.
			p Функция распределения величины #[+m X]: #[+m F(x)= \begin{cases} 0,x \lt 0\\ 1- e^{-\lambda x},x\ge 0 \end{cases}]
			p Числовые характеристики можно найти по формулам: #[+m M(X)=\frac{1}{\lambda}, \quad D(X)=\frac{1}{\lambda^2}, \quad \sigma= \frac{1}{\lambda}].
			figure
				img(src='https://www.matburo.ru/tv/tvformul/image186.jpg')
				figcaption Плотность распределения при различных значениях #[+m \lambda \gt 0]:
		dt: dfn Равномерное распределение
		dd
			p Равномерный закон распределения используется при анализе ошибок округления при проведении числовых расчётов (например, ошибка округления числа до целого распределена равномерно на отрезке), в ряде задач массового обслуживания, при статистическом моделировании наблюдений, подчинённых заданному распределению.
			p Плотность распределения на отрезке #[+m() (a;b)]: #[+m f(x)= \begin{cases} 0,x \le a\\ \frac {1}{b-a},a \lt x \le b, \\ 0,x \gt b, \\ \end{cases}]. 
			p Функция распределения: #[+m F(x)=\begin{cases} 0,x \le a\\ \frac {x-a}{b-a},a \lt x \le b, \\ 1,x \gt b, \\ \end{cases}]. 
			p Числовые характеристики равномерно распределенной случайной величины: #[+m M(X)=\frac{a+b}{2}, \quad D(X)=\frac{(b-a)^2}{12}, \quad \sigma=\frac{b-a}{2\sqrt 3}]. 
			figure
				img(src='https://www.matburo.ru/tv/tvformul/image196.jpg')
				figcaption График плотности вероятностей
		dt(lang="en"): dfn Bell curve
		dt(lang="en"): dfn Gaussian distribution
		dt(lang="en"): dfn Normal Distribution 
		dt: dfn распределение Гаусса
		dt: dfn Нормальное распределение
		dd
			+m({"\\mu": "Mean", "\\sigma": "Standard deviation", "x": "Normal random variable"}).block f(x)= \frac 1{\sigma \sqrt{2\pi}}\exp \left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
			p.intro играет важнейшую роль во многих областях знаний, особенно в физике. Физическая величина подчиняется нормальному распределению, когда она подвержена влиянию огромного числа случайных помех. Ясно, что такая ситуация крайне распространена, поэтому можно сказать, что из всех распределений в природе чаще всего встречается именно нормальное распределение — отсюда и произошло одно из его названий.
			figure
				img(src='https://www.matburo.ru/tv/tvformul/image206.jpg')
				figcaption Пример графика плотности распределения для различных значений среднего и СКО
			p Нормальный закон распределения случайной величины с параметрами #[+m \mu=0, \sigma=1: f(x)= \frac 1{\sqrt{2\pi}}\exp \left(-\frac{x^2}2\right)] называется стандартным или нормированным, а соответствующая нормальная кривая - стандартной или нормированной.
			p Функция Лапласа определяется как: #[+m \Phi(x)= \frac{1}{\sqrt{2\pi}}\int_0^x e^{-t^2/2} dt] 
			p Вероятность попадания нормально распределенной случайной величины #[+m X] в заданный интервал #[+m() (\alpha, \beta)]: #[+m P(\alpha \lt X \lt \beta) = \Phi\left( \frac{\beta-\mu}{\sigma} \right) - \Phi\left( \frac{\alpha-\mu}{\sigma} \right)]. 
			p Вероятность отклонения нормально распределенной случайной величины #[+m X] на величину #[+m \delta] от математического ожидания (по модулю). #[+m P(|X -\mu|\lt \delta) = 2 \Phi\left( \frac{\delta}{\sigma} \right)]. 
			p Defined as the probability density function f(x) for the continuous random variable, say x, in the system. One of the most important continuous probability distributions. Is a very important statistical data distribution pattern occurring in many natural phenomena, such as height, blood pressure, lengths of objects produced by machines, etc. Here, we are going to discuss the normal distribution formula and examples in detail.
			p(title="two characteristics") The two characteristics of the normal distribution are: The mean, median, and mode are equal. The normal distribution is unimodal and symmetric.
			p The distribution is said to be a #[dfn standard normal distribution] if the mean is equal to zero and the standard deviation is equal to 1.
			details.example
				summary Find the probability density function for the normal distribution where #[+m \mu = 4, \sigma = 2, x = 3]
				+m.block.
					\begin{aligned}
					f(3)= \frac{1}{\sqrt{2\pi (2)^{2}}}e^{\frac{-(3-4 )^{2}}{2(2)^{2}}} = \\
						\frac{1}{2\sqrt{2\pi }}e^{\frac{-1}{8}} = \\
						0.19947 \times e^{-0.125} = \\
						0.19947 \times 0.882496 = \\
						0.17603 \\
					\end{aligned}
				p Therefore, the probability density function for the normal distribution is 0.17603.
	figure
		table
			thead: tr
				th Characteristic
				th Normal
				th Poisson
			tbody
				tr
					td Continuous or discrete
					td Continuous
					td Discrete
				tr
					td Parameter
					td Mean (µ) and standard deviation (σ)
					td Lambda (λ)
				tr
					td Shape
					td Bell-shaped
					td Depends on λ
				tr
					td Symmetry
					td Symmetrical
					td Asymmetrical (right-skewed). As λ increases, the asymmetry decreases.
				tr
					td Range
					td −∞ to ∞
					td 0 to ∞
		figcaption the most important differences between normal distributions and Poisson distributions:
</template>
