# Document for Phase 1

This is the attachment document to be submitted for phase 1 of course project.
The unittest can be run in this directory with

```
python3 lexer_test.py
```

To run any code:

```
python3 main.py -f FILENAME
```

## 1. Lexical analysis

Lexical analysis is the initial phase of the compilation process, where the source code is analyzed to generate tokens. This process involves scanning the input text and converting it into a sequence of tokens representing the language's syntactic elements. The lexer, implemented in the `lexer.py` file, performs this task by recognizing patterns defined in regular expressions and categorizing them into different token types. Lexical analysis is crucial as it provides the foundation for subsequent compilation phases to operate on.

## 2. Lexical structure in PLY

### Defining tokens

In PLY, the lexical structure of the language is expressed through the definition of tokens using regular expressions. In the `lexer.py` file, the `tokens` variable is a list of token names, defined as module-level variables. Each token is associated with a regular expression pattern, prefixed with `t_`, specifying how it should be recognized in the input text. Additionally, special tokens like `t_ignore` are defined to specify characters that should be ignored by the lexer, such as whitespace and comments.

### Defining keywords

Reserved keywords, such as language-specific keywords with special meanings, are defined as tokens using a dictionary named `reserved` in `lexer.py`. The keys of this dictionary represent the reserved keywords, and the values correspond to their token names. Keywords are validated by checking if the token value matches any key in the `reserved` dictionary, and if so, the token type is updated accordingly.


### PLY Processing

The `ply.lex.lex()` function initializes the lexer, while the `input()` function feeds input text to the lexer. The lexer iterates through the input text, tokenizing it based on the defined patterns, and generates `LexToken` objects representing each token. These tokens consist of a `type` attribute identifying the token type and a `value` attribute containing the token's value.

## 3. Code Explanation

### a. Keywords

Keywords are defined in `lexer.py` as a dictionary named `reserved`, where keys are reserved words, and values are their corresponding token names. During tokenization, the lexer checks if the token value matches any key in the `reserved` dictionary. If a match is found, the token type is updated to the corresponding keyword token type.

```
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    # Add more keywords as needed
}
```

### b. Comments

Comments are defined in `lexer.py` using a regular expression pattern prefixed with `t_ignore_`, indicating that they should be ignored by the lexer. The pattern matches any text between `#` symbols, allowing for single-line comments in the input text.

```
t_ignore_COMMENT = r'\#.*'
```

### c. Whitespaces

Whitespace characters, such as spaces and tabs, are ignored by the lexer using the `t_ignore` token. The regular expression pattern matches whitespace characters, instructing the lexer to skip over them during tokenization.

```
t_ignore = ' \t'
```

### d. Operators & delimiters

Operators and delimiters, such as `+`, `-`, `=`, and parentheses, are defined as tokens in `lexer.py` using regular expression patterns. Each pattern specifies the corresponding operator or delimiter symbol, allowing the lexer to tokenize them accordingly.

```
t_PLUS = r'\+'
t_MINUS = r'-'
# Define other operators and delimiters
```

### e. Decimal literals

Decimal literals are recognized by the lexer using a regular expression pattern in `lexer.py`. The pattern matches decimal numbers, including both integer and fractional parts, allowing for the recognition of decimal literals in the input text.

```
t_DECIMAL = r'-?\d+\.\d+'
```

### f. String literals

String literals are recognized in `lexer.py` using regular expression patterns that match text enclosed in single or double quotation marks. The lexer distinguishes string literals based on these patterns and tokenizes them accordingly.

```
t_STRING = r'\".*?\"'
```

### g. Function names

Function names are defined as tokens in `lexer.py` using regular expression patterns. The patterns match valid function name syntax, allowing the lexer to tokenize function names appropriately.

```
t_FUNCTION = r'[a-zA-Z_][a-zA-Z0-9_]*'
```

## 4. Distinguishing elements

### a. Function & variable names

Function names and variable names are distinguished by their lexical structure. Function names typically start with lowercase letters followed by alphanumeric characters or underscores, while variable names follow a similar pattern but may start with uppercase letters. This distinction is enforced by the regular expression patterns used to recognize function and variable names in the lexer.

### b. Keywords & variable names

Keywords and variable names are distinguished during tokenization by checking if the token value matches any reserved keyword in the `reserved` dictionary. If a match is found, the token type is updated to the corresponding keyword token type. Otherwise, the token is classified as a variable name based on its lexical structure.

### c. Operators > and >=

The `>` and `>=` operators are distinguished by their distinct regular expression patterns in `lexer.py`. These patterns specify the exact symbols corresponding to each operator, allowing the lexer to tokenize them appropriately.

### d. String literals and variable names

String literals and variable names are distinguished based on their lexical structure and syntax. String literals are recognized by their enclosing quotation marks and are tokenized accordingly. Variable names follow specific naming conventions, such as starting with lowercase letters, which allows the lexer to differentiate them from string literals during tokenization.

### e. Comments and other code

Comments are distinguished from other code elements by their lexical structure and the regular expression pattern used to define them in `lexer.py`. The pattern matches comment syntax, allowing the lexer to ignore comments during tokenization and focus on tokenizing other code elements.


## 5. My thought

The implementation of the lexer using PLY in `lexer.py` demonstrates a clear understanding of lexical analysis concepts and tokenization. The code follows the conventions and guidelines provided by PLY for defining tokens and patterns, resulting in a robust lexer capable of tokenizing input text effectively. The use of regular expressions simplifies the process of pattern matching and tokenization, making the lexer concise and efficient.

Overall, the assignment provided valuable experience in implementing lexical analysis using PLY and reinforced the importance of proper tokenization in the compilation process. It was relatively straightforward to define tokens and patterns in PLY, although ensuring proper distinction between elements required careful consideration of lexical structure and syntax. Through this assignment, I gained a deeper understanding of how lexical analysis serves as the foundation for subsequent compilation phases and learned practical skills in implementing a lexer using PLY.

## 6. Author

Minh Hoang - minh.hoang@tuni.fi