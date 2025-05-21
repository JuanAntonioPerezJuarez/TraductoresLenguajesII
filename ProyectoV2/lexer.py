#lexer.py
import re
from tokens import tokens # Asegúrate de que se importa correctamente el diccionario de tokens

class Lexer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.pos = 0
        self.token_list = []

    def lex(self):
        while self.pos < len(self.input_string):
            match = None
            for token, pattern in tokens.items():
                regex = re.compile(pattern)
                match = regex.match(self.input_string, self.pos)
                if match:
                    value = match.group(0)
                    if token != 'SALTO LINEA':
                        self.token_list.append((token, value))
                    self.pos = match.end()
                    break

            if not match:
                print("Error: Caracter no reconocido -", self.input_string[self.pos])
                self.pos += 1
        return self.token_list
    
class CodigoTresDirecciones:
    def __init__(self, tokens):
        self.tokens = tokens
        self.temp_count = 1
        self.code = []

    def generate_code(self):
        for token, value in self.tokens:
            if token == 'Palabra reservada':
                self.code.append(f"t{self.temp_count} = {value}")
                self.temp_count += 1
            elif token == 'ASIGNACION':
                self.code.append(f"{value} = t{self.temp_count - 1}")
            elif token == 'ENTERO' or token == 'REAL' or token == 'Comillas':
                self.code.append(f"t{self.temp_count} = {value}")
                self.temp_count += 1
            elif token == 'SUMA' or token == 'RESTA' or token == 'MULTIPLICACION' or token == 'DIVISION':
                self.code.append(f"t{self.temp_count} = t{self.temp_count - 2} {value}t{self.temp_count - 1}")
                self.temp_count += 1
            elif token == 'OPERADOR_RELACIONAL' or token == 'AND_LOGICO' or token == 'OR_LOGICO' or token == 'NOT_LOGICO':
                self.code.append(f"t{self.temp_count} = t{self.temp_count - 2} {value}t{self.temp_count - 1}")
                self.temp_count += 1
            elif token == 'PARENTESIS_IZQUIERDO' or token == 'PARENTESIS_DERECHO' or token == 'LLAVE_IZQUIERDA' or token == 'LLAVE_DERECHA':
                pass
            elif token == 'PUNTO_Y_COMA':
                self.code.append("") # Separador de instrucciones
            elif token == 'SALTO LINEA':
                pass # No se necesita generar código para el salto de línea
        return self.code
    
    def write_code_to_file(self, filename):
        with open(filename, 'w') as f:
            for line in self.code:
                f.write(line + '\n')
        
input_string = """
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
 """
lexer = Lexer(input_string)
token_list = lexer.lex()
codigo_tres_direcciones = CodigoTresDirecciones(token_list)
codigo_tres_direcciones_result = codigo_tres_direcciones.generate_code()
codigo_tres_direcciones.write_code_to_file('Codigo_tres_direcciones.txt')
