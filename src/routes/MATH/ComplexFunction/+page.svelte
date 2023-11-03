<script>
	import {Math} from 'docs-lib';</script>

<template lang="pug">

h2 Complex numbers
+m() (a+bi)^2=a^2+2abi-b^2 \\ (a+bi)(a-bi)=a^2+abi-abi+b^2=a^2+b^2 \\ (a+bi)^3=(a^2+2abi-b^2)(a+bi)=a^3+2a^2bi-ab^2+a^2bi-2ab^2-b^3i=a^3+3a^2bi-3ab^2-b^3i
hgroup
	h4 Imaginary Numbers
	+source(links=['http://www.milefoot.com/math/complex/imagnumbers.htm','http://www.milefoot.com/math/complex/squarerootofi.htm', 'http://www.milefoot.com/math/complex/sqrootsimag.htm','http://www.milefoot.com/math/complex/imagandtrig.htm'])

p.intro What is #[+m \sqrt{-1}] ? A symbol thrust upon earthlings by an alien culture? Well, not quite... (unless you view mathematics as representative of an alien culture... but we won't go there). The "usual" numbers "normal" people work with are called #[em real numbers]. They include whole numbers, fractions, decimals, negative numbers, square roots of positive numbers, and numbers like #[+m \pi]. 
dl
	dt Imaginary number #[+m i = \sqrt{-1} \text{ or } i^2 = -1]. #[small electrical engineers will use #[+m j] instead of #[+m i], because they use #[+m i] to represent inductive force, alias current]
	dd.intro 
		p The real numbers include basically anything that a calculator will turn into a decimal, or anything that has a position on the number line. But #[+m \sqrt{-1}] does not have a position on the number line. There is no number we can square to get negative one.#[br] So we can't use a real number for #[+m \sqrt{-1}]. We must use a different kind of number. #[span.history The sixteenth century mathematicians who first seriously worked with #[+m \sqrt{-1}] weren't sure what its significance was, so they called it an imaginary number #[small , a very unfortunate term cause in fact, there is nothing imaginary about #[+m \sqrt{-1}] (But it did take two centuries before mathematicians generally understood its significance)].] #[mark We don't need any other definitions for square roots of other numbers, having #[+m i] is enough. #[span.example We can write #[+m \sqrt{-9} = 3i], since the square root of 9 is 3, and the square root of a negative number will produce the number #[+m i].]]
		figure
			img(alt="alt string" src='http://www.milefoot.com/math/complex/images/numberline.gif')
			figcaption Number line
	dd Imaginary number is the number that not real. #[mark Real numbers are complex numbers, so are imaginary numbers. #[strong Just like a whole number is also a fraction].]
	dt Pure imaginary numbers #[+m b \in \mathbb{R}: bi]
	dd Product of a nonzero real number #[+m b] with the imaginary number #[+m i]. The collection of numbers created by taking square roots of the negative numbers. #[mark None of the pure imaginary numbers have a position on the number line].
	dt Complex numbers
	dd 
		p The collection of numbers created by adding a real number with a pure imaginary number. 
		p To draw them #[small when they aren't on the number line,] we need second number line to represent the pure imaginary part of the complex number#[small , cause a one-dimensional number line will not sufficient] #[eg we need a two-dimensional picture to represent complex numbers]. So the real numbers are points on the horizontal axis. #[em Imaginary numbers] are located somewhere other than the horizontal axis. #[mark #[dfn Pure imaginary numbers] are points on the vertical axis (other than the origin). #[dfn Complex numbers] include all possible points in the picture].
		figure.example
			img(alt="alt string" src='http://www.milefoot.com/math/complex/images/argand.gif')
			figcaption The complex number in algebraic form #[+m 2+3i], represented by a point.
	dd(title="Algebraic form") 
		p: mark Complex numbers in #[dfn algebraic form] are represented as #[+m a,b \in \mathbb{R}: a+bi]
		h1 Square Root
		p.intro What about #[+m \sqrt{i}], for instance? Won't we need a #[+m j], or some other invention (er, dimension)? Well..., you can take everything to extremes, but we won't need to. #[span.example #[+m() (2+3i)^2 = (2+3i)(2+3i) = 4+6i+6i+9i^2 = 4+12i-9 = -5+12i]. Therefore, the square root of #[+m -5+12i] is #[+m 2+3i]]. It turns out that the Square Root of #[+m i] is another complex number. We won't need a #[+m j]. We won't need a third dimension for #[+m \sqrt{i}].
		p(title="An algebraic derivation") Assume there is a number #[+m z_1 = a_1+b_1i] which represents #[+m z_2 = \sqrt{a_2+b_2i} = z_1^2]. Since #[+m= String.raw`(a_1+b_1i)^2 = a_1^2+2a_1b_1i+b_1^2 i^2 = \htmlClass{mark}{ \left[a_1^2-b_1^2\right]+[2a_1b_1]i}`] and since #[strong this result should equal the number #[+m a_2+b_2i]], we obtain the following system of equations #[+m \begin{cases} a_1^2-b_1^2 &=a_2 \\ 2a_1b_1 &=b_2 \end{cases}].
		ol.example(title="Find square roots of")
			li: p Assume there is a number #[+m a+bi] which represents #[+m \sqrt{i}]. Since #[+m= String.raw`(a+bi)^2 = a^2+2abi+b^2 i^2 = \left[a^2-b^2\right]+[2ab]i`] and since this result should equal the number #[+m i], we obtain the following system of equations: #[+m \begin{cases} a^2-b^2 &=0 \\ 2ab &=1 \end{cases}]. When the first equation is solved for the variable #[+m a], we learn that the variables #[+m a] and #[+m b] are either equal or opposites. From the second equation, we know that the product is a positive one-half, so the variables #[+m a] and #[+m b] must be equal. (If they were opposite, the product would have been negative.) Therefore, the second equation becomes #[+m 2a^2=1], whose solution is #[+m a = \pm \frac{\sqrt2}2]. Therefore, the number #[+m i] has two square roots (just like positive numbers do). They are #[+m \frac{\sqrt2}2 + \frac{\sqrt2}2 i] and #[+m -\frac{\sqrt2}2 - \frac{\sqrt2}2 i].
			li 
				+m.block.task 3+4i
				p Since #[+m= String.raw`(a+bi)^2 = a^2+2abi+b^2 i^2 = \left[a^2-b^2\right]+[2ab]i`] we need to solve the system of equations #[+m \begin{cases} a^2-b^2 &=3 \\ 2ab &=4 \end{cases}]. #[small We can't solve this system as quickly as we did when we found the square root of #[+m i], but it still can be done].
				ol
					li Solving the second equation for the variable #[+m b], we get #[+m b=\frac2a]. 
					li Substituting this quantity into the first equation, we get #[+m a^2-\frac{4}{a^2}=3]. 
					li Clearing the fractions gives #[+m a^4-3a^2-4=0]. 
					li This can be solved by factoring, so #[+m a^2=4] or #[+m a^2=-1]. But we want real values for the variable #[+m a], so we discard #[+m -1]. 
					li Therefore, #[+m a^2=4], and the values of #[+m a] are #[+m 2] and #[+m -2]. Using #[+m b=\frac2a], we find #[+m b=\pm 1]. #[span.asnwer So the two square roots of #[+m 3+4i] are #[+m 2+i] and #[+m -2-i]].
			li
				+m.block.task 2+3i
				+m.block.solution.
					\begin{cases} a^2-b^2 &=2 \\ 2ab &=3 \end{cases} \Rightarrow 
					\text{Exress and substitute }b \begin{cases} a^2 - \frac{9}{4a^2} =2 \\ b=\frac{3}{2a} \end{cases} \Rightarrow
					\begin{cases} a^2 - \frac{9}{4a^2} &=2 \mid \cdot 4a^2 \\ b&=\frac{3}{2a} \end{cases} \Rightarrow 
					\begin{cases} 4a^4-8a^2-9=0 \\ b=\frac{3}{2a} \end{cases}
					\\ 
					\text{Solve quadratic equation } a^2 = 1 \pm \frac{\sqrt{13}}2 \text{ and discard the negative sign for real values } a^2 = 1 + \frac{\sqrt{13}}2 \Rightarrow
					a = \pm \sqrt{1+\frac{\sqrt{13}}2} = \pm \frac12 \sqrt{4+2\sqrt{13}}
					\\ 
					\text{So }a = \pm \frac12 \sqrt{4+2\sqrt{13}} : b=\frac{3}{2a}= \pm \frac{3}{\sqrt{4+2\sqrt{13}}}
				p.solution So the two square roots of #[+m 2+3i] are #[+m \frac12 \sqrt{4+2\sqrt{13}} + \frac{3}{\sqrt{4+2\sqrt{13}}} i] and #[+m -\frac12 \sqrt{4+2\sqrt{13}} - \frac{3}{\sqrt{4+2\sqrt{13}}} i].
	dd(title="Trigonometric form")
		figure
			img(alt="alt string" src='http://www.milefoot.com/math/complex/images/argand2.gif')
			figcaption Graphical representation of #[+m 2+3i]. The parts of the complex number #[+m 2+3i] are shown by the horizontal and vertical sides of the triangle. The hypotenuse of the right triangle has length #[+m \sqrt{13}], found by using the Pythagorean Theorem or the distance formula.
		p In the triangle, if we use #[+m \theta] for the name of the angle at the origin, then we can rewrite the number #[+m 2+3i] by using its trigonometric components. The horizontal component is #[+m \sqrt{13}\cos \theta], the vertical component is #[+m \sqrt{13}(\sin \theta)i], so the number #[+m 2+3i] is the same as #[+m \sqrt{13}(\cos \theta + i \sin \theta)]. #[mark Basically, every complex number can be written in the form #[+m a + bi = r(\cos \theta + i\sin \theta)].]
		p #[span.intro There are many identities in trigonometry, and they are the key to multiplying and dividing complex numbers.] Suppose we have the two complex numbers #[+m r(\cos \theta + i \sin \theta)] and #[+m s(\cos Q + i \sin Q)]. When we multiply them using distributive property, we obtain #[+m rs (\cos \theta \cos Q + i \cos \theta \sin Q + i \sin \theta \cos Q - \sin \theta \sin Q)]. But the formulas for the sine and cosine of a sum allow us to rewrite this result as #[+m [r (\cos \theta + i \sin \theta)][s (\cos Q + i \sin Q)] = rs[\cos(P+Q)+i\sin(P+Q)]] 
		p #[+m r(\cos \theta + i \sin \theta) * s(\cos Q + i \sin Q) = rs (\cos \theta \cos Q + i \cos \theta \sin Q + i \sin \theta \cos Q - \sin \theta \sin Q) = rs[\cos(P+Q)+i\sin(P+Q)]]. In words, multiplying complex numbers involves multiplying their distances from the origin, and adding their angles.
		p We can derive a similar formula for dividing complex numbers. That formula is #[+m \frac{r (\cos \theta + i \sin \theta)}{s (\cos Q + i \sin Q)} = \frac{r}{s}[\cos(P-Q)+i\sin(P-Q)]] 
		h5 Powers and roots
		p Since exponents represent repeated multiplication, we can derive a formula for powers of complex numbers. That formula is known as #[b DeMoivre's Theorem]: #[+m \left[r(\cos \theta+i\sin \theta) \right]^n = r^n (\cos nP + i \sin nP)] 
		p We can also use this formula to do roots, by using fractions for the variable #[+m n]. However, roots are not unique, since the trigonometric functions are periodic. The formula which gives the #[+m n]th roots is #[+m= String.raw`[r (\cos \theta + i \sin \theta)]^{\frac{1}{n}} = r^\frac{1}{n} \left( \cos \frac{P+2k\pi}{n}+i\sin \frac{P+2k\pi}{n}\right)`]. #[strong This formula not only does square roots, but all kinds of roots].
		p So what is the square root of #[+m 2+3i]? In trigonometric form, the original number is #[+m \sqrt{13}(\cos \theta + i\sin \theta)], where the angle #[+m P = \arctan \frac32]. Therefore, the square roots are #[+m \sqrt{\sqrt{13}}\left( \cos\frac12\arctan\frac32+i\sin\frac12\arctan\frac32\right)] and #[+m \sqrt{\sqrt{13}}\left( \cos(\pi+\frac12\arctan\frac32)+i\sin(\pi+\frac12\arctan\frac32)\right)].
