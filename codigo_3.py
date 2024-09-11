# Arquivos json de teste no diretorio "json", de abril a agosto
import tkinter as tk #biblioteca padrao para criaçao de interfaces com python
from tkinter.filedialog import askopenfilename 
import json

class Screen:
    def __init__(self, main):
        self.main = main
        self.main.title("Faturamento")
        self.main.grid_rowconfigure(8, weight=1)
        self.main.grid_columnconfigure((0,1,2,3,4), weight=1)
        
        #--- Fontes e dimensoes ---
        self.fonte_high= ("Arial", 20)
        self.fonte_mediumm= ("Arial", 16)
        self.font_low= ("Arial", 12)
        self.button_width = 15
        self.button_height = 2
        #---====================---
        
        self.faturamento_diario = None
        self.campos_1()
        
    def campos_1(self):
        # Label
        self.lbl_title = tk.Label(self.main, font=self.fonte_high, text="Dados sobre faturamento.")
        self.lbl_title.grid(row=0, column=1, columnspan=3, padx=5, pady=5)
        
        # Label
        self.lbl_instrucao = tk.Label(self.main, font=self.fonte_mediumm, text="Selecione um arquivo json.")
        self.lbl_instrucao.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
        
        # Botao selecionar arquivo json
        self.btn_select_file = tk.Button(self.main, font=self.fonte_mediumm, text="Selecionar\narquivo",
                                         width=self.button_width, height=self.button_height, bd=3, highlightthickness=0, command=self.carregar_faturamento)
        self.btn_select_file.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
        
        # Label informativa sobre o arquivo selecionado 
        self.lbl_result = tk.Label(self.main, font=self.font_low, text="", fg="blue")
        self.lbl_result.grid(row=4, column=1, columnspan=3, padx=5, pady=5)
        
        # Label de resultado das estatistica do json 
        self.lbl_estatisticas = tk.Label(self.main, font=self.fonte_mediumm, text="", fg="green")
        self.lbl_estatisticas.grid(row=5, column=1, columnspan=3, padx=5, pady=5)

        # Botao reset/clear
        self.btn_reset = tk.Button(self.main, font=self.fonte_mediumm, text="Limpar",
                                         width=self.button_width, height=self.button_height, bd=3, highlightthickness=0, command=self.reset)
        self.btn_reset.grid(row=8, column=1, columnspan=3, padx=5, pady=5)

    def carregar_faturamento(self):
        # Abre uma janela no explorador de arquivos para selecionar o arquivo JSON
        caminho_arquivo = askopenfilename(title="Selecione o arquivo de faturamento JSON", filetypes=[("JSON files", "*.json")])
        
        if caminho_arquivo:
            try:
                with open(caminho_arquivo, 'r') as arquivo:
                    dados = json.load(arquivo)
                faturamento_diario = dados.get("faturamento_diario", None)
                           
                if faturamento_diario is not None:
                    self.lbl_result.config(text=f"Arquivo carregado com sucesso!\n{len(faturamento_diario)} dias de faturamento encontrados.", fg="green")
                    # Calcular estatísticas
                    menor_faturamento, maior_faturamento, dias_acima_media, media_mensal = self.calcular_estatisticas(faturamento_diario)
                    # Exibir resultados
                    self.exibir_resultados(menor_faturamento, maior_faturamento, dias_acima_media, media_mensal)
                else:
                    self.lbl_result.config(text="Erro: o arquivo não contém 'faturamento_diario'.", fg="yellow")
                
            except json.JSONDecodeError:
                self.lbl_result.config(text="Erro ao ler o arquivo JSON. Verifique o formato.", fg="red")
        else:
            self.lbl_result.config(text="Nenhum arquivo foi selecionado.", fg="red")

    def calcular_estatisticas(self, faturamento):
        faturamento_valido = [valor for valor in faturamento if valor > 0]

        menor_faturamento = min(faturamento_valido)
        maior_faturamento = max(faturamento_valido)

        # Calcular a média do faturamento mensal (apenas dias com faturamento)
        media_mensal = sum(faturamento_valido) / len(faturamento_valido)

        # Contar o número de dias com faturamento superior à média
        dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

        return menor_faturamento, maior_faturamento, dias_acima_da_media, media_mensal

    def exibir_resultados(self, menor, maior, dias_acima_media, media_mensal):
        resultado_texto = (
            f"Menor faturamento do mês: R${menor:.2f}\n"
            f"Maior faturamento do mês: R${maior:.2f}\n"
            f"Média mensal: R${media_mensal:.2f}\n"
            f"N° de dias com faturamento > à média mensal: {dias_acima_media}"
        )
        self.lbl_estatisticas.config(text=resultado_texto)
        
    def reset(self):
        # Limpa os textos exibidos nas labels
        self.lbl_result.config(text="")
        self.lbl_estatisticas.config(text="")
        # Resetara variável do faturamento
        self.faturamento_diario = None
        
def init_screen():
    Main = tk.Tk()
    app = Screen(Main)
    Main.geometry("500x420")
    Main.mainloop()
    
init_screen()