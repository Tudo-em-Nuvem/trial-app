from globals import get_service, set_product_for_product_page
service = get_service()

def product_page(product_id):
  product = service.find_product_by_id(product_id)
  set_product_for_product_page(product)
  html=f"""<html>
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

          .form-select {{
            appearance: none;
            -webkit-appearance: none;
            -moz-appearance: none;
            background: #fff;
            padding: 0.375rem 2.25rem 0.375rem 0.75rem;
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

          .buttonsDiv {{
            display: flex;
            justify-content: space-between;
          }}

          .btnAttClient {{
            width: 80%;
            border-radius: 6px 0px 0px 6px;
          }}

          .btnDeleteClient {{
            width: 20%;
            border-radius:  0px 6px 6px 0px;
          }}

        </style>
      </head>
      <body> 
        <div class="container-fluid">
          <h1>Editar Produto</h1>

          <div class="mb-3">
            <label class="form-label">Nome</label>
            <input type="text" id="name" data-original="{product['name']}" value="{product['name']}" class="form-control">
          </div>

          <div class="mb-3">
            <label class="form-label">Valor</label>
            <input type="number" id="price" data-original="{product['price']}" value="{product['price']}" class="form-control">
          </div>

          <div class="buttonsDiv">
            <button type="button" class="btnAttClient btn btn-primary" onclick="sendInputValue()" disabled>Atualizar Produto</button>
            <button type="button" class="btnDeleteClient btn btn-danger" onclick="deleteProduct()">Excluir Produto</button>
          </div>
        </div>
      </body>
      <script>
        const name = document.getElementById('name');
        const price = document.getElementById('price');

        name.addEventListener('input', () => {{
          document.querySelector('.btnAttClient').disabled = !checkInputsIsDifferent();
        }});

        price.addEventListener('input', () => {{
          document.querySelector('.btnAttClient').disabled = !checkInputsIsDifferent();
        }});


        function checkInputsIsDifferent() {{
          const originalName = name.getAttribute('data-original');
          const originalPrice = price.getAttribute('data-original');
          return name.value !== originalName || price.value !== originalPrice;
        }}

        function sendInputValue() {{
          name.setAttribute('data-original', name.value);
          price.setAttribute('data-original', price.value);
          document.querySelector('.btnAttClient').disabled = !checkInputsIsDifferent()

          var data = {{
            name: name.value,
            price: price.value
          }};

          pywebview.api.update_product(data);
        }}

        function deleteProduct() {{
          pywebview.api.delete_product();
        }}
      </script>
</html>
  """
  return html