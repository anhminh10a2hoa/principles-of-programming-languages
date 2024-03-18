# Document for Phase 2

This is the attachment document to be submitted for phase 2 of course project.

To run any code:

```
python3 main.py -f FILENAME
```

# Syntax Analysis and PostHaste Language

## 1. What is syntax analysis and how is it related to other parts in compilation?

Syntax analysis, also known as parsing, is the process of analyzing the structure of a sequence of tokens to determine if it conforms to the grammar rules of a language. It checks the arrangement of tokens to ensure they form valid expressions or statements according to the language syntax. Syntax analysis is a crucial step in compilation as it precedes semantic analysis and code generation. It ensures that the code is syntactically correct before further processing.

## 2. How is the syntactic structure of the language expressed in the PLY tool?

In the PLY tool, the syntactic structure of the language is expressed using parser rules defined in BNF (Backus-Naur Form) notation. These rules define the grammar of the language, specifying how different language constructs can be formed from tokens. Each parser rule corresponds to a syntactic rule of the language, and the relationships between these rules define the overall structure of the language.

## 3. Explain in English what the syntax of the following elements mean:

- **The do-unless statement:** This statement in PostHaste language represents a loop structure that executes a block of statements until a specified condition becomes true. It continues to execute the block unless the condition evaluates to true. Optionally, an 'otherwise' block can be provided to execute when the condition becomes true.
- **Procedure call:** It refers to invoking a procedure (or function) by its name along with the required arguments (if any). This allows executing the code defined within the procedure at the point of the call.

## 4. There are three BNF constructs in the syntax that begin with the keyword “do”. How do they differ from each other?

- The `do_until_statement` executes a block of statements repeatedly until a specified condition becomes true.
- The `do_unless_statement` executes a block of statements repeatedly unless a specified condition becomes true.
- The `do_statement` is not explicitly defined in the given code, but typically it would represent a generic loop structure without any specific condition.

## 5. Is it possible to define a “nested” function, i.e., to define a new function inside another function? Why or why not?

No, it's not possible to define nested functions in the PostHaste language as per the provided syntax rules. This limitation is due to the absence of syntax rules for defining functions within other functions.

## 6. How should the PostHaste BNF be changed if we wanted to use semicolons at the end of each statement instead of commas separating statements?

To use semicolons at the end of each statement, the BNF for `statement_list` should be modified to include semicolons as terminators instead of commas. For example:

```python
statement_list : statement SEMICOLON
               | statement_list statement SEMICOLON
```

## 7. Would it be possible to find out the year of date returned from a function in the similar fashion (today()'year)? Why or why not?

No, it wouldn't be possible because the syntax rules do not support accessing attributes or properties of values returned from functions in PostHaste. The language syntax only allows accessing attributes of variables with an apostrophe.

## 8. Is the following allowed by the syntax: 3---2? What about xx---yy? Why or why not?

Neither `3---2` nor `xx---yy` are allowed by the syntax. The syntax analyzer would notice the error in the `expression` rule where it expects a valid expression but encounters an unexpected token (`MINUS`). The syntax rules do not define such expressions with multiple consecutive arithmetic operators.

## 9. Can a procedure call appear inside a function definition? Explain why you ended up with the answer you gave.

Yes, a procedure call can appear inside a function definition in PostHaste language. The function definition allows for executing statements, and procedure calls are valid statements within the language syntax. However, the execution of the procedure call would depend on the control flow of the function.

## 10. In which parts of a program can the “unless expression” `do 1 unless xx<2 otherwise 2 done` appear?

The "unless expression" `do 1 unless xx<2 otherwise 2 done` can appear in places where a statement or a block of statements is expected. This includes places such as within loops (`do_until_statement`, `do_unless_statement`), as part of conditional statements (`if` statements), or as standalone statements within a program.

## 11. How does the syntax figure out which one of these is meant in each case when the equals sign = is used for initializing a variable, doing an assignment, and comparing values?

The syntax determines the meaning of the equals sign based on the context in which it is used. If the equals sign is used in a variable definition (`variable_definition`), it is interpreted as initializing a variable. If it appears within an assignment statement (`assignment`), it signifies assigning a value to a variable. In comparison expressions (`expression`), the equals sign is interpreted as a comparison operator. The syntax analyzer distinguishes between these contexts based on the syntactic rules and the surrounding grammar.

# Author

Minh Hoang - minh.hoang@tuni.fi