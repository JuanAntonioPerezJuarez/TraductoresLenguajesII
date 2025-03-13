# Analizador Sintáctico para Listas de Números

## Descripción
Este programa implementa un analizador sintáctico (parser) que valida expresiones matemáticas simples que consisten en dígitos separados por operadores '+' o '-'. El parser está construido utilizando el método de análisis sintáctico recursivo descendente.

## Gramática
El analizador valida expresiones que siguen esta gramática:
```
<lista> ::= <dígito> <resto_lista>
<resto_lista> ::= '+' <dígito> <resto_lista> | '-' <dígito> <resto_lista> | ε
```

Donde:
- `<lista>` representa una lista de números
- `<dígito>` representa un solo dígito (0-9)
- `<resto_lista>` representa el resto de la lista después del primer dígito
- `ε` (epsilon) representa una cadena vacía

## Requisitos
- Python 3.x

## Uso
1. Ejecuta el archivo `practica1.py`
2. Ingresa una expresión cuando se te solicite
3. El programa mostrará si la expresión es válida o no

```bash
python practica1.py
```

## Ejemplos válidos
- `1+2+3`
- `5-7+9`
- `8`
- `2+3-4+5-6`

## Ejemplos inválidos
- `+1+2` (debe comenzar con un dígito)
- `1+` (operador sin dígito siguiente)
- `1++2` (operadores consecutivos)
- `1+a` (caracteres no permitidos)

## Estructura del código
- `Parser`: Clase principal que maneja el análisis sintáctico
  - `__init__`: Inicializa el parser con una expresión
  - `parse`: Método principal que inicia el análisis
  - `lista`: Maneja la regla de producción para `<lista>`
  - `resto_lista`: Maneja la regla de producción para `<resto_lista>`

## Limitaciones
- El parser solo acepta dígitos individuales (0-9), no números de múltiples dígitos
- Solo soporta los operadores '+' y '-'
