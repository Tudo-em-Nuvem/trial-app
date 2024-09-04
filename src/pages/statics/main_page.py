from globals import get_service

service = get_service()
def main_page():
  return f"""<html>
      <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <style>

          .info {{
            display: flex;
            justify-content: center;
          }}

          .item {{
            color: white;
            background-color: #23272a;
            margin: 0.625rem;
            align-items: center;
            padding: 0.625rem;
            border-radius: 5px;
          }}

          body {{
            color: white;
            background-color: #2c2f33;
          }}

          td {{
            cursor: pointer;
          }}

        </style>
      </head>

      <body>
        <div class="container-fluid">
          <h3>Próximas renovações</h3>
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
  clients = service.list_clients()[0:5]

  return f"""<table class="table"><tr> <th scope="col">Domínio</th><th scope="col">Data</th></tr>
        {"".join([f"<tr data-id={client["_id"]} onclick='clickTableClients(this)'><td>{client['domain']}</td> <td>{min([product['date_renovation'] for product in client['produtos']]).strftime("%d/%m/%Y")}</td></tr>" for client in clients])}
      </table>
  """
