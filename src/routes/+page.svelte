<script lang="ts">
	import Math from '$lib/components/Math.svelte';
	import Switcher from '$lib/components/Switcher.svelte';
	import Header from './Header.svelte';
	import Task from './Task.svelte';
	import book_1 from '$lib/books/DifferentialsEquations.pdf?url';
</script>

<Math expression={'(2+3i)^2 = (2+3i)(2+3i) = 4+6i+6i+9i^2 = 4+12i-9 = -5+12i'} />
<template lang="pug">
ol.example(title="Найти все делители числа n")
	li n = 10: Для этого поделим число на нименьший простой делитель например 2 и в результате 5,2,1
+LPTASK('x_1+x_2\\eq 7','x_1-3x_3\\le 2') 
+LPTASK('c_1x_1+c_2x_2+…+c_nx_n',String.raw`b_1\quad\ge/\le/= \quad a_{11}x_1+a_{12}x_2+…+a_{1n}x_n \\ b_2 \quad\ge/\le/= \quad a_{21}x_1+a_{22}x_2+…+a_{2n}x_n \\ \vdots \\ b_m \quad \ge/\le/= \quad a_{m1}x_1+a_{m2}x_2+…+a_{mn}x_n \\ x_1,x_2,…,x_n \ge 0`).beauty.block
p.intro What about #[+m \sqrt{i}], for instance? Won't we need a #[+m() j], or some other invention (er, dimension)? Well..., you can take everything to extremes, but we won't need to. #[+m() (2+3i)^2 = (2+3i)(2+3i) = 4+6i+6i+9i^2 = 4+12i-9 = -5+12i]. Therefore, the square root of #[+m() -5+12i] is #[+m() 2+3i]. It turns out that the Square Root of #[+m() i] is another complex number. We won't need a #[+m() j]. We won't need a third dimension for #[+m() \sqrt{i}].
+LPTABLE([[0,0,0,1,2,3,4],[223,23,324,242,323,24,42]])
div #[+m({'z':'чето $xyz$','x':'чето','m':'чето'}) x_2+h+z=z^m];
+source(links=['https://www.mathsisfun.com/calculus/second-derivative.html','https://www.mathsisfun.com/calculus/differential-equations-solution-guide.html','https://www.mathsisfun.com/algebra/degree-expression.html'] books=[{index: 1,page: 3}])
section.showcase
	figure
		ol.columns.example(title="Some task")
			li Some example
			li And new one
			li And new one
			li And new one
			li And new one
			li And new one
			li And new one
			li And new one
			li And new one
			li And new one
			li And new one
			li And new one
			li And new one Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore rem architecto asperiores? Autem fuga hic consequuntur laboriosam corrupti? Delectus molestias reiciendis non beatae magni distinctio voluptate fugiat sit hic neque!
			li And new one Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore rem architecto asperiores? Autem fuga hic consequuntur laboriosam corrupti? Delectus molestias reiciendis non beatae magni distinctio voluptate fugiat sit hic neque!
			li And new one Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore rem architecto asperiores? Autem fuga hic consequuntur laboriosam corrupti? Delectus molestias reiciendis non beatae magni distinctio voluptate fugiat sit hic neque!
		figcaption Example list
	figure
		details.example
			summary 
				p Каким должна быть ЭДС второго источника тока, в цепи для того, чтобы сила тока через сопротивление была равна #[+m I]? ЭДС первого источника тока #[+m \mathcal{E}_1]. Внутренние сопротивления источников тока соответственно #[+m r_1] и #[+m r_2].
				img(alt="alt string" src="./PHYSICS/img/ЗаданиеВтороеПравилоКирхгофа.png")
			ol  
				li Рассмотрим узел #[+m A], запишем для него уравнение для токов, используя первое правило Кирхгофа. Положим, что положительными являются токи, которые входят в узел: #[+m I-I_1-I_2=0]. 
				li Обходя контур будем двигаться по часовой стрелке. Применяя второе правило Кирхгофа для контура #[+m ADFEA] получим уравнение: #[+m IR+I_2r_2=\mathcal{E}_2]. Для контура #[+m EABCDFE] имеем: #[+m IR+I_1r_1=\mathcal{E}_1]. Мы получили систему из трех независимых уравнений для трех неизвестных: #[+m \begin{cases} I - I_1 - I_2 =0\\ IR+I_2r_2=\mathcal{E}_2 \\ IR+I_1r_1=\mathcal{E}_1 \end{cases}]. 
				li Из полученной системы выразим искомую ЭДС #[+m \mathcal{E}_2 = IR+(I - I_1)r_2 \Rightarrow \mathcal{E}_2 = IR+\left(I - \frac{IR-\mathcal{E}_1}{r_1}\right)r_2]
			+m.block.solution \mathcal{E}_2 = IR - \frac{r_2(Ir_1+IR-\mathcal{E}_1)}{r_1}
</template>
<Switcher>
	<p>
		Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui aut eligendi magnam obcaecati.
		Suscipit natus, accusantium assumenda aut repellat minima? Ex beatae maxime sunt, harum quaerat
		reiciendis nesciunt obcaecati ad.
	</p>
	<p style="color: red">
		Another Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut omnis eius et. Vitae eius
		rerum explicabo, doloremque illo, beatae temporibus dolorum dolor quibusdam voluptatem
		distinctio ipsa commodi cupiditate, labore totam?
	</p>
</Switcher>
