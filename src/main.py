from globals import get_service
import webview
import webview.menu as wm
from frontend.api import Api
from frontend.events import Events
from pages import pages

class Window():
  def __init__(self):
    self.Events = Events()
    self.Service = get_service()

    api = Api()
    self.window = webview.create_window('Main Window', html='<h1>Carregando...</h1>', js_api=api, width=800, height=720,focus=True,)
    self.window.events.loaded += self.Events.on_loaded
    webview.start(menu=self.menu)

  def load_main_page(self):
    self.window.load_html(pages.main_page)

  def load_clients_page(self):
    self.window.load_html(pages.clients_page)

  def products_page(self):
    self.window.load_html(pages.products_page)

  @property
  def menu(self):
    return [
      wm.Menu(
        'Menu',
        [
          wm.MenuAction('Home', self.load_main_page),
          wm.MenuAction('Clientes', self.load_clients_page),
          wm.MenuAction('Produtos', self.products_page),
        ],
      ),
    ]

def click_me():
  active_window = webview.active_window()
  if active_window:
    active_window.load_html('<h1>You changed this window!</h1>')


if __name__ == '__main__':
  window = Window()
