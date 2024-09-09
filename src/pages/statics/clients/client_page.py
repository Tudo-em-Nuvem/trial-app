from globals import set_client_for_client_page, get_service
service = get_service()

def client_page(client_id):
  client = service.find_client_with_id(client_id)
  if client is None:
    client = service.find_client_with_domain(client_id)

  set_client_for_client_page(client)

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

        .mb-3 {{
          margin-bottom: 1rem;
        }}

        .form-label {{
          font-weight: bold;
        }}

        .form-control {{
          border: 1px solid #ccc;
          border-radius: 0.25rem;
        }}

        .inLine {{
          display: flex;
          gap: 0.938rem;
        }}

        .notInline {{
          display: flex;
          margin-right: 1rem;
          flex-direction: column;
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

        td {{
          cursor: pointer;
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
        <h1>{client['domain']}</h1>
        <div class="mb-3 notInLine">
          <label class="form-label">Domínio</label>
          <input type="text" id="domain" value="{client['domain']}" data-original="{client['domain']}" class="form-control">
        </div>
        <div class="mb-3 notInLine">
          <label class="form-label">Informações</label>
          <textarea style="height: 100px;" id="info" data-original="{client['info']}" class="form-control">{client['info']}</textarea>
        </div>
        <div class="mb-3 notInLine">
          <label class="form-label">Observações</label>
          <textarea style="height: 100px;" id="obs" data-original="{client['obs']}" class="form-control">{client['obs']}</textarea>
        </div>
        <div class="mb-3 notInLine">
          <label class="form-label">E-mail Adm</label>
          <input type="text" id="email" value="{client['emailAdmin']}" data-original="{client['emailAdmin']}" class="form-control">
        </div>

        <div class="mb-3 inLine">
          <div class = "notInline">
            <label for="gdap" class="form-label">gdap</label>
            {_get_select_menu_sim_nao(client, 'gdap')}
          </div>

          <div class ="notInline">
            <label for="cobrancaRecorrente" class="form-label">Cobranca Recorrente</label>
            {_get_select_menu_sim_nao(client, 'cobrancaRecorrente')}
          </div>
        </div>

        <div class="buttonsDiv">
          <button type="button" class="btnAttClient btn btn-primary" onclick="sendInputValue()" disabled>Atualizar Cliente</button>
          <button type="button" class="btnDeleteClient btn btn-danger" onclick="deleteCliente()">Excluir Cliente</button>
        </div>

        <div class="table" style="margin-top: 1.25rem">
          {_get_menu_products_by_client(client)}
        </div>

        <div style="margin-bottom: 1.25rem" >
          <button type="button" class="btn btn-primary" onclick="addProduct()">Adicionar Produto</button>
        </div>
      </div>
    </body>

    <script>
      var inputDomain = document.getElementById('domain')
      var inputInfo = document.getElementById('info')
      var inputObs = document.getElementById('obs')
      var inputEmail = document.getElementById('email')
      var inputGDAP = document.getElementById('gdap')
      var inputCobrancaRecorrente = document.getElementById('cobrancaRecorrente')

      function checkInputsIsDifferent() {{
        const originalDomain = inputDomain.getAttribute('data-original')
        const originalInfo = inputInfo.getAttribute('data-original')
        const originalObs = inputObs.getAttribute('data-original')
        const originalEmail = inputEmail.getAttribute('data-original')
        const originalGDAP = inputGDAP.getAttribute('data-original')
        const originalCobrancaRecorrente = inputCobrancaRecorrente.getAttribute('data-original')

        return inputDomain.value !== originalDomain ||
          inputInfo.value !== originalInfo ||
          inputObs.value !== originalObs ||
          inputEmail.value !== originalEmail ||
          inputGDAP.value !== originalGDAP ||
          inputCobrancaRecorrente.value !== originalCobrancaRecorrente
      }}

      inputDomain.addEventListener('input', () => {{
        // transform h1 domain
        document.querySelector('h1').innerText = inputDomain.value
        document.querySelector('.btnAttClient').disabled = !checkInputsIsDifferent()
      }})

      inputInfo.addEventListener('input', () => {{
        document.querySelector('.btnAttClient').disabled = !checkInputsIsDifferent()
      }})

      inputObs.addEventListener('input', () => {{
        document.querySelector('.btnAttClient').disabled = !checkInputsIsDifferent()
      }})

      inputEmail.addEventListener('input', () => {{
        document.querySelector('.btnAttClient').disabled = !checkInputsIsDifferent()
      }})

      inputGDAP.addEventListener('input', () => {{
        document.querySelector('.btnAttClient').disabled = !checkInputsIsDifferent()
      }})

      inputCobrancaRecorrente.addEventListener('input', () => {{
        document.querySelector('.btnAttClient').disabled = !checkInputsIsDifferent()
      }})

      function sendInputValue() {{
        inputDomain.setAttribute('data-original', inputDomain.value)
        inputInfo.setAttribute('data-original', inputInfo.value)
        inputObs.setAttribute('data-original', inputObs.value)
        inputEmail.setAttribute('data-original', inputEmail.value)
        inputGDAP.setAttribute('data-original', inputGDAP.value)
        inputCobrancaRecorrente.setAttribute('data-original', inputCobrancaRecorrente.value)
        document.querySelector('.btnAttClient').disabled = !checkInputsIsDifferent()
      
        var actualizedInfoAndObs = {{
          domain: inputDomain.value,
          info: inputInfo.value,
          obs: inputObs.value,
          email: inputEmail.value,
          gdap: inputGDAP.value,
          cobrancaRecorrente: inputCobrancaRecorrente.value
        }}

        pywebview.api.update_client_info(actualizedInfoAndObs)
      }}

      function deleteCliente() {{
        pywebview.api.delete_client()
      }}

      function clickTableProductInClient(row) {{
        var string = row.dataset.id;
        pywebview.api.clickTableProductInClient(string).then(showResponse)
      }}

      function addProduct() {{
        pywebview.api.listProductsToAddInClient()
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
    tipo = "gdap" if gdap_or_cobranca_recorrente == "gdap" else "cobrancaRecorrente"

    html = f"""<select name="{tipo}" id="{tipo}" class="form-select"  data-original="?">
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

    html = html.replace('?', 'sim' if client[tipo] else 'nao')
    return html
