# Reaproveitado partes do código_3 para criaçao da interface.
# Criado o arquivo faturamento_estados.json, para usar neste código. 
# Sendo possivel calcular o porcentual com diferentes json's dês de que o nome do arquivo tenha "faturamento_estados"

import tkinter as tk
from tkinter.filedialog import askopenfilename 
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Screen:
    def __init__(self, main):
        self.main = main
        self.main.title("Porcentual de faturamento por Estado")
        self.main.grid_rowconfigure(10, weight=1)
        self.main.grid_columnconfigure((0,1,2,3,4), weight=1)
        
        #--- Fontes e dimensoes ---
        self.fonte_high= ("Arial", 20)
        self.fonte_medium= ("Arial", 16)
        self.font_low= ("Arial", 12)
        self.button_width = 15
        self.button_height = 2
        #--- ================== ---
        
        self.campo()
        self.canvas = None  # Para armazenar o gráfico

    def campo(self):
        # Label
        self.lbl_title = tk.Label(self.main, font=self.fonte_high, text="Porcentual por Estado.")
        self.lbl_title.grid(row=0, column=1, columnspan=3, padx=5, pady=5)
        
        # Botao selecionar arquivo json
        self.btn_select_file = tk.Button(self.main, font=self.fonte_medium, text="Selecionar\narquivo",
                                         width=self.button_width, height=self.button_height, bd=3, highlightthickness=0, command=self.carregar_faturamento)
        self.btn_select_file.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
        
        # Botao reset/clear
        self.btn_reset = tk.Button(self.main, font=self.fonte_medium, text="Limpar",
                                   width=self.button_width, height=self.button_height, bd=3, highlightthickness=0, command=self.limpar_grafico)
        self.btn_reset.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
        
        # Label para mensagens
        self.lbl_result = tk.Label(self.main, font=self.font_low, text="")
        self.lbl_result.grid(row=4, column=0, columnspan=5, padx=5, pady=5)

    def carregar_faturamento(self):
        # Abre uma janela no explorador de arquivos para selecionar o arquivo JSON
        caminho_arquivo = askopenfilename(title="Selecione o arquivo de faturamento JSON", filetypes=[("JSON files", "*.json")])
        
        if caminho_arquivo:
            try:
                with open(caminho_arquivo, 'r') as arquivo:
                    dados = json.load(arquivo)
                faturamento_estados = dados.get("faturamento_estados", None)
                           
                if faturamento_estados is not None:
                    self.lbl_result.config(text=f"Arquivo carregado com sucesso!\nGerando gráfico...", fg="green")
                    self.gerar_grafico(faturamento_estados)
                else:
                    self.lbl_result.config(text="Erro: o arquivo não contém 'faturamento_estados'.", fg="red")
                
            except json.JSONDecodeError:
                self.lbl_result.config(text="Erro ao ler o arquivo JSON. Verifique o formato.", fg="red")
        else:
            self.lbl_result.config(text="Nenhum arquivo foi selecionado.", fg="red")

    def gerar_grafico(self, faturamento_estados):
        # Limpar gráfico anterior, se houver
        self.limpar_grafico()

        # Dados para o gráfico de pizza
        estados = list(faturamento_estados.keys())
        valores = list(faturamento_estados.values())
        total_faturamento = sum(valores)
        percentuais = [(valor / total_faturamento) * 100 for valor in valores]

        # Criar gráfico de pizza
        fig, ax = plt.subplots()
        ax.pie(percentuais, labels=estados, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Garantir que o gráfico seja um círculo
        
        # Adicionar o gráfico ao Tkinter
        self.canvas = FigureCanvasTkAgg(fig, master=self.main)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=5, column=1, columnspan=3, padx=5, pady=5)

    def limpar_grafico(self):
        # Limpar o gráfico atual, se houver
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None
        self.lbl_result.config(text="") 
         
def init_screen():
    Main = tk.Tk()
    app = Screen(Main)
    Main.geometry("600x730")
    Main.mainloop()
    
init_screen()