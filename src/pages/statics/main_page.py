from globals import get_service

service = get_service()
def main_page():
  return f"""<html>
      <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <style>

          body {{
            font-family: Arial, sans-serif; /* Choose a suitable font */
            background-color: #f0f0f0;
          }}

          .container-fluid {{
            max-width: 960px; /* Adjust the max width as needed */
            margin: 0 auto;
            padding: 20px;
          }}

          h3 {{
            color: #333;
            text-align: center;
          }}

          table {{
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
          }}

          th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
          }}

          th {{
            background-color: #f2f2f2;
          }}   

          .info {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 40px;
          }}

          .item {{
            border: 1px solid #ddd;
            padding: 20px;
            text-align: center;
          }}

          .item h3 {{
            margin-bottom: 10px;
          }}

          .item h4 {{
            font-size: 18px;
            font-weight: bold;
          }}

          td {{
            cursor: pointer;
          }}
        </style>
      </head>

      <body>
        <div class="container-fluid">
          <h2 style="justify-content: center; align-items: center; display: flex;">Próximas renovações</h2>
          {_get_menu_clients()}
        </div>

        <div class="container-fluid info"> 
          <div class="item">
            <h3>Quantidade de Clientes</h3>
            <h4>{len(service.list_clients())}</h4>	
          </div>

          <div class="item">
            <h3>Total de licenças</h3>
            <h4>{sum([licencas for client in service.list_clients() for licencas in [licencas for produto in client['produtos'] for licencas in [produto['licenses']]]])}</h4>
          </div>

          <div class="item">
            <h3>Valor de Trial/Mensal</h3>
            <h4>{round(sum(produto['price'] * produto['licenses'] for client in service.list_clients() for produto in client['produtos']), 2)}</h4>
          </div>
        </div>
      </body>
      <script>
        function clickTableClients(row) {{
          var string = row.dataset.id;
          pywebview.api.clickTableClients(string).then(showResponse)
        }}
      </script>
    </html>
"""

def _get_menu_clients():
  clients = service.get_clients_by_date_products()[0:5]
  
  # PRECISO FAZER COM QUE OS CLIENTES CUJO O PRODUTO TENHA SIDO EXPIRADO, IGNORAR.
  try:
    return f"""<table class="table"><tr> <th scope="col">Domínio</th><th scope="col">Data</th></tr>
      {"".join([f"<tr data-id={client["_id"]} onclick='clickTableClients(this)'><td>{client['domain']}</td> <td>{min([product['date_renovation'] for product in client['produtos'] if not product['expired']]).strftime("%d/%m/%Y")}</td></tr>" for client in clients])}
      </table>
    """
  
  except:
    return """<h3 style="justify-content: center; align-items: center; display: flex;">Não há clientes com produtos ativos</h3>"""
