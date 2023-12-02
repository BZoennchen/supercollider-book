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

```{code-cell} python3
:tags: [remove-input]
import IPython.display as ipd
```

(sec-medium-and-form)=
# Medium and Form

>There is neither a medium without form nor a form without medium.
>The difference of mutual dependency and independency is pivotal. -- Niklas Luhmann {cite}`luhmann:1986`

What is art and what makes an artwork an artwork?
Even as someone who is not educated in the history of art or any other field of art-related theory such as aesthetics, this question makes me restless.
In my opinion, good art reveals something unspeakable about my own *throwness*.
It irritates, it breaks rules and laws by giving us a glimpse into the *infinite*.
Confronted with something beyond understanding, we stand there in awe; feeling relieved and in total connection with what is.
This description is an unspecific expression of a feeling but that is the point: I cannot write down what I means.

The German sociologist Niklas Luhmann gave rather theoretical but much more helpful analysis of art by relating it to his concept of medium and form.
According to him, a medium consists of a large number of elements or, in the case of the time dimension, events.
In fact, there are so many elements within a medium that any cognition has to operate by selection.
Forms, on the other hand, emerge by the concentration of dependency relations between elements.
These relations have to be supported by the medium.
The *loose coupling* and *separability* of elements of the medium lead to this effect.
We do not perceive the medium itself but the form which coordinates elements within the medium.

Luhmann defines medium in relation to form, i.e., relatively.
Therefore, forms can be the medium of a new form.
A *medium* is any set of loosely coupled elements that, if rigidly coupled, build a *form*.
Only by the detour of observing the form, can an observer relate to the medium.
The form catches attention and refers to the medium.
We can ask: How came this form into being?

Sound is the form of air.
It is literally the compression (rigid coupling) of air molekules our ear perceives.
And when the air is too thin, we recognize it because the creation of the form fails---no sound can be perceived.
In Luhmann's contructivist framework, sound requires a listener.
In other words, if a tree falls down in the deep forest and no one is listening, then the event won't make a sound.
Air will be compressed and a wave, that is, energy will travel from the event through the air but there will be no sound.

The relation between form and its medium is selection.
For example, a sentence is a selection from a language, i.e., its medium.
A computer program is a selection from a programming language.
A painting is a selection from the domain of all possible color arrangements.
A performance is a selection from all possible played tones, and each played tone is a form of the air.
The form of art is an artwork.

From a point of information theory {cite}`shannon:1948`, a form reduces the entropy of its medium.
It reduces the number of possible connections.
Each drawn stroke, each played note, each move in a performance reduces the possibilities of what can be drawn, played, or performed next.
The *horizon of the possible* gets narrowed down.
Similar to Heidegger's understanding of a craftsman, the artist brings the medium into form and the medium 'uses' the artist to become a form.
The artist might has an idea of the final work but the process of making and shaping it inevitable influences the process itself---it is a contingency.
We can say that every artwork is **contingent**; other fixations, combinations and recombinations, that is, other forms of the medium would alse have been possible.
In its final stage, the artwork is confronted by the expectation of the audience and it has to convince---it has to make sense under the assumption of its contingency.
The audience knows that the artwork could have been different, and so it asks: Why is it this way? What does it mean? What is the intention of the artist?
Its singularity aspiration will be investigated and it has to stand its ground against other works of art and other possible realizations within their medium.
Critics will judge the artwork and the market will determine if they were right.

Luhmann is not so much interested in historical or cultural *horizons of the possible* but he asks a more general question:

>What is art beyond certain culturalistic, stylistic dependencies and genres?

But to answer this general question, in a typical Luhmannian fashion, he uses a very abstract framework:

>Artworks are not just traces of human activity [...].
>Neither do they arise as simple relicts of purposeful behavior like tools, houses, streets or radioactive radiation.
>They serve [...] as transmission of sense. -- Niklas Luhmann

