<script>
	import { text } from '@sveltejs/kit';
	import { Math } from 'docs-lib';
</script>

<template lang="pug">
mixin img
	img(alt="alt string" src!=`#[+m lib/img/physics/]{attributes.src}` height=attributes.height width=attributes.width)

h1 Полезные ресурсы
ul.columns
	li #[a(href="https://engineering.purdue.edu/wcchew/ece604s20/Lecture%20Notes/" lang="En") Lectures on Electromagnetic Field Theory. Weng Cho CHEW1 Spring 2020, Purdue University]
	li #[a(href="https://tsput.ru/res/fizika/1/KR_ELEC/l0.htm") Пособие преподователей Тульского государственного педагогического университета им. Л. Н. Толстого]
	li #[a(href="https://youtu.be/2QOa5YC1990")  Коэффициент мощности и реактивные элементы]

article: include mechanics

//- article: include electro/electrodynamics

</template>
