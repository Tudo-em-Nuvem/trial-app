from globals import get_service, get_client_for_client_page

service = get_service()

def list_products_to_add_in_client_page():
  client = get_client_for_client_page()

  html = f"""
  <html> 
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

        h3 {{
          text-align: center;
        }}

        table {{
          border-collapse: collapse;
          width: 100%;
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

          td {{
          cursor: pointer;
          }}

      </style>
    </head>
    <body>
      <div class="container-fluid"> 
        <h3>Adicionar para {client["domain"]}</h3>
        {_get_menu_products()}
      </div>
    </body>
    <script>
      function clickTableProductToAddInClient(element) {{
        const id = element.getAttribute('data-id');
        pywebview.api.clickTableProductToAddInClient(id);
      }}
    </script>
  </html>
  """

  return html

def _get_menu_products():
  products = service.list_products()

  return f"""<table class="table" style="margin-top: 1.25rem"><tr><th scope="col">Nome</th><th scope="col">Valor</th></tr>
    {''.join([f'<tr data-id={product["_id"]} onclick="clickTableProductToAddInClient(this)"><td>{product["name"]}</td><td>{product["price"]}</td></tr>' for product in products])}
  """
 