A medium cannot take on any form but only those which can be composed by its elements.
Form and medium share the same elements.
The difference consists solely in the loose and rigid coupling of elements.
How the medium passes the form to its elements depends on the properties of the medium itself.
The medium opens the possibilities of giving form and it also narrows it down.

The elements of a medium are rather independent.
For example, the color of a pixel of an image is technically independent of the colors of all other pixels.
Only because of this property can images picture almost anything.
We can arrange pixels as we desire.
Money is a medium since payments can be made in almost any denomination and they are independent of the sense and means of other payments.
Each letter in a programming code is inpdependent of any other letter.
Of course, similar to natural languages, only a small subset of programming code make sense, i.e. form a valid program that can be compiled, interpreted or executed.
Interestingly, the medium is very oblivious and the artist can utilize this property of the medium to manipulate the form.
The low interdependency of the medium's elements opens a space of fiction and simulation---of stories about unicorns.

Luhmann understands the artwork as **communication of order** in a form arrangement which does not happen by itself.
However, art does not utilize the medium to transmit a real order of the real world to the senses.
Instead, art forms its mediums to create a **contingent alternative version of reality**.
It does this by exploring the different possibilities of ordering elements within the medium.
Through art, we can explore new possibilities of the acoustic and optical world and make them available and experiential.
Thereby we gain more non-obvious possible ways of ordering the world.

In the relation between medium and form, the more rigid form prevails because it is less movable.
However, this is a risky endeavor for the form.
It might decay or, if it is reproducible, evolve.
Within forms, this assertive property repeats.
Sand adjusts to the stone, not the other way around.

According to Luhmann, a form can create a medium, Luhmann refers to a *second-order medium*.
Sound is a form of air but tones, which are sound, make up the medium of music.
We could also say that rhythyms (medium) make up a sound (form/medium) which can make up rhythyms (form).
Compare the following three sounds.
The first one is a rhythym, by increasing the frequency of the rhythym it turns into an infinite tone and by manipulating the amplitude of the tone, we arrive at a rhythym.

```isc
{Impulse.ar(5)!2}.play
{Impulse.ar(160)!2}.play
{Env.perc().ar(gate:Impulse.ar(1)) *  Impulse.ar(160)!2}.play
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../sounds/impulse_5_hz.mp3'
ipd.Audio(audio_path)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../sounds/impulse_160_hz.mp3'
ipd.Audio(audio_path)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../sounds/impulse_impulse.mp3'
ipd.Audio(audio_path)
```

In a musical piece, any tone can, in principle, follow or can be combined with any other tone except the form of the music piece "decides" otherwise.
Importantly, music functions as communication only for those who can recognize (and inform each other about) the difference between medium and form; only those who can hear the uncoupled space within the played music; only those who listen and recognize that, through its tonality, the music makes much more sounds possible than normally expected but it is disciplined by the form.

>Art establishes rules of inclusion that serves the difference of medium and form as medium. -- Niklas Luhmann

A *(second-order) medium* can be the difference of medium and form.
I think this statement is crucial because it explains why we have certain rules, e.g. music theory, despite art forming a medium to create alternative versions of reality.
These rules are contingent, that is, they could be very different but they are necessary to mark the outside (and with it the inside).
Rules exclude and include at the same time thus establish the possibility of making a difference.
What we call objects are in fact differences.
*Differentiation* and *indication* go hand in hand {cite}`brown:1969`.
Pointing to a chair and calling it 'chair' is not a representational operation in the sense that we are naming an object.
Instead it is an act of *differentiation* and *indication*---there are no objects, only differences.
A form might establish a medium of art by using it for the purpose of expression.
In other words, the difference between medium and form can function as a medium.
It can be the *released possibility* for the combination of mediums and forms for the forming through *communication*.
The more rigid form forces through greater flexibility but it is at risk of failing, it can be criticized, surpassed, or put into the museum.

