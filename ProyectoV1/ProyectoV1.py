import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from lexer import Lexer
from tkinter import messagebox

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.current_token = None
        self.errors = []
        
    def get_next_token(self):
        if self.current_token_index < len(self.tokens):
            self.current_token = self.tokens[self.current_token_index]
            self.current_token_index += 1
        else:
            self.current_token = None
        return self.current_token

    def match(self, expected_type):
        if self.current_token and self.current_token[0] == expected_type:
            token = self.current_token
            self.get_next_token()
            return token
        else:
            self.errors.append(f"Error de sintaxis: se esperaba {expected_type}, se encontró {self.current_token[0] if self.current_token else 'EOF'}")
            return None

    def parse(self):
        self.get_next_token()
        self.program()
        return len(self.errors) == 0, self.errors

    def program(self):
        """
        program -> statement_list
        """
        self.statement_list()

    def statement_list(self):
        """
        statement_list -> statement statement_list | ε
        """
        if self.current_token:
            self.statement()
            self.statement_list()

    def statement(self):
        """
        statement -> assignment | print_statement
        """
        if self.current_token:
            if self.current_token[0] == 'IDENTIFIER':
                self.assignment()
            elif self.current_token[0] == 'PRINT':
                self.print_statement()
            else:
                self.errors.append(f"Error de sintaxis: declaración inválida en {self.current_token[1]}")

    def assignment(self):
        """
        assignment -> IDENTIFIER = expression
        """
        self.match('IDENTIFIER')
        self.match('ASSIGN')
        self.expression()

    def expression(self):
        """
        expression -> term ((PLUS|MINUS) term)*
        """
        self.term()
        while self.current_token and self.current_token[0] in ['PLUS', 'MINUS']:
            self.get_next_token()
            self.term()

    def term(self):
        """
        term -> factor ((MULTIPLY|DIVIDE) factor)*
        """
        self.factor()
        while self.current_token and self.current_token[0] in ['MULTIPLY', 'DIVIDE']:
            self.get_next_token()
            self.factor()

    def factor(self):
        """
        factor -> NUMBER | IDENTIFIER | (expression)
        """
        if not self.current_token:
            self.errors.append("Error de sintaxis: expresión incompleta")
            return

        if self.current_token[0] == 'NUMBER':
            self.match('NUMBER')
        elif self.current_token[0] == 'IDENTIFIER':
            self.match('IDENTIFIER')
        elif self.current_token[0] == 'LPAREN':
            self.match('LPAREN')
            self.expression()
            self.match('RPAREN')
        else:
            self.errors.append(f"Error de sintaxis: factor inválido {self.current_token[1]}")

    def print_statement(self):
        """
        print_statement -> PRINT LPAREN (expression|STRING) RPAREN
        """
        self.match('PRINT')
        self.match('LPAREN')
        if self.current_token[0] in ['STRING', 'IDENTIFIER', 'NUMBER']:
            self.get_next_token()
        else:
            self.errors.append("Error de sintaxis: se esperaba una expresión o cadena en print")
        self.match('RPAREN')

