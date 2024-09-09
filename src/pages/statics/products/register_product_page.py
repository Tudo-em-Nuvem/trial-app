from globals import get_service

service = get_service()

def register_products_page():
  html = f"""<html>
    <head>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
      <style>
        body {{
          font-family: Arial, sans-serif;
          background-color: #f0f0f0;
        }}

        h1 {{
          text-align: center;
        }}

        .container-fluid {{
          max-width: 960px;
          margin: 0 auto;
          padding: 20px;
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

      </style>
    </head>
    <body>
      <div class="container-fluid">
        <h1>Cadastro de Produtos</h1>
        <div class="mb-3">
          <label class="form-label">Nome</label>
          <input type="text" class="form-control" id="name">
        </div>
        <div class="mb-3">
          <label class="form-label">Valor</label>
          <input type="number" class="form-control" id="price">
        </div>
        <div class="mb-3">
          <button class="btn btn-primary" onclick="registerProduct()" disabled>Adicionar</button>
        </div>
      </div>
    </body>
    <script>
      const name = document.getElementById('name')
      const price = document.getElementById('price')

      function checkFields() {{
        return name.value && price.value
      }}

      document.getElementById('name').onchange = function() {{
        document.querySelector('button').disabled = !checkFields()
      }}

      document.getElementById('price').onchange = function() {{
        document.querySelector('button').disabled = !checkFields()
      }}

      function registerProduct() {{
        let fields = {{
          name: name.value,
          price: price.value
        }}

         pywebview.api.register_product(fields)
      }}
    </script>
  </html>
"""

  return html
