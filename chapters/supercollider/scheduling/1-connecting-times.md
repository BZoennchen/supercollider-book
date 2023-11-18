# The Entanglement of Time

>An algorithm is on the verge of time: on the one hand, it is strictly structural – a formal, unchanging entity.
Not only a formula, however, but a formula that prescribes steps to be made one after another, depending on one another.
It is a formula that exists in order to unfold, in the form of a process, in time and over time, and dependent on its past inputs. -- Julian Rohrhuber {cite}`rohrhuber:2018`

According to Rohrhuber, while both domains, i.e., mathematics and computer science, are formal disciplines, they have a different relation with time.
Mathematical equations are static and stateless.
Like a *calculator* they take in some argument $x$ and return some value $y(x)$, where $x$ is not evolving into anything.
They can incorporate time, for example, if we consider differential equations, but nothing unfolds within a mathematical function.
Time can only be modeled by a mathematical object but is not implicitely relevant for the computation of a function.

One exception to this rule is the logic developed by Georg Spencer-Brown in his mostly ignored work *The Laws of Form* {cite}`brown:1969`.
Spencer-Brown introduces the concept of the *re-entry* by resolving self-referential paradoxes in time.
While the self-referential relation is a pardox in the static world, it becomes a self-generating process in the dynamic world.
This leads quite naturally to the formalization of an unfolding process, thus it is surprising that his work was mostly ignored by the computer science community.

While being a finite and static description, algorithms, describe such processes that unfold in time.
In many instances they are stateful, they do work, they transform or construct something step by step in a specific order.
If we reason about algorithm, we reason about time.
We even reason about the amount of time an algorihm requires and call this *time complexity*.
However, it is not a specific time period but an estimation of the number of steps an algorithm requires.
It measures not a specific time but some or many potential time(s) in which the decribed process happens.
Therefore, without mentioning time explicitly, algorithms are a logical representation of it.
And if they are executed, their logical time gets connected to a physical time. 

If we compose or play music, we reason about the physical time, i.e., the relation between time intervals.
Your ears are very sensitive to rhythms and small deviations immidiatly strike us.
Therefore, we very carefully make sure that everything is synchronized as inteded and everyone plays in time.
Combining the act of composing or playing music with the act of developing algorithms leads us to an interesting entanglement of two worlds.
We do not only combine two activities but two concepts of time: the logical with the physical!