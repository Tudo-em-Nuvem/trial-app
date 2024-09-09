from globals import get_service

service = get_service()

def register_client_page():
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
          padding: 0.375rem 0.75rem;
        }}

        .inLine {{
          display: flex;
          justify-content: space-between;
        }}

        .notInline {{
          margin-right: 1rem;
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

        .btn-primary[disabled] {{
          opacity: 0.65;
          cursor: not-allowed;
        }}
      </style>
    </head>
    <body>
      <div class="container-fluid">
        <h1>Registrar cliente</h1>

        <div class="mb-3">
          <label class="form-label">Domínio</label>
          <input type="text" id="domain" class="form-control">
        </div>

        <div class="mb-3">
          <label>Criação de Tenant</label>
          <input type="date" id="date_tenant" class="form-control">
        </div>

        <div class="mb-3">
          <label class="form-label">Informações</label>
          <input type="text" id="info" class="form-control">
        </div>

        <div class="mb-3">
          <label class="form-label">Observações</label>
          <input type="text" id="obs" class="form-control">
        </div>

        <div class="mb-3">
          <label class="form-label">E-mail Adm</label>
          <input type="text" id="email" class="form-control">
        </div>

        <div class="mb-3 inLine">
          <div class="notInline ">
            <label class="form-label">GDAP</label>
            <select name="gdap" id="gdap" class="form-select">
              <option value="sim">Sim</option>
              <option value="nao">Não</option>
            </select>
          </div>

          <div class="notInline ">
            <label class="form-label">Cobrança Recorrente</label>
            <select name="cobrancaRecorrente" id="cobrancaRecorrente" class="form-select">
              <option value="sim">Sim</option>
              <option value="nao">Não</option>
            </select>
          </div>
        </div>

        <div class="mb-3">
          <button class="btn btn-primary" onclick="registerClient()" disabled>Adicionar</button>
        </div>
      </div>
    </body>

    <script>
      function registerClient() {{
        const domain = document.getElementById('domain').value
        const date_tenant = document.getElementById('date_tenant').value
        const info = document.getElementById('info').value
        const obs = document.getElementById('obs').value
        const email = document.getElementById('email').value
        const gdap = document.getElementById('gdap').value
        const cobrancaRecorrente = document.getElementById('cobrancaRecorrente').value

        pywebview.api.registerClient({{
          domain,
          date_tenant,
          info,
          obs,
          email,
          gdap,
          cobrancaRecorrente
        }})
      }}

      function checkAllInputsHasValue() {{
        const domain = document.getElementById('domain').value
        const date_tenant = document.getElementById('date_tenant').value
        const info = document.getElementById('info').value
        const obs = document.getElementById('obs').value
        const email = document.getElementById('email').value

        return domain && info && date_tenant && obs && email
      }}

      document.getElementById('domain').onchange = function() {{
        document.querySelector('button').disabled = !checkAllInputsHasValue()
      }}

      document.getElementById('info').onchange = function() {{
        document.querySelector('button').disabled = !checkAllInputsHasValue()
      }}

      document.getElementById('obs').onchange = function() {{
        document.querySelector('button').disabled = !checkAllInputsHasValue()
      }}

      document.getElementById('date_tenant').onchange = function() {{
        document.querySelector('button').disabled = !checkAllInputsHasValue()
      }}

      document.getElementById('email').onchange = function() {{
        document.querySelector('button').disabled = !checkAllInputsHasValue()
      }}
    </script>
  </html>"""

  return html
