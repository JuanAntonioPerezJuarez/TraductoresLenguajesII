import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from lexer import Lexer

class LexicalAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador")
        self.root.configure(bg='#f0f0f0')  # Color de fondo suave
        
        # Configuración de estilos
        style = ttk.Style()
        style.configure("Treeview",
                       background="#ffffff",
                       fieldbackground="#ffffff",
                       foreground="#333333")
        style.configure("Treeview.Heading",
                       background="#e1e1e1",
                       font=('Arial', 9, 'bold'))
        style.configure("TButton",
                       padding=5,
                       background="#4a90e2")

        # Frame principal con padding
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Área de texto con borde y fondo
        self.text_area = tk.Text(
            main_frame,
            wrap="word",
            width=50,
            height=10,
            font=('Consolas', 10),
            bg='white',
            relief="solid",
            borderwidth=1
        )
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.text_area.insert(tk.END, "a = 7\nb = 2\nsuma = a+b\nresta = ab\nprint('suma:',suma, '\nResta:',resta )\n\n")

        # Frame para botones
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=5)

        # Botones estilizados
        self.read_button = ttk.Button(
            button_frame,
            text="Leer archivo",
            command=self.read_file,
            style="TButton"
        )
        self.read_button.pack(side=tk.LEFT, padx=5)

        self.analyze_button = ttk.Button(
            button_frame,
            text="Analizar léxicamente",
            command=self.analyze_lexically,
            style="TButton"
        )
        self.analyze_button.pack(side=tk.LEFT, padx=5)

        self.create_table()
        
        # Frame para la tabla semántica
        self.semantic_frame = ttk.Frame(main_frame)
        self.semantic_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Tabla semántica
        self.semantic_tree = ttk.Treeview(
            self.semantic_frame,
            columns=("Lexma", "Token", "Coincidencia"),
            show="headings",
            height=10
        )
        
        # Configuración de columnas
        for col in ("Lexma", "Token", "Coincidencia"):
            self.semantic_tree.heading(col, text=col)
            self.semantic_tree.column(col, width=150)

        self.semantic_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar para tabla semántica
        self.semantic_scrollbar = ttk.Scrollbar(
            self.semantic_frame,
            orient="vertical",
            command=self.semantic_tree.yview
        )
        self.semantic_scrollbar.pack(side=tk.RIGHT, fill="y")
        self.semantic_tree.configure(yscrollcommand=self.semantic_scrollbar.set)

    def create_table(self):
        # Frame para la primera tabla
        self.table_frame = ttk.Frame(self.root)
        self.table_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Primera tabla
        self.tree = ttk.Treeview(
            self.table_frame,
            columns=("Lexma", "Token"),
            show="headings",
            height=10
        )
        
        # Configuración de columnas
        for col in ("Lexma", "Token"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar para primera tabla
        self.scrollbar = ttk.Scrollbar(
            self.table_frame,
            orient="vertical",
            command=self.tree.yview
        )
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

                for token_input, token_file in zip(tokens_input, tokens_file):
                    lexma_input, token_name_input = token_input[1], token_input[0]
                    lexma_file, token_name_file = token_file[1], token_file[0]
                    coincidence = "✓" if lexma_input == lexma_file and token_name_input == token_name_file else "✗"
                    
                    # Insertar con tags para colorear
                    tag = "valid" if coincidence == "✓" else "invalid"
                    self.semantic_tree.insert("", "end", 
                                           values=(lexma_input, token_name_input, coincidence),
                                           tags=(tag,))
                
                # Configurar colores para las filas
                self.semantic_tree.tag_configure("valid", background="#e6ffe6")
                self.semantic_tree.tag_configure("invalid", background="#ffe6e6")

if __name__ == "__main__":
    root = tk.Tk()
    app = LexicalAnalyzerGUI(root)
    root.mainloop()