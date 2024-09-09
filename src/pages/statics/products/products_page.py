from globals import get_service

service = get_service()

def products_page():
  html = f"""<html>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <body>
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

        .scrollDiv {{
          overflow-y: auto;
          max-height: 300px; /* Ajuste a altura máxima conforme necessário */
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

        td {{
          cursor: pointer;
        }}

        th {{
          background-color: #f2f2f2;   
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
      </style>
      <div class="container-fluid">
        <button type="button" class="btn btn-primary" onclick="register_product()">Adicionar Produto</button>
        <div class="scrollDiv"> 
          {_get_menu_products()}
        </div>
      </div>
    </body>
    <script>
        function click_table_product(row) {{
          var string = row.dataset.id;
          pywebview.api.click_table_product(string).then(showResponse)
        }}

        function register_product() {{
          pywebview.api.open_register_product()
        }}
    </script>
  </html>
  """

  return html

def _get_menu_products():
  products = service.list_products()

  return f"""<table class="table" style="margin-top: 1.25rem"><tr><th scope="col">Nome</th><th scope="col">Valor</th></tr>
    {''.join([f'<tr data-id={product["_id"]} onclick="click_table_product(this)"><td>{product["name"]}</td><td>{product["price"]}</td></tr>' for product in products])}
  """