<iframe src="https://www.ncl.ac.uk/webtemplate/ask-assets/external/maths-resources/images/Expo_form_complx_num.pdf" frameborder="0"></iframe>
hgroup
	h4 Using #[+m i] as an Exponent
	+source(links=['http://www.milefoot.com/math/complex/exponentofi.htm'])
p.intro There is a relationship between #[a(href='http://www.milefoot.com/math/complex/imagandtrig.htm') imaginary numbers and trigonometry], which produces the multiplication formula #[+m= String.raw`\left[r(\cos \theta+i\sin \theta)\right]\left[s(\cos \theta_1+i\sin \theta_1)\right]= rs\left[\cos(\theta+\theta_1)+i\sin(\theta+\theta_1)\right]`]. This formula basically states that multiplication of complex numbers is related to addition of angles.
	| #[br]There is another situation in which multiplication turns into addition, which you may call from your beginning algebra days. Exponent rules have the property that #[+m a^xa^y = a^{\theta+y}]. So we might expect a connection between complex numbers and exponential functions. And such a connection does exist! It is not normally studied until calculus, because of the difficulties in the details. But we won't let that stop us...
p To do this view some series representations of the functions:
+m.block e^x = 1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\frac{x^4}{4!}+\frac{x^5}{5!}+\ldots \\ \cos x = 1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+\ldots \\ \sin x = x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\ldots \\ \cos x + \sin x = 1+x-\frac{x^2}{2!}-\frac{x^3}{3!}+\frac{x^4}{4!}+\frac{x^5}{5!}-\frac{x^6}{6!}-\frac{x^7}{7!}+\ldots
p By introducing the imaginary number #[+m i] in exponent change signs of some parts and multiply sinus we get equality: 
+m.block e^{i\theta} = \cos \theta + i\sin \theta = 1+i\theta-\frac{\theta^2}{2!}-\frac{i\theta^3}{3!}+\frac{\theta^4}{4!}+\frac{i\theta^5}{5!}-\ldots 
p(title="Different bases") To raise other numbers to the power #[+m i] use the following relationship: #[+m a^\theta = (e^{\ln a})^\theta = e^{\theta \ln a}].
ol
	li: +m e^{i\theta} = \begin{cases}\theta = 1: \cos 1 + i\sin 1 \approx 0.5403+0.8415i \\ \theta = \pi: \cos\pi + i\sin\pi =-1+0i=-1\end{cases} 
	li: +m 2^i = e^{i\ln 2} = \cos\ln 2+i\sin\ln 2 \approx 0.7692+0.6390i
	li #[+m i^i = e^{i\ln i} = e^{i\ln\left(\cos\frac \pi 2+i\sin\frac \pi 2\right)} = e^{i\ln e^{\frac{i\pi}2}} = e^{\frac{-\pi}2} \approx 0.2079] - #[strong an imaginary number to an imaginary power is a real number!]
