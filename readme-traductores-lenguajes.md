# Traductores de Lenguajes II

## Información General del Curso

- **Clave:** I7027
- **Modalidad:** Escolarizada
- **Tipo:** Curso
- **Área de formación:** Básica particular
- **Créditos:** 8

## Prerrequisitos
- Teoría de la Computación (I5802)
- Traductores de Lenguajes I (I7025)

## Descripción del Curso
En esta asignatura se desarrolla un compilador completo, incluyendo análisis léxico, análisis sintáctico, análisis semántico, optimización y generación de código objeto. El curso está diseñado para proveer a los estudiantes las herramientas, conocimientos y habilidades necesarias para el desarrollo de compiladores, basándose en los conocimientos previos de Teoría de la Computación.

## Objetivos
- Definir, diseñar, construir y programar las fases de un traductor o compilador
- Implementar técnicas de análisis léxico, sintáctico y semántico
- Generar código intermedio y código objeto
- Aplicar técnicas de optimización de código

## Contenido Temático

### 1. Análisis Léxico
- Funciones del analizador léxico
- Componentes léxicos, patrones y lexemas
- Creación de tabla de tokens
- Errores léxicos
- Generadores de analizadores léxicos
- Aplicaciones (caso de estudio)

### 2. Análisis Sintáctico
- Introducción y función del analizador sintáctico
- Gramáticas libres de contexto
- Análisis sintáctico descendente mediante método recursivo
- Análisis sintáctico descendente mediante método no recursivo
- Análisis sintáctico ascendente
- Gramáticas ambiguas
- Definiciones dirigidas por sintaxis

### 3. Definición Dirigida por Sintaxis
- Gramáticas con atributos
- Construcción de árboles sintácticos
  - Implementación con programación orientada a objetos
  - Construcción durante análisis sintáctico descendente y ascendente

### 4. Análisis Semántico
- Comprobación de tipos
  - Expresiones de tipos
  - Sistema de tipos
  - Conversión de tipos
  - Comprobación estática y dinámica
- Tabla de símbolos
  - Estructura
  - Declaraciones de variables, procedimientos y funciones
  - Reglas de ámbito y estructuras de bloques

### 5. Generación de Código Intermedio
- Código de tres direcciones
  - Traducción de expresiones
  - Traducción de referencias a arreglos
  - Traducción de expresiones lógicas
  - Código de corto circuito
  - Instrucciones para control de flujo
  - Procedimientos

### 6. Generación de Código Objeto
- Introducción a la máquina objeto
- Código ensamblador
  - Asignación de valores
  - Expresiones aritméticas
  - Control de flujo
  - Procedimientos y funciones
- Generación de código objeto a partir de árboles sintácticos

### 7. Optimización
- Optimización de mirilla
  - Eliminación de instrucciones redundantes
  - Eliminación de código inalcanzable
  - Optimizaciones de flujo de control
  - Simplificación algebraica y reducción por fuerza
- Generación de código óptimo para expresiones
  - Números de Ershov
  - Generación de código a partir de árboles de expresión etiquetados

## Evaluación
- Exámenes parciales: 20%
- Entrega de Análisis Léxico: 20%
- Entrega de Análisis Sintáctico: 20%
- Entrega de Análisis Semántico: 20%
- Entrega de Generación de Código: 20%

## Referencias Bibliográficas

### Básicas
- Aho, A.V.; Lam, M.S.; Sethi, R.; Ullman (2007). *Compilers: principles, techniques, and tools*. Addison-Wesley. ISBN: 9780321491695
- Parr, T. (2012). *The definitive ANTLR 4 reference*. The Pragmatic Programmers.
- Cortadella, J. (2015). *Compilers lecture notes*

### Complementarias
- Appel, A.W.; Ginsburg, M. (2004). *Modern compiler implementation in C*. Cambridge University Press. ISBN: 0521607655
- Appel, A.W.; Palsberg, J. (2002). *Modern compiler implementation in Java*. Cambridge University Press. ISBN: 052182060X

## Material de Apoyo
- Videos relacionados al temario disponibles en los enlaces proporcionados en el programa

## Requisitos de Acreditación
- Calificación mínima de 60
- Asistencia mínima del 80% a clases y actividades
