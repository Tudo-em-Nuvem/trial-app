from globals import get_service, get_client_for_client_page, set_product_for_client

service = get_service()

def add_product_to_client_page(product_id):
  client = get_client_for_client_page()
  product = service.find_product_by_id(product_id)
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

      h4 {{
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
        justify-content: center;
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

      .btn-primary[disabled] {{
        opacity: 0.65;
        cursor: not-allowed;
      }}
        </style>
      </head>

      <body>
        <div class="container-fluid">
          <h1>Produto de {client['domain']}</h1>
          <h4>{product['name']}</h4>
          
          <div class="mb-3">
            <label class="form-label">Valor</label>
            <input type="number" id="price" value="{product["price"]}" class="form-control">
          </div>

          <div class="mb-3">
            <label>Data de renovação</label>
            <input type="date" id="date_renovation" class="form-control">
          </div>


          <div class="mb-3">
            <label class="form-label">Quantidade de licenças</label>
            <input type="number" id="licenses" class="form-control">
          </div>

          <div class="mb-3 inLine">
            <button class="btn btn-primary" onclick="registerProduct()" disabled>Adicionar</button>
          </div>
        </body>

        <script>
          function registerProduct() {{
            const price = document.getElementById('price').value
            const licenses = document.getElementById('licenses').value
            const date_renovation = document.getElementById('date_renovation').value

            pywebview.api.addProductInClient({{
              price,
              licenses,
              date_renovation
            }})
          }}

          function checkAllInputsHasValue() {{
            const price = document.getElementById('price').value
            const licenses = document.getElementById('licenses').value
            const date_renovation = document.getElementById('date_renovation').value

            return price && licenses && date_renovation
          }}

          // onchange inputs, check if all inputs has value to enable button

          document.getElementById('price').onchange = function() {{
            document.querySelector('button').disabled = !checkAllInputsHasValue()
          }}

          document.getElementById('licenses').onchange = function() {{
            document.querySelector('button').disabled = !checkAllInputsHasValue()
          }}

          document.getElementById('date_renovation').onchange = function() {{
            document.querySelector('button').disabled = !checkAllInputsHasValue()
          }}
        
        </script>
      </html>
  """

  return html
