<script>
	import {Math} from 'docs-lib';</script>

<template lang="pug">
dl
	dt #[dfn Factorial function #[+m !]]
		+source(links=['https://www.mathsisfun.com/numbers/factorial.html'])
	dd
		p Means to multiply a series of descending natural numbers.
		ul.example
			li: +m 4! = 4 × 3 × 2 × 1 = 24
			li: +m 7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5,040
			li: +m 1! = 1
		p.note Generally agreed that #[+m 0! = 1]. It may seem funny that multiplying no numbers together gets us 1, but #[mark it helps simplify a lot of equations].


h3 Combinatorial analysis
	+source(links=['https://encyclopediaofmath.org/wiki/Combinatorial_analysis'])
dl
	dt Combinatorial analysis
	dd The branch of mathematics devoted to the solution of problems of choosing and arranging the elements of certain (usually finite) sets in accordance with prescribed rules. Each such rule defines a method of constructing some configuration of elements of the given set, called a #[dfn combinatorial configuration] #[span.example permutations, combinations and arrangements]. One can therefore say that the aim of combinatorial analysis is the study of combinatorial configurations. This study includes questions of the existence of combinatorial configurations, algorithms and their construction, optimization of such algorithms, as well as the solution of problems of enumeration, in particular the determination of the number of configurations of a given class.
p #[dfn #[+m n]-set] - A set #[+m X] of #[+m n] elements and #[dfn Combination of size #[+m m]] is #[+m m]-subset of #[+m n]-set (#[+m m \le n])
dl 
	dt Binomial coefficients #[+m C_{n}^{m} = C(n, m) = \begin{pmatrix} n \\ m \end{pmatrix} = \frac{n (n - 1) \dots (n - m + 1)}{m!}] 
	dd The number of combinations of size #[+m m] from #[+m n] distinct elements. #[span.example #[+m n=5,m=3: \begin{pmatrix} 5 \\ 3 \end{pmatrix} = \frac{5*\overbrace{(5-1)}^4*\overbrace{(5-3+1)}^3}{3!} = \frac{5*4*3}{3*2} = 5*2 = 10] #[+m () (1,2,3),()]]
