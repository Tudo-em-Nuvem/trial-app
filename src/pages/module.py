from pages.statics import list_product_in_client_page
from pages.statics import main_page
from pages.statics import client_page
from pages.statics import product_by_client_page
from pages.statics import add_product_to_client_page

class Pages():
  @property 
  def main_page(self):
    return main_page()

  def client_page(self, client_id):
    return client_page(client_id)

  def product_by_client_page(self, product_id):
    return product_by_client_page(product_id)

  def list_products_in_client_page(self):
    return list_product_in_client_page()

  def add_product_to_client_page(self, product_id):
    return add_product_to_client_page(product_id)
