class Parser:
    def __init__(self, expression):
        self.expression = expression
        self.index = 0

    def parse(self):
        self.index = 0
        try:
            result = self.lista()
            if self.index == len(self.expression):
                return "Cadena aceptada"
            else:
                raise SyntaxError("Expresión mal formada")
        except SyntaxError as e:
            return str(e)

    def lista(self):
        if self.index < len(self.expression) and self.expression[self.index].isdigit():
            self.index += 1  # Acepta un solo dígito
            self.resto_lista()
            return True
        else:
            raise SyntaxError("Se esperaba un dígito")

    def resto_lista(self):
        if self.index < len(self.expression) and self.expression[self.index] in ('+', '-'):
            self.index += 1  # Avanza sobre '+' o '-'
            if self.index < len(self.expression) and self.expression[self.index].isdigit():
                self.index += 1  # Acepta el dígito después del operador
                self.resto_lista()  # Llamada recursiva para más elementos
            else:
                raise SyntaxError("Se esperaba un dígito después de '+' o '-'")
        # Si no hay '+' o '-', se permite la cadena vacía (epsilon)
        return True

# Ejemplo de uso
if __name__ == "__main__":
    expression = input("Ingrese una lista de números con + o -: ")
    parser = Parser(expression.replace(" ", ""))  # Elimina espacios en blanco
    result = parser.parse()
    print(result)