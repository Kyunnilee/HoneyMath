# How HoneyMath is made

HoneyMath prompt was designed as a new Programming Language, GPT 4.o can understand.
I defined some new syntaxs for defining Functions/Classes/Variables.

# Functions/ Classes
### Definition of Functions/ Classes

Functions are defined by using square brackets `[ ]`. Functions can take parameters as input using `Args`.Here is a function definition template:

```
[~Function Name,Args:any_args_name]
    [INSTRUCTIONS]

        `INSTRUCTIONS` works like `__init__` in python class.
         It defines some nature of the functions/classes and execute automatically.

    [BEGIN]

        Code block start with `[BEGIN]` and end with `[END]`, just like C++ use {}.
        Code can be described by natural language or command/functions defined previously,or mix of them.

    [END]
```

### Call Functions/Class
To call functions, just functions/class use `execute <~Function Name>` or just `<~Function Name>`.
If function has any arg as input,you can call it like:

```
~function_name <args_name>
```

For example,

```
teach <topic>
```

Basically it is flexible about how to call a function. Just "telling" llm to call a function also works.

# Variables

### Definition
To define variables used in HoneyMath, just use `var`
```
var version = 1.0.0
```

or use a common talkable language

```
Level is "elementry" or  Level : "elementry"
```

You can also use variable to define a inline function, for example:

```
var random-number = <generate a random integer number>
```

### Referencing Variables
When calling or referencing a defined variable, you can write:

```
say "Hi! I am **HoneyMathGPT**, GPT specialized for generating math problems by python. My version is <version> made by Heekyung Lee."
```
