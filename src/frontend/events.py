import webview
from globals import get_service
from pages import pages

class Events():
  def __init__(self):
    self.Service = get_service()

  def on_loaded(self, window: webview.Window):
    window.events.loaded -= self.on_loaded
    window.load_html(pages.main_page)    

  def open_client(self, client_id):
    active_window = webview.active_window()
    if active_window:
      page = pages.client_page(client_id=client_id)
      active_window.load_html(page)

  def open_product(self, product_id):
    active_window = webview.active_window()
    if active_window:
      page = pages.product_by_client_page(product_id=product_id)
      active_window.load_html(page)

  def open_list_products_to_client(self):
    active_window = webview.active_window()
    if active_window:
      page = pages.list_products_in_client_page()
      active_window.load_html(page)

  def open_product_to_add_in_client(self, product_id):
    active_window = webview.active_window()
    if active_window:
      page = pages.add_product_to_client_page(product_id=product_id)
      active_window.load_html(page)