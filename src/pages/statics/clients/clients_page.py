from globals import get_service

service = get_service()

def clients_page():
  html = f"""<html>
    <head>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
      <style>

          body {{
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
          }}

          .container-fluid {{
            max-width: 960px;
            margin: 0 auto;
            padding: 20px;
          }}

          .inLine {{
            display: inline-block;
            margin-right: 10px; /* Adjust the margin as needed */
          }}

          .scrollDiv {{
            overflow-y: auto; /* Enable vertical scrolling */
            max-height: 600px; /* Adjust the maximum height */
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
            background-color:   
            #f2f2f2;
          }}

          .btn-primary {{
            background-color: #007bff;
            border-color: #007bff;
            color: #fff;
            padding: 0.375rem 0.75rem;
            font-size: 1rem;
            line-height: 1.5;
            border-radius: 0.25rem;   
          }}

          td {{
            cursor: pointer;
          }}

      </style>

    </head>
    <body>
      <div class="container-fluid">
        <div class="inLine">
          <input type="text" id="search" class="form-control" placeholder="Pesquisar" onkeyup="searchButton()">
        </div>

        <button type="button" class="btn btn-primary" onclick="register_client()">Adicionar Cliente</button>

        <div class="scrollDiv">
          {_get_menu_clients()}
        </div>

      </div>
    </body>
    <script>
      function searchButton(){{
        const search = document.getElementById('search').value
        const table = document.getElementById('clientsTable')
        const tr = table.getElementsByTagName('tr')

        for (let i = 0; i < tr.length; i++){{
          const td = tr[i].getElementsByTagName('td')[0]
          if (td){{
            if (td.innerHTML.toUpperCase().indexOf(search.toUpperCase()) > -1){{
              tr[i].style.display = ''
            }} else {{
              tr[i].style.display = 'none'
            }}
          }}
        }}
      }}

      function register_client(){{
        pywebview.api.open_register_client()
      }}

      function clickTableClients(row) {{
          var string = row.dataset.id;
          pywebview.api.clickTableClients(string).then(showResponse)
        }}

    </script>
  </html>"""

  return html

def _get_menu_clients():
  clients = service.list_clients()
  
  return f"""<table id="clientsTable" class="table"><tr> <th scope="col">Domínio</th><th scope="col">Data</th></tr>
        {"".join([f"<tr data-id={client["_id"]} onclick='clickTableClients(this)'><td>{client['domain']}</td> <td>{client['tenantCreation'].strftime("%d/%m/%Y")}</td></tr>" for client in clients])}
      </table>
  """