dl
	dt General formula #[+m= String.raw`r^{a_2} e^{-b_2\theta}[\cos(b_2\ln r+a_2\theta + 2a_2k\pi)+i\sin(b_2\ln r+a_2\theta + 2a_2k\pi)]`] for #[+m() (a_1+b_1i)^{a_2+b_2i}] a complex number #[+m a_1+b_1i] to a complex power #[+m a_2+b_2i]
	dd
		ol
			li Change base #[+m() (a_1+b_1i)^{a_2+b_2i} = e^{(a_2+b_2i)\ln(a_1+b_1i)}]
			li Rewrite #[+m a_1+b_1i] in exponential form #[+m re^{i\theta}] and get #[+m e^{(a_2+b_2i)\ln re^{i\theta}}]
			li Transform #[+m= String.raw`e^{(a_2+b_2i)\ln re^{i\theta}} = e^{(a_2+b_2i)(\ln r + i\theta)} = e^{(a_2\ln r-b_2\theta)+i(b_2\ln r+a_2\theta)} = e^{a_2\ln r-b_2\theta}e^{i(b_2\ln r+a_2\theta)} = r^{a_2} e^{-b_2\theta}[\cos(b_2\ln r+a_2\theta)+i\sin(b_2\ln r+a_2\theta)]`]
			li But this formula give many answers, because there are many ways to describe the angle #[+m \theta] in trigonometric functions, so allow #[+m \theta] to vary by multiples of #[+m 2\pi]: #[+m= String.raw`r^{a_2} e^{-b_2\theta}[\cos(b_2\ln r+a_2\theta + 2a_2k\pi)+i\sin(b_2\ln r+a_2\theta + 2a_2k\pi)]`]
	

