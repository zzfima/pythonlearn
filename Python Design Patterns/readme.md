- Creational Patterns, Polymorphism is often used.
- Structural Patterns take advantage of Inheritance a lot.
- Behavioral Patterns heavily use methods and their signatures.
- Interfaces are used across all these different types of design patterns.

### Understanding Pattern context
To use design patterns effectively, you need to know the context in which 
the design patterns work best. It is also important to know what is used to describe 
the design pattern context. A pattern context consists of the following: 
participants, quality attributes, forces, and consequences. 
- Participants refer to the classes involved to form a design pattern. These classes 
involved in the design pattern, they play a different roles to accomplish the goals of the design pattern. 
- Quality attributes refer to these nonfunctional requirements such as usability, 
modifiability, reliability, performance, and so on. Quality attributes have an impact 
on the entire software, and these quality attributes are typically addressed only by 
the architectural solutions. 
- Forces are various factors or trade-offs you consider when you're 
trying to adopt a particular design pattern. These forces are typically 
manifested in quality attributes such as modifiability, usability, reliability, 
performance, etc. If you don't reason about these forces very well you may end up 
facing some unintended consequences. 
- And these consequences could be side effects such as worse performance when you're trying to use 
one of the design patterns to accomplish better security. The ultimate responsibility 
really falls on the decision makers who will be choosing a particular design pattern 
despite the consequences. 

Knowing when to use a design pattern and when not to use it, 
is crucial, especially because the design patterns can cause more problems instead of solving 
problems when they're misused.

A Pattern Language consists of name, context, problem, solution, and related patterns.

- The names of patterns should capture the gist of the pattern, and these names 
become an essential part of a vocabulary during the design process. Therefore, they need 
to be especially meaningful and memorable. 
- The context provides a scenario in which these patterns may be used. The context also 
provides more insights on when to use the pattern and when not to use the pattern. 
- The problem part of the pattern description describes a design challenge the 
pattern is trying to address. 
- And the solution part of the pattern description specifies the pattern itself. The patterns are 
specified in terms of their structures and behaviors. The structure in this case specifies 
the relationships in between the elements used in the pattern. The behaviors specify 
all the interactions in between these elements used in the pattern. 
- The last part of the pattern language is the related patterns. These lists other 
patterns used together with the pattern being described, or similar but different patterns.
It is important in these related patterns sections of the pattern descriptions, 
to describe exactly what these subtle differences in between the patterns being described.
This sums up a typical pattern language. In fact, this is the pattern language we'll be using to 
describe the patterns in this course. 
- In addition, once you get the handle of the pattern language, you should be able to define 
your own pattern if necessary.