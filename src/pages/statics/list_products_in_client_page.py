from globals import get_service, get_client_for_client_page

service = get_service()

def list_product_in_client_page():
  client = get_client_for_client_page()

  html = f"""
  <html> 
    <head> 
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
      <style>
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
        <h3>Adicionar para {client["domain"]}</h3>
        {_get_menu_products()}
      </div>
    </body>
    <script>
      function clickTableProductInClient(element) {{
        const id = element.getAttribute('data-id');
        pywebview.api.clickTableProductInClient(id);
      }}
    </script>
  </html>
  """

  return html

def _get_menu_products():
  products = service.list_products()

  return f"""<table class="table" style="margin-top: 1.25rem"><tr><th scope="col">Nome</th><th scope="col">Valor</th></tr>
    {''.join([f'<tr data-id={product["_id"]} onclick="clickTableProductInClient(this)"><td>{product["name"]}</td><td>{product["price"]}</td></tr>' for product in products])}
  """
 