class AnalizadorLexico:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Lexico")
        self.text_area = tk.Text(self.root, wrap="word", width=50, height=10)
        self.text_area.pack(padx=10, pady=10)
        self.text_area.insert(tk.END, "a = 7\nb = 2\nsuma = a+b\nresta = ab\nprint('suma:',suma, '\\nResta:',resta )\n\n")

        self.read_button = tk.Button(self.root, text="Leer archivo", command=self.read_file)
        self.read_button.pack(pady=5)
        self.analyze_button = tk.Button(self.root, text="Analizar léxicamente", command=self.analyze_lexically)
        self.analyze_button.pack(pady=5)
        
        self.create_table()
        

    def create_table(self):
        self.table_frame = ttk.Frame(self.root)
        self.table_frame.pack(padx=10, pady=0)
        self.tree = ttk.Treeview(self.table_frame, columns=("Lexma", "Token"),show="headings", height=10)
        self.tree.heading("Lexma", text="Lexma")
        self.tree.heading("Token", text="Token")
        self.tree.pack(side=tk.LEFT)
        self.scrollbar = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")
        self.tree.configure(yscrollcommand=self.scrollbar.set)

    def update_table(self, tokens):
        for token in tokens:
            lexma, token_name = token[1], token[0]
            self.tree.insert("", "end", values=(lexma, token_name))

    def read_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)

    def analyze_lexically(self):
        content = self.text_area.get("1.0", tk.END)
        tokens = self.lexer.analyze(content)
        self.update_table(tokens)

    def analyze_lexically(self):
        input_string = self.text_area.get("1.0", tk.END)
        lexer = Lexer(input_string)
        tokens = lexer.lex()
        self.tree.delete(*self.tree.get_children())

        for token in tokens:
            lexma, token_name = token[1], token[0]
            self.tree.insert("", "end", values=(lexma, token_name))
        
        self.compare_with_file(tokens)

    def compare_with_file(self, tokens_input):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()   
                lexer = Lexer(content)
                tokens_file = lexer.lex()

                self.semantic_tree.delete(*self.semantic_tree.get_children())

                # Determinar la longitud máxima para la comparación
                max_length = max(len(tokens_input), len(tokens_file))
                
                # Rellenar la tabla con la comparación
                for i in range(max_length):
                    if i < len(tokens_input) and i < len(tokens_file):
                        # Ambos tokens existen
                        token_input = tokens_input[i]
                        token_file = tokens_file[i]
                        lexma_input, token_name_input = token_input[1], token_input[0]
                        lexma_file, token_name_file = token_file[1], token_file[0]
                        
                        # Verificar coincidencia exacta
                        coincidence = "valido" if (lexma_input == lexma_file and 
                                                token_name_input == token_name_file) else "invalido"
                        
                        # Insertar en la tabla con color según coincidencia
                        self.semantic_tree.insert("", "end", values=(lexma_input, 
                                                                token_name_input, 
                                                                coincidence),
                                                tags=(coincidence,))
                    elif i < len(tokens_input):
                        # Solo existe en el código de entrada
                        token_input = tokens_input[i]
                        self.semantic_tree.insert("", "end", 
                                                values=(token_input[1], 
                                                    token_input[0], 
                                                    "invalido - token extra"),
                                                tags=("invalido",))
                    else:
                        # Solo existe en el archivo de comparación
                        token_file = tokens_file[i]
                        self.semantic_tree.insert("", "end", 
                                                values=(token_file[1], 
                                                    token_file[0], 
                                                    "invalido - token faltante"),
                                                tags=("invalido",))

                # Agregar colores para mejor visualización
                self.semantic_tree.tag_configure("valido", foreground="green")
                self.semantic_tree.tag_configure("invalido", foreground="red")

                # Mostrar resumen de la comparación
                total_tokens = max_length
                valid_tokens = sum(1 for i in range(min(len(tokens_input), len(tokens_file))) 
                                if tokens_input[i] == tokens_file[i])
                
                messagebox.showinfo("Resultado de la comparación",f"Total de tokens: {total_tokens}\n", f"Tokens coincidentes: {valid_tokens}\n"f"Porcentaje de similitud: {(valid_tokens/total_tokens)*100:.2f}%")

    def analyze_lexically(self):
        input_string = self.text_area.get("1.0", tk.END)
        lexer = Lexer(input_string)
        tokens = lexer.lex()
        self.tree.delete(*self.tree.get_children())

        # Actualizar la tabla de tokens
        for token in tokens:
            lexma, token_name = token[1], token[0]
            self.tree.insert("", "end", values=(lexma, token_name))
        
        # Realizar análisis sintáctico
        parser = Parser(tokens)
        is_valid, errors = parser.parse()
        
        # Mostrar resultado del análisis sintáctico
        if is_valid:
            tk.messagebox.showinfo("Análisis Sintáctico", "El programa es sintácticamente válido")
        else:
            error_message = "\n".join(errors)
            tk.messagebox.showerror("Análisis Sintáctico", f"Errores encontrados:\n{error_message}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnalizadorLexico(root)
    root.mainloop()
   