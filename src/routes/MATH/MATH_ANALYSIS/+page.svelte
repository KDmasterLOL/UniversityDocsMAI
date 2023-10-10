<script>
	import Math from '$lib/components/Math.svelte';
</script>

<template lang="pug">
ol(title="Литература")
	li Ильин В.А., Позняк Э.Г. Основы математического анализа В 2-х частях. часть 1 и 2
ol(title="Интересно")
	li: a(href="https://youtu.be/3zRubo5fHUo") великая теорема ферма
	li: a(href="https://youtu.be/0GorifJmJVM") кватернионы
	li: a(href="https://youtu.be/FdHB5SXddvY") Суть алгебры
	li: a(href="https://youtu.be/wdMeIC95uBo") Задача Мишустина
	li: a(href="https://youtu.be/EYsr0DZWMCg") 10 глупых вопросов МАТЕМАТИКУ | Алексей Савватеев 
	li: a(href="https://youtu.be/7kR1e5BaNB0") Как мировая элита использует теорию игр (Д. Перетолчин, А. Савватеев) 
	li: a(href="https://youtube.com/playlist?list=PLZjXXN70PH5ilxFCrbVJyNofV0_yC2IgH") Суть матанализа
h1 Об о всем и ни о чем
dl 
	dt Параметрическая функция #[+m f(t)]
		a(href="https://www.khanacademy.org/math/multivariable-calculus/thinking-about-multivariable-function/ways-to-represent-multivariable-functions/a/parametric-functions" lang="En")
	dd функция с одним одноразмерным входным значение и мультиразмерных выходом
	dt Параметр 
	dd входное значение параметрической функции
	dt Параметризация кривой
	dd нахождение параметрической функции кривой заданной функцией нескольких переменных
	dt Приращение переменной #[+m \Delta х = x_1 - x_0]
		a(href="https://lms2.sseu.ru/courses/eresmat/gloss/g28.htm")
	dd разность двух значений переменной #[+m x]
	dt Приращение функции #[+m \Delta f(х) = f(x_1) - f(x_0)] соответствующее данному приращению аргумента #[+m \Delta х]
	dd разность двух значений функции от соответствующих аргументов
figure
	ol
		li #[+m() (A)] - фигура с именем #[+m A]
		li #[+m A] - площадь фигуры #[+m() (A)]
		li #[+m \Delta] - приращение
		li #[+m \dd] - дифференциал
	figcaption: h1 Обозначения
h1 FAQ
dl
	dt Как запомнить что производная от #[+m \cos x] это #[+m -\sin x], а от #[+m \sin x] просто #[+m \cos x]
	dd
		p Производная имеет физический смысл скорости изменения в какую либо из сторон - положительную или отрицательную - и #[+m \cos 0 = 1,\cos \pi = 0:\cos 0 \gt \cos \pi] из этого следует что #[+m= String.raw`x\in [0;\pi]:\dd{\qty(\cos x)}\le 0`], то есть можно сказать как только косинус появляется на свет в точке 0 он сразу начинает падать в низ. И так как синус и косинус описывают скорости изменения друг друга, а #[+m x\in [0;\pi]:\sin x \ge 0], то нужно брать синус со знаком минус
		
//- article: include intro
//- article: include series
//- article: include integrals
//- article: include differentials

</template>