Luhmann further argues that the art system (as a social system), like any social system, differentiates itself from its environment.
It is no longer part of religion or politics but does its own thing on its own terms.
In the cold world of functional differentiation, it serves a specific and unique function within society.
This naturally leads to the question of what function the art system actually fulfils?
A question we cannot answer here.

However, we can point out a precondition for the functional differentiation of the art system, that is, *second-order observation*.
One has to be able to observe what others observe.
Through second-order observation, the concrete bond between observer and artwork "as it is" dissolves.
An artwork signals to the observer that it earns attention.
If you observe an artwork, you can speculate about the artist's intention.
You can observe that others have their interpretation and you know that they know that you know about this fact.
They know that you can observe their interpretation and they can observe yours.
At the same time, the artist is aware of this too and it might prompt the artist to talk about her work.
Communication about works of art and the artwork itself are interdependent.
There is no art without communication and one can only communicate about art if there is an artwork to talk about.
This strange loop, this self-referential relation, sets the system of art in motion.
In a typical Luhmannian fashion (inspired by Spencer-Brown's concept of *re-entry* {cite}`brown:1969`): the paradox becomes a generator in time!

The constructive liberties of such a social system are solely grounded in communication.
If communication 'happens' everything else is secondary.
Crucial is the condition of symbolic generalization, that is, **the property of the medium to exceed the diversity of things** and the condition of **unification** to enable communication.
If art does not exeed the diversity of things, there is nothing worth communicating about and if there is no unification, sense and language fail as medium of communication---dissolution and recombination enable diversity and the selection of the particular.

Information can only be transmitted if the artwork could be different and *that which is not* is always also indicated by *that what is*.
The artwork fixes all possibilities and we can talk about reasons why it is constructed or performed this way and not any other way.
This seems consistent with the information theory of Claude Shannon {cite}`shannon:1948`.
To communicate about art we have to be aware of these liberties and we have to use them because, again, to gain information one has to eliminate uncertainty---artworks have to surprise us.

By the *re-entry* {cite}`brown:1969` communication about art can become a form of art.
Acknowledging the properties of the medium, events within the system of art have to be loosely coupled and there have to exist plenty of them.
This includes the system of art itself!
Consequently, art will be mocked by observers, exhibitors, buyers, and, in the end, by itself.
Dissolution can become an end in itself thus the medium no longer serves the form but the form serves the medium.
In that stage, form wants to show that it is in fact a medium.
For an observer, this kind of art is paradoxical.
Luhmann remarks that this path is narrow but the consideration of the dissolution of paradoxes can become fruitful.

It is plausible that there are limits to art determined by the limits of "natural" mediums, e.g., what we can see and hear.
But what are the limits of art with respect to society?
If a piece of art shows "facts" realistically, it indicates its flipside, its unmarked space, its contingency: reality could be different.
Therefore, we should be careful to judge the motionless dance, the toneless music, or the empty canvas.
These works of art rely on second-order observation and the re-entry.
But it is a risky business!
Whether these works are recognized as art is contingent.

The difference between medium and form can be driven into the improbable but only within the frame in which the communication of the form can succeed.
Art that heavily utilizes second-order observation seems to be the kind of art that tends to critique and to persue the channeling of attention for the sake of it.
In a Nietzschian sense, it *negates* and does not *affirm* (life).
Contemporary art wants to subvert standards and conformities to make what is absent visible---to break free, to dissolve;
Andy Warhol presents the mondane as artwork effectivly following the logic of the re-entry.
Communication about art, i.e., about what it is, becomes a work of art---it gets reintroduced into the system.
That is why contemporary art feels less real, because it is further and further away from physical mediums of perception (air, wood, ink).
Second-order evaluation is of course fueled by the fact that art is highly commodified.
Furthermore, the artist becomes increasingly the center of communication and he or she forms an identity in the mode of *profilicity*---curating a profile based on the evaluation by the *global village*.
Therefore, subversion becomes impossible.
What we get is a film like Barbie---the simulation of subversion.