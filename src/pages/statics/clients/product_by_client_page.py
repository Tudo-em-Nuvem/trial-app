from bson import ObjectId
from globals import get_service, get_client_for_client_page, set_product_for_client

service = get_service()
def product_by_client_page(product_id):
  client = get_client_for_client_page()
  product = None

  for p in client['produtos']:
    if p['_id'] == ObjectId(product_id):
      product = p
      break

  set_product_for_client(product)

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

          h1 {{
            text-align: center;
          }}

          h2 {{
            text-align: center;
          }}

          .mb-3 {{
            margin-bottom: 1rem;
          }}

          .form-label {{
            font-weight: bold;
          }}

          .form-control {{
            border: 1px solid #ccc;
            border-radius: 0.25rem;
            padding: 0.375rem 0.75rem;
          }}

          .inLine {{
            display: flex;
            justify-content: space-between;
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

          .btn-danger {{
            background-color: #dc3545;
            border-color: #dc3545;
            color: #fff;
            padding: 0.375rem 0.75rem;
            font-size:   
          1rem;
            line-height: 1.5;
            border-radius: 0.25rem;
          }}
        </style>
      </head>

      <body>
        <div class="container-fluid">
          <h1>Produto de {client['domain']}</h1>
          <h2>{product['name']}</h4>

          <div class="mb-3">
            <label class="form-label">Valor</label>
            <input type="number" id="price" value="{product['price']}" class="form-control">
          </div>
          
          <div class="mb-3">
            <label class="form-label">Licenças</label>
            <input type="number" id="licenses" value="{product['licenses']}" class="form-control">
          </div>

          <div class="mb-3">
            <label>Data de renovação</label>
            <h5>{product['date_renovation'].strftime('%d/%m/%Y')}</h5>
            <input type="date" id="date_renovation" class="form-control">
          </div>

          <div class="mb-3 inLine">
            <button class="btn btn-primary" onclick="updateProduct()">Atualizar</button>
            <button class="btn btn-danger" onclick="removeProduct()">Remover</button>
          </div>
        </body>

        <script>
          function updateProduct() {{
            const price = document.getElementById('price').value
            const licenses = document.getElementById('licenses').value
            const date_renovation = document.getElementById('date_renovation').value

            pywebview.api.update_product_by_client({{
              price,
              licenses,
              date_renovation
            }})
          }}

          function removeProduct() {{
            pywebview.api.remove_product_by_client()
          }}
        </script>
      </html>
  """
  return html
