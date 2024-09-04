from globals import set_client_for_client_page, get_service
service = get_service()

def client_page(client_id):
  client = service.find_client_with_id(client_id)
  set_client_for_client_page(client)

  html = f"""<html>
    <head>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
      <style>
        body {{
          color: white;
          background-color: #2c2f33;
          }}

        .inLine {{
          display: flex;
          gap: 0.938rem;
        }}

        .notInline {{
          display: flex;
          flex-direction: column;
        }}

        td {{
          cursor: pointer;
        }}
      </style>
    </head>
    <body>
      <div class="container-fluid">
        <h1>{client['domain']}</h1>
        <div class="mb-3">
          <label class="form-label">Domínio</label>
          <input type="text" id="domain" value="{client['domain']}" class="form-control">
        </div>
        <div class="mb-3">
          <label class="form-label">Informações</label>
          <input type="text" id="info" value="{client['Info']}" class="form-control">
        </div>
        <div class="mb-3">
          <label class="form-label">Observações</label>
          <input type="text" id="obs" value="{client['Obs']}" class="form-control">
        </div>
        <div class="mb-3">
          <label class="form-label">E-mail Adm</label>
          <input type="text" id="email" value="{client['emailAdmin']}" class="form-control">
        </div>

        <div class="mb-3 inLine">
          <div class = "notInline">
            <label for="GDAP" class="form-label">GDAP</label>
            {_get_select_menu_sim_nao(client, 'GDAP')}
          </div>

          <div class ="notInline">
            <label for="cobrancaRecorrente" class="form-label">Cobranca Recorrente</label>
            {_get_select_menu_sim_nao(client, 'cobrancaRecorrente')}
          </div>
        </div>

        <button type="button" class="btn btn-primary" onclick="sendInputValue()">Atualizar Cliente</button>
        <div class="table" style="margin-top: 1.25rem">
          {_get_menu_products_by_client(client)}
        </div>

        <div style="margin-bottom: 1.25rem" >
          <button type="button" class="btn btn-primary" onclick="addProduct()">Adicionar Produto</button>
        </div>
      </div>

    </body>
    <script>
      function sendInputValue() {{
        var inputDomain = document.getElementById('domain')
        var inputInfo = document.getElementById('info')
        var inputObs = document.getElementById('obs')
        var inputEmail = document.getElementById('email')
        var inputGDAP = document.getElementById('GDAP')
        var inputCobrancaRecorrente = document.getElementById('cobrancaRecorrente')

        var actualizedInfoAndObs = {{
          domain: inputDomain.value,
          info: inputInfo.value,
          obs: inputObs.value,
          email: inputEmail.value,
          GDAP: inputGDAP.value,
          cobrancaRecorrente: inputCobrancaRecorrente.value
        }}

        pywebview.api.update_client_info(actualizedInfoAndObs)
      }}

      function clickTableProductInClient(row) {{
        var string = row.dataset.id;
        pywebview.api.clickTableProductInClient(string).then(showResponse)
      }}

      function addProduct() {{
        pywebview.api.addProductInClient()
      }}
    </script>
  </html>
  """
  return html

def _get_menu_products_by_client(client):
  return f"""<table class="table"><tr> <th scope="col">Produto</th><th scope="col">licencas</th><th scope="col">Valor</th><th scope="col">total</th><th scope="col">Renovação</th></tr>
        {"".join([f"<tr data-id={product['_id']} onclick='clickTableProductInClient(this)'><td>{product['name']}</td> <td>{product['licenses']}</td><td>$ {product['price']}</td><td>$ {round(product['price'] * product['licenses'], 2)}</td><td>{product['date_renovation'].strftime("%d/%m/%Y")}</td></tr>" for product in client['produtos']])}
  """

def _get_select_menu_sim_nao(client, gdap_or_cobranca_recorrente):
    tipo = "GDAP" if gdap_or_cobranca_recorrente == "GDAP" else "cobrancaRecorrente"

    html = f"""<select name="{tipo}" id="{tipo}" class="form-select">
        1
        2
      </select>
    """

    if client[tipo]:
      html = html.replace('1', '<option value="sim">Sim</option>')
      html = html.replace('2', '<option value="nao">Não</option>')
    else:
      html = html.replace('1', '<option value="nao">Não</option>')
      html = html.replace('2', '<option value="sim">Sim</option>')

    return html
