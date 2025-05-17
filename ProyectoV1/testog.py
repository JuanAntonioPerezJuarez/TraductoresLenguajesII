# gui.py
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from lexer import Lexer

class LexicalAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador")
        self.text_area = tk.Text(self.root, wrap="word", width=50, height=10)
        self.text_area.pack(padx=10, pady=10)
        self.text_area.insert(tk.END, "a = 7\nb = 2\nsuma = a+b\nresta = ab\nprint('suma:',suma, '\\nResta:',resta )\n\n")
        self.read_button = tk.Button(self.root, text="Leer archivo",
        command=self.read_file)
        self.read_button.pack(pady=5)
        self.analyze_button = tk.Button(self.root, text="Analizar lÃ©xicamente",
        command=self.analyze_lexically)
        self.analyze_button.pack(pady=5)
        self.create_table()
        self.semantic_frame = ttk.Frame(self.root)
        self.semantic_frame.pack(padx=10, pady=10)
        self.semantic_tree = ttk.Treeview(self.semantic_frame, columns=("Lexma", "Token","Coincidencia"), show="headings", height=10)
        self.semantic_tree.heading("Lexma", text="Lexma")
        self.semantic_tree.heading("Token", text="Token")
        self.semantic_tree.heading("Coincidencia", text="Coincidencia")
        self.semantic_tree.pack(side=tk.LEFT)
        self.semantic_scrollbar = ttk.Scrollbar(self.semantic_frame, orient="vertical",
        command=self.semantic_tree.yview)
        self.semantic_scrollbar.pack(side=tk.RIGHT, fill="y")
        self.semantic_tree.configure(yscrollcommand=self.semantic_scrollbar.set)

    def create_table(self):
        self.table_frame = ttk.Frame(self.root)
        self.table_frame.pack(padx=10, pady=0)
        self.tree = ttk.Treeview(self.table_frame, columns=("Lexma", "Token"),
        show="headings", height=10)
        self.tree.heading("Lexma", text="Lexma")
        self.tree.heading("Token", text="Token")
        self.tree.pack(side=tk.LEFT)
        self.scrollbar = ttk.Scrollbar(self.table_frame, orient="vertical",
        command=self.tree.yview)
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
                    coincidence = "valido" if lexma_input == lexma_file and token_name_input == token_name_file else "invalido"
                    self.semantic_tree.insert("", "end", values=(lexma_input, token_name_input, coincidence))

if __name__ == "__main__":
    root = tk.Tk()
    app = LexicalAnalyzerGUI(root)
    root.mainloop()