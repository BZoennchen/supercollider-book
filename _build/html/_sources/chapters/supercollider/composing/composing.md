# Composing

>[The mechanical engine] might act upon other things besides numbers, were objects found whose mutual fundamental relations could be expressed by those of the abstract science of operations, and which should be also susceptible of adaptations to the action of the operating notation and mechanism of the engine. [...] Supposing, for instance, that the fundamental relations of pitched sounds in the science of harmony and of musical composition were susceptible of such expression and adaptations, the engine might compose elaborate and scientific pieces of music of any degree of complexity or extent. -- *Ada Lovelace*

This quote from one of the famous *Ada Lovelace*, one of the first programmers, shows that the foundations of *algorithmic/artificial composing* are over a thousand years old.
Around 1026 the music theoretician and Benedictine *Guido d'Arezzo* developed one of the first techniques to construct melodies semi-automatically by parsing Latin text into chords.
He mapped each vowel contained in the Latin text to a specific pitch determined by a table.
His method supplied three choices for each vowel such that for a text with $n$ vowels, there were $3^n$ possible outcomes.
*Guido's* intention was to ease his students from the burden of an unlimited space of possibilities;
giving the freedom by structure.
There was still a lot of room for personal taste.
Even in those early days, algorithms were employed to limit and explore the space of possible melodies.
It also shows that composing was a compelling task in the past.

This has not fundamentally changed, even if we have more tools than ever at our hands.
The process of composing, and deciding how to go about it, can be one of the most challenging things about SuperCollider.
The jump from modifying simple examples to producing a full-scale piece can be tough because there is no single or best way to do things.
We run into the *burden of freedom*.
However, *artifical systems* might not be creative by themselves but they can help us to

1. explore the conceptual space 
2. combine familiar concept, and
3. transform ideas to create something new.

As the composer *Herbert Brün* put it:

>Whereas the human mind, conscious of its conceived purpose, approaches even an artificial system with a selective attitude and so becomes aware of only the preconceived implications of the system, the computers would show the total of available content. Revealing far more than only the tendencies of the human mind, this nonselective picture of the mind-created system should be of significant importance. -- *Herbert Brün* (1970)

SuperCollider can be used to build this kind of *artificial system*.
It provides us not only with a context in which we can compose music but is general and powerful enough to construct a new one.
However, with great power comes great responsibility.
In contrast to *digital audio workstations (DAWs)* such as *Reason* or *Ableton*, SuperCollider does not force the user into a *preferred* way of working; such compulsion can be liberating.
Instead, SC offers very different ways to accomplish the artits goal and it is his or her responsibility to find their own style.

Many different approaches are feasible to generate and assemble a composition.
Consequently, showing an extensive list of different techniques is impossible and undesirable.
But I will try to give you some starting points.