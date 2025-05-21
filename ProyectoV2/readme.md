# Analizador Léxico y Generador de Código de Tres Direcciones

## Descripción
Este proyecto implementa un analizador léxico para un lenguaje de programación simple, con una interfaz gráfica de usuario que permite cargar, editar y analizar código fuente. El analizador identifica tokens como palabras reservadas, identificadores, operadores, números y otros elementos léxicos. Además, incluye un generador de código de tres direcciones para representaciones intermedias.

## Componentes Principales

### 1. tokens.py
Contiene la definición de todos los tokens reconocidos por el analizador léxico. Cada token está asociado con una expresión regular que define su patrón.

Tokens implementados:
- Palabras reservadas
- Números enteros y reales
- Operadores aritméticos (suma, resta, multiplicación, división)
- Operadores relacionales (<, >, <=, >=, !=, ==)
- Operadores lógicos (AND, OR, NOT)
- Símbolos de puntuación y agrupación
- Comillas y caracteres especiales

### 2. lexer.py
Implementa el analizador léxico y el generador de código de tres direcciones:

- **Clase Lexer**: Analiza una cadena de entrada y la convierte en una lista de tokens.
  - `__init__`: Inicializa el lexer con una cadena de entrada.
  - `lex()`: Procesa la cadena de entrada y genera la lista de tokens.

- **Clase CodigoTresDirecciones**: Genera código de tres direcciones a partir de una lista de tokens.
  - `generate_code()`: Convierte los tokens en representaciones de código de tres direcciones.
  - `write_code_to_file()`: Escribe el código generado en un archivo.

### 3. ProyectoV2.py
Implementa la interfaz gráfica de usuario para el analizador léxico:

- **Clase LexicalAnalyzerGUI**: Crea una interfaz donde los usuarios pueden:
  - Cargar archivos de código fuente
  - Editar código directamente en la aplicación
  - Ejecutar el análisis léxico
  - Visualizar los tokens identificados
  - Comparar con análisis de otros archivos

## Funcionalidades

1. **Análisis léxico**: Convierte el código fuente en tokens.
2. **Generación de código intermedio**: Crea representaciones de código de tres direcciones.
3. **Carga de archivos**: Permite cargar código desde archivos externos.
4. **Comparación de análisis**: Compara el análisis de diferentes códigos fuente.

## Uso

1. Ejecute `ProyectoV2.py` para iniciar la interfaz gráfica.
2. Escriba o cargue código fuente en el área de texto.
3. Haga clic en "Analizar léxicamente" para generar la lista de tokens.
4. Para comparar con otro archivo, utilice la función correspondiente después del análisis.

## Requisitos

- Python 3.x
- Tkinter (normalmente incluido en instalaciones estándar de Python)

## Ejemplo de entrada

```
begin
entero a;
a:=1;
if(a<10)
while(a<10)
a:=a+1;
endwhile;
else
while(a>0)
a:=a-1;
endwhile;
end;
end
```

## Características de la Interfaz

- Área de texto para edición de código
- Botones para leer archivos y analizar el código
- Tabla de visualización de tokens reconocidos
- Tabla para comparación de análisis con indicadores visuales de coincidencia
- Diseño limpio con estilos y colores para mejor legibilidad

## Extendiendo el Analizador

Para añadir soporte para nuevos tokens:
1. Agregue la definición del token al diccionario en `tokens.py`
2. Si es necesario, actualice la lógica de generación de código en `CodigoTresDirecciones`

## Notas
- Este proyecto fue desarrollado con fines educativos y puede ser mejorado o adaptado para otros propósitos.
- La funcionalidad actual se centra en el análisis léxico y no incluye análisis sintáctico o semántico completo.
