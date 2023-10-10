<script>
	import Math from '$lib/components/Math.svelte';
</script>

<template lang="pug">
table#GOST-font
  tr 
    th Параметры шрифта	
    th Обозначение
    th Относительный размер #[+m h]
    th(colspan=8) Размеры (мм)
  tr 
    th Paзмер шрифта - высота прописных букв и цифр 
    td h 
    td (10/10) 
    td 1.8 
    td 2.5 
    td 3.5 
    td 5 
    td 7 
    td 10 
    td 14 
    td 20
  tr
    th Высота строчных букв 
    td c 
    td (7/10) 
    td 1.3 
    td 1.8 
    td 2.5 
    td 3.5 
    td 5 
    td 7 
    td 10 
    td 14
  tr
    th Ширина прописных букв и цифр: 
    td(rowspan=9) g 
  tr
    td И, Й, П, Н, Т, Ц, Б, В, К, О, Р, У, Ч, Ь, Э, Я 
    td (6/10) 
    td 1.1 
    td 1.5 
    td 2.1 
    td 3 
    td 4.2 
    td 6 
    td 8.4 
    td 12
  tr
    td Г, Е, З, С, П, 2, 3, 4, 5, 6, 7, 8, 9, 0 
    td (5/10) 
    td 0.9 
    td 1.25 
    td 1.75 
    td 2.5 
    td 3.5 
    td 5 
    td 7 
    td 10
  tr
    td А, Д, М, Х, Ы, Ю 
    td (7/10) 
    td 1.3 
    td 1.8 
    td 2.5 
    td 3.5 
    td 5 
    td 7 
    td 10 
    td 14
  tr
    td Ж, Ш, Щ, Ф, Ъ 
    td (8/10) 
    td 1.4 
    td 2 
    td 2.8 
    td 4 
    td 5.6 
    td 8 
    td 12 
    td 16
  tr
    th Ширина строчных букв: 
  tr
    td а, б, в, г, д, у, з, и, й, к, л, н, р, о, с, у, х, ч, ц 
    td (5/10) 
    td 0.9 
    td 1.25 
    td 1.75 
    td 2.5 
    td 3.5 
    td 5 
    td 7 
    td 10
  tr
    td ъ, ь, з, я, ж, т, ф, ш, щ 
    td (7/10) 
    td 1.3 
    td 1.8 
    td 2.5 
    td 3.5 
    td 5 
    td 7 
    td 10 
    td 14
  tr
    td ы, ю, м 
    td (6/10) 
    td 1.1 
    td 1.5 
    td 2.1 
    td 3 
    td 4.2 
    td 6 
    td 8.4 
    td 12
  tr
    th Толщина линий шрифта 
    td d 
    td (1/10) 
    td 0.18 
    td 0.25 
    td 0.35 
    td 0.5 
    td 0.7 
    td 1 
    td 1.4 
    td 2
  tr
    th Расстояние между буквами 
    td a 
    td (2/10) 
    td 0.35 
    td 0.5 
    td 0.7 
    td 1 
    td 1.4 
    td 2 
    td 2.8 
    td 4
  tr
    th Минимальный шаг строк 
    td b 
    td (17/10) 
    td 3 
    td 4 
    td 6 
    td 8.5 
    td 12 
    td 17 
    td 24 
    td 34
  tr
    th Минимальное расстояние между словами 
    td e 
    td (6/10) 
    td 1.1 
    td 1.5 
    td 2.1 
    td 3 
    td 4.2 
    td 6 
    td 8.4 
    td 12
figure 
  img(src="./Шрифты.png" alt="")
  figcaption Шрифт


</template>

<style lang="scss">
	$highlight-color: rgba(255, 255, 0, 0.3);

	#GOST-font {
		margin: auto;

		td {
			text-align: center;
			padding: 0.3rem;
		}

		th {
			border-top: 0.1rem solid var(--text-color);
			padding: 0.3rem;
		}

		tr:not(:nth-child(4)) {
			td:nth-last-child(-n + 8) {
				border: 0.1rem solid var(--text-color);
			}
		}

		border-collapse: collapse;
		overflow: hidden;

		td,
		th {
			position: relative;
		}

		tr:hover {
			background-color: $highlight-color;
		}

		td:hover::after {
			content: '';
			height: 10000px;
			left: 0;
			position: absolute;
			top: -5000px;
			width: 100%;
			z-index: -1;
		}

		td:hover::after,
		th:hover::after {
			background-color: $highlight-color;
		}
	}
</style>
