from pages.statics import list_products_to_add_in_client_page
from pages.statics import main_page
from pages.statics import client_page
from pages.statics import product_by_client_page
from pages.statics import add_product_to_client_page
from pages.statics import clients_page
from pages.statics import register_client_page
from pages.statics import products_page
from pages.statics import product_page
from pages.statics import register_products_page

class Pages():
  @property 
  def main_page(self):
    return main_page()

  def client_page(self, client_id):
    return client_page(client_id)

  def product_by_client_page(self, product_id):
    return product_by_client_page(product_id)

  def list_products_to_add_in_client_page(self):
    return list_products_to_add_in_client_page()

  def add_product_to_client_page(self, product_id):
    return add_product_to_client_page(product_id)

  @property
  def clients_page(self):
    return clients_page()

  def register_client_page(self):
    return register_client_page()

  @property
  def products_page(self):
    return products_page()
  
  def product_page(self, product_id):
    return product_page(product_id)
  
  def register_product_page(self):
    return register_products_page()