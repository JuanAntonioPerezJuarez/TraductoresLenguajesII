# Analizador y Evaluador de Expresiones Matemáticas

Este script de Python (`practica4.py`) implementa un analizador y evaluador de expresiones matemáticas utilizando técnicas de análisis sintáctico descendente recursivo. Convierte expresiones matemáticas en un árbol de sintaxis abstracta (AST), y luego las evalúa o muestra en diferentes notaciones.

## Características

- Análisis léxico para tokenizar expresiones matemáticas
- Análisis sintáctico para construir un árbol de sintaxis abstracta
- Soporte para operaciones básicas: suma, resta, multiplicación y división
- Evaluación de expresiones que contienen únicamente valores numéricos
- Visualización de expresiones en notación infija y postfija
- Manejo de errores para errores de sintaxis y división por cero

## Cómo Funciona

El programa consta de varios componentes:

1. **Lexer**: Convierte la cadena de entrada en tokens utilizando expresiones regulares
2. **Parser**: Implementa un analizador descendente recursivo para construir un AST según reglas gramaticales
3. **Nodos del Árbol**: Representan operaciones y valores en el AST
4. **Recorrido del Árbol**: Funciones para evaluar y mostrar el AST

### Reglas Gramaticales

El analizador implementa la siguiente gramática:

```
E → T {(+ | -) T}
T → F {(* | /) F}
F → (E) | ID | NUM
```

Donde:
- E representa una expresión
- T representa un término
- F representa un factor
- ID representa un identificador (variable)
- NUM representa un número

## Uso

Ejecute el script e ingrese una expresión matemática cuando se le solicite:

```
python practica4.py
```

### Ejemplo

Entrada:
```
Ingrese la expresión matemática: (5+3)*2-4/2
```

Salida:
```
Expresión en notación postfija: 5 3 + 2 * 4 2 / -
Expresión en notación infija: ((5 + 3) * 2) - (4 / 2)
Resultado de la operación: 14.0
```

## Clases y Funciones

### Clases

- `Nodo`: Representa un nodo de operación en el AST (nodo interno)
- `Hoja`: Representa un nodo hoja (número o identificador)
- `Lexer`: Tokeniza la expresión de entrada
- `Parser`: Construye el AST basado en reglas gramaticales

### Funciones

- `imprimir_postorden()`: Convierte el AST a notación postfija
- `imprimir_infijo()`: Convierte el AST a notación infija con paréntesis
- `evaluar_arbol()`: Evalúa el árbol de expresión (solo funciona con valores numéricos)

## Limitaciones

- No puede evaluar expresiones que contienen variables (identificadores)
- Solo soporta operaciones aritméticas básicas (+, -, *, /)
- No hay soporte para exponenciación u otras operaciones avanzadas

## Manejo de Errores

El script maneja los siguientes tipos de errores:

- Errores de sintaxis (cuando la expresión no sigue la gramática)
- División por cero
- Intento de evaluar una expresión que contiene variables

## Licencia

[Inserte su información de licencia aquí]