p Newton binomial formula #[+m () (1 + t)^{n} =\\sum_{m = 0}^n \left (\begin{array}{c} n \\ m \end{array}\\right ) t^{m} ,\\\left (\begin{array}{c} n \\ 0 \end{array}\\right ) = 1]. 
p An ordered #[+m m]-subset is called an arrangement of size #[+m m]. The number of arrangements of size #[+m m] of #[+m n] distinct elements is equal to #[+m A (n, m) =\n (n - 1) \dots (n - m + 1)]. For #[+m m = n] an arrangement is a permutation of the elements of #[+m X], the number of such permutations being #[+m P (n) = n!].
p The rise of the fundamental notions and developments of combinatorial analysis was parallel with the development of other branches of mathematics such as algebra, number theory, probability theory, all closely linked to combinatorial analysis. The formula expressing the number of combinations in terms of the binomial coefficients and the Newton binomial formula for positive integers #[+m n] was already known to the mathematicians of the Ancient Orient. Magic squares (cf. #[a(title='Magic square' href='https://encyclopediaofmath.org/wiki/Magic_square') Magic square]) of order three were studied for mystical ends. The birth of combinatorial analysis as a branch of mathematics is associated with the work of B. Pascal and P. (de) Fermat on the theory of games of chance. These works, which formed the foundations of probability theory, contained at the same time the principles for determining the number of combinations of elements of a finite set, and thus established the traditional connection between combinatorial analysis and probability theory.
p A large contribution to the systematic development of combinatorial methods was provided by G. Leibniz in his dissertation Ars Combinatoria (the Art of Combinatorics) in which, apparently, the term "combinatorial" appeared for the first time. Of great significance for the establishment of combinatorial analysis was the paper Ars Conjectandi (the Art of Conjecturing) by J. Bernoulli; it was devoted to the basic notions of probability theory, and a number of combinatorial notions were of necessity set forth and applications to the calculation of probabilities were given. It can be said that with the appearance of the works of Leibniz and Bernoulli, combinatorial methods started to be an independent branch of mathematics.
p A major contribution to the development of combinatorial methods was provided by L. Euler. In his papers on the partitioning and decomposition of positive integers into summands he laid down the beginnings of one of the basic methods of calculating combinatorial configurations, namely the method of generating functions.
p The 1950s are associated with an expansion of interest in combinatorial analysis in connection with the rapid development of cybernetics and discrete mathematics and the wide application of computer techniques. In this period an interest in classical combinatorial problems was activated.
p Two factors proved to be of influence in the formation of the direction of subsequent investigations. On the one hand, the choice of the objects of investigation; on the other, the formation of the aims of the investigation, depending in the final reckoning on the complexity of the objects under study. If the combinatorial configuration under investigation has a complex character, then the aim of the investigation is to elucidate the conditions for its existence and to develop algorithms for its construction.
p A large well-developed branch of combinatorial analysis is the theory of block designs (cf. #[a(title='Block design' href='https://encyclopediaofmath.org/wiki/Block_design') Block design], and also [2], [3], [10]); the main problems of this branch relate to questions of classification, conditions of existence and methods of constructing certain classes of block designs. A special case of block designs are the so-called balanced incomplete block designs or #[+m () (b, v, r, k, \lambda )]- configurations, which are defined as collections of #[+m b] #[+m k]-subsets of some #[+m v]- set, called blocks, with the condition that each element appears in #[+m r] blocks and each pair of elements in #[+m \lambda] blocks. When #[+m b = v], and hence when #[+m r = k], a #[+m () (b, v, r, k, \lambda )]- configuration is called a #[+m () (v, k, \lambda )]- configuration, or a symmetric balanced incomplete block design. Even for #[+m () (v, k, \lambda )]- configurations the question of necessary and sufficient conditions for their existence remains unsolved (1988). For the existence of #[+m () (v, k, \lambda )]- configurations it is necessary that when #[+m v] is even, #[+m k - \lambda] be a perfect square, while when #[+m v] is odd, the equation
p #[+m z^{2} =\(k - \lambda ) x^{2} + (- 1)^{(v - 1)/2} \lambda y^{2}]
p must have an integral solution in #[+m x, y, z], not all zero.
p When #[+m v = n^{2} + n + 1], #[+m k = n + 1], #[+m \lambda = 1]a#[+m () (v, k, \lambda )]- configuration represents a projective plane of order #[+m n] and is a particular case of a finite geometry containing a finite number of points and lines under prescribed incidence conditions. Corresponding to each projective plane of order #[+m n] there is a unique complete set of #[+m n - 1] pairwise orthogonal Latin squares of order #[+m n](cf. #[a(title='Latin square' href='https://encyclopediaofmath.org/wiki/Latin_square') Latin square]). In order that a projective plane of order #[+m n] exists, it is necessary that for #[+m n \equiv 1, 2](#[+m \mathop{\rm mod} 4]) there exist integers #[+m a, b] such that
p #[+m n = a^{2} + b^{2} .]
p An affirmative solution to the question of the existence of projective planes of order #[+m n] has been obtained only for #[+m n = p^\alpha], where #[+m p] is a prime number and #[+m \alpha] is a positive integer. Even for #[+m n = 10] this question remains open (1988). Related to this circle of questions is a result in connection with the falsification of the Euler conjecture on the non-existence of pairs of orthogonal Latin squares of order #[+m n = 4k + 2], #[+m k = 1, 2 , . . .](see #[a(title='Classical combinatorial problems' href='https://encyclopediaofmath.org/wiki/Classical_combinatorial_problems') Classical combinatorial problems]).
p Another direction in combinatorial analysis relates to #[a(title='Selection theorems' href='https://encyclopediaofmath.org/wiki/Selection_theorems') selection theorems]. At the foundation of a whole series of results along these lines is the P. Hall theorem on the existence of a system of distinct representatives (a transversal) of a family of subsets #[+m () (X_{1} \dots X_{n} )] of a set #[+m X], that is, a system of elements #[+m () (x_{1} \dots x_{n} )] such that #[+m x_{i} \in X_{i}] and #[+m x_{i} \neq x_{j}] when #[+m i \neq j]. A transversal exists if and only if for any #[+m i_{1} \dots i_{k}] such that #[+m 1 \leq i_{1} < \dots < i_{k} \leq n], #[+m 1 \leq k \leq n], the following inequality holds:
p #[+m | X_{i_{1}} \cup \dots \cup X_{i_{k}} | \geq k,]
p where #[+m | Y |] is the number of elements in #[+m Y]. A corollary of Hall's theorem is the theorem on the existence of Latin squares, stating that any Latin rectangle of order #[+m k \times n], #[+m 1 \leq k \leq n - 1], can be extended to a Latin square of order #[+m n]. Another corollary of Hall's theorem: Any non-negative matrix #[+m A = \| a_{ij} \|_{i, j = 1}^{n}] such that
p #[+m \sum_{i = 1}^n a_{ij} =\\sum_{j = 1}^n a_{ij} =\t > 0,]
p can be represented in the form
p #[+m A =\\alpha_{1} \Pi_{1} + \dots + \alpha_{s} \Pi_{s} ,]
p where #[+m \Pi_{1} \dots \Pi_{s}] are permutation matrices of order #[+m n] and #[+m s \leq (n - 1)^{2} + 1]. Hall's theorem also implies that the minimum number of rows and columns of a non-negative matrix containing all positive elements is equal to the maximum number of elements that pairwise are not in the same row or in the same column. The extremal property of partially ordered sets, which is analogous to this theorem, is established by the theorem stating that the minimum number of non-intersecting chains is the same as the size of the maximal subset consisting of pairwise-incomparable elements. The following theorem also bears an extremal character: If for an #[+m n]- set #[+m X] one collects all the #[+m C (n, r)] combinations of #[+m r] elements and partitions them into #[+m k] non-intersecting classes, then, given an integer #[+m m], there exists an #[+m n_{0} = n_{0} (m, r, k)] such that for #[+m n \geq n_{0}] there is a subset of #[+m m] elements #[+m Y \subset X] for which all the #[+m C (m, r)] combinations belong to the same class.
p The travelling-salesman problem is an extremal problem too; it consists in composing the shortest route visiting #[+m n] towns and returning to the starting point, where the distances between the towns are known. This problem has applications in the study of transportation networks. Combinatorial problems of an extremal character are considered in the theory of flows in networks and in graph theory.
p A significant portion of combinatorial analysis consists of enumeration problems. For their solution one either indicates a method of sorting out combinatorial configurations of a given class, or one determines the number of them, or one does both. Typical results of enumeration problems are: The number of permutations of order #[+m n] with #[+m k] cycles is equal to #[+m | S (n, k) |], where #[+m S (n, k)] is the Stirling number of the first kind, defined by the equation
p #[+m x (x - 1) \dots (x - n + 1) =\\sum_{k = 0}^n S (n, k) x^{k} ;]
p the number of partitions of a set of #[+m n] elements into #[+m k] subsets is equal to the Stirling number of the second kind
p #[+m \sigma (n, k) =\{ \frac{1}{k!}} \sum_{j = 0}^{ k} (- 1)^{j} \left (\begin{array}{c} k \\ j \end{array}\\right ) (k - j)^{n} ;]
p and, the number of arrangements of #[+m m] distinct objects in #[+m n] distinct cells with no cell empty is equal to #[+m n! \sigma (m, n)].
p A useful device for the solution of enumeration problems is the permanent of a matrix. The permanent of a matrix #[+m A = \| a_{ij} \|](#[+m i = 1 \dots n]; #[+m j = 1 \dots m], #[+m n \leq m]) the elements of which belong to some ring, is defined by the formula
p #[+m \mathop{\rm per} A =\\sum_{(j_{1} \dots j_{n} )} a_{1j_{1}} \dots a_{nj_{n}} ,]
p where the summation is carried out over all possible arrangements of size #[+m n] from #[+m m] distinct elements. The number of transversals of some family of subsets of a finite set is equal to the permanent of the corresponding incidence matrix.
p A whole class of problems on the determination of the number of permutations with restricted positions reduces to the calculation of permanents. For convenience, these problems are sometimes formulated as problems on the arrangement of mutually non-attacking pieces on an #[+m n \times n] chessboard. Connected with the determination of the permanents of certain classes of matrices are variants of the problem of dimers, which arises in the study of the phenomenon of adsorption and consists in the determination of the number of ways of combining the atoms of di-atomic molecules on some surface. Its solution can also be obtained in terms of Pfaffians (cf. #[a(href='https://encyclopediaofmath.org/wiki/Pfaffian' title='Pfaffian') Pfaffian]), which are certain functions of matrices close to determinants. The problem of the number of Latin rectangles (squares) is also connected with the development of effective methods for calculating permanents of certain #[+m () (0, 1)]- matrices.
p For the calculation of permanents one applies the formula:
p #[+m \mathop{\rm per} A =\\sum_{k = m - n}^{ m} (- 1)^{k - m + n} \left (\begin{array}{c} k \\ m - n \end{array}\\right ) S_{k} ,]
p #[+m S_{k} = \sum_{1 \leq j_{1} < \dots < j_{k} \leq m} \prod_{i = 1}^n \left (\sum_{l = 1}^{ m} a_{il} - \sum_{r = 1}^{ k} a_{ij_{r}} \right ) .]
p There are a large number of inequalities giving an estimate of the size of the permanent in certain classes of matrices. The determination of the extremal values of the permanent in specific classes of non-negative matrices is of interest. For a #[+m () (0, 1)]- matrix #[+m A] with given values #[+m r_{1} \dots r_{n}] of the number of ones in the rows one has the estimate
p #[+m \mathop{\rm per} A \leq \prod_{i = 1}^n (r!)^{1/r_{i}} ,]
p cf. [12]. The famous #[a(title='Van der Waerden conjecture' href='https://encyclopediaofmath.org/wiki/Van_der_Waerden_conjecture') van der Waerden conjecture], that the minimum permanent of a doubly-stochastic matrix of order #[+m n] is equal to #[+m n!/n^{n}] was proved, independently, by D.I. Falikman (1979) and G.P. Egorichev (1980), cf. [13].
p An important role in the solution of enumeration problems is played by the method of generating functions (cf. #[a(title='Generating function' href='https://encyclopediaofmath.org/wiki/Generating_function') Generating function]). A generating function
p #[+m f (t) =\\sum_{n = 0}^\infty a_{n} t^{n}]
p sets up a correspondence between the sequence #[+m () (a_{0} , a_{1} , . . . )] and the elements of some ring, and is regarded as a formal power series. According to this definition, generating functions are effectively used for the solution of enumeration problems in parallel with methods of recurrence relations and finite-difference equations. In obtaining asymptotic formulas for the generating functions, analytic functions of a real or complex variable are usually employed. In the latter case, the Cauchy integral is applied in finding expressions for the coefficients.
p There are results in the direction of a possible unification of enumeration methods; these are connected with the study of so-called incidence algebras and the use of the Möbius function on a partially ordered set (see for example, [10]). In the solution of enumeration problems, an essential role is played by the formalization of the concept of indistinguishability of objects. The use of the notion of equivalence of objects with respect to a certain group of permutations in combination with the application of the method of generating functions forms the basis of the so-called Pólya theory of enumeration (see [10]), the essence of which is as follows. Consider the set #[+m Y^{X}] of configurations
p #[+m f: X \rightarrow Y,\\| X | = m,\\| Y | = n.]
p On the set #[+m X], a group #[+m A] of permutations acts, thus defining an equivalence relation #[+m \sim] under which #[+m f \sim f_{1}], #[+m f, f_{1} \in Y^{X}], if there exists an #[+m \alpha \in A] such that #[+m f (\alpha (x)) = f_{1} (x)] for all #[+m x \in X]. To each #[+m y \in Y] corresponds a characteristic #[+m= String.raw`[ y] = (s_{1} \dots s_{k} )`], where #[+m s_{i}], #[+m i = 1 \dots k], are elements of an Abelian group. The characteristic of the configuration #[+m f] is given by the formula #[+m= String.raw`[ f] =\\sum_{x \in X} [ f (x)]`] .
p If #[+m a (s_{1} \dots s_{k} )] is the number of elements #[+m y \in Y] with a given value of the characteristic and #[+m b_{m} (s_{1} \dots s_{k} )] is the number of inequivalent configurations #[+m f \in Y^{X}],
p #[+m F (y_{1} \dots y_{k} ) =\\sum_{(s_{1} \dots s_{k} )} a (s_{1} \dots s_{k} ) y_{1}^{s_{1}} \dots y_{k}^{s_{k}} ,]
p #[+m \Phi_{m} (y_{1} \dots y_{k} ) = \sum_{(s_{1} \dots s_{k} )} b (s_{1} \dots s_{k} ) y_{1}^{s_{1}} \dots y_{k}^{s_{k}} ,]
p then Pólya's fundamental theorem states that
p #[+m \Phi_{m} (y_{1} \dots y_{k} ) =]
p #[+m =\Z (F (y_{1} \dots y_{k} ), F (y_{1}^{2} \dots y_{k}^{2} ) \dots F (y_{1}^{m} \dots y_{k}^{m} )),]
p where #[+m Z] is the cyclic index of the group #[+m A], defined by the equation
p #[+m Z (t_{1} \dots t_{m} ; A) =]
p #[+m =\\sum_{j_{1} + 2j_{2} + \dots + mj_{m} = n} C (j_{1} \dots j_{m} ; A) t_{1}^{j_{1}} \dots t_{m}^{j_{m}} ,]
p and #[+m C (j_{1} \dots j_{m} ; A)] is the number of elements of the cyclic class #[+m \{ 1^{j_{1}} \dots m^{j_{m}} \}](cf. #[a(title='Symmetric group' href='https://encyclopediaofmath.org/wiki/Symmetric_group') Symmetric group]) of #[+m A]. This theorem is based on Burnside's lemma: The number of equivalence classes #[+m N (A)] defined on the set #[+m X] by the permutation group #[+m A] is given by the formula
p #[+m N (A) =\{ \frac{1}{| A |}} \sum_{\alpha \in A} j_{1} (\alpha ),]
p where #[+m j_{1} (\alpha )] is the number of unit cycles of #[+m \alpha \in A]. Pólya's theory has applications in the solution of enumeration problems in graph theory and in the enumeration of carbon chemical compounds. There is a generalization of Pólya's theory to the case when the equivalence of two configurations is defined by two groups #[+m G] and #[+m H] acting on #[+m X] and #[+m Y], respectively (see [4] and [10]). In this form it is applied, for example, in the determination of the number of non-isomorphic abstract automata.
p If #[+m X = \{ 1 \dots m \}], #[+m Y = \{ a_{1} \dots a_{n} \}] and #[+m \sigma : X \rightarrow Y], where #[+m a_{j}] is used as an image #[+m \alpha_{j}] times, then the expression
p #[+m= String.raw`[ \sigma ] =\[ a_{1}^{\alpha_{1}} \dots a_{n}^{\alpha_{n}} ] ,\\\alpha_{1} + \dots + \alpha_{n} = m,`]
p is called the first specification of #[+m \sigma]. If the numbers #[+m \alpha_{1} \dots \alpha_{n}] contain #[+m \beta_{0}] zeros, #[+m \beta_{1}] ones, etc., then the expression
p #[+m= String.raw`[[ 0^{\beta_{0}} \dots m^{\beta_{m}} ],\\\beta_{0} + \dots + \beta_{m} = n, ]`]
p #[+m \beta_{1} + 2 \beta_{2} + \dots + m \beta_{m} = m,]
p is called the second specification. Under some specification of the groups #[+m G] and #[+m H] defining the equivalence of configurations #[+m \sigma : X \rightarrow Y], it is possible to give a method of constructing generating functions for the enumeration of the inequivalent configurations. This method, called the general combinatorial scheme, can be subdivided into four particular cases, according as the groups #[+m G] and #[+m H] take values in the identity group #[+m E] or the symmetric groups #[+m S_{n}] of corresponding orders. These particular cases are the models for the majority of the known combinatorial schemes (see [9], [10]).
p 1) The commutative non-symmetric case: #[+m G = S_{m}], #[+m H = E]. This models combination schemes of distributing identical objects into different cells, etc. The generating function for the enumeration of inequivalent configurations #[+m \sigma] such that
p #[+m= String.raw`[ \sigma ] =\[ a_{1}^{\alpha_{1}} \dots a_{n}^{\alpha_{n}} ] ,`]
p #[+m \alpha_{i} \in \Lambda_{i} \subseteq \mathbf N_{0} =\\{ 0, 1 , . . . \} ,\\Lambda = (\Lambda_{1} \dots \Lambda_{n} ),]
p has the form:
p #[+m \Phi (t; x_{1} \dots x_{n} ; \Lambda ) =\\prod_{j = 1}^n\\sum_{\alpha_{j} \in \Lambda_{j}} (tx_{j} )^{\alpha_{j}} .]
p 2) The non-commutative non-symmetric case: #[+m G = E], #[+m H = E]. This models allocation schemes of distributing distinct objects into different cells, etc. The generating function for the enumeration of inequivalent configurations #[+m \sigma] such that
p #[+m= String.raw`[ \sigma ] =\[ a_{1}^{\alpha_{1}} \dots a_{n}^{\alpha_{n}} ] ,\\\alpha_{i} \in \Lambda_{i} ,\\\Lambda = (\Lambda_{1} \dots \Lambda_{n} ),`]
p has the form:
p #[+m \widetilde \Phi (t; x_{1} \dots x_{n} ; \Lambda ) =\\prod_{j = 1}^n\\sum_{\alpha_{j} \in \Lambda_{j}} \frac{t^{\alpha_{j}}}{\alpha_{j} !} x_{j}^{\alpha_{j}} .]
p 3) The commutative symmetric case: #[+m G = S_{m}], #[+m H = S_{n}]. This models schemes of distributing identical objects into identical cells, the enumeration of the partitions of natural numbers, etc. The enumeration of configurations #[+m \sigma] such that
p #[+m= String.raw`[[ \sigma ] =\[ [ 0^{\beta_{0}} \dots m^{\beta_{m}} ] ] ,\\\beta_{j} \in \Lambda_{j} ,\\\Lambda = (\Lambda_{1} , \Lambda_{2} , . . . ), ]`]
p is based on the use of generating functions of the form:
p #[+m \Psi (t; x_{1} , . . . ; \Lambda ) =\\prod_{j = 1}^\infty\\sum_{\beta_{j} \in \Lambda_{j}} (x_{j} t^{j} )^{\beta_{j}} .]
p 4) The non-commutative symmetric case: #[+m G = E], #[+m H = S_{n}]. This models schemes of partitioning finite sets into blocks, distributing distinct objects into identical cells, etc. The enumeration of configurations #[+m \sigma] such that
p #[+m= String.raw`[[ \sigma ] =\[ [ 0^{\beta_{0}} \dots m^{\beta_{m}} ] ] ,\\\beta_{j} \in \Lambda_{j} ,\\\Lambda = (\Lambda_{1} , \Lambda_{2} , . . . ), ]`]
p is based on the use of generating functions of the form:
p #[+m \widetilde \Psi (t; x_{1} , . . . ; \Lambda ) =\\prod_{j = 1}^\infty\\sum_{\beta_{j} \in \Lambda_{j}} \left (\frac{x_{j} t^{j}}{j!} \right )^{\beta_{j}} { \frac{1}{\beta_{j} !}} .]
p An important place in combinatorial analysis is taken up by asymptotic methods. They are applied both for the simplification of complex finite expressions for large values of the parameters entering into them, as well as for obtaining approximate formulas in roundabout ways when the exact formulas are unknown. It is sometimes convenient to formulate a combinatorial problem of an enumerative character as a problem of finding the characteristics of the distribution of some random process. Such an interpretation makes it possible to apply the well-developed apparatus of probability theory for finding asymptotics or limit theorems. Classical schemes of random allocations of objects in cells are open to a detailed investigation from these points of view; so also are random partitions of sets, the cyclic structure of random permutations, as well as various classes of random graphs, including graphs of mappings (see [8], [9], [11]).
p The probabilistic approach is applied in the study of the combinatorial properties of symmetric groups and semi-groups. The limiting distribution of the order of a random element of the symmetric group #[+m S_{n}] as #[+m n \rightarrow \infty] has been investigated, as also have the asymptotics of the probability of the generation of random elements of them. For certain classes of random non-negative matrices, the distributions have been studied of the number of zero rows in a matrix and in permanents, and estimates have been given of the probability of the primitiveness of such matrices. For the proof of the existence of combinatorial configurations without constructing them, one sometimes employs a certain specific probabilistic device. The essence of this device consists in the proof of the existence of the configuration (without constructing it) by means of an estimate of the probability of some event (see [7]).
h6 References
table: tbody
	tr
		td [1]
		td J. Riordan, "An introduction to combinational analysis" , Wiley (1958)
	tr
		td [2]
		td H.J. Ryser, "Combinatorial mathematics" , #[i Carus Math. Monogr.] , #[b 14] , Math. Assoc. Amer. (1963)
	tr
		td [3]
		td M. Hall, "Combinatorial theory" , Blaisdell (1967)
	tr
		td [4]
		td E.F. Beckenbach (ed.) , #[i Applied combinatorial mathematics] , Wiley (1964)
	tr
		td [5]
		td F. Harary, "Graph theory" , Addison-Wesley (1969) pp. Chapt. 9
	tr
		td [6]
		td F Harary, E. Palmer, "Graphical enumeration" , Acad. Press (1973)
	tr
		td [7]
		td P. Erdös, J. Spencer, "Probabilistic methods in combinatorics" , Acad. Press (1974)
	tr
		td [8]
		td V.F. Kolchin, V.P. Chistyakov, "Combinatorial problems of probability theory" #[i Itogi Nauk. i Tekhn. Teor. Veroyatnost. Mat. Stat. Teoret. Kibernet.] , #[b 11] (1974) pp. 5–45 (In Russian)
	tr
		td [9]
		td V.N. Sachkov, , #[i Questions of cybernetics. Proc. Seminar on Combinatorial Mathematics] , Moscow (1973) pp. 146–164 (In Russian)
	tr
		td [10]
		td V.N. Sachkov, "Combinatorial methods in discrete mathematics" , Moscow (1977) (In Russian)
	tr
		td [11]
		td V.N. Sachkov, "Probabilistic methods in combinatorial analysis" , Moscow (1978) (In Russian)
	tr
		td [12]
		td H. Minc, "Permanents" , Addison-Wesley (1978)
	tr
		td [13]
		td G.P. [G.P. Egorichev] Egorychev, "The solution of van der Waerden's problem for permanents" #[i Adv. in Math.] , #[b 42] : 3 (1981) pp. 299–305