hgroup 
	h4 Functions of Complex Numbers
	+source(links=['http://www.milefoot.com/math/complex/functionsofi.htm'])
h5 Logarithm functions  
p Since a complex number can be written in exponential form as #[+m re^{i\theta}], a logarithm is almost immediate. We get #[+m \ln re^{i\theta} = \ln r + \ln e^{i\theta} = \ln r + i\theta], which gives the principal value of the natural logarithm. But the angle #[+m \theta] is not unique, as it can vary by multiples of #[+m 2\pi]. Therefore, the formula for the natural logarithm of a complex number is #[+m \ln re^{i\theta} = \ln r + i\theta + 2k\pi i].
ol.example
	li Find the natural logarithm of #[+m i]. Its principal value is #[+m \ln i = \ln {1e^{\frac{i\pi}2} } = \frac \pi 2 i].
	li The natural logarithm of negative one. Its principal value is #[+m \ln{-1} = \ln 1e^{i\pi} = i\pi] #[small thought you couldn't take logarithms of negative numbers! You can, but the answers are not real numbers.]
p #[mark We can use the change-of-base formula to find other base logarithms (including complex bases)]. #[span.example: +m \log_i e = \frac{\ln e}{\ln i} = \frac 1{\frac \pi 2 i} = \frac{-2} \pi  i].
h5 Trigonometric Functions
p Because of the formula #[+m e^{i\theta}=\cos \theta+i\sin \theta], we can immediately obtain some formulas for the sine and cosine functions, in terms of complex exponentials #[+m \cos \theta = \frac{e^{i\theta}+e^{-i\theta}}2, \sin \theta = \frac{e^{i\theta}-e^{-i\theta}}{2i}]. These formulas are often used as definitions of the trigonometric functions for complex numbers.
p Substituting the quantity #[+m i\theta] in place of the variable #[+m \theta], we can produce formulas for pure imaginary numbers #[+m \cos{i\theta} = \frac{e^\theta+e^{-\theta}}2 = \cosh \theta, \qquad \sin{i\theta} = \frac{e^{-\theta}-e^\theta}{2i} = i\sinh \theta] . Notice that the results are related to the hyperbolic functions.
p Then, using the formulas for the sine and cosine of the sum of two angles, we can obtain formulas for the sine and cosine of complex numbers.
| #[+m \cos(a+bi) = \cos a \cosh b - i\sin a \sinh b] #[+m \sin(a+bi) = \sin a \cosh b + i\cos a \sinh b] 
p As an example, consider the cosine of #[+m i]. We get #[+m \cos i = \cos 0 \cosh 1 - i\sin 0 \sinh 1 = \cosh 1 = \frac{ e^1+e^{-1} }2 \approx 1.5431 ].
h5 Hyperbolic Functions
p Using the connection between hyperbolic functions and trigonometric functions, the results for hyperbolic functions are almost immediate.
| #[+m \cosh(a+bi) = \cosh a \cos b + i\sinh a \sin b] #[+m \sinh(a+bi) = \sinh a \cos b + i\cosh a \sin b] 
p As an example, consider the hyperbolic cosine of #[+m i]. We get #[+m \cosh i = \cosh 0 \cos 1 + i\sinh 0 \sin 1 = \cos 1 \approx 0.5403 ].
h5 Inverse Trigonometric Functions
p Since #[+m \cos \theta = \frac{e^{i\theta}+e^{-i\theta}}2], we can find the inverse by replacing the function with the variable #[+m y], swapping #[+m \theta] and #[+m y], then solving for #[+m y]. After the variable swap, we have #[+m \theta = \frac{e^{iy}+e^{-iy}}2]. Multiplying both sides by #[+m 2e^{iy}] gives the equation #[+m 0 = e^{2iy} - 2xe^{iy} + 1]. This can be solved using the quadratic formula, to get #[+m e^{iy} = \frac{2x \pm \sqrt{4x^2-4}}2]. After simplifying, we can take the natural logarithm of both sides and divide by #[+m i]. Then, the result is #[+m= String.raw`\cos^{-1} \theta = -i\ln\left[\theta\pm i\sqrt{1-\theta^2}\right]`]
p (A factor of #[+m i] typically appears as the coefficient of the square root so that the similarities between the inverse cosine and inverse sine formulas are more apparent.)
p By similar arguments, the inverse sine formula is found to be #[+m= String.raw`\sin^{-1} \theta = -i\ln\left[i\theta\pm \sqrt{1-\theta^2}\right]`] and the inverse tangent formula is #[+m \tan^{-1} \theta = \frac i2 \ln\frac{i+\theta}{i-\theta}] 
p As an example, consider the inverse cosine of #[+m i]. We shall find only one of its many values, by using the plus sign in the formula. We get: #[+m= String.raw`\cos^{-1} i = -i\ln\left[i+i\sqrt{1-i^2}\right] = -i\ln\left[(1+\sqrt2)i\right]`]. Then we use the logarithm formula to continue: #[+m= String.raw`-i\ln\left[(1+\sqrt2)i\right] = -i\ln\left[(1+\sqrt2)e^{\frac{i\pi}2}\right] = -i\left[\ln(1+\sqrt2) +\frac \pi 2i \right]`]. This can be simplified, and we get #[+m= String.raw`-i\left[\ln(1+\sqrt2) +\frac \pi 2i \right] = \frac \pi 2 -i\ln(1+\sqrt2) \approx 1.57-0.88i`].
h5 Inverse Hyperbolic Functions
p The formulas are identical to those previously found for inverse hyperbolic functions: #[+m= String.raw`\cosh^{-1} \theta = \ln\left[\theta\pm \sqrt{\theta^2-1}\right] \\ \sinh^{-1} \theta = \ln\left[\theta\pm \sqrt{\theta^2+1}\right]`]
p For example, one of the values of the inverse hyperbolic cosine of #[+m i] (using the plus sign in the formula) is: #[+m= String.raw`-i\left[\ln(1+\sqrt2) +\frac \pi 2i \right] = \frac \pi 2 -i\ln(1+\sqrt2) \approx 1.57-0.88i`]. Then using the logarithm formula, we get: #[+m= String.raw`\ln\left[(1+\sqrt2)i\right] =\ln(1+\sqrt2)+\frac \pi 2i \approx 0.88+1.57i`].

























dl.example
	dt Доказать справедливость равенств #[+m \overline{z_1z_2}=\overline{z_1}\overline{z_2}, \overline{\left(\frac{z_1}{z_2} \right) }=\frac{ \overline{z_1} }{ \overline{z_2} }, \overline{(z^n)}=(\overline{z})^n]
	dd
		ol
			li: +m \overline{z_1z_2}=\overline{z_1}\overline{z_2} \Rightarrow \overline{(a_1+b_1i) * (a_2+b_2i)} = \overline{a_1+b_1i} * \overline{a_2+b_2i} \Rightarrow \overline{([a_1a_2-b_1b_2]+[a_2b_1+a_1b_2]i)} = (a_1-b_1i) * (a_2-b_2i) \Rightarrow ([a_1a_2-b_1b_2]-[a_2b_1+a_1b_2]i) \equiv ([a_1a_2-b_1b_2]+[-a_2b_1-a_1b_2]i)
			li: +m \overline{\left(\frac{z_1}{z_2} \right) }=\frac{ \overline{z_1} }{ \overline{z_2} } \Rightarrow \overline{\left(\frac{a_1+b_1i}{a_2+b_2i} \right) } = \frac{ \overline{a_1+b_1i} }{ \overline{a_2+b_2i} } \Rightarrow \overline{\left(\frac{(a_1+b_1i)(a_2-b_2i)}{(a_2+b_2i)(a_2-b_2i)} \right) }=\frac{a_1-b_1i}{a_2-b_2i} \Rightarrow \overline{ \frac{ [a_1a_2+b_1b_2]+[-b_2a_1+b_1a_2]i }{ a_2^2+b_2 } }=\frac{(a_1-b_1i)(a_2+b_2i)}{(a_2-b_2i)(a_2+b_2i)} \Rightarrow \frac{[a_1a_2+b_1b_2]-[-b_2a_1+b_1a_2]i}{a_2^2+b_2^2}=\frac{[a_1a_2+b_1b_2]+[b_2a_1-b_1a_2]i}{a_2^2+b_2^2} \Rightarrow \frac{[a_1a_2+b_1b_2]+[b_2a_1-b_1a_2]i}{a_2^2+b_2^2}=\frac{[a_1a_2+b_1b_2]+[b_2a_1-b_1a_2]i}{a_2^2+b_2^2}
			li: +m \overline{(z^n)}=(\overline{z})^n \Rightarrow \overline{([\arg z(\sin \theta+ i\cos \theta)]^n)}=(\overline{\arg z(\sin \theta+ i\cos \theta)})^n
	dt Найти #[+m \Re z,\Im z \quad \text{If} \begin{cases}z = \cos{1-i}\\ z = \sh 2i\end{cases}]
	dd
		ol
			li: +m z = \cos{1-i} \Rightarrow z = \frac{e^{i(1-i)}+e^{-i(1-i)} }2 \Rightarrow z = 2^{-1} (e^{1+i}+e^{1-i}) \Rightarrow z = 2^{-1} (ee^i+ee^{-i}) \Rightarrow z = 2^{-1} (e(\cos 1 + i\sin 1)+e(\cos 1 - i\sin 1)) \Rightarrow z = 2^{-1} e(\cos 1 + i\sin 1 + \cos 1 - i\sin 1) \Rightarrow z = 2^{-1} e(\cos 1 + \cos 1) \Rightarrow z = 2^{-1} 2e\cos 1 \Rightarrow z = 0.54e
	dt Найти #[+m z=ie^{-\frac \pi7}: |z|, \arg z]
	dd
		ol
			li Выразим комплексное в экспоненциальной форме в виде тригонометрическом #[+m z = ie^{-\frac \pi7} \Rightarrow z = -\sin{\frac \pi7} + i\cos{\frac \pi7}]
			li.solution Аргумент комлексного числа уже виден и в экспоненциальной форме #[+m \arg z = \frac \pi7], как впринципе и длина но тригонометрический вид позволяет это точнее разглядеть так как синус и косинус с одинаковыми аргументами от 0 до #[+m 2\pi] образуют окружность с радиусом в единицу так и по главному тригонометрическому тождеству #[+m \sin^2 \theta + \cos^2 \theta = 1] понятно что #[+m |z| = \sqrt{(-\sin{\frac \pi7})^2 + (\cos{\frac \pi7})^2} = 1]
	dt: +m \begin{aligned}z_1 = (1-\sqrt 3)i\\z_2=-2e^{\frac \pi3 i}\end{aligned},z = z_1z_2: |z|, \arg z
	dd
		ol 
			li: +m z = [(1-\sqrt 3)i][-2e^{\frac \pi3 i}] = 
//- include temp

</template>
