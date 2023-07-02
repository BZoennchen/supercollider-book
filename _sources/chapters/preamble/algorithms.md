# Algorithms

The origin of the term *algorithm* was obscure for quite a while.
Historians only late discovered that the term emerged from a slight modification of the name of the renowned Persian author Abu Ja'far Muhammad ibn Musa al-Khwarizmi. 
This name was Latinized to Algorismi and later translated into Middle High German as Algorismus. 
In more recent times, the word was linked with the Greek term *arithmetic*, thus giving rise to the term *algorithm*.

For an extended period, *algorithm* was primarily associated with a combination of arithmetic operations, including addition, subtraction, multiplication, and division. 
Around 1950, the term began to reference Euclid's celebrated algorithm for determining the greatest common divisor.
Consequently, the concept of an algorithm as a combination of purely arithmetic operations started to fade.
Instead, algorithms started to incorporate combinatorial operations and control structures.

In contemporary times, we correlate the term *algorithm* with concepts such as recipe, computational instruction, process, procedure, method, routine, and so forth.

Let us have a look to Euclid's famous algorithm.
Given two natural numbers $n, m \in \mathbb{N}$, we want to find the greatest common divsor $d$ of those two numbers, that is,

$$\exists k_1, k_2 \in \mathbb{N} : n = k_1 \cdot d \ \land \ m = k_2 \cdot d$$

and $d$ is the largest number that fulfills this condition.
Clearly, if one of the numbers is a multiple of the other, we are done.
Otherwise, one number, let's say $n$, has to be larger.

Interestingly, we can subtract $m$ from $n$ while keeping the greatest common divisor unchanged meaning that $n-m$ and $n$ have the same common divisor than $n$ and $m$.
We can show this by the following equation

$$n-m = (k_1 \cdot d) - (k_2 \cdot d) = (k_1 - k_2) \cdot d$$

Since $n > m$ we can follow $k_1 - k_2 > 0$.
Imagine two sticks of length $n$ and $m$.
If there is another stick $d$ that divides both sticks, then it has to divide the shorter stick.
Therefore, it has to divide the rest ($n-m$) of the longer stick as well.
Since this relation is recursive, we can subtract the greater from the smaller number until the smaller divides the larger.

```{prf:algorithm} Eucld's Algorithm
:label: alg-euclid

**Inputs** Two numbers $n, m \in \mathbb{N}$.

**Output** The greatest common divisor of $n$ and $m$.

1. While $n < m \ \lor \ m < n$
    1. If $m > n$
        1. $t \leftarrow m$
        2. $m \leftarrow n$
        3. $n \leftarrow t$
    2. $n \leftarrow n - m$
	
2. return $m$
```

An algorithm is a finite sequence of explicitly described executable instructions, such as a text or program code, designed to yield a finite output within a finite number of steps for a specific finite input.
Importantly, it uses only a finite amount of memory space at any point during its execution.

Since algorithms describe a sequence of executable instructions, they have a strange relation to time.
In *Algorithmic Music and the Philosophy of Time* Julian Rohrhuber states that

>an algorithm is on the *verge of time*: [...] it is strictly structural -- a formal, unchanging entity. Not only formal, however, but a formula that prescribes steps to be made one after another, depending on one another. It is a formula that exists in order to unfold, in the form of a process, in time and over time, and dependent on its past inputs. -- Julian Rohrhuber

Like any algorithm, Euclid's algorithm is a description of a causal path into the future even though there is no physical time mentioned explicitly.
Instead the algorithms is there to be executed, i.e., to be transformed into a program.
Apart from this timely quality, an algorithm is like a written story: it can unfold but is also unchanging; its content does not change but it can unfold logically. 



TODO