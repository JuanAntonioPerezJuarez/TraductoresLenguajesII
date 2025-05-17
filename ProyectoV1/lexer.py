class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[0] if text else None

    def error(self):
        raise Exception('Error de análisis léxico')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def skip_comment(self):
        while self.current_char and self.current_char != '\n':
            self.advance()
        if self.current_char == '\n':
            self.advance()

    def number(self):
        result = ''
        while self.current_char and (self.current_char.isdigit() or self.current_char == '.'):
            result += self.current_char
            self.advance()
        return float(result) if '.' in result else int(result)

    def identifier(self):
        result = ''
        while self.current_char and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        return result

    def string(self):
        self.advance()  # Skip the opening quote
        result = ''
        while self.current_char and self.current_char != "'":
            result += self.current_char
            self.advance()
        if self.current_char == "'":
            self.advance()  # Skip the closing quote
        return result

    def lex(self):
        tokens = []
        
        keywords = {
            'print': 'PRINT',
            'if': 'IF',
            'else': 'ELSE',
            'while': 'WHILE',
            'for': 'FOR',
            'def': 'DEF',
            'return': 'RETURN'
        }

        while self.pos < len(self.text):
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == '#':
                self.skip_comment()
                continue

            if self.current_char.isdigit():
                tokens.append(('NUMBER', str(self.number())))
                continue

            if self.current_char.isalpha() or self.current_char == '_':
                identifier = self.identifier()
                token_type = keywords.get(identifier, 'IDENTIFIER')
                tokens.append((token_type, identifier))
                continue

            if self.current_char == "'":
                tokens.append(('STRING', self.string()))
                continue

            if self.current_char == '=':
                self.advance()
                if self.current_char == '=':
                    tokens.append(('EQUALS', '=='))
                    self.advance()
                else:
                    tokens.append(('ASSIGN', '='))
                continue

            if self.current_char == '+':
                tokens.append(('PLUS', '+'))
                self.advance()
                continue

            if self.current_char == '-':
                tokens.append(('MINUS', '-'))
                self.advance()
                continue

            if self.current_char == '*':
                tokens.append(('MULTIPLY', '*'))
                self.advance()
                continue

            if self.current_char == '/':
                tokens.append(('DIVIDE', '/'))
                self.advance()
                continue

            if self.current_char == '(':
                tokens.append(('LPAREN', '('))
                self.advance()
                continue

            if self.current_char == ')':
                tokens.append(('RPAREN', ')'))
                self.advance()
                continue

            if self.current_char == ',':
                tokens.append(('COMMA', ','))
                self.advance()
                continue

            if self.current_char == '\n':
                tokens.append(('NEWLINE', '\\n'))
                self.advance()
                continue

            # Si llegamos aquí, encontramos un carácter que no reconocemos
            raise Exception(f'Carácter no reconocido: {self.current_char}')

        return tokens
