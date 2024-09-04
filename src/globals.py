from backend.service import Service

client_for_client_page = None
get_client_for_client_page = lambda: client_for_client_page

def set_client_for_client_page(client):
  global client_for_client_page
  client_for_client_page = client
  return client_for_client_page

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
