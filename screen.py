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
    container.grid_rowconfigure(4, weight=1)
    container.grid_rowconfigure(5, weight=1)
    container.grid_columnconfigure(0, weight=1)
    container.grid_columnconfigure(1, weight=1)
    container.grid_columnconfigure(2, weight=1)
    
    
    self.controls = tk.Label(container, text="CONTROLE DE TRIALS", font=("Arial", 13), bg="black", fg="white")
    
    self.clientes = tk.Button(container, text="CLIENTES", font=("Arial", 11), bg="#1ea5ac", fg="white")
    self.produtos = tk.Button(container, text="PRODUTOS", font=("Arial", 11), bg="#1ea5ac", fg="white")
    self.relatorios = tk.Button(container, text="RELATORIOS", font=("Arial", 11), bg="#1ea5ac", fg="white")
    
    self.renovacoes = tk.Label(container, text="Proximas renovacoes", font=("Arial", 11), bg="black", fg="white", pady=15)
    self.dominio1 = tk.Label(container, text="dominio1.com.br \n 27/05/04 \n dias para o vencimento: 10", font=("Arial", 11), bg="#1ea5ac", fg="white", pady=15, width=50)

    self.controls.grid(row=0, column=1)
    
    self.clientes.grid(row=1, column=0)
    self.renovacoes.grid(row=2, column=0, columnspan=2)
    self.dominio1.grid(row=3, column=0, columnspan=2)
    
    self.produtos.grid(row=1, column=1)
    
    self.relatorios.grid(row=1, column=2)
    
if __name__ == "__main__":
  app = Screen()
  app.mainloop()