# Proxies

[SuperCollider](https://supercollider.github.io/) supports live programming via its powerful [Just In Time programming library (JITLib)](https://doc.sccode.org/Overviews/JITLib.html).
It allows the use of dynamic modification and interconnection of proxies.

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

Definition-classes, such as ``Pdef``, ``Tdef`` and ``Ndef``, bind a symbol to an object in a specific way:

```isc
Pdef(\name)         // returns the proxy
Pdef(\name, object) // sets the source and returns the proxy
```

## Environments

Another way, for server side node proxies, is an environment that returns placeholders on demand.
``Environments`` manage namespaces, e.g. 

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

We can also create our own low-level proxy object using ``TaskProxy``, ``PatternProxy`` or ``NodeProxy`` respectively.
