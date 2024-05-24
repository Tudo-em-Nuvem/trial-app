import tkinter as tk
from tkinter import ttk
from app import App

class Screen(tk.Tk):
  def __init__(self):
    super().__init__()
          
    self.title("App Thiago")
    self.geometry("720x550")
    self.resizable(True, True)
          
    self.a = App()
    self.domains = self.a.vencimentos_proximos_dias(20)
          
    container = tk.Frame(self, bg="black")
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
          
    self.panel = ttk.Treeview(container)
    self.panel["columns"] = ("dominio", "data", "dias para o vencimento")
    self.panel.column("#0", width=0, stretch=tk.NO)
    self.panel.column("dominio", width=200, minwidth=100, stretch=tk.NO)
    self.panel.column("data", width=100, minwidth=100, stretch=tk.NO)
    self.panel.column("dias para o vencimento", width=50, minwidth=50, stretch=tk.NO)
          
    self.panel.heading("dominio", text="Domínio")
    self.panel.heading("data", text="Data")
    self.panel.heading("dias para o vencimento", text="Dias para o Vencimento")
          
    for domain in self.domains:
      self.panel.insert("", "end", values=(domain['dominio'], domain['vencimento'], domain['dias_para_vencer']))
          
    self.scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.panel.yview)
    self.panel.configure(yscrollcommand=self.scrollbar.set)
          
    self.panel.grid(row=3, column=0, columnspan=2, rowspan=4, padx=85, sticky="nsew")
    self.scrollbar.grid(row=4, column=1, sticky="ns")

    self.controls = tk.Label(container, text="CONTROLE DE TRIALS", font=("Arial", 13), bg="black", fg="white")
          
    self.clientes = tk.Button(container, text="CLIENTES", font=("Arial", 11), bg="#1ea5ac", fg="white")
    self.produtos = tk.Button(container, text="PRODUTOS", font=("Arial", 11), bg="#1ea5ac", fg="white")
    self.relatorios = tk.Button(container, text="RELATORIOS", font=("Arial", 11), bg="#1ea5ac", fg="white")
          
    self.renovacoes = tk.Label(container, text="Próximas renovações", font=("Arial", 11), bg="black", fg="white", pady=15)
          
    self.value_trial = tk.Label(container, text="Valor do Trial/Mensal", font=("Arial", 11), bg="black", fg="white", pady=15)
    text_value = f"R$ {str(self.a.valor_mes)}"
    self.value = tk.Label(container, text=text_value, font=("Arial", 11), bg="#1ea5ac", fg="white", height=3, width=20)
          
    self.qnt_customers = tk.Label(container, text="Quantidade de Clientes", font=("Arial", 11), bg="black", fg="white", pady=15)
    text_qnt_customers = str(self.a.quantidade_de_clientes)
    self.customers = tk.Label(container, text=text_qnt_customers, font=("Arial", 11), bg="#1ea5ac", fg="white", height=3, width=20)
          
    self.qnt_licencas = tk.Label(container, text="Quantidade de Licenças", font=("Arial", 11), bg="black", fg="white", pady=15)
    text_qnt_licencas = str(self.a.quatnidade_de_licencas)
    self.licencas = tk.Label(container, text=text_qnt_licencas, font=("Arial", 11), bg="#1ea5ac", fg="white", height=3, width=20)
          
    self.controls.grid(row=0, column=1, padx=10, pady=10)
          
    self.clientes.grid(row=1, column=0, padx=10, pady=10)
    self.renovacoes.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
          
    self.produtos.grid(row=1, column=1, padx=10, pady=10)
    self.relatorios.grid(row=1, column=2, padx=10, pady=10)
          
    self.value_trial.grid(row=2, column=2, padx=10, pady=10)
    self.value.grid(row=3, column=2, padx=10, pady=10)
    self.qnt_customers.grid(row=4, column=2, padx=10, pady=10)
    self.customers.grid(row=5, column=2, padx=10, pady=10)
    self.qnt_licencas.grid(row=6, column=2, padx=10, pady=10)
    self.licencas.grid(row=7, column=2, padx=10, pady=10)

if __name__ == "__main__":
  app = Screen()
  app.mainloop()
    