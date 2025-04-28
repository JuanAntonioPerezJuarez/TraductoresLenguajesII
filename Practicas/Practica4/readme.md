# Mathematical Expression Parser and Evaluator

This Python script (`practica4.py`) implements a mathematical expression parser and evaluator using recursive descent parsing techniques. It converts mathematical expressions into an abstract syntax tree (AST), then evaluates or displays them in different notations.

## Features

- Lexical analysis to tokenize mathematical expressions
- Syntax analysis to build an abstract syntax tree
- Support for basic operations: addition, subtraction, multiplication, and division
- Evaluation of expressions containing only numeric values
- Display of expressions in both infix and postfix notation
- Error handling for syntax errors and division by zero

## How It Works

The program consists of several components:

1. **Lexer**: Converts the input string into tokens using regular expressions
2. **Parser**: Implements a recursive descent parser to build an AST according to grammar rules
3. **Tree Nodes**: Represent operations and values in the AST
4. **Tree Traversal**: Functions to evaluate and display the AST

### Grammar Rules

The parser implements the following grammar:

```
E → T {(+ | -) T}
T → F {(* | /) F}
F → (E) | ID | NUM
```

Where:
- E represents an expression
- T represents a term
- F represents a factor
- ID represents an identifier (variable)
- NUM represents a number

## Usage

Run the script and enter a mathematical expression when prompted:

```
python practica4.py
```

### Example

Input:
```
Ingrese la expresión matemática: (5+3)*2-4/2
```

Output:
```
Expresión en notación postfija: 5 3 + 2 * 4 2 / -
Expresión en notación infija: ((5 + 3) * 2) - (4 / 2)
Resultado de la operación: 14.0
```

## Classes and Functions

### Classes

- `Nodo`: Represents an operation node in the AST (internal node)
- `Hoja`: Represents a leaf node (number or identifier)
- `Lexer`: Tokenizes the input expression
- `Parser`: Builds the AST based on grammar rules

### Functions

- `imprimir_postorden()`: Converts the AST to postfix notation
- `imprimir_infijo()`: Converts the AST to infix notation with parentheses
- `evaluar_arbol()`: Evaluates the expression tree (only works with numeric values)

## Limitations

- Cannot evaluate expressions containing variables (identifiers)
- Only supports basic arithmetic operations (+, -, *, /)
- No support for exponentiation or other advanced operations

## Error Handling

The script handles the following types of errors:

- Syntax errors (when the expression doesn't follow the grammar)
- Division by zero
- Attempt to evaluate an expression containing variables

## License

[Insert your license information here]
