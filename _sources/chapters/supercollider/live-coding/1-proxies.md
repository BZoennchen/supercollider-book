# Proxies

A [Synth](sec-synths) in [SuperCollider](https://supercollider.github.io/) consists of a network of [UGens](sec-ugens) whose shape cannot be changed once it has started playing. 
Although this makes for a very efficient design, it limits interactivity.
The [Just In Time programming library (JITLib)](https://doc.sccode.org/Overviews/JITLib.html) {cite}`campo:2005,rohrhuber:2009,wilson:2011` attempts to overcome this limitation by introducing proxies, abstract placeholders which allow seamlessly switching between different audio graph definitions. 
When a new Synth definition is assigned to the proxy, the previous synth is stopped and a new one starts, usually using a cross-fade.
This allows the use of dynamic modification and interconnection of proxies.

```{admonition} Proxy
:name: def-proxy
:class: definition
A *proxy* is a placeholder that is used to operate on something that does not yet exist.
```

In a live programming environment, we often want to use something before it is there, e.g., to set up our setting in a non-linear way.
For this reason, the JITLib of SuperCollider offers us different ways to define proxies.

For example, an *OutputProxy* is used to represent multiple outputs of a UGen, even if only one UGen is created eventually.
Proxies can be redefined, making them highly flexible and dynamic.
They can refer to functions, patterns, or tasks and work at either audio ``ar`` or control ``kr`` rate.

There are three types of proxies:

1. for tasks: [TaskProxy](https://doc.sccode.org/Classes/TaskProxy.html), [Tdef](https://doc.sccode.org/Classes/Tdef.html)
2. for synths: [NodeProxy](https://doc.sccode.org/Classes/NodeProxy.html), [Ndef](https://doc.sccode.org/Classes/Ndef.html), [ProxySpace](https://doc.sccode.org/Classes/ProxySpace.html)
3. for patterns:  [PatternProxy](https://doc.sccode.org/Classes/PatternProxy.html), [PbindProxy](https://doc.sccode.org/Classes/PbindProxy.html),  [Pdef](https://doc.sccode.org/Classes/Pdef.html), [Pdefn](https://doc.sccode.org/Classes/Pdefn.html), [Pbindef](https://doc.sccode.org/Classes/Pbindef.html), [Psym](https://doc.sccode.org/Classes/Psym.html), [Pnsym](https://doc.sccode.org/Classes/Pnsym.html), [Fdef](https://doc.sccode.org/Classes/Fdef.html), [Pdict](https://doc.sccode.org/Classes/Pdict.html)

In section [Pattern](sec-playing-pattern), we already discussed some of these pattern proxies without calling them by this term.
Wihtin one type these different classes are semantically interchangeable but translate to different programming styles.

```{admonition} Client and Server Side Proxies
:name: attention-proxy-client-server-side
:class: attention
Pattern and task proxies operate client side.
Synth proxies, i.e. nodes, operate server side.
```

## Definition Classes

Definition-classes, such as [Pdef](https://doc.sccode.org/Classes/Pdef.html), [Tdef](https://doc.sccode.org/Classes/Tdef.html) and [Ndef](https://doc.sccode.org/Classes/Ndef.html), bind a symbol to an object in a specific way:

```isc
Pdef(\name)         // returns the proxy
Pdef(\name, object) // sets the source and returns the proxy
```

## Environments

Another way, for server side node proxies, is an environment that returns placeholders on demand.
[Environments](https://doc.sccode.org/Classes/Environment.html) manage namespaces, e.g. 

```isc
~a = 4
```

is equivalent to

```isc
currentEnvironment.put(\a, 4)
```

The default ``currentEnvironment`` provides us with client side variables.
Using 

```isc
ProxySpace.push(s) // s is a audio server
```

exchanges this client side 'variable' environment with a server side environment holding [NodeProxies](https://doc.sccode.org/Classes/NodeProxy.html).
As a consequent 

```isc
~a = {SinOsc.ar(244!2) * 0.5;}
```

is no longer a standard ``sclang`` variable but a node proxy on the server!

## Lower Level Proxies

We can also create our own low-level proxy object using [TaskProxy](https://doc.sccode.org/Classes/TaskProxy.html), [PatternProxy](https://doc.sccode.org/Classes/PatternProxy.html) or [NodeProxy](https://doc.sccode.org/Classes/NodeProxy.html) respectively.
