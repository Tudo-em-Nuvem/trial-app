import sys
import webview
import webview.menu as wm
from service import Service

class Api:
  def __init__(self):
    self.Events = Events()
    self.Service=  Service()
  def init(self):
    response = {'message': 'Hello from Python {0}'.format(sys.version)}
    return response
  
  def clickTableClients(self, id):
    self.Events.open_client(id)

  def update_client_info(self, client, value):
    attInfo = value['info']
    attObs = value['obs']

    if attInfo != client['Info'] :
      self.Service.update_client_by_id(client, {'Info': attInfo})

    if attObs != client['Obs']:
      self.Service.update_client_by_id(client, {'Obs': attObs})

    print(value)

class Pages():
  def __init__(self):
    self.Service = Service()

  @property 
  def main_page(self):
    return f"""<html>
      <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <style>

          .info {{
            display: flex;
            justify-content: center;
          }}

          .item {{
            color: white;
            background-color: #23272a;
            margin: 10px;
            align-items: center;
            padding: 10px;
            border-radius: 5px;
          }}

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
          <h3>Próximas renovações</h3>
          {self._get_menu_clients()}
        </div>

        <div class="container-fluid info"> 
          <div class="item">
            <h3>Quantidade de Clientes</h3>
            <h4>{len(self.Service.list_clients())}</h4>	
          </div>

          <div class="item">
            <h3>Total de licenças</h3>
            <h4>{sum([licencas for client in self.Service.list_clients() for licencas in [licencas for produto in client['produtos'] for licencas in [produto['licences']]]])}</h4>
          </div>

          <div class="item">
            <h3>Valor de Trial/Mensal</h3>
            <h4>{sum(produto['price'] * produto['licences'] for client in self.Service.list_clients() for produto in client['produtos'])}</h4>
          </div>

        </div>
      </body>
      <script>
        function clickTableClients(row) {{
          var string = row.dataset.id;
          pywebview.api.clickTableClients(string).then(showResponse)
        }}
      </script>
    </html>
"""

  def client_page(self, client_id):
    client = self.Service.find_client_with_id(client_id)
    return f"""<html>
      <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <style>
          body {{
            color: white;
            background-color: #2c2f33;
            }}
          
          .table {{
            padding: 10px;
          }}
        </style>
      </head>
      <body>
        <div class="container-fluid">
          <h1>{client['domain']}</h1>
          <div class="mb-3">
            <label class="form-label">Informações</label>
            <input type="text" id="info" value="{client['Info']}" class="form-control" >
          </div>
          <div class="mb-3">
            <label class="form-label">Observações</label>
            <input type="text" id="obs" value="{client['Obs']}" class="form-control" >
          </div>
          {self._get_menu_products_by_client(client)}
            <button type="button" class="btn btn-primary" onclick="sendInputValue()">Atualizar Cliente</button>
        </div>
      </body>
      <script>
        inputInfo = document.getElementById('info')
        inputObs = document.getElementById('obs')

        function sendInputValue() {{
          atualizedInfoAndObs = {{
            info: inputInfo.value,
            obs: inputObs.value
          }}

          pywebview.api.update_client_info({client}, atualizedInfoAndObs).then(showResponse)
        }}
      </script>
    </html>
"""

  def _get_menu_clients(self):
    clients = self.Service.list_clients()[0:5]

    return f"""<table class="table"><tr> <th scope="col">Domínio</th><th scope="col">Data</th></tr>
          {"".join([f"<tr data-id={client["_id"]} onclick='clickTableClients(this)'><td>{client['domain']}</td> <td>{min([product['date_renovation'] for product in client['produtos']]).strftime("%d/%m/%Y")}</td></tr>" for client in clients])}
        </table>
    """

  def _get_menu_products_by_client(self, client):
    return f"""<table class="table"><tr> <th scope="col">Produto</th><th scope="col">licencas</th><th scope="col">Valor</th><th scope="col">total</th><th scope="col">Renovação</th></tr>
          {"".join([f"<tr><td>{product['name']}</td> <td>{product['licences']}</td><td>$ {product['price']}</td><td>$ {product['price'] * product['licences']}</td><td>{product['date_renovation'].strftime("%d/%m/%Y")}</td></tr>" for product in client['produtos']])}
"""
class Events():
  def __init__(self):
    self.Pages = Pages()
    self.Service = Service()

  def on_loaded(self, window):
    window.events.loaded -= self.on_loaded
    window.load_html(self.Pages.main_page)    

  def open_client(self, client_id):
    active_window = webview.active_window()
    if active_window:
      page = self.Pages.client_page(client_id=client_id)
      active_window.load_html(page)

class Window():
  def __init__(self):
    self.Events = Events()
    self.Service = Service()
    self.Pages = Pages()

    self.html = '<h1>Carregando...</h1>'
    api = Api()
    self.window = webview.create_window('Main Window', html=self.html, js_api=api)
    self.window.events.loaded += self.Events.on_loaded
    print('a')
    webview.start(menu=self.menu)

  def load_main_page(self):
    self.window.load_html(self.Pages.main_page)

  @property
  def menu(self):
    return [
      wm.Menu(
        'Menu',
        [
          wm.MenuAction('Home', self.load_main_page),
          wm.MenuAction('Clientes', change_active_window_content),
          wm.MenuAction('Produtos', click_me),
        ],
      ),
    ]

def change_active_window_content():
  active_window = webview.active_window()
  if active_window:
    active_window.load_html('<h1>You changed this window!</h1>')

def click_me():
  active_window = webview.active_window()
  if active_window:
    active_window.load_html('<h1>You clicked me!</h1>')

def say_this_is_window_2():
  active_window = webview.active_window()
  if active_window:
    active_window.load_html('<h1>This is window 2</h2>')

if __name__ == '__main__':
  window = Window()
