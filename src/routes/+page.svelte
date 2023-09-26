<script>
	import Math from '$lib/components/Math.svelte';

</script>


<Math expression={"x_2+10_{123}"}></Math>
<Math expression={"x_2+10_{123}"}></Math>
<Math expression={"(2+3i)^2 = (2+3i)(2+3i) = 4+6i+6i+9i^2 = 4+12i-9 = -5+12i"}></Math>
<figure>
	<template lang="pug">
		+m() x_1' + x^{223} + \sum
		p.intro What about #[+m \sqrt{i}], for instance? Won't we need a #[+m() j], or some other invention (er, dimension)? Well..., you can take everything to extremes, but we won't need to. #[+m() (2+3i)^2 = (2+3i)(2+3i) = 4+6i+6i+9i^2 = 4+12i-9 = -5+12i]. Therefore, the square root of #[+m() -5+12i] is #[+m() 2+3i]. It turns out that the Square Root of #[+m() i] is another complex number. We won't need a #[+m() j]. We won't need a third dimension for #[+m() \sqrt{i}].

		div #[+m({'z':'чето','x':'чето','m':'чето'}) x_2+h+z=z^m];
	</template>

	<figcaption>Formula with some description of used symbols</figcaption>
</figure>

