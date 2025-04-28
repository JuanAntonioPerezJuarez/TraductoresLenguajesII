import re

class Nodo:
    def __init__(self, operacion, izquierda=None, derecha=None):
        self.operacion = operacion
        self.izquierda = izquierda
        self.derecha = derecha

class Hoja:
    def __init__(self, tipo, valor):
        self.tipo = tipo  # Puede ser "id" o "num"
        self.valor = valor

# Analizador Léxico
class Lexer:
    def __init__(self, input_text):
        self.tokens = []
        self.index = 0
        self.input_text = input_text
        self.tokenize()

    def tokenize(self):
        patterns = [
            ('NUM', r'\d+'),
            ('ID', r'[a-zA-Z][a-zA-Z0-9]*'),
            ('PLUS', r'\+'),
            ('MINUS', r'-'),
            ('MUL', r'\*'),
            ('DIV', r'/'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('WHITESPACE', r'\s+'),
        ]
        combined_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in patterns)
        regex = re.compile(combined_pattern)
        for match in regex.finditer(self.input_text):
            kind = match.lastgroup
            value = match.group()
            if kind != 'WHITESPACE':
                self.tokens.append((kind, value))

    def next_token(self):
        if self.index < len(self.tokens):
            tok = self.tokens[self.index]
            self.index += 1
            return tok
        else:
            return ('EOF', 'EOF')

    def peek_token(self):
        if self.index < len(self.tokens):
            return self.tokens[self.index]
        else:
            return ('EOF', 'EOF')

# Analizador Sintáctico
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.token = self.lexer.next_token()

    def eat(self, token_type):
        if self.token[0] == token_type:
            self.token = self.lexer.next_token()
        else:
            raise SyntaxError(f"Se esperaba {token_type}, pero se encontró {self.token}")

    def parse(self):
        nodo = self.E()
        if self.token[0] != 'EOF':
            raise SyntaxError("Cadena extra después de la expresión válida")
        return nodo

    def E(self):
        nodo = self.T()
        while self.token[0] in ('PLUS', 'MINUS'):
            if self.token[0] == 'PLUS':
                self.eat('PLUS')
                nodo = Nodo('+', nodo, self.T())
            elif self.token[0] == 'MINUS':
                self.eat('MINUS')
                nodo = Nodo('-', nodo, self.T())
        return nodo

    def T(self):
        nodo = self.F()
        while self.token[0] in ('MUL', 'DIV'):
            if self.token[0] == 'MUL':
                self.eat('MUL')
                nodo = Nodo('*', nodo, self.F())
            elif self.token[0] == 'DIV':
                self.eat('DIV')
                nodo = Nodo('/', nodo, self.F())
        return nodo

    def F(self):
        if self.token[0] == 'LPAREN':
            self.eat('LPAREN')
            nodo = self.E()
            self.eat('RPAREN')
            return nodo
        elif self.token[0] == 'ID':
            value = self.token[1]
            self.eat('ID')
            return Hoja('id', value)
        elif self.token[0] == 'NUM':
            value = self.token[1]
            self.eat('NUM')
            return Hoja('num', value)
        else:
            raise SyntaxError("Se esperaba ( o identificador o número")

# Funciones auxiliares para recorrer el árbol
def imprimir_postorden(nodo):
    if isinstance(nodo, Hoja):
        return f"{nodo.valor}"
    else:
        return f"{imprimir_postorden(nodo.izquierda)} {imprimir_postorden(nodo.derecha)} {nodo.operacion}"

def imprimir_infijo(nodo):
    if isinstance(nodo, Hoja):
        return f"{nodo.valor}"
    else:
        return f"({imprimir_infijo(nodo.izquierda)} {nodo.operacion} {imprimir_infijo(nodo.derecha)})"

def evaluar_arbol(nodo):
    if isinstance(nodo, Hoja):
        if nodo.tipo == 'num':
            return int(nodo.valor)
        else:
            raise ValueError("No se puede evaluar un identificador")
    else:
        izquierda = evaluar_arbol(nodo.izquierda)
        derecha = evaluar_arbol(nodo.derecha)
        if nodo.operacion == '+':
            return izquierda + derecha
        elif nodo.operacion == '-':
            return izquierda - derecha
        elif nodo.operacion == '*':
            return izquierda * derecha
        elif nodo.operacion == '/':
            if derecha == 0:
                raise ZeroDivisionError("División entre cero")
            return izquierda / derecha

# Ejemplo de uso
if __name__ == "__main__":
    entrada = input("Ingrese la expresión matemática: ")
    lexer = Lexer(entrada)
    parser = Parser(lexer)

    try:
        arbol = parser.parse()
        print("Expresión en notación postfija:", imprimir_postorden(arbol))
        print("Expresión en notación infija:", imprimir_infijo(arbol))
        resultado = evaluar_arbol(arbol)
        print("Resultado de la operación:", resultado)
    except SyntaxError as e:
        print("Error de sintaxis:", e)
    except ValueError as e:
        print("Error de evaluación:", e)
    except ZeroDivisionError as e:
        print("Error de evaluación:", e)