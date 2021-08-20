(sec-distributions)=
# Random distributions

In SuperCollider there are many build-in sampling functions.
On the client side we can use those while on the server side, that is, within a ``SynthDef`` we have to use the respective ``UGen`` counterpart.
For example,

```isc
(
var lo = 3.0, hi = 7.0;
hi.rand + lo;
)
```

on the client side (**sc-lang**) translates to

```isc
var lo = 3.0, hi = 7.0;
Rand(lo, hi);
```

within a ``SynthDef``.

The following build-in sampling functions can be used, where the receiver ``x`` is a number:

+ ``coin(x)``: returns ``true`` with the probability of ``x`` and ``false`` with the probability ``x-1``.
+ ``rand(x)``: uniformly distributed number from ``0`` up to ``x`` (exclusive).
+ ``rand2(x)``: uniformly distributed number from ``-x`` up to ``x``.
+ ``rrand(a, b)``: a random number in the interval ]``a``, ``b``[.
+ ``linrand(x)``: a linearly distributed random number from zero to ``x``.
+ ``bilinrand(x)``: a bilateral linearly distributed random number from ``-x`` to ``x``.
+ ``sum3rand(x)``: a random number from ``-x`` to ``x`` is the result of summing three uniform random generators to yield a bell-like distribution.
+ ``gauss(x, sigma)``: a gaussian distributed random number with the standard deviation ``sigma``.
+ ``exprand(a, b)``: an exponentially distributed random number in the interval ]``a``, ``b``[.

I added the class method ``histrogram`` to the ``Utils`` class

```isc
*histogram {
		arg values, steps = 500;
		var histogram;
		histogram = values.histo(steps: steps).normalizeSum;
		^histogram;
	}
```

so that we can plot the distribution to get some intuition. {numref}`Figure {number} <fig-plot-dists>` shows the results of the following code:

```isc
(
Utils.histogram( values: {rand(4.0)}!1000000, steps: 100 ).plot(name: "uniform");
Utils.histogram( values: {linrand(4.0)}!1000000, steps: 100 ).plot(name: "linear");
Utils.histogram( values: {bilinrand(4.0)}!1000000, steps: 100 ).plot(name: "bilinear");
Utils.histogram( values: {sum3rand(4.0)}!1000000, steps: 100 ).plot(name: "pseudo gauss");
Utils.histogram( values: {gauss(0.0, standardDeviation: 1.0)}!1000000, steps: 100 ).plot(name: "gauss");
Utils.histogram( values: {exprand(4.0, 0.5)}!1000000, steps: 100 ).plot(name: "exp");
)
```

```{figure} ../../figs/plot-dists.png
---
width: 800px
name: fig-plot-dists
---
Plot of a histogram of ``rand(x)``, ``linrand(x)``, ``exprand(a, b)``, ``bilinrand(x)``, ``sum3rand(x)``, ``gauss(x, sigma)``.
```

The corresponding ``UGen``s are called:

+ ``Rand``,
+ ``LinRand``, and
+ ``ExpRand``.
