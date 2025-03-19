class Parser:
    def __init__(self, expression):
        self.expression = expression.replace(" ", "")  # Eliminamos espacios
        self.index = 0
        
    def parse(self):
        self.index = 0
        try:
            result = self.expr()
            if self.index == len(self.expression):
                return "Notación postfija: " + result
            else:
                raise SyntaxError("Expresión mal formada: caracteres no procesados al final")
        except SyntaxError as e:
            return str(e)
            
    def expr(self):
        """
        Maneja las expresiones con + y -
        expr -> term { ('+' | '-') term }
        """
        left = self.term()
        
        while self.index < len(self.expression) and self.expression[self.index] in ('+', '-'):
            op = self.expression[self.index]
            self.index += 1
            right = self.term()
            # Construimos la notación postfija: primero operandos, luego operador
            left = left + " " + right + " " + op
            
        return left
        
    def term(self):
        """
        Maneja las expresiones con * y /
        term -> factor { ('*' | '/') factor }
        """
        left = self.factor()
        
        while self.index < len(self.expression) and self.expression[self.index] in ('*', '/'):
            op = self.expression[self.index]
            self.index += 1
            right = self.factor()
            # Construimos la notación postfija: primero operandos, luego operador
            left = left + " " + right + " " + op
            
        return left
        
    def factor(self):
        """
        factor -> '(' expr ')' | number
        """
        if self.index < len(self.expression) and self.expression[self.index] == '(':
            self.index += 1
            result = self.expr()
            if self.index < len(self.expression) and self.expression[self.index] == ')':
                self.index += 1
                return result
            else:
                raise SyntaxError("Falta cerrar paréntesis")
        elif self.index < len(self.expression) and self.expression[self.index].isdigit():
            return self.number()
        else:
            raise SyntaxError("Número o paréntesis esperado")
            
    def number(self):
        """
        Procesa números enteros
        number -> digit { digit }
        """
        num = ''
        while self.index < len(self.expression) and self.expression[self.index].isdigit():
            num += self.expression[self.index]
            self.index += 1
        return num
        
# Ejemplo de uso
if __name__ == "__main__":
    expression = input("Ingrese una expresión matemática: ")
    parser = Parser(expression)
    result = parser.parse()
    print(result)