h6 Comments
p The marriage problem is the following. Let there be a set #[+m \{ g_{1} \dots g_{n} \}] of #[+m n] girls and a set #[+m \{ b_{1} \dots b_{m} \}] of #[+m m] boys. Each girl #[+m g_{i}] likes a subset #[+m B_{i} \subset \{ b_{1} \dots b_{m} \}] of boys. When is it possible that each girl marries a boy she likes? The solution is of course given by the P. Hall theorem on distinct representatives, and this theorem is also known as the marriage theorem or the P. Hall marriage theorem. The abbreviation SDR is often used for systems of distinct representatives. Let #[+m G] be the bipartite graph (cf. #[a(title='Graph, bipartite' href='https://encyclopediaofmath.org/wiki/Graph,_bipartite') Graph, bipartite]) consisting of the vertices #[+m \{ g_{1} \dots g_{n} , b_{1} \dots b_{m} \}] and with an edge joining #[+m g_{i}] and #[+m b_{j}] if and only if girl #[+m i] likes boy #[+m j](and no other edges). Then a solution of the marriage problem provides a matching, and in this context the marriage theorem is also known as the P. Hall matching theorem.
p A good up-to-date book on design theory is [a1]. For more on extremal problems in graph theory cf. [a2]. For more on the dimer problem and other uses of combinatorics in theoretical physics cf., e.g., [a3]. Finally, [a4] is completely devoted to transversal theory including infinite versions.
h6 References
table: tbody
	tr
		td [a1]
		td D.R. Hughes, F.C. Piper, "Design theory" , Cambridge Univ. Press (1985)
	tr
		td [a2]
		td B. Bollobas, "Extremal graph theory" , Acad. Press (1978)
	tr
		td [a3]
		td J.K. Percus, "Combinatorial methods" , Springer (1971)
	tr
		td [a4]
		td L. Mirsky, "Transversal theory" , Acad. Press (1971)




