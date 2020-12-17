# IEEE-Xtreme-14.0
This repository contains codes in pyhton for the problem statements that were asked in IEEE Xtreme 14.0
## Linearly Separable Samples
Time limit: 12500 ms
Memory limit: 256 MB

A linear classifier, especially the Support Vector Machine (SVM), is a popular tool in the task of pattern recognition and artificial intelligence. An essential problem for the linear classifier is whether the given samples are linearly separable.

Let’s consider the 2D cases without the bias term. Each sample has two features, x1∈Rx_{1} \in \mathbb Rx1​∈R and x2∈Rx_{2} \in \mathbb Rx2​∈R, and a label y∈{1,−1}y \in \{ 1,-1\}y∈{1,−1}. You will be given TTT queries. For each query you are given a group of points on a 2D plane, your task is to determine whether the positive samples (labelled 111) and the negative samples (labelled −1-1−1) can be separated by a line through the origin (0,0)(0,0)(0,0). If a line goes through some positive and/or negative points but separates all other points, it can be also accepted.

Mathematically speaking, you are asked to find whether there exist w1∈Rw_{1} \in \mathbb Rw1​∈R and w2∈Rw_{2} \in \mathbb Rw2​∈R , s.t.s. t.s.t.

⟨[w1,w2],[x1,x2]⟩=w1x1+w2x2≥0  IFF  y=1\langle[ w_{1},w_{2}], [x_{1},x_{2}]\rangle = w_{1}x_{1}+w_{2}x_{2}\ge0\;\mathrm{IFF}\;y=1 ⟨[w1​,w2​],[x1​,x2​]⟩=w1​x1​+w2​x2​≥0IFFy=1

⟨[w1,w2],[x1,x2]⟩=w1x1+w2x2≤0  IFF  y=−1\langle[ w_{1},w_{2}], [x_{1},x_{2}]\rangle = w_{1}x_{1}+w_{2}x_{2}\leq0\;\mathrm{IFF}\;y=-1 ⟨[w1​,w2​],[x1​,x2​]⟩=w1​x1​+w2​x2​≤0IFFy=−1

hold for all samples (x1,x2),y(x_1,x_2),y(x1​,x2​),y.

Standard input

The first line of the input has an integer TTT which represents the number of queries. Then, TTT queries follow. The first line of each query has an integer NNN that denotes the number of points in the query. Each of the following NNN rows has two floating point numbers and an integer separated by single spaces. They represent the two features x1x_{1}x1​, x2 x_{2}x2​ and the label yyy of one point.
Standard output

For each query, output the answer on a single line. Output YES if the given points can be separated by a line through the origin, and NO otherwise.

Constraints and notes

    1≤T≤101\leq T\leq101≤T≤10
    1≤N≤1051 \leq N \leq 10^51≤N≤105
    −100.0≤x1,x2≤100.0-100.0 \leq x_{1},x_{2} \leq 100.0−100.0≤x1​,x2​≤100.0
    y=1y=1y=1 or y=−1y=-1y=−1
    x1,x2x_1, x_2x1​,x2​ are given with at most two decimal points.
    Points may overlap and have the same x1,x2x_1, x_2x1​,x2​.
    For 50%50\%50% of the test data, 1≤N≤5 0001 \leq N \leq 5\,0001≤N≤5000 
    
## Mosaic Decoration I
Time limit: 2500 ms
Memory limit: 256 MB

Zapray lives in a big mansion that has NNN bathrooms. He wants to decorate the bathroom walls using mosaic tiles of two colors: black and pink. The iiith bathroom needs BiB_iBi​ black tiles and PiP_iPi​ pink tiles. Mosaic tiles are sold in piles. Zapray can buy one pile of 101010 black tiles for CBC_BCB​ dollars, and one pile of 101010 pink tiles for CPC_PCP​ dollars. How much money does he need in total to decorate all the NNN bathrooms?

Standard input

The input contains three integers N,CB,CPN, C_B, C_PN,CB​,CP​ on the first line.

The next NNN lines each have two integers. The iiith line has BiB_iBi​ and PiP_iPi​.

Standard output

Output a single integer, the amount of money in dollars that Zapray needs to decorate all his bathrooms.

Constraints and notes

    2≤N≤1002 \leq N \leq 1002≤N≤100
    1≤CB,CP≤1 0001 \leq C_B, C_P \leq 1\,0001≤CB​,CP​≤1000
    1≤Bi,Pi≤1 0001 \leq B_i, P_i \leq 1\,0001≤Bi​,Pi​≤1000 
