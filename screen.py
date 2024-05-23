import tkinter as tk

class Screen(tk.Tk):
  def __init__(self):
    super().__init__()
    
    self.title("App thiago")
    self.geometry("720x550")
    self.resizable(True, True)
    
    container = tk.Frame(self, bg="black")
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_rowconfigure(1, weight=0)
    container.grid_rowconfigure(2, weight=0)
    container.grid_rowconfigure(3, weight=0)
    container.grid_rowconfigure(4, weight=0)
    container.grid_rowconfigure(5, weight=0)
    container.grid_rowconfigure(6, weight=0)
    container.grid_rowconfigure(7, weight=0)
    container.grid_rowconfigure(8, weight=1)
    container.grid_rowconfigure(9, weight=1)
    container.grid_columnconfigure(0, weight=1)
    container.grid_columnconfigure(1, weight=1)
    container.grid_columnconfigure(2, weight=1)
    
    
    self.controls = tk.Label(container, text="CONTROLE DE TRIALS", font=("Arial", 13), bg="black", fg="white")
    
    self.clientes = tk.Button(container, text="CLIENTES", font=("Arial", 11), bg="#1ea5ac", fg="white")
    self.produtos = tk.Button(container, text="PRODUTOS", font=("Arial", 11), bg="#1ea5ac", fg="white")
    self.relatorios = tk.Button(container, text="RELATORIOS", font=("Arial", 11), bg="#1ea5ac", fg="white")
    
    self.renovacoes = tk.Label(container, text="Proximas renovacoes", font=("Arial", 11), bg="black", fg="white", pady=15)
    self.dominio1 = tk.Label(container, text="dominio1.com.br \n 27/05/04 \n dias para o vencimento: 10", font=("Arial", 11), bg="#1ea5ac", fg="white", pady=15, width=50)
    
    self.value_trial = tk.Label(container, text="Valor do Trial/Mensal", font=("Arial", 11), bg="black", fg="white", pady=15)
    self.value = tk.Label(container, text="R$ 8000,00", font=("Arial", 11), bg="#1ea5ac", fg="white", height=3, width=20)
    
    self.qnt_customers = tk.Label(container, text="Quantidade de Clientes", font=("Arial", 11), bg="black", fg="white", pady=15)
    self.customers = tk.Label(container, text="35", font=("Arial", 11), bg="#1ea5ac", fg="white", height=3, width=20)
    
    self.qnt_licencas = tk.Label(container, text="Quantidade de Licencas", font=("Arial", 11), bg="black", fg="white", pady=15)
    self.licencas = tk.Label(container, text="500", font=("Arial", 11), bg="#1ea5ac", fg="white", height=3, width=20)
    
    self.controls.grid(row=0, column=1)
    
    self.clientes.grid(row=1, column=0)
    self.renovacoes.grid(row=2, column=0, columnspan=2)
    self.dominio1.grid(row=3, column=0, columnspan=2)
    
    self.produtos.grid(row=1, column=1)
    
    self.relatorios.grid(row=1, column=2)
    self.value_trial.grid(row=2, column=2)
    self.value.grid(row=3, column=2)
    self.qnt_customers.grid(row=4, column=2)
    self.customers.grid(row=5, column=2)
    self.qnt_licencas.grid(row=6, column=2)
    self.licencas.grid(row=7, column=2)
    
if __name__ == "__main__":
  app = Screen()
  app.mainloop()