from backend.service import Service

_client_for_client_page = None
get_client_for_client_page = lambda: _client_for_client_page

def set_client_for_client_page(client):
  global _client_for_client_page
  _client_for_client_page = client
  return _client_for_client_page

defined_service = False
service = None

def get_service():
  global defined_service
  if not defined_service:
    defined_service = True
    global service
    service = Service()
  return service

product_for_client = None
get_product_for_client = lambda: product_for_client

def set_product_for_client(product):
  global product_for_client
  product_for_client = product
  return product_for_client

_product_for_product_page = None
get_product_for_product_page = lambda: _product_for_product_page
def set_product_for_product_page(product):
  global _product_for_product_page
  _product_for_product_page = product
  return _product_for_product_page
