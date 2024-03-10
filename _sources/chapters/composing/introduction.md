# Introduction

>[The mechanical engine] might act upon other things besides numbers, were objects found whose mutual fundamental relations could be expressed by those of the abstract science of operations, and which should be also susceptible of adaptations to the action of the operating notation and mechanism of the engine. [...] Supposing, for instance, that the fundamental relations of pitched sounds in the science of harmony and of musical composition were susceptible of such expression and adaptations, the engine might compose elaborate and scientific pieces of music of any degree of complexity or extent. -- *Ada Lovelace*

This quote by *Ada Lovelace*, one of the most famous and first programmers of all time, shows that the foundations of *algorithmic* and *artificial compositions* are over a thousand years old.
It is remarkable how she already envisioned complex algorithmic composition executed by *the engine*.

Around 1026 the music theoretician and Benedictine *Guido d'Arezzo* developed one of the first known techniques to construct melodies semi-automatically by parsing Latin text into chords.
He mapped each vowel contained in the Latin text to a specific pitch determined by a table.
His method supplied three choices for each vowel such that for a text with $n$ vowels, there were $3^n$ possible outcomes.
*Guido's* intention was to ease his students from the burden of an unlimited space of possibilities;
giving them freedom by structure.
There was still room for personal taste but not so much to feel overwhelmed.
Even in those early days, algorithms were employed to limit and explore the space of possible melodies.
It also shows that composing was a compelling task in the past.

This has not fundamentally changed, even if we have more tools than ever at our hands inspired by a diverse set of fields ranging from probabilistic approaches, generative grammars, to neural networks.
The process of composing, and deciding how to go about it, can be one of the most challenging things about algorithmic composition.
The jump from modifying simple examples to producing a full-scale piece can be tricky because there is no single or best way to do things.
We run into the *burden of freedom*.
Furthermore, we must think about time and how we can connect the physical with the logical.

Now, before we can move on we have to talk about the elephant in the room, that is, *deep learning*.
Where symbolic approaches lean more towards the intelligence of algorithms, machine learning, especially deep learning, leans towards the intelligence within the data.
Researchers and developers made significant progress in the field of deep learning using generative models to output arguable impressive results.
For example, [Continue](https://magenta.tensorflow.org/studio/standalone#continue) (from [Google's Magenta](https://magenta.tensorflow.org/) project) uses a recurrent neural network (RNN) to generate notes that are likely to follow your drum beat or melody.
[OpenAI](https://openai.com/) released [MuseNet](https://openai.com/blog/musenet/), a deep neural network that can generate 4-minute musical compositions with ten different instruments and can combine styles from country to Mozart to the Beatles.

One fundamental problem I see with systems that purely rely on deep learning models is that they often offer little possibility to make the medium visible.
Especially if they are large and use a prompt-based interface, forms of the medium, at least for me, tend to be uninteresting.
They do not show the algorithms, data, or training process behind the scenes.
By definition, deep learning models try to imitate the logic and structure of the data they were trained on.
They learn rich representations of the data which are part of the so-called *latent space*.
Each dimension of the latent space, if it is semantically well-structured, represents a fundamental charactersitics of the training data.
Thus by navigating within the latent space, one can get novel and interesting results.
However, if this is only possible via text descriptions, the model tends to output results that are likely thus rather uninteresting.
The lack of direct control over the navigation through the latent space offers non-experts an easy way to get good results and experts frustratingly opaque and uncontrolable kind of interaction.

If we should call these techniques *algorithmic compositions* is at least debatable because the algorithm that generates is not defined by the artist but by the model architecture and the data the model is trained on.

In general, *artificial "intelligence" systems*, by which I mean systems that are based on machine learning or other symbolic methods, might not be creative by themselves, but they can help us to

1. explore the conceptual space 
2. combine familiar concepts, and
3. transform ideas to create something new.

As the composer *Herbert Brün* puts it:

>Whereas the human mind, conscious of its conceived purpose, approaches even an artificial system with a selective attitude and so becomes aware of only the preconceived implications of the system, the computers would show the total of available content. Revealing far more than only the tendencies of the human mind, this nonselective picture of the mind-created system should be of significant importance. -- *Herbert Brün* (1970)

A prime example is the [discovery of a new algorithm for matrix multiplication](https://www.nature.com/articles/s41586-022-05172-4) made by another machine learning algorithm.
The discovered method outperforms all known algorithms for some instances.
The authors estimate that humans did not find the method because of the missing intuition.
In that sense, the machine is less biased because it has no concept of purpose and it does not act on intuition.
Concerning our modern *system of control* that is based on algorithms constructed by algorithms that learn from data semi-automatically, this claim can be challenged.
However, it remains true that machines can help us to get rid of our personal biases, even if they might introduce new ones.

SuperCollider can be used to build a kind of *artificial system*.
It provides us not only with a context in which we can compose music but is general and powerful enough to construct a new one.
However, as we know form comics: with great power comes great responsibility.
In contrast to *digital audio workstations (DAWs)* such as *Reason* or *Ableton*, SuperCollider is far less restrictive;
there is no *preferred* way of working.
Such compulsion can be liberating.
Instead, SuperCollider offers very different ways to accomplish the artist's goal, and it is our responsibility to find our own style.

Many different approaches are feasible to generate and assembling a composition.
Consequently, showing an extensive list of different techniques is impossible and undesirable.
But I will try to give you some starting points.