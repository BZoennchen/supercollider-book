---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Algorithms

>An algorithm is on the *verge of time*: [...] it is strictly structural -- a formal, unchanging entity.
>Not only formal, however, but a formula that prescribes steps to be made one after another, depending on one another.
>It is a formula that exists in order to unfold, in the form of a process, in time and over time, and dependent on its past inputs. -- Julian Rohrhuber

I am deeply fascinated by algorithms. 
My critique of [technology](sec-technology-and-art), which will also permeate this section, arises from a place of love and appreciation. 
Following my Ph.D., I penned an article titled [Informatics - A Love Letter](https://bzoennchen.github.io/Pages/2021/06/08/Informatics-a-love-letter.html) in which I unabashedly express my gratitude towards the discipline. 
For me, informatics or computer science is both an art and a science that has vastly expanded my realm of possibilities. 
Perhaps for this reason, I am driven to safeguard this craft from potential decline.

## Introduction

Since algorithms describe a sequence of executable instructions, they have a strange relation to time.
On the one hand an algorithm is a description of a causal path into the future even though there is no physical time mentioned explicitly.
Instead, the algorithms is there to be executed, i.e., to be transformed into a running program.
Apart from this timely quality, an algorithm is like a story: it can unfold but is also unchanging; its content does not change but it can unfold logically.
This is, in fact, very similar to a musical piece which can be performed in time but also exists independet of it.

Similar to natural numbers, it's challenging to determine whether an algorithm pre-exists and thus we can discover and utilize it, or if it comes into being as we invent it {cite}`rohrhuber:2018`. 
While this debate may seem inconsequential in practical terms, it holds significant importance in the philosophy of mathematics. 
Personally, I align with the late Wittgenstein, which posits that numbers, as well as algorithms, are abstractions of our daily practices and behavior and that a lot of confusion stems from our misuse of language.

The origin of the term *algorithm* was obscure for quite a while.
Historians only late discovered that the term emerged from a slight modification of the name of the renowned Persian author Abu Ja'far Muhammad ibn Musa al-Khwarizmi.
At that time *algorism* meant "the specific step-by-step method of performing written elementary arithmetic".
The name was Latinized to *algorismi* and later translated into middle high German as *Algorismus*.
In more recent times, the word was linked with the Greek term *arithmetic*, thus giving rise to the term *algorithm*.
For an extended period, the term *algorithm* was primarily associated with a combination of arithmetic operations, including addition, subtraction, multiplication, and division. 

Around 1950, the term began to reference Euclid's celebrated algorithm for determining the greatest common divisor.
Consequently, the concept of an algorithm as a combination of purely arithmetic operations started to fade.
Instead, algorithms started to incorporate combinatorial operations and control structures.
At the same time the development of scientific computation and early high level programming languages, such as Algol58 and its derivatives (short for ALGOrithmic Language) took palce.
From that time on, an *algorithm* was understood to be a set of defined steps that if followed in the correct order will computationally process input (instructions and/or data) to produce a desired outcome {cite}`miyazaki:2012`.

The efficiency of an algorithm can be enhanced by either refining the logic component or by improving the control over its use, including altering data structures (input) to improve efficiency.
For many problems, one can prove certain optimal time and space complexities.
For instance, we know that sorting $n$ cards requires $\mathcal{O}(n\log(n))$ time and $\mathcal{O}(n)$ space.

As reasoned logic, the formulation of an algorithm is, in theory at least, independent of programming languages and the machines that execute them;
The theoretical fundament of algorithms, computer as well as programming languages is the (universal) *Turing machine* (1937) and the *lambda calculus* (1932) which are both equivalent.
Importantly, *Turing machines* and the *lambda calculus* are equivalent in computational power: each can efficiently simulate the other.

In contemporary times, we correlate the term *algorithm* with concepts such as recipe, computational instruction, process, procedure, method, routine, and so forth.
Today, algorithms are the threads that tie together most of the subfields of computer science.

## Euclid's Algorithm

Since it is one of the first discovered algorithms, let us have a look at Euclid's famous algorithm.

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

```{prf:algorithm} Euclid's Algorithm
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

### Bjorklund's Algorithm

While the *Euclidean algorithm* computes the greatest common divisor of two given integers, Godfried Toussaint demonstrated in {cite}`toussaint:2005`, *The Euclidean Algorithm Generates Traditional Musical Rhythms*, that the structure of the Euclidean algorithm can be utilized efficiently to generate a broad family of rhythms. 
These rhythms are predominantly used in Sub-Saharan African music and world music at large.

If we divide time into $n$ intervals, and we consider another given number of $m < n$ pulses, then the problem is to distribute the pulses as evenly as possible among these intervals.
Pulses in time form a rhythm.
For instance, to distribute $m=3$ pulses across $n=8$ intervals, gives us the following result:

$$[1 0 0 1 0 0 1 0],$$

here $1$ stands for a pulse while $0$ stands for no pulse.
It sounds like the following:

```{code-cell} python3
:tags: [remove-input]
import IPython.display as ipd
audio_path = '../../sounds/hh-3-8.mp3'
ipd.Audio(audio_path)
```

Now you might think: well isn't this easy? I just divide $n$ by $m$ to receive $n/m$ bins and put a zero in each of these bins?
$\lfloor 8/3 \rfloor = 2$ thus we have two times three "spots" and one times two spots.
Therefore, we get two times $[100]$ and one time $[10]$, right?
Yes in this case the result is correct but this is not true in general.

Suppose we have $n = 13$ and $m = 5$.
Then we get three times $[100]$ and two times $[10]$ but $[1001001001010]$ is incorrect!
The correct result is

$$[1001010010100].$$

The algorithm to generate a vast range of musical rhythms was introduced by Eric Bjorklund in {cite}`bjorklund:2003` but for a completely different setting.
He was interested in a timing system in neutron accelerators which shows that, because of their abstract nature, algorithms developed in one discipline can have applications in many other disciplines.
Bjorklund's algorithm is basically the *Euclidean algorithm* but in another context.

So, let me use $n = 13$ and $m=5$, to show you how it works.
We start by considering a sequence (of sequences) consisting of 5 ones followed by $8 = 13-5$ zeros:

$$[1][1][1][1][1][0][0][0][0][0][0][0][0].$$

We have two groups of sequences: 5 times $[1]$ and 8 times $[0]$.
We mix in the larger group into the smaller one.
This is similar to the operation $n \leftarrow n-m$:

$$[10][10][10][10][10][0][0][0].$$

Again, we are left with two new groups.
One consisting of 5 times $[10]$ the other consisting of 3 times $[0]$.
Now we subtract $5-3 = 2$ by again mixing the larger group into the smaller one:

$$[100][100][100][10][10].$$

This leaves us with 3 and 2.
Finally, we arrive at

$$[10010][10010][100] = [1001010010100].$$

It sounds like the following:

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../sounds/hh-5-13.mp3'
ipd.Audio(audio_path)
```

As we saw in this example, Bjorklund's algorithm recursively concatinates Euclidean rhythms of shorter length according to back-substitution.
At a conceptual level, the procedure resembles Euclid's recursive divide-with remainder approach, using subsequences and symbol replacement in place of integer division and back-substitution.

### Morrill's Algorithm

In a recent report {cite}`morrill:2022` Thomas Morrill outlined a strategy to compute the *Euclidean rhythm* by hand more easily, avoiding the recursive nature of the *Euclidean algorithm*.
He proposes the *Euclidean matrix* consistent of three rows.
The first row, called *index row*, is equal to $(-1, 0, 1, 2, \ldots, n-1)^\top$.
The second one, called *integer row*, is equal to the first one multiplied by $m$.
The entries of row 3, called *residue row*, are each equal to the corresponding.

After the computation of the *Euclidean matrix* we can write down a 1 at index $i$ if the $i$-th entry of the *residue row* is larger than the $i+1$-th entry. 
Otherwise we write down a 0.
For further details I refer to the paper.

This procedure gives us not the exact same result but a shifted version.
Let me write down the *Euclidean matrix* for our last example.
I also added a fourth row containing the rhythm.

$$\begin{bmatrix} -1 & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 \\ -5 & 0 & 5 & 10 & 15 & 20 & 25 & 30 & 35 & 40 & 45 & 50 & 55 & 60 \\ 8 & 0 & 5 & 10 & 2 & 7 & 12 & 4 & 9 & 1 & 6 & 11 & 3 & 8 \\ \hline 1 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & 1 & 0 & - \end{bmatrix}$$

Following the instructions in the paper, we get:

$$[1001001010010]$$

which is a shifted version of the output of Bjorklund's algorithm.

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../sounds/hh-5-13-shifted.mp3'
ipd.Audio(audio_path)
```

Isn't it fascinating that an algorithm discovered thousands of years ago not only remains relevant today, but is also adapted for novel purposes?

## Limits of Computation

Something magical and beautiful happens when a sequence of operations exploits the underlying structure to uncover new pattern.
The rigid definition of the algorithm and its relentless execution is alienating and fascinating at the same time.  

An algorithm is a finite sequence of executable instructions designed to yield a finite output within a finite number of steps for a specific finite input.
Importantly, it uses only a finite amount of memory space at any point during its execution.
Algorithms can be written down in a programming languages.
This code is compiled or interpreted (or both) -- a process that transforms the code into a language the concrete machine can understand and execute.

However, algorithms can also run on our brain.
A simple example might be the sorting algorithm you use for stacking books onto the shelves in your home. 
The inputs in this case are the books (and more particularly the book titles and authors). 
The output is the ordered sequence of books that ends up on your shelves.
But that’s just what an algorithm is in the abstract. 

While philosophers such as Leibniz and Descartes once dreamed of a *universal language* that could resolve any scientific problem within a comprehensive calculus, Kurt Gödel showed in 1931 that this modern pursuit was ultimately futile.
In *Principles of Theoretical Logic*, David Hilbert and Wilhelm Ackermann proposed the idea of an algorithm capable of determining the truth or falsity of any first-order logical expression. 
This question, known as the *decidability problem*, is often illustrated by the *halting problem* of a Turing machine. 
These works made the formalists' objectives appear increasingly achievable, until Kurt Gödel, in his publication *On Formally Undecidable Propositions of the Principia Mathematica and Related Systems*, set clear limitations to their ambitions. 
Firstly, he demonstrated that a sufficiently robust system that includes at least arithmetic cannot prove its own consistency. 
Secondly, he showed that within such a system, there can be propositions that are neither provable nor disprovable.

Later, Alen Turing showed that there is no *Turing machine* $\mathcal{H}$ (program) that can compute for any given *Turing machine* $\mathcal{T}$ given as a description $\alpha_\mathcal{T}$ (source code) if it halts or not.
This demonstrated that there are well-defined questions that are *undecidable*, or in other words, there are problems that are not *Turing-computable*. Considering that any existing calculating machine is conceptually no more powerful than a *Turing machine*, this implies that there are problems that cannot be computed by executing an algorithm.

Consequently, the works of Albert Thoralf Skolem and Jacques Herbrand eventually led to the limitation regarding the predicate calculus, asserting that for a proposition deemed true in the calculus, its truth can be proven in a finite number of steps.
Conversely, in the other case, the proof may either be successful or unsuccessful.
This situation is often referred to as the *semi-decidability* of the predicate calculus.

This discovery signifies a fissure in the *modern perspective* and presages our current *postmodern condition*.

## Algocracy

In the modern digital and information age, algorithms have a very particular character. 
They lie at the heart of the digital network created by the internet of things, and the associated revolutions in AI and robotics. 
Algorithms are used to collect and process information from surveillance equipment, to organise that information and use it to form recommendations and action plans, to implement those action plans, and to learn from this process.

Everyday we are exposed to the ways in which websites use algorithms to perform searches, personalise advertising, match us with potential romantic partners, and recommend a variety of products and services.
We are perhaps less-exposed to the ways in which algorithms are (and can be) used to trade stocks, identify terrorist suspects, assist in medical diagnostics, match organ donors to potential donees, and facilitate public school admissions. 
The multiplication of such uses is what gives rise to the phenomenon of *algocracy*, i.e. *rule by algorithms*.

Digital spaces are imbued with values, determined by the control and regulation of permissible actions.
*Cyberspace*, as it's often termed, have never been free from regulation, despite common misconceptions.
Rather than being shaped by traditional architectural forms meant to regulate physical spaces, digital spaces are regulated by *source code*.
The design of websites or applications, dictated by this code, significantly influences the behavior of their users.
In other words, the very structure of these platforms functions as a form of regulation, guiding user interactions and activities.
In {cite}`lessig:2006` Lawrence Lessig states:

>Codes constitute cyberspaces; spaces enable and disable individuals and groups. The selections about code are therefore in part a selection about who, what, and, most important, what ways of life will be enabled and disabled. -- Lawrence Lessig

And in his book *Technology and the Lifeworld*, Don Ihde discusses technolog -- including algorithm -- as an expandasion or limit of possibilities.
In our digital age, algorithms go beyond mere functionality or direct control.
They realise judgements behind.
{cite}`rosengruen:2022` argues that Western societies are currenty shifting from *rule of law* to *rule of code*:

>[...] source code is about to become the main regulator of individual and institutional behavior that regulates all other regulators including law -- Sebastian Rosengrün 

Rosengrün's argument is not centered on the premise that regulation is inherently detrimental, or that large companies harbor malicious intentions.
Instead, he acknowledges the necessity, and indeed the inevitability, of regulation.
Moreover, he observes that the alignment of corporate regulatory practices with their profit-making objectives is to be expected.
He forcefully advocates for the *rule of law* as an indispensable prerequisite for a democratic society.
Consequently, any attempt to replace it, could precipitate the dissolution of such a society.
For this reason, Rosengrün asserts that code must be not only open but also subject to regulation.
He underscores the potential dangers of allowing code to regulate law.
For instance, when *machine learning* is used in the policy-making process, it is unrealistic to expect that law will maintain supremacy over code.

The process of developing algorithms necessitates translating a given task into human language.
This is among the most challenging fields in software engineering. 
Developers then convert this human language sequence of defined steps into code. 

In computer science literature, the emphasis is primarily on the design of an algorithm, its performance evaluation, and the verification of its optimality from a purely technical standpoint.
When the discourse veers towards the role of algorithms in real-world situations, it typically centers on how algorithms practically execute specific tasks.
In other words, algorithms are seen as epitomes of rationality, blending the precision of mathematics with the impartiality of technology. 
Although there may be variation among programmers in the way they craft code, the translation process is typically depicted as a technical, harmless, and intuitive exercise.

This is how algorithms are mostly presented by computer scientists and technology companies: that they are "purely formal beings of reason" {cite}`kitchin:2014`.
Due to their formal structure, modern thinking often attributes a form of neutrality to algorithms. 
However, 

>in each step of algorithm design human judgment is involved.

In Rob Kitchin's work {cite}`kitchin:2014`, he discusses an algorithm that was supposed to calculate the number of "ghost estates" in Ireland. 
Ghost estates are a phenomenon that emerged in the aftermath of the Irish property bubble. When developers went bankrupt, numerous housing developments were left unfinished and under-occupied.

However, designing the algorithm to identify these estates proves to be a complex task. 
Given a national property database with details on the ownership and construction status of all housing developments, you could construct an algorithm that sifts through the database to calculate the number of ghost estates.

But, what guidelines should the algorithm follow? 
Is an estate considered a "ghost estate" if less than 50% of it is occupied and completed, or is less than 75% sufficient? 
Which coding language should be used to implement the algorithm? 
Is there value in enhancing the program, for example, by combining it with another set of algorithms to illustrate the locations of these ghost estates on a digital map?

Answering these questions requires discernment and judgment. 
If these aspects are not well-considered, it can result in a multitude of problems.

Understandably, it seems logical for computer scientists to concentrate on the creation of efficient algorithms while other disciplines regulate the application of these algorithms.
However, this assumption is contingent upon the capability of these other disciplines and the general public to effectively carry out this role.

How algorithms are most often understood is very narrowly framed and lacking in critical reflection.
We should at least recognize and appreciate increasing ubiquity of algorithms, and once we understand the two translation problems, the need to think critically about algorithms becomes much more apparent.
If algorithms are going to be the lifeblood of modern technological infrastructures, if those infrastructures are going to shape and influence more and more aspects of our lives, and if the discernment and judgment of algorithm-designers is key to how they do this, then it is important that we make sure we understand how that discernment and judgment operates.

The concept that almost every action we undertake can be deconstructed into and processed via algorithms is fundamentally *reductionist*.
It presumes that complicated, frequently nebulous, relational, and contextual social and economic exchanges and ways of existence can be logically dismantled, simulated, and interpreted, while only forfeiting a minimal amount of implicit knowledge and situational variables.

>Algorithms do not just process data, they produce, affirm and certify knowledge through a particular logic built on specific assumptions.
>Computation asserts and prioritizes a particular epistemological way of making sense of and acting in the world; of codifying practices and knowledges and processing them using algorithms. -- Tarleton Gillespie

As Gillespie {cite}`gillespie:2014` highlighted, algorithmic thinking favors a particular method of comprehension and a *utilitarian rationality* grounded on precisely defined scientific understanding and pragmatic instrumental knowledge. 
This preference tends to sideline and supplant knowledge obtained from practice and deliberation, as well as knowledge rooted in experience.

If algorithms are going to sit at the heart of contemporary life, it seems like they should be of interest to all disciplines especially to social science, philosophy and the arts but also to the everyday practitioners!
The algorithms' objectivity, impartiality, and legitimacy has to be critically analysed.

In this context, *algorithmic music* (as well as other creative coding endeavors) is not only a means of artistic expression but a discipline that enables the understanding of algorithms phenomenologically via experiencing the raw phenomena without the introduction of any metaphysical abstraction.
Furthermore, it shifts algorithmic thinking away from *utilitarian rationality* towards knowledge rooted in experience.

>Code is not purely abstract and mathematical; it has significant social, political, and aesthetic dimensions -- Montfort et al. {cite}`montfort:2012`

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../sounds/jam.mp3'
ipd.Audio(audio_path)
```