//- div
	h3 Combinatorial analysis
		+source(links=['https://encyclopediaofmath.org/wiki/Combinatorial_analysis'])
	dl
		dt Combinatorial analysis
		dd The branch of mathematics devoted to the solution of problems of choosing and arranging the elements of certain (usually finite) sets in accordance with prescribed rules. Each such rule defines a method of constructing some configuration of elements of the given set, called a #[dfn combinatorial configuration] #[span.example permutations, combinations and arrangements]. One can therefore say that the aim of combinatorial analysis is the study of combinatorial configurations. This study includes questions of the existence of combinatorial configurations, algorithms and their construction, optimization of such algorithms, as well as the solution of problems of enumeration, in particular the determination of the number of configurations of a given class.
	p #[dfn #[+m n]-set] - A set #[+m X] of #[+m n] elements and #[dfn Combination of size #[+m m]] is #[+m m]-subset of #[+m n]-set (#[+m m \le n])
	dl 
		dt Binomial coefficients #[+m C_{n}^{m} = C(n, m) = \begin{pmatrix} n \\ m \end{pmatrix} = \frac{n (n - 1) \dots (n - m + 1)}{m!}] 
		dd The number of combinations of size #[+m m] from #[+m n] distinct elements. #[span.example #[+m n=5,m=3: \begin{pmatrix} 5 \\ 3 \end{pmatrix} = \frac{5*\overbrace{(5-1)}^4*\overbrace{(5-3+1)}^3}{3!} = \frac{5*4*3}{3*2} = 5*2 = 10] #[+m() (1,2,3),()]]
	p Newton binomial formula #[+m() (1 + t)^{n} =\\sum_{m = 0}^n \left (\begin{array}{c} n \\ m \end{array}\\right ) t^{m} ,\\\left (\begin{array}{c} n \\ 0 \end{array}\\right ) = 1]. 
	p An ordered #[+m m]-subset is called an arrangement of size #[+m m]. The number of arrangements of size #[+m m] of #[+m n] distinct elements is equal to #[+m A (n, m) =\n (n - 1) \dots (n - m + 1)]. For #[+m m = n] an arrangement is a permutation of the elements of #[+m X], the number of such permutations being #[+m P (n) = n! ].
	p The rise of the fundamental notions and developments of combinatorial analysis was parallel with the development of other branches of mathematics such as algebra, number theory, probability theory, all closely linked to combinatorial analysis. The formula expressing the number of combinations in terms of the binomial coefficients and the Newton binomial formula for positive integers #[+m n] was already known to the mathematicians of the Ancient Orient. Magic squares (cf. #[a(title='Magic square' href='https://encyclopediaofmath.org/wiki/Magic_square') Magic square]) of order three were studied for mystical ends. The birth of combinatorial analysis as a branch of mathematics is associated with the work of B. Pascal and P. (de) Fermat on the theory of games of chance. These works, which formed the foundations of probability theory, contained at the same time the principles for determining the number of combinations of elements of a finite set, and thus established the traditional connection between combinatorial analysis and probability theory.
	p A large contribution to the systematic development of combinatorial methods was provided by G. Leibniz in his dissertation Ars Combinatoria (the Art of Combinatorics) in which, apparently, the term "combinatorial" appeared for the first time. Of great significance for the establishment of combinatorial analysis was the paper Ars Conjectandi (the Art of Conjecturing) by J. Bernoulli; it was devoted to the basic notions of probability theory, and a number of combinatorial notions were of necessity set forth and applications to the calculation of probabilities were given. It can be said that with the appearance of the works of Leibniz and Bernoulli, combinatorial methods started to be an independent branch of mathematics.
	p A major contribution to the development of combinatorial methods was provided by L. Euler. In his papers on the partitioning and decomposition of positive integers into summands he laid down the beginnings of one of the basic methods of calculating combinatorial configurations, namely the method of generating functions.
	p The 1950s are associated with an expansion of interest in combinatorial analysis in connection with the rapid development of cybernetics and discrete mathematics and the wide application of computer techniques. In this period an interest in classical combinatorial problems was activated.
	p Two factors proved to be of influence in the formation of the direction of subsequent investigations. On the one hand, the choice of the objects of investigation; on the other, the formation of the aims of the investigation, depending in the final reckoning on the complexity of the objects under study. If the combinatorial configuration under investigation has a complex character, then the aim of the investigation is to elucidate the conditions for its existence and to develop algorithms for its construction.
	p A large well-developed branch of combinatorial analysis is the theory of block designs (cf. #[a(title='Block design' href='https://encyclopediaofmath.org/wiki/Block_design') Block design], and also [2], [3], [10]); the main problems of this branch relate to questions of classification, conditions of existence and methods of constructing certain classes of block designs. A special case of block designs are the so-called balanced incomplete block designs or #[+m() (b, v, r, k, \lambda ) ]- configurations, which are defined as collections of #[+m b] #[+m k]-subsets of some #[+m v]- set, called blocks, with the condition that each element appears in #[+m r] blocks and each pair of elements in #[+m \lambda ] blocks. When #[+m b = v ], and hence when #[+m r = k ], a #[+m() (b, v, r, k, \lambda ) ]- configuration is called a #[+m() (v, k, \lambda ) ]- configuration, or a symmetric balanced incomplete block design. Even for #[+m() (v, k, \lambda ) ]- configurations the question of necessary and sufficient conditions for their existence remains unsolved (1988). For the existence of #[+m() (v, k, \lambda ) ]- configurations it is necessary that when #[+m v] is even, #[+m k - \lambda ] be a perfect square, while when #[+m v] is odd, the equation
	p #[+m z^{2} =\(k - \lambda ) x^{2} + (- 1)^{(v - 1)/2} \lambda y^{2} ]
	p must have an integral solution in #[+m x, y, z ], not all zero.
	p When #[+m v = n^{2} + n + 1 ], #[+m k = n + 1 ], #[+m \lambda = 1 ]a#[+m() (v, k, \lambda ) ]- configuration represents a projective plane of order #[+m n] and is a particular case of a finite geometry containing a finite number of points and lines under prescribed incidence conditions. Corresponding to each projective plane of order #[+m n] there is a unique complete set of #[+m n - 1 ] pairwise orthogonal Latin squares of order #[+m n](cf. #[a(title='Latin square' href='https://encyclopediaofmath.org/wiki/Latin_square') Latin square]). In order that a projective plane of order #[+m n] exists, it is necessary that for #[+m n \equiv 1, 2 ](#[+m \mathop{\rm mod} 4 ]) there exist integers #[+m a, b ] such that
	p #[+m n = a^{2} + b^{2} . ]
	p An affirmative solution to the question of the existence of projective planes of order #[+m n] has been obtained only for #[+m n = p^\alpha ], where #[+m p] is a prime number and #[+m \alpha ] is a positive integer. Even for #[+m n = 10 ] this question remains open (1988). Related to this circle of questions is a result in connection with the falsification of the Euler conjecture on the non-existence of pairs of orthogonal Latin squares of order #[+m n = 4k + 2 ], #[+m k = 1, 2 , . . . ](see #[a(title='Classical combinatorial problems' href='https://encyclopediaofmath.org/wiki/Classical_combinatorial_problems') Classical combinatorial problems]).
	p Another direction in combinatorial analysis relates to #[a(title='Selection theorems' href='https://encyclopediaofmath.org/wiki/Selection_theorems') selection theorems]. At the foundation of a whole series of results along these lines is the P. Hall theorem on the existence of a system of distinct representatives (a transversal) of a family of subsets #[+m() (X_{1} \dots X_{n} ) ] of a set #[+m X], that is, a system of elements #[+m() (x_{1} \dots x_{n} ) ] such that #[+m x_{i} \in X_{i} ] and #[+m x_{i} \neq x_{j} ] when #[+m i \neq j ]. A transversal exists if and only if for any #[+m i_{1} \dots i_{k} ] such that #[+m 1 \leq i_{1} < \dots < i_{k} \leq n ], #[+m 1 \leq k \leq n ], the following inequality holds:
	p #[+m | X_{i_{1}} \cup \dots \cup X_{i_{k}} | \geq k, ]
	p where #[+m | Y | ] is the number of elements in #[+m Y]. A corollary of Hall's theorem is the theorem on the existence of Latin squares, stating that any Latin rectangle of order #[+m k \times n ], #[+m 1 \leq k \leq n - 1 ], can be extended to a Latin square of order #[+m n]. Another corollary of Hall's theorem: Any non-negative matrix #[+m A = \| a_{ij} \|_{i, j = 1}^{n} ] such that
	p #[+m \sum_{i = 1}^n a_{ij} =\\sum_{j = 1}^n a_{ij} =\t > 0, ]
	p can be represented in the form
	p #[+m A =\\alpha_{1} \Pi_{1} + \dots + \alpha_{s} \Pi_{s} , ]
	p where #[+m \Pi_{1} \dots \Pi_{s} ] are permutation matrices of order #[+m n] and #[+m s \leq (n - 1)^{2} + 1 ]. Hall's theorem also implies that the minimum number of rows and columns of a non-negative matrix containing all positive elements is equal to the maximum number of elements that pairwise are not in the same row or in the same column. The extremal property of partially ordered sets, which is analogous to this theorem, is established by the theorem stating that the minimum number of non-intersecting chains is the same as the size of the maximal subset consisting of pairwise-incomparable elements. The following theorem also bears an extremal character: If for an #[+m n]- set #[+m X] one collects all the #[+m C (n, r) ] combinations of #[+m r] elements and partitions them into #[+m k] non-intersecting classes, then, given an integer #[+m m], there exists an #[+m n_{0} = n_{0} (m, r, k) ] such that for #[+m n \geq n_{0} ] there is a subset of #[+m m] elements #[+m Y \subset X ] for which all the #[+m C (m, r) ] combinations belong to the same class.
	p The travelling-salesman problem is an extremal problem too; it consists in composing the shortest route visiting #[+m n] towns and returning to the starting point, where the distances between the towns are known. This problem has applications in the study of transportation networks. Combinatorial problems of an extremal character are considered in the theory of flows in networks and in graph theory.
	p A significant portion of combinatorial analysis consists of enumeration problems. For their solution one either indicates a method of sorting out combinatorial configurations of a given class, or one determines the number of them, or one does both. Typical results of enumeration problems are: The number of permutations of order #[+m n] with #[+m k] cycles is equal to #[+m | S (n, k) | ], where #[+m S (n, k) ] is the Stirling number of the first kind, defined by the equation
	p #[+m x (x - 1) \dots (x - n + 1) =\\sum_{k = 0}^n S (n, k) x^{k} ; ]
	p the number of partitions of a set of #[+m n] elements into #[+m k] subsets is equal to the Stirling number of the second kind
	p #[+m \sigma (n, k) =\{ \frac{1}{k!}} \sum_{j = 0}^{ k} (- 1)^{j} \left (\begin{array}{c} k \\ j \end{array}\\right ) (k - j)^{n} ; ]
	p and, the number of arrangements of #[+m m] distinct objects in #[+m n] distinct cells with no cell empty is equal to #[+m n! \sigma (m, n) ].
	p A useful device for the solution of enumeration problems is the permanent of a matrix. The permanent of a matrix #[+m A = \| a_{ij} \| ](#[+m i = 1 \dots n ]; #[+m j = 1 \dots m ], #[+m n \leq m ]) the elements of which belong to some ring, is defined by the formula
	p #[+m \mathop{\rm per} A =\\sum_{(j_{1} \dots j_{n} )} a_{1j_{1}} \dots a_{nj_{n}} , ]
	p where the summation is carried out over all possible arrangements of size #[+m n] from #[+m m] distinct elements. The number of transversals of some family of subsets of a finite set is equal to the permanent of the corresponding incidence matrix.
	p A whole class of problems on the determination of the number of permutations with restricted positions reduces to the calculation of permanents. For convenience, these problems are sometimes formulated as problems on the arrangement of mutually non-attacking pieces on an #[+m n \times n ] chessboard. Connected with the determination of the permanents of certain classes of matrices are variants of the problem of dimers, which arises in the study of the phenomenon of adsorption and consists in the determination of the number of ways of combining the atoms of di-atomic molecules on some surface. Its solution can also be obtained in terms of Pfaffians (cf. #[a(href='https://encyclopediaofmath.org/wiki/Pfaffian' title='Pfaffian') Pfaffian]), which are certain functions of matrices close to determinants. The problem of the number of Latin rectangles (squares) is also connected with the development of effective methods for calculating permanents of certain #[+m() (0, 1) ]- matrices.
	p For the calculation of permanents one applies the formula:
	p #[+m \mathop{\rm per} A =\\sum_{k = m - n}^{ m} (- 1)^{k - m + n} \left (\begin{array}{c} k \\ m - n \end{array}\\right ) S_{k} , ]
	p #[+m S_{k} = \sum_{1 \leq j_{1} < \dots < j_{k} \leq m} \prod_{i = 1}^n \left (\sum_{l = 1}^{ m} a_{il} - \sum_{r = 1}^{ k} a_{ij_{r}} \right ) . ]
	p There are a large number of inequalities giving an estimate of the size of the permanent in certain classes of matrices. The determination of the extremal values of the permanent in specific classes of non-negative matrices is of interest. For a #[+m() (0, 1) ]- matrix #[+m A] with given values #[+m r_{1} \dots r_{n} ] of the number of ones in the rows one has the estimate
	p #[+m \mathop{\rm per} A \leq \prod_{i = 1}^n (r!)^{1/r_{i}} , ]
	p cf. [12]. The famous #[a(title='Van der Waerden conjecture' href='https://encyclopediaofmath.org/wiki/Van_der_Waerden_conjecture') van der Waerden conjecture], that the minimum permanent of a doubly-stochastic matrix of order #[+m n] is equal to #[+m n!/n^{n} ] was proved, independently, by D.I. Falikman (1979) and G.P. Egorichev (1980), cf. [13].
	p An important role in the solution of enumeration problems is played by the method of generating functions (cf. #[a(title='Generating function' href='https://encyclopediaofmath.org/wiki/Generating_function') Generating function]). A generating function
	p #[+m f (t) =\\sum_{n = 0}^\infty a_{n} t^{n} ]
	p sets up a correspondence between the sequence #[+m() (a_{0} , a_{1} , . . . ) ] and the elements of some ring, and is regarded as a formal power series. According to this definition, generating functions are effectively used for the solution of enumeration problems in parallel with methods of recurrence relations and finite-difference equations. In obtaining asymptotic formulas for the generating functions, analytic functions of a real or complex variable are usually employed. In the latter case, the Cauchy integral is applied in finding expressions for the coefficients.
	p There are results in the direction of a possible unification of enumeration methods; these are connected with the study of so-called incidence algebras and the use of the Möbius function on a partially ordered set (see for example, [10]). In the solution of enumeration problems, an essential role is played by the formalization of the concept of indistinguishability of objects. The use of the notion of equivalence of objects with respect to a certain group of permutations in combination with the application of the method of generating functions forms the basis of the so-called Pólya theory of enumeration (see [10]), the essence of which is as follows. Consider the set #[+m Y^{X} ] of configurations
	p #[+m f: X \rightarrow Y,\\| X | = m,\\| Y | = n. ]
	p On the set #[+m X], a group #[+m A] of permutations acts, thus defining an equivalence relation #[+m \sim ] under which #[+m f \sim f_{1} ], #[+m f, f_{1} \in Y^{X} ], if there exists an #[+m \alpha \in A ] such that #[+m f (\alpha (x)) = f_{1} (x) ] for all #[+m x \in X ]. To each #[+m y \in Y ] corresponds a characteristic #[+m [ y] = (s_{1} \dots s_{k} ) ], where #[+m s_{i} ], #[+m i = 1 \dots k ], are elements of an Abelian group. The characteristic of the configuration #[+m f] is given by the formula #[+m= String.raw`[ f] =\\sum_{x \in X} [ f (x)]`] .
	p If #[+m a (s_{1} \dots s_{k} ) ] is the number of elements #[+m y \in Y ] with a given value of the characteristic and #[+m b_{m} (s_{1} \dots s_{k} ) ] is the number of inequivalent configurations #[+m f \in Y^{X} ],
	p #[+m F (y_{1} \dots y_{k} ) =\\sum_{(s_{1} \dots s_{k} )} a (s_{1} \dots s_{k} ) y_{1}^{s_{1}} \dots y_{k}^{s_{k}} , ]
	p #[+m \Phi_{m} (y_{1} \dots y_{k} ) = \sum_{(s_{1} \dots s_{k} )} b (s_{1} \dots s_{k} ) y_{1}^{s_{1}} \dots y_{k}^{s_{k}} , ]
	p then Pólya's fundamental theorem states that
	p #[+m \Phi_{m} (y_{1} \dots y_{k} ) = ]
	p #[+m =\Z (F (y_{1} \dots y_{k} ), F (y_{1}^{2} \dots y_{k}^{2} ) \dots F (y_{1}^{m} \dots y_{k}^{m} )), ]
	p where #[+m Z] is the cyclic index of the group #[+m A], defined by the equation
	p #[+m Z (t_{1} \dots t_{m} ; A) = ]
	p #[+m =\\sum_{j_{1} + 2j_{2} + \dots + mj_{m} = n} C (j_{1} \dots j_{m} ; A) t_{1}^{j_{1}} \dots t_{m}^{j_{m}} , ]
	p and #[+m C (j_{1} \dots j_{m} ; A) ] is the number of elements of the cyclic class #[+m \{ 1^{j_{1}} \dots m^{j_{m}} \} ](cf. #[a(title='Symmetric group' href='https://encyclopediaofmath.org/wiki/Symmetric_group') Symmetric group]) of #[+m A]. This theorem is based on Burnside's lemma: The number of equivalence classes #[+m N (A) ] defined on the set #[+m X] by the permutation group #[+m A] is given by the formula
	p #[+m N (A) =\{ \frac{1}{| A |}} \sum_{\alpha \in A} j_{1} (\alpha ), ]
	p where #[+m j_{1} (\alpha ) ] is the number of unit cycles of #[+m \alpha \in A ]. Pólya's theory has applications in the solution of enumeration problems in graph theory and in the enumeration of carbon chemical compounds. There is a generalization of Pólya's theory to the case when the equivalence of two configurations is defined by two groups #[+m G] and #[+m H] acting on #[+m X] and #[+m Y], respectively (see [4] and [10]). In this form it is applied, for example, in the determination of the number of non-isomorphic abstract automata.
	p If #[+m X = \{ 1 \dots m \} ], #[+m Y = \{ a_{1} \dots a_{n} \} ] and #[+m \sigma : X \rightarrow Y ], where #[+m a_{j} ] is used as an image #[+m \alpha_{j} ] times, then the expression
	p #[+m [ \sigma ] =\[ a_{1}^{\alpha_{1}} \dots a_{n}^{\alpha_{n}} ] ,\\\alpha_{1} + \dots + \alpha_{n} = m, ]
	p is called the first specification of #[+m \sigma ]. If the numbers #[+m \alpha_{1} \dots \alpha_{n} ] contain #[+m \beta_{0} ] zeros, #[+m \beta_{1} ] ones, etc., then the expression
	p #[+m [[ 0^{\beta_{0}} \dots m^{\beta_{m}} ]],\\\beta_{0} + \dots + \beta_{m} = n, ]
	p #[+m \beta_{1} + 2 \beta_{2} + \dots + m \beta_{m} = m, ]
	p is called the second specification. Under some specification of the groups #[+m G] and #[+m H] defining the equivalence of configurations #[+m \sigma : X \rightarrow Y ], it is possible to give a method of constructing generating functions for the enumeration of the inequivalent configurations. This method, called the general combinatorial scheme, can be subdivided into four particular cases, according as the groups #[+m G] and #[+m H] take values in the identity group #[+m E] or the symmetric groups #[+m S_{n} ] of corresponding orders. These particular cases are the models for the majority of the known combinatorial schemes (see [9], [10]).
	p 1) The commutative non-symmetric case: #[+m G = S_{m} ], #[+m H = E ]. This models combination schemes of distributing identical objects into different cells, etc. The generating function for the enumeration of inequivalent configurations #[+m \sigma ] such that
	p #[+m [ \sigma ] =\[ a_{1}^{\alpha_{1}} \dots a_{n}^{\alpha_{n}} ] , ]
	p #[+m \alpha_{i} \in \Lambda_{i} \subseteq \mathbf N_{0} =\\{ 0, 1 , . . . \} ,\\Lambda = (\Lambda_{1} \dots \Lambda_{n} ), ]
	p has the form:
	p #[+m \Phi (t; x_{1} \dots x_{n} ; \Lambda ) =\\prod_{j = 1}^n\\sum_{\alpha_{j} \in \Lambda_{j}} (tx_{j} )^{\alpha_{j}} . ]
	p 2) The non-commutative non-symmetric case: #[+m G = E ], #[+m H = E ]. This models allocation schemes of distributing distinct objects into different cells, etc. The generating function for the enumeration of inequivalent configurations #[+m \sigma ] such that
	p #[+m [ \sigma ] =\[ a_{1}^{\alpha_{1}} \dots a_{n}^{\alpha_{n}} ] ,\\\alpha_{i} \in \Lambda_{i} ,\\\Lambda = (\Lambda_{1} \dots \Lambda_{n} ), ]
	p has the form:
	p #[+m \widetilde \Phi (t; x_{1} \dots x_{n} ; \Lambda ) =\\prod_{j = 1}^n\\sum_{\alpha_{j} \in \Lambda_{j}} \frac{t^{\alpha_{j}}}{\alpha_{j} !} x_{j}^{\alpha_{j}} . ]
	p 3) The commutative symmetric case: #[+m G = S_{m} ], #[+m H = S_{n} ]. This models schemes of distributing identical objects into identical cells, the enumeration of the partitions of natural numbers, etc. The enumeration of configurations #[+m \sigma ] such that
	p #[+m [[ \sigma ]] =\[ [ 0^{\beta_{0}} \dots m^{\beta_{m}} ] ] ,\\\beta_{j} \in \Lambda_{j} ,\\\Lambda = (\Lambda_{1} , \Lambda_{2} , . . . ), ]
	p is based on the use of generating functions of the form:
	p #[+m \Psi (t; x_{1} , . . . ; \Lambda ) =\\prod_{j = 1}^\infty\\sum_{\beta_{j} \in \Lambda_{j}} (x_{j} t^{j} )^{\beta_{j}} . ]
	p 4) The non-commutative symmetric case: #[+m G = E ], #[+m H = S_{n} ]. This models schemes of partitioning finite sets into blocks, distributing distinct objects into identical cells, etc. The enumeration of configurations #[+m \sigma ] such that
	p #[+m [[ \sigma ]] =\[ [ 0^{\beta_{0}} \dots m^{\beta_{m}} ] ] ,\\\beta_{j} \in \Lambda_{j} ,\\\Lambda = (\Lambda_{1} , \Lambda_{2} , . . . ), ]
	p is based on the use of generating functions of the form:
	p #[+m \widetilde \Psi (t; x_{1} , . . . ; \Lambda ) =\\prod_{j = 1}^\infty\\sum_{\beta_{j} \in \Lambda_{j}} \left (\frac{x_{j} t^{j}}{j!} \right )^{\beta_{j}} { \frac{1}{\beta_{j} !}} . ]
	p An important place in combinatorial analysis is taken up by asymptotic methods. They are applied both for the simplification of complex finite expressions for large values of the parameters entering into them, as well as for obtaining approximate formulas in roundabout ways when the exact formulas are unknown. It is sometimes convenient to formulate a combinatorial problem of an enumerative character as a problem of finding the characteristics of the distribution of some random process. Such an interpretation makes it possible to apply the well-developed apparatus of probability theory for finding asymptotics or limit theorems. Classical schemes of random allocations of objects in cells are open to a detailed investigation from these points of view; so also are random partitions of sets, the cyclic structure of random permutations, as well as various classes of random graphs, including graphs of mappings (see [8], [9], [11]).
	p The probabilistic approach is applied in the study of the combinatorial properties of symmetric groups and semi-groups. The limiting distribution of the order of a random element of the symmetric group #[+m S_{n} ] as #[+m n \rightarrow \infty ] has been investigated, as also have the asymptotics of the probability of the generation of random elements of them. For certain classes of random non-negative matrices, the distributions have been studied of the number of zero rows in a matrix and in permanents, and estimates have been given of the probability of the primitiveness of such matrices. For the proof of the existence of combinatorial configurations without constructing them, one sometimes employs a certain specific probabilistic device. The essence of this device consists in the proof of the existence of the configuration (without constructing it) by means of an estimate of the probability of some event (see [7]).
	h6 References
	table: tbody
		tr
			td [1]
			td J. Riordan, "An introduction to combinational analysis" , Wiley (1958)
		tr
			td [2]
			td H.J. Ryser, "Combinatorial mathematics" , #[i Carus Math. Monogr.] , #[b 14] , Math. Assoc. Amer. (1963)
		tr
			td [3]
			td M. Hall, "Combinatorial theory" , Blaisdell (1967)
		tr
			td [4]
			td E.F. Beckenbach (ed.) , #[i Applied combinatorial mathematics] , Wiley (1964)
		tr
			td [5]
			td F. Harary, "Graph theory" , Addison-Wesley (1969) pp. Chapt. 9
		tr
			td [6]
			td F Harary, E. Palmer, "Graphical enumeration" , Acad. Press (1973)
		tr
			td [7]
			td P. Erdös, J. Spencer, "Probabilistic methods in combinatorics" , Acad. Press (1974)
		tr
			td [8]
			td V.F. Kolchin, V.P. Chistyakov, "Combinatorial problems of probability theory" #[i Itogi Nauk. i Tekhn. Teor. Veroyatnost. Mat. Stat. Teoret. Kibernet.] , #[b 11] (1974) pp. 5–45 (In Russian)
		tr
			td [9]
			td V.N. Sachkov, , #[i Questions of cybernetics. Proc. Seminar on Combinatorial Mathematics] , Moscow (1973) pp. 146–164 (In Russian)
		tr
			td [10]
			td V.N. Sachkov, "Combinatorial methods in discrete mathematics" , Moscow (1977) (In Russian)
		tr
			td [11]
			td V.N. Sachkov, "Probabilistic methods in combinatorial analysis" , Moscow (1978) (In Russian)
		tr
			td [12]
			td H. Minc, "Permanents" , Addison-Wesley (1978)
		tr
			td [13]
			td G.P. [G.P. Egorichev] Egorychev, "The solution of van der Waerden's problem for permanents" #[i Adv. in Math.] , #[b 42] : 3 (1981) pp. 299–305
	h6 Comments
	p The marriage problem is the following. Let there be a set #[+m \{ g_{1} \dots g_{n} \} ] of #[+m n] girls and a set #[+m \{ b_{1} \dots b_{m} \} ] of #[+m m] boys. Each girl #[+m g_{i} ] likes a subset #[+m B_{i} \subset \{ b_{1} \dots b_{m} \} ] of boys. When is it possible that each girl marries a boy she likes? The solution is of course given by the P. Hall theorem on distinct representatives, and this theorem is also known as the marriage theorem or the P. Hall marriage theorem. The abbreviation SDR is often used for systems of distinct representatives. Let #[+m G] be the bipartite graph (cf. #[a(title='Graph, bipartite' href='https://encyclopediaofmath.org/wiki/Graph,_bipartite') Graph, bipartite]) consisting of the vertices #[+m \{ g_{1} \dots g_{n} , b_{1} \dots b_{m} \} ] and with an edge joining #[+m g_{i} ] and #[+m b_{j} ] if and only if girl #[+m i] likes boy #[+m j](and no other edges). Then a solution of the marriage problem provides a matching, and in this context the marriage theorem is also known as the P. Hall matching theorem.
	p A good up-to-date book on design theory is [a1]. For more on extremal problems in graph theory cf. [a2]. For more on the dimer problem and other uses of combinatorics in theoretical physics cf., e.g., [a3]. Finally, [a4] is completely devoted to transversal theory including infinite versions.
	h6 References
	table: tbody
		tr
			td [a1]
			td D.R. Hughes, F.C. Piper, "Design theory" , Cambridge Univ. Press (1985)
		tr
			td [a2]
			td B. Bollobas, "Extremal graph theory" , Acad. Press (1978)
		tr
			td [a3]
			td J.K. Percus, "Combinatorial methods" , Springer (1971)
		tr
			td [a4]
			td L. Mirsky, "Transversal theory" , Acad. Press (1971)

</template>
