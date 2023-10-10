section.example of task (my imagination)
$$
\begin{aligned}
z=x+y \to \max \\
\begin{cases}
2x-y\le2 \\
3x+y\le4 \\
2y+x\ge1 \\
\end{cases}
\end{aligned}
\quad
\begin{aligned}$$
$$
z=x+y+0s_1+0s_2+0e_1 \to \max \\
\begin{cases}
2x-y + s_1 = 2 \\
3x+y + s_2 = 4 \\
2y+x - e_1 = 1 \\
\end{cases}
\end{aligned}
\\
\begin{array}{ccccc|c}
1 & 1 & 0 & 0 & 0 & z \\
\hline
2 & 1 & 1 & 0 & 0 & 2 & \\
3 & 1 & 0 & 1 & 0 & 4 & \\
1 & 2 & 0 & 0 & -1 & 1 & \\
\end{array} \quad
\begin{array}{cccccc|c}
0 & 0 & 0 & 0 & 0 & 1 & w \\
\hline
2 & 1 & 1 & 0 & 0 & 0 & 2  \\
3 & 1 & 0 & 1 & 0 & 0 & 4  \\
1 & 2 & 0 & 0 & -1 & 1 & 1  \\
\end{array} \quad
\begin{array}{cccccc|c}
1 & 1 & 0 & 0 & 0 & 0 & z \\
\hline
2 & 1 & 1 & 0 & 0 & 0 & 2  \\
3 & 1 & 0 & 1 & 0 & 0 & 4  \\
1 & 2 & 0 & 0 & -1 & 1 & 1  \\
\end{array} \quad
$$