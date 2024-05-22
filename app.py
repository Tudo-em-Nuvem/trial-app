from datetime import date
import pandas as pd

class App:
  def __init__(self):
    self.dados_excel = pd.read_excel("ms365 trials.xlsx", header=0)
    self.data_hoje = date.today()

  def vencimentos_proximos_dias(self, dias: int) -> list:
    itens_proximos = []

    dominios = self.dados_excel["DOMÍNIO"].to_list()
    vencimentos = self.dados_excel["VENCIMENTO"].to_list()
    vencimento: pd.Timestamp

    for vencimento, dominio in zip(vencimentos, dominios):
      try:
        if abs(self.data_hoje - vencimento.date()).days < dias and vencimento.date() >= self.data_hoje:
          itens_proximos.append({
            "dominio": dominio,
            "vencimento": vencimento.date().strftime("%d/%m/%Y"),
            "dias_para_vencer": abs(self.data_hoje - vencimento.date()).days
          })

      except: continue
    return itens_proximos

  @property 
  def proximos_vencimentos(self) -> list:
    itens_proximos = self.vencimentos_proximos_dias(30)
    sorted_itens = sorted(itens_proximos, key=lambda x: x["dias_para_vencer"])
    return sorted_itens

  @property
  def valor_mes(self) -> float:
    valor_mes = 0
    vencimento: pd.Timestamp
    dominios_somados = []

    for dominio, valor, vencimento in zip(self.dados_excel["DOMÍNIO"], self.dados_excel["VALOR"], self.dados_excel["VENCIMENTO"]):
      if vencimento.month == self.data_hoje.month and vencimento.year == self.data_hoje.year and dominio not in dominios_somados:
        valor_mes += valor
        dominios_somados.append(dominio)

    return round(valor_mes, 2)

  @property
  def quantidade_de_clientes(self) -> int:
    dominios = list(set(self.dados_excel["DOMÍNIO"].to_list()))

    for count, dominio in enumerate(dominios):
      if dominio == None:
        dominios.remove(dominio)

      print(count, dominio, type(dominio))
    return len(dominios)
  
  @property
  def quatnidade_de_licencas(self) -> int:
    licencas = self.dados_excel["USUÁRIOS"].to_list()
    dominios = self.dados_excel["DOMÍNIO"].to_list()

    dominios_somados = []
    licencas_total = 0

    for licenca, dominio in zip(licencas, dominios):

      try:
        if dominio not in dominios_somados:

          if '+' in str(licenca):
            licenca_splited = str(licenca).split('+')

            for licenca in licenca_splited:
              licencas_total += int(licenca)
            continue
        
          licencas_total += int(licenca)
          dominios_somados.append(dominio)

      except: continue

    return licencas_total

a = App()

print(a.quatnidade_de_licencas)
