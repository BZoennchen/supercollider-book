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

(sec-algorithms)=
# The Logic of the Algorithm

>An algorithm is on the *verge of time*: [...] it is strictly structural---a formal, unchanging entity.
>Not only formal, however, but a formula that prescribes steps to be made one after another, depending on one another.
>It is a formula that exists in order to unfold, in the form of a process, in time and over time, and dependent on its past inputs. -- Julian Rohrhuber

I am deeply fascinated by algorithms. 
My critique of [technology](sec-technology-and-art), which will also permeate this section, arises from a place of love and appreciation.
Technological advancements have liberated us humans from the constraints of nature.
And it is unlikely that many individuals would choose to reside in an era prior to the *industrial revolution*.
However, as already mentioned, technology may have set us on an immutable course of existence that could ultimately lead to disaster.

For me personally, technology is lifesaving and emancipatory.
Following my Ph.D., I even penned an article titled [Informatics - A Love Letter](https://bzoennchen.github.io/Pages/2021/06/08/Informatics-a-love-letter.html) in which I unabashedly express my gratitude towards the discipline. 
Informatics---or computer science---is both: an art and a science that has vastly expanded my realm of possibilities.
It also seems glaringly obvious that if we want to find a solution to the escalating impacts of climate change, we will depend on technology.
Any other solution could be so detrimental that I can't even begin to envision the consequences.
And lastly, if we reject technology for instrumental reasons, we stay in the same mode; we stay *gestellt* because we neglect technology based on a technological way of thinking.
Perhaps for these reasons, I am driven to safeguard this craft from potential decline.

## Etymology and Evolution

The term algorithm has a long and layered history.
Its etymology traces back to the name of the 9th-century Persian mathematician Abū Jaʿfar Muḥammad ibn Mūsā al-Khwārizmī, whose influential work on Indian numerals was translated into Latin in the 12th century as Algoritmi de numero Indorum.
The Latinized form Algoritmi (a transliteration of al-Khwārizmī) came to refer to a set of rules for calculation using Hindu-Arabic numerals.
Over time, algorism—originally the name for these positional arithmetic techniques—evolved into algorithm, a neologism that eventually detached from its purely numerical connotation.

For centuries, the term was closely tied to elementary arithmetic operations such as addition, subtraction, multiplication, and division. Only much later, particularly in the 20th century, did algorithm expand in meaning to encompass general computational procedures. One historical turning point was the renewed interest in Euclid’s algorithm for computing the greatest common divisor—an early and elegant example of a finite, stepwise method with guaranteed termination.

By the mid-20th century, with the development of scientific computing and high-level programming languages (notably Algol 58 and its successors—Algorithmic Language), the modern understanding of an algorithm as an abstract, mechanical procedure for solving a problem took hold.
This shift included not just numerical methods but also combinatorial procedures, recursive definitions, and control structures such as conditionals and loops.

Formally, an algorithm is a finite, well-defined sequence of instructions that takes some input (data and/or parameters) and produces an output through deterministic computation. 
Crucially, this definition is independent of the hardware or software used for implementation.
The theoretical foundation for this view was laid in the 1930s by Alonzo Church's lambda calculus (1932) and Alan Turing's model of computation (1936), both of which were shown to be computationally equivalent---a result that grounds the Church–Turing thesis: 

>any effectively calculable function can be computed by a Turing machine.

Today, the concept of an algorithm underpins all areas of computer science, from artificial intelligence and machine learning to cryptography, computer graphics, and software engineering. Algorithms are commonly associated with terms like procedure, routine, recipe, or mechanism, but their importance goes far beyond metaphor. They are formal, analyzable objects that can be optimized for time and space complexity. For example, comparison-based sorting has a known lower bound of $\mathcal{O}(n\log(n))$ time and $\mathcal{O}(n)$ space in the worst case, and many efficient algorithms (e.g., merge sort, heapsort) meet this bound.

Moreover, algorithm design often involves not just logical correctness but also resource-aware structuring.
For instance, choosing appropriate data representations or applying heuristic or probabilistic strategies to reduce computational overhead.

In short, an algorithm is not merely a set of instructions---it is a formal, dynamic process that defines the logic and rhythm of computation.
As such, it plays a foundational role not only in computer science, but in the broader understanding of procedural knowledge, mechanization, and even temporality itself.

## The Construction of Time

Since algorithms describe sequences of executable instructions, they have a peculiar relationship to time.
In his essay *Algorithmic Music and the Philosophy of Time* {cite}`rohrhuber:2018`, Julian Rohrhuber argues that algorithms are more than static step-by-step procedures: they are *liminal entities*, suspended between logic and experience, structure and change.
Algorithms, he suggests, offer a way to rethink time—not as a simple flow from past to future, but as a complex interplay of *logical time*, *physical time*, and *perceptual experience*.

An algorithm, in its abstract form, is timeless: a fixed set of rules or instructions.
Yet it is also designed to be executed, which necessarily implies unfolding over time.
This *duality* means that an algorithm is both **like a story**, capable of being told and retold without change, and **like a machine**, capable of enacting a process in the world. 
It is **unchanging in form**, but **temporal in function**.

However, the unfolding of an algorithm does not merely occur in time---it actively structures time.
Algorithms generate sequences, causal relations, loops, and delays.
A loop, for example, is a logical form that manifests as a temporal process when executed.
Like a clock, algorithms can represent time; like a calculator, they can produce effects in time. 
They are both *symbolic* and *operational*.

This is why algorithmic music, as Rohrhuber emphasizes, is not simply music made with algorithms.
Rather, it is a medium through which we can experiment with time itself, rendering audible the interplay between logical structure and its temporal actualization.
Because sound is inherently temporal, algorithmic music becomes a privileged site for exploring how time is constructed, perceived, and even alienated.

The *halting problem* further complicates this picture: for some algorithms, we cannot know in advance whether they will terminate or loop infinitely.
This open-endedness echoes our own lived experience of time---unpredictable, sometimes looping, sometimes stalling, never fully foreseeable.

Although *iteration* and *recursion* can be formally transformed into one another, Rohrhuber points out that they model time differently.
Iteration expresses a linear, forward-moving time.
Recursion, by contrast, evokes a circular or layered temporality---time that folds back on itself.
It allows us to imagine temporal worlds where past, present, and future are not neatly separated.

This leads to Rohrhuber's critical distinction between time as **passage** and time as **encounter**.
In the first, time flows from future to past.
In the second, time becomes a kind of landscape in which events are situated—something we navigate, not something that simply carries us forward.
Algorithmic music exposes both dimensions: the passage of sound in real time, and the deeper logical structures that condition what can be heard and when.

At this point, the connection to Spencer-Brown's *Laws of Form* {cite}`brown:1969` becomes clear.
In that work, time is not the stage on which forms appear; rather, it comes into being as soon as a form is drawn, erased, and drawn again.
The rhythm of distinction itself generates what we later name "earlier" and "later". 
As Spencer-Brown writes:

The act of **making a distinction**---of marking one side from another---is not only the foundation of form but a generative operation that can produce time.
Time, in this view, emerges from the operation that re-enters itself: recursion.
This self-reference gives rise to a *trace of states,* and thus to **memory**.
It is not pre-given but arises from the *oscillation* between *marked* and *unmarked* states.

Repetition---distinguishing more than once---is necessary to construct a sequence.
A *single crossing* of a boundary marks a change, but not yet a sequence.
As soon as this operation is repeated, i.e.

```
mark (1) -> unmark (2) -> mark (3) -> ...
```
a **sense of before and after emerges**.
This is the temporal distinction.
But with it also comes a paradox.
A *re-entering operation* such as "This sentence is false" generates a form that is neither strictly marked nor unmarked.
It *oscillates* endlessly. 
Spencer-Brown embraces this paradox, unlike Bertrand Russell who sought to avoid it.
For Spencer-Brown, paradox is not failure but the very foundation of form and temporality.

This notion leads to *re-entry*---the form observing itself.
With each recursive loop, the system retains a trace of prior states, allowing it to distinguish between "before" and "now": the very condition of memory.
Time, then, becomes a dimension of self-referentiality, where a system can reflect on its own prior distinctions.
As Niklas Luhmann adds, **systems do not inhabit an objective, external clock-time**.
**Each system constructs its own temporal structure, based on the operations it performs and observes.**

Interestingly, in programming, e.g. in ``sclang``, we write:

```isc
i = 1;
i = (-1)/i;
```

which looks like a paradox!
How can $i$ be equal to $(-1)$ divided by itself when the division clearly changes $i$ whatever it currently is?
When executing the second line over and over again ``i`` oscillates between 1 and -1.
Of course, computer scientists, programmers, and mathematicians will point out that the equal sign should not be confused with the equal sign of mathematics.
The former is an assignment, that is, an act, an operation that works on $i$, or what Spencer-Brown calls *step* and the latter means equality, that is, it states that two expressions are equal in value.
Therefore, we usually use the arrow sign in our pseudocode, i.e. $i \leftarrow (-1)/i$ instead of the equality sign $i = (-1)/i$ to avoid confusion.
And mathematicians usually define a sequence like:

\begin{equation*}
\begin{split}
i_0 &= 1\\
i_k &= (-1) / i_{k-1} \text{, for } k = 1, 2, \ldots 
\end{split}
\end{equation*}

which can be expressed as an explicid form:

$$i_k = (-1)^k \text{, }k \in \mathbb{N}_0.$$

The former is imperative---telling the computer / observer what to do---the latter is declarative---describing a fact or relationship.
Because the relation is unstable (there is no fix point) it is a *productive paradox*.
To eradicate time, we introduce infinity (an infinite sequence).
And to eradicate space or memory, we use knowledge (*compressed memory*), e.g. we know that $(-1)^k = 1$ for all even $k$ thus we can compress the infinite sequence back into a (generative) algorithm.

Through execution, algorithms construct temporal worlds---ones not always aligned with human intuition; they decompress.
This can be productively alienating, forcing us to rethink the conditions under which time appears at all.
In this sense,

>an algorithm is not just a machine that operates in time, but a machine that creates time through the recursive play of distinction and indication.

The implications are significant.
First, algorithms are not just temporal in use—they are temporal in essence.
Second, computation is not neutral: the way an algorithm encodes time and causality shapes our experience.
And finally, when mediated through algorithms, time becomes fragmented, recursive, nonlinear, and fundamentally uncertain.

Let me repeat: In contrast to the notion of *physical time* as a fixed dimension in physics---be it Newtonian absolute time or relativistic proper time---Spencer-Brown treats time as emergent.
It arises not as a pre-given container for events, but through the rhythmic repetition of distinctions.
Time begins when a form is drawn, erased, and drawn again. 
In this view, physical time---with its clock-based regularity---may can be seen as a stabilized trace of recursive operations, an emergent order from the logical oscillation between marked and unmarked states.
What physics treats as measurable, external time may, from this perspective, be the formal consequence of internal, self-observing operations.

So, at this point the reader might ask: Can we reconcile *physical time* with *logical time*?
This should be possible if the former is more fundamental than the latter, right?
In other words, how, assuming Spencer-Brown's *Laws of Form*, does physical time emerge in such a model?

One possible interpretation is that what we call physical time---measured by atomic clocks or celestial movements---is a stabilized trace of these logical rhythms.
That is, 

>physical time is the observable regularity produced by repeated, self-similar operations of distinction.

Just as a vibrating cesium atom defines a second by its regular transitions, a recursive logical system generates a sense of time through the consistency of its internal oscillations.
The metricization of time in physics may thus be seen not as a fundamental given, but as an emergent regularity: a rhythm rendered legible and measurable.

This idea also resonates with certain developments in physics itself.
In *loop quantum gravity* and other approaches to quantum cosmology, time is no longer treated as a continuous background parameter, but as something that emerges from more fundamental, non-temporal structures.
Similarly, Ilya Prigogine's work on non-equilibrium thermodynamics emphasizes time as an irreversible process, not a symmetric coordinate {cite}`prigogine:1997`.
And Carlo Rovelli {cite}`rovelli:2018` has argued that time is not a universal feature of the world, but a relational effect that arises from interactions between systems.

Spencer-Brown's logic gives philosophical and formal expression to this shift: time is not the frame for events---it is the result of forms interacting, repeating, and observing themselves.
Algorithms, in this context, are not just mechanisms that use time; they are processes that construct temporal structure, especially when they include recursion, iteration, and memory.

### Euclid's Algorithm

One of the earliest known algorithms in recorded history is **Euclid’s algorithm** for computing the greatest common divisor (GCD) of two natural numbers. 
Given $n, m \in \mathbb{N}$, the goal is to find the largest number $d$ such that

$$\exists k_1, k_2 \in \mathbb{N} : n = k_1 \cdot d \quad \text{and} \quad m = k_2 \cdot d,$$

and no larger number satisfies this condition. 
If one of the numbers is a multiple of the other, the solution is immediate. Otherwise, we assume without loss of generality that \( n > m \).
The key insight is that subtracting the smaller number from the larger does not change the GCD. In fact, \( \gcd(n, m) = \gcd(n - m, m) \), because:

To visualize this, imagine two sticks of lengths  $n$ and $m$. 
If a third stick $d$ can evenly divide both, it must divide the shorter stick—and thus, also the *remainder* when the longer is reduced by the shorter.
Repeating this logic recursively, we can subtract the smaller from the larger until both are equal: that number is the GCD.

```{prf:algorithm} Euclid's Algorithm
:label: alg-euclid

**Inputs:** Two numbers $n, m \in \mathbb{N}$.

**Output:** The greatest common divisor of $n$ and $m$.

1. While $n < m$ or $m < n$
    1. If $m > n$
        1. $t \leftarrow m$
        2. $m \leftarrow n$
        3. $n \leftarrow t$
    2. $n \leftarrow n - m$
	
2. return $m$
```

This iterative algorithm generates a sequence of state pairs $(n,m,t)_k$.
For example, with $n = 84$ and $m = 378$, we *observe*:

$$(84,378)_1, (378,84)_2, (294,84)_3, (210,84)_4, (126,84)_5, (42,84)_6, (84,42)_7, (42,42)_8$$

In SuperCollider syntax (``sclang``), the implementation looks like this:

```isc
(
n = 84;
m = 378;

while({(n < m) || (m < n)}, {
  if(m > n, {t = m; m = n; n = t;});
  n = n - m;
  [n,m].postln; // to print n and m
});
)
```

A more mathematically elegant form is the recursive version:

```{prf:algorithm} Euclid's Algorithm (recursivly)
:label: alg-euclid-recusive

**Inputs:** Two numbers $n, m \in \mathbb{N}$.

**Output:** The greatest common divisor of $n$ and $m$.

1. If $n == m$
    1. return $n$

2. If $m > n$
    1. return gcd(m,n)
3. Else
    1. return gcd(n-m,m)
```

```isc
(
~gcd = {
  arg n, m;
  [n,m].postln;
  if(m == n, {^n;});
  if(m > n, 
    {^~gcd.(m,n);},
    {^~gcd.(n-m,m);}
  );
};
~gcd.(84,378).postln;
)
```

Recursion is often praised for its expressiveness and elegance: it mirrors the mathematical definition directly, avoiding explicit state management like loops or counters.
It can be seen as declarative---stating what to compute rather than how---and philosophically, perhaps closer to the paradoxical logic of form:
$gcd(n,m) = gcd(n−m,m)$ echoes the unresolved recursion at the heart of processes that generate time.

However, recursion also comes with trade-offs:

+ It often requires more memory due to stack usage.
+ It can be less efficient than iteration for large inputs.
+ Each recursive call retains a trace of prior states, which—ironically—can become a burden in practical computation.

In contrast, iteration "*forgets*" as it proceeds: only the current values are retained; past states are discarded.
Its trace vanishes quickly.
Recursion, by contrast, accumulates a history, and only resolves once the entire chain of self-reference collapses into a result.

Understanding recursion also challenges our intuitions.
While iteration reflects a linear, causal sequence---matching our everyday experience of time---recursion introduces nested layers of causality, echoing a structure of time that is circular, folded, or delayed.
This may explain why humans often find recursive processes harder to grasp: we live in iteration, but are in fact inherently recursive, that is, self-referential and reflexive---there lives an "I" in myself; I have re-entered myself.

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
And isn't it even more fascinating, that you constructed time by *indicating* and *drawing a distinction* between the *marked* (1) and *unmarked* state (0) observing the algorithms (recorded) execution.

## Limits of Computation

Something magical things happens when a finite sequence of operations uncovers structure and reveals patterns previously unseen.
The algorithm---rigid in form yet generative in execution---is both alienating and beautiful.
It follows rules without deviation, and in doing so, often surprises us.

Formally, an algorithm is a finite sequence of executable instructions that, given a finite input, produces a finite output in a finite number of steps---using only a finite amount of memory at any point.
Algorithms are typically expressed in programming languages, which are then compiled or interpreted into machine code that a physical computer can execute.

Yet algorithms are not confined to machines.
Humans run them too---when sorting books, calculating tips, or solving puzzles.
The "inputs" might be titles, prices, or rules; the "outputs" are the actions we take.
This universality of the algorithmic perspective once inspired philosophical dreams of complete formalization.

In the early 17th century, thinkers such as Leibniz's intellectual heirs and later in the 20th century formalists like Russell and Hilbert envisioned a universal logical system---a calculus ratiocinator---capable of resolving any mathematical statement by mechanical reasoning.
In *Grundzüge der theoretischen Logik* {cite}`hilbert:1928`, Hilbert and Ackermann raised the question now known as the *Entscheidungsproblem*: can there be an algorithm that decides the truth or falsity of any statement in first-order logic?

Initially, it seemed plausible and it is known that this is true for *propositional logic* and the *Presburger arithmetic* (arithmetic of natural numbers with addition but not multiplication).
But this vision encountered a decisive rupture in 1931, when Kurt Gödel, in *Über formal unentscheidbare Sätze der Principia Mathematica* {cite}`goedel:1931`, demonstrated two groundbreaking results:

1. **Incompleteness:** Any sufficiently expressive formal system (one that includes arithmetic) will contain true statements that are unprovable within that system.
2. **Inconsistency barrier:** Such a system cannot prove its own consistency without contradiction.

Gödel's work revealed the inherent limits of formal systems: there is no algorithm that can decide the truth of every statement within arithmetic.
Not all questions can be mechanized.

Building on Gödel's insights, Alan Turing introduced the concept of the *Turing machine* as a model for what it means to compute.
In his 1936 paper *On Computable Numbers* {cite}`turing:1936`, he formulated the *halting problem*: can a machine determine, for any given program and input, whether that program will eventually halt or run forever?

Turing proved that no such machine exists.
More precisely, **there is no general algorithm that can decide whether an arbitrary program halts**.
This result established the existence of *undecidable problems*: well-posed, meaningful questions that cannot be answered by any algorithm.
This also implied that no physical or digital machine---being at most as powerful as a Turing machine---can compute everything.

Further developments by Herbrand, Skolem, and others revealed more nuanced boundaries.
In first-order predicate logic, semi-decidability prevails: if a formula is provable, there exists an algorithm that will eventually find a proof.
But if it is unprovable, the algorithm may run forever {cite}`skolem:1970`.
We can recognize truth by success, but not falsity by failure---a fundamental asymmetry in logic and computation.

The limitations discovered by Gödel and Turing are not arbitrary---they arise from a deep structural feature of formal systems: their capacity to refer to themselves. Both Gödel's and Turing’s theorems exploit self-reference to reveal internal contradictions or undecidable conditions.
Gödel constructs a formal statement that essentially says:

>This statement is not provable within this system.

If the system could prove it, it would be inconsistent. 
If it cannot prove it, then the statement is true but unprovable—demonstrating incompleteness.
This is a formalized version of the liar paradox: "This sentence is false".
It creates a loop within the system that the system cannot resolve from within.

Similarly, Turing’s proof of the halting problem constructs a machine $\mathcal{H}$ that is supposed to determine whether any machine $\mathcal{T}$ halts on input $x$. But then he defines a machine $\mathcal{D}$ that feeds its own description to $\mathcal{H}$  and inverts the result. The result is a contradiction: if $\mathcal{H}$ says $\mathcal{D}$ halts, then $\mathcal{D}$ runs forever---and vice versa.
Again, a loop of self-reference generates undecidability.

This is exactly the kind of paradoxical *re-entry* that Spencer-Brown analyzes in *Laws of Form* {cite}`brown:1969`.
In his system, the act of drawing a distinction is the beginning of form, but when a form refers to itself---when the distinction is applied to its own operation---paradox arises. This is not a flaw but a fundamental feature: the form re-enters the form.

In this light, Gödel's and Turing's results are not merely technical limits but **deep logical consequences of systems that are powerful enough to observe themselves**.
They are manifestations of what Spencer-Brown formalizes: the moment a system includes itself in its domain of discourse, it becomes incomplete, unstable, or paradoxical---but also potentially creative, open-ended, and dynamic.

These discoveries mark a fissure in the modern epistemic project: the dream of full formalization collapses not by external failure, but through internal paradox.
The algorithm, once a symbol of certainty, becomes a boundary marker---demarcating not only what can be computed, but what cannot even be known by formal means.

>The very techniques that reveal the limits of formal systems—self-reference, paradox, recursion—are the same structures that, in Spencer-Brown’s logic, generate time, form, and meaning. What formal logic excludes as paradox, Laws of Form embraces as the ground of creation.

This transition, from the certainties of modern logic to the open-endedness of computation, anticipates the *postmodern condition*: an era not of clear foundations, but of recursive limits, undecidable structures, and generative paradoxes.
Maybe Richard Rorty was right after all: the view of philosophy---including mathematics and physics---as the faculty that has traditionally aimed to uncover timeless, foundational truths---something like the "*mirror of nature*" (a metaphor he critiques in earlier work {cite}`rorty:1979`)---might have outlived its usefulness.
We may should surrender the idea of discovering universal truths and instead focus on *cultural* and *linguistic creativity*.
Instead of asking for truth we may want to ask for usefulness and communicative effectiveness.

There is no "God's-eye view" from which we can assess all perspectives neutrally.
For Rorty, language---including mathematical, physical and computational language---is contingent.
His confederate, Derrida, shuttered the philosophical tradtion by showing that what we take as *literal* or *proper* meanings are built upon layers of methophor that have become naturalized thought repetition {cite}`derrida:1974`.
Terms like *substance*, *subject*, *truth*, and Heidegger's *Being* have roots in sensory or physical metaphors that we can not escape---we can not go outside or beyond language and it does not have a transparent link to a stable, pre-given reality.

But Metaphors are existential.
By shaping how we conceptualize and interact with the world, metaphors play a crucial role in the formation of both personal identities and comprehensive philosophical systems.
They have a foundational role in the realms of human experience.
Therefore, we should take them seriously not because they refer to what Rorty calls "really real" but because they mean a lot to us.

This meaning is always mediated by a network of other signs and shaped by cultural, historical, and metaphorical context.
It arises from *difference* within language itself---a word is not pointing directly to a thing but it gets is meaning by how it differs from other words.
There is no ultimate *signified*---words do not lead back to a final, real meaning but each sign points to another sign in a chian.
It is difference and deferral, i.e. *différance*.

Thus truth is like a flicker---a momentary effect produced by a play of signs, none of which have fixed meaning.
You might feel you "have" the truth for a moment---but that truth is never self-identical, never whole, and always open to being undone by the play of signs that brought it into being.
Derrida *decontructs* the traditional view that language reflects reality; that words are label for things and truth is correspondence; that a statement is true if it matches reality.

Take the sentence: "There is a glass of water on the table".
In ordinary terms, most people would say: This statement is true if there is, in fact, a glass of water on the table.
This is the *correspondence theory of truth*: a statement is true if it matches reality.
But Rorty rejects the correspondence theory as metaphysically confused.
He doesn't say statements like this are not true---he says the notion of "truth as correspondence to reality" is unhelpful and unnecessary.
The statement "There is a glass of water on the table" is true if our peers (or linguistic community) would agree that it is appropriate to assert it---given what we observe and how we talk.
Truth is what it is good for us to believe (pragmatism).
Rorty does not deny that the glass of water exists.
The sentence is true not because it corresponds to reality in some metaphysical way but because it’s useful, warranted, and coherent within our practices.

Similarily Derrida wouldn't deny that such a sentence can function meaningfully. But he would interpret the question not in terms of correspondence or even pragmatic success, but in terms of language’s internal play, difference, and deferred meaning.
Even a simple sentence like this relies on (1) a shared system of signs and differences (what "glass", "water", "table" mean) and (2) a context (what table? where? when? how is "glass" being used?).
But crucially, for him, context is never fully stable or closed.
Meaning always relies on differences, and no word has a meaning that is completely fixed.
Even if the referent exists (the actual glass), the sentence's meaning is still subject to drift, re-interpretation, or breakdown.
In saying, "There *is* a glass of water," we act as though we are pointing to something fully present.
But this assertion already assumes a metaphysics of presence---that meaning is anchored in a stable, present "*now*".
Yet "glass", "water", "table" only mean what they mean through differences from other terms.
Each word points beyond itself in an infinite chain of references (glass -> vessel -> transparency -> fragility... etc.).
Meaning is never fully *there*. It is constructed and deferred.
If Rorty says 

>truth is what your peers let you get away with saying,

Derrida might say:

>Meaning is what temporarily survives the endless sliding of signifiers.

This does not mean that formal logical systems, such as Tarski's theory of truth can be refuted.
They work perfectly fine as a tool for logicians.
But it is one way to operate in a specific system and another to generalize this system into a universal theory of truth that applies to ethics, politics, or everyday speech.
Truth in natural language isn't formal because formal statements requires a formal system within they can be true or false---one might say valid or invalid.
We shouldn't pretend "truth" is a metaphysical relation.
Derrida would probably go further and would argue that all language is vulnerable to slippage, undecidability, and recursive instability, even formal logic.
He would say:

>Derrida is saying you can't ultimately escape the problem of meaning and self-reference---not even with meta-languages.

Furthermore, he suggests that reality is always mediated through language.
We do not experience a raw "real" but a linguistically filtered version of it.
Even what we think of as direct experience is shaped by language categories---time, object, cause, identity, etc.

>Everything we take as given—including reality—is already interpreted through signs. If knowledge is only valid when it is perfectly grounded, then no knowledge is ever valid. But maybe knowledge never needed perfect ground to be meaningful, useful, or rich. We are not standing on a foundation but on a sailing ship with imperfect intruments and changes in wind but we still get somewhere; we still orient ourselves, even if there's no final, fixed land; we probe, test, revise---forever.

What a wonderful world it is.
An open world free from the tyranny of metaphysical absolutes and full of plurality, ambiguity, and revision.
It means responsibility---because without the comfort of absolute truth, we must continually examine, justify, and remain open to change.

For Spencer-Brown---to close the circle---mathematics is grounded in the most basic epistemological operation: the drawing of a boundary.
Derrida exposes the instability of the marked/unmarked distinction.
He shows how every system of meaning is haunted by what it excludes, just like Spencer-Brown’s unmarked state remains implicitly necessary.
At this point Rorty comes in to warn us of yet another "*final vocabulary*" that Spencer-Brown might wish to reach.
For all of them, language is a human construct, not something that maps perfectly onto reality.
Because of this, no single vocabulary can claim to be the "correct" one for describing "the world".
Consequently, all faculties of philosophy should be more about self-creation than discovering some essential, pre-existing self or truth {cite}`rorty:2016`.
Like poets or artists, individuals should aim to create new, meaningful ways of being.

>We should aim for better futures, not for objective, ahistorical knowledge. -- Richard Rorty

## Rational Machines, Cultural Systems

In the literature of computer science, algorithms are predominantly discussed in technical terms---how they are designed, evaluated for performance, and proven to be optimal. Even when applied to real-world contexts, they are generally seen as mechanisms for executing well-defined tasks with mathematical precision and technological neutrality.

This perception portrays algorithms as purely formal beings of reason, as Rob Kitchin notes {cite}`kitchin:2014`.
While programmers might differ in their coding styles, algorithm design is often framed as a value-neutral, apolitical activity.
As a developer myself, I recognize this mindset.
When writing code to solve a problem, I rarely pause to consider the broader social implications or reflect on the values implicitly embedded in the software I produce.

Yet the truth is more complex. 
Algorithms are deeply woven into the normative fabric of both the digital and tangible worlds.
In today's interconnected society---shaped by the internet of things, AI, and robotics—algorithms don’t merely function.
They structure, filter, decide, and "learn".
They manage surveillance data, shape recommendations, generate action plans, and influence how decisions are made and justified.
Their impact on living, social and psychic systems (minds) does not arise from intrinsic sense-making but from their influence on communication, perception, and cognitive processes {cite}`zoennchen:2025`.

We are constantly exposed to their influence.
Algorithms drive search engines, personalize advertisements, recommend entertainment, and match romantic partners. Less visibly, they also trade stocks, aid in diagnosing illness, match organ donors, identify criminal suspects, and allocate students to public schools.
These are not just technical feats—they are acts of judgment.

At the core of algorithm development lies a process of translation. 
Tasks must first be expressed in human language---a notoriously ambiguous and contingent medium. Developers then transcribe these imperfect descriptions into code. 
At every stage, human judgment is exercised, and this judgment is shaped by historical and cultural contexts.

>Even algorithms cannot escape history; they cannot escape social and cultural evolution.

Digital spaces, then, are not neutral arenas.
They are structured by values, controlled through code that defines what actions are possible and permissible.
One could argue that the primary purpose of an algorithm is to automate socially successful practices, to encode *scripts* {cite}`latour:1992` that relieve us of the burden of negotiation and deliberation.
Thus, so-called "cyberspace" has never been free of regulation---it has always been governed, just not by walls or gates, but by source code.

This code governs behavior.
The design of a platform determines how people interact within it. As Lawrence Lessig famously observed:

>Codes constitute cyberspaces; spaces enable and disable individuals and groups. The selections about code are therefore in part a selection about who, what, and, most important, what ways of life will be enabled and disabled. -- {cite}`lessig:2006`

In our digital age, algorithms do more than automate---they govern.
Niklas Luhmann described them as *transparent* *evolutionary achievements* that reduce complexity and transform uncertainty into manageable ignorance {cite}`luhmann:1998`.
Transparent here does not mean understandable in detail; it means functionally observable.
Like a clock, we might not know how it works, but we can tell if it is working.

This functional transparency can be both beneficial and harmful.
It suppresses dissent---not always maliciously, but by foreclosing alternative operations {cite}`nassehi:2019`.
The danger escalates when this suppression becomes systemic.

John Danaher calls this condition *algocracy*---a regime where algorithms play a decisive role in governance {cite}`danaher:2016`. Sebastian Rosengrün takes this further, arguing that Western societies may be shifting from the *rule of law* to the *rule of code*:

>Source code is about to become the main regulator of individual and institutional behavior that regulates all other regulators including law. -- {cite}`rosengruen:2022`

Importantly, Rosengrün does not claim that regulation is inherently bad, nor does he assume malicious corporate intent.
Instead, he insists that law---not profit-driven code---must remain the foundation of democratic governance.
His warning is clear: if source code supersedes law, democratic institutions are at risk.

We must also account for a new generation of algorithms---those driven by data rather than explicit design.
Here Luhmann's conceptation has to be extended because for systems are "artificial intelligent" it is no longer obvious to differentiate between a working and a mailfunctioning system.
These systems are not only *intransparent* because we can not explain how they work in details but because we can not tell if they work at all.
In that sense they introduce a new form of contingency into society that, in the past, led to the invention of norms (social interactions are plagued by a *double-contingency* "I'll do what you want if you do what I want").
These *intransparent* systems, such as artificial neural networks (ANNs), learn structures from patterns in training data, often beyond human interpretability.
They find structures in communication and feeding them back into communication, that is, society forming a feedback loop of communication.

>Unlike traditional algorithms, which are explicitly designed by developers, artificial neural networks construct their computational structures from data. [...] The data contains patterns of communication that psychic systems themselves cannot make sense of. -- {cite}`zoennchen:2025`

In Rob Kitchin’s case study of an algorithm meant to count Ireland’s "ghost estates," we see the challenges of this data-driven approach {cite}`kitchin:2014`.
The task appears straightforward: count under-occupied housing developments.
But which metrics matter? Is 50% completion enough? Or 75%? Should the algorithm visualize its findings on a map? 
Every choice is a judgment call.
Yet, as algorithms increasingly "learn" from data rather than follow fixed rules, these judgments can become implicit and untraceable—baked into the very architecture of AI.

In such cases, decisions are no longer made by individuals or even institutions in the traditional sense.
Instead, they are *loosely coupled* to the collective communications of society---reflected and reinforced through training data.

It's tempting to assume that while computer scientists build algorithms, other disciplines will step in to regulate their use.
But this division of labor assumes that those other disciplines---and the public—have the capability and authority to do so.
Too often, algorithms are discussed within narrow, technically focused frameworks.
We must broaden our understanding.
If algorithms are to underpin our technological infrastructures, influence our social institutions, and mediate our everyday lives, then the judgment behind their design must be critically examined.

Algorithmic thinking is inherently reductionist. It assumes that complex, context-sensitive social and economic exchanges can be modeled and simulated with only minimal loss. But this assumption is rarely scrutinized.

>Algorithms do not just process data; they produce, affirm, and certify knowledge through a particular logic built on specific assumptions. — Tarleton Gillespie {cite}`gillespie:2014`

As Gillespie and others argue, algorithmic reasoning privileges a utilitarian rationality---a logic grounded in scientific abstraction and instrumental efficiency.
This displaces forms of knowledge rooted in lived experience, deliberation, and embodied practice.
Data-driven algorithms, for all their power, cannot (yet) observe thought or consciousness.
They cannot grasp subjective experience.

If algorithms are to remain central to modern life, they must become a matter of interest across disciplines---from computer science to philosophy, from the arts to everyday civic life.
Their legitimacy and neutrality must be scrutinized, not assumed.

>Code is not purely abstract and mathematical; it has significant social, political, and aesthetic dimensions. — Montfort et al. {cite}`montfort:2012`

In this context, fields like algorithmic music offer more than creative expression.
They invite a *phenomenological engagement* with code---allowing us to experience algorithmic behavior directly, without metaphysical abstraction.
This kind of engagement shifts us away from *utilitarian rationality* and toward knowledge grounded in *perception* and a more *intermediate cognition*.
But to re-emphasize Rorty's {cite}`rorty:2016` warning: we should not go overboard with this *romanticized* approach---that is, we should not assume that it contains "the truth" or a more direct relation to "the really real".

If we are to live with algorithms---and more importantly, live well with them---then we must learn to see them not just as tools, but as active social, cultural, and philosophical artifacts.
As systems that may be soon decoupled from psychic and social systems meaning that we will lose (direct) control over them.
They may very well co-evolve in an interdependent relation along side us and if they should become *autopoietic* we have to understand their *couplings* with social and psychic systems.

Here I wanna close with Rorty's words to emphasize that, while *imagination* is important, it can produce horrific ideas.
Without bounds, *romanticism* can create a monster.
And only because something is contingent does not imply we should change it.

>If we can avoid the fallacy of thinking either that the contingency of a social practice implies that it should be dropped or that the sheer novelty of a suggested practice is sufficient reason to adopt it, then intellectual life will survive the collapse of the appearance-reality distinction, as well as the relativization of rationality. [...F]uture intellectuals will not be closer to the way things really are than Plato was, but their imaginations will be dominated by a different sense of what it is to be human---one that takes our finitude for granted rather than attempting to escape from it. -- Richard Rorty {cite}`rorty:2016`

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../sounds/jam.mp3'
ipd.Audio(audio_path)
```