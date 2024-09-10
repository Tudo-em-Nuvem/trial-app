from bson import ObjectId
from frontend.events import Events
import sys
from globals import get_client_for_client_page, get_service, get_product_for_client, get_product_for_product_page
import datetime

class Api:
  def __init__(self):
    self.Events = Events()
    self.Service =  get_service()

  def init(self):
    response = {'message': 'Hello from Python {0}'.format(sys.version)}
    return response
  
  def clickTableClients(self, id):
    self.Events.open_client(id)

  def update_client_info(self, value):
    domain, attInfo, attObs, attEmail, attGDAP, attCobrancaRecorrente = value['domain'], value['info'], value['obs'], value['email'], value['gdap'], value['cobrancaRecorrente']
    client = get_client_for_client_page()
    updates = {}
 
    if domain != client['domain']:
      updates['domain'] = domain

    if attInfo != client['info']:
      updates['info'] = attInfo
    
    if attObs != client['obs']:
      updates['obs'] = attObs
    
    if attEmail != client['emailAdmin']:
      updates['emailAdmin'] = attEmail

    attGDAP = True if attGDAP == 'sim' else False
    if attGDAP != client['gdap']:
      updates['gdap'] = attGDAP

    attCobrancaRecorrente = True if attCobrancaRecorrente == 'sim' else False
    if attCobrancaRecorrente != client['cobrancaRecorrente']:
      updates['cobrancaRecorrente'] = attCobrancaRecorrente

    self.Service.update_client_by_id(client['_id'], updates)

  def clickTableProductInClient(self, id):
    self.Events.open_product_by_client(id)

  def update_product_by_client(self, value):
    price, licenses, date_renovation, expired = value['price'], value['licenses'], value['date_renovation'], value['expired']

    client = get_client_for_client_page()
    product = get_product_for_client()

    product_index = next((i for i, p in enumerate(client['produtos']) if p['_id'] == ObjectId(product['_id'])), None)

    if product_index is not None:
      client['produtos'][product_index]['price'] = float(price)
      client['produtos'][product_index]['licenses'] = int(licenses)
      client['produtos'][product_index]['expired'] = True if expired == 'sim' else False

      if date_renovation.strip() != '':
        date_renovation = datetime.datetime.strptime(date_renovation, '%Y-%m-%d')
        client['produtos'][product_index]['date_renovation'] = date_renovation

    self.Service.update_client_by_id(client['_id'], {'produtos': client['produtos']})
    self.Events.open_client(client['_id'])

  def remove_product_by_client(self):
    client = get_client_for_client_page()
    product = get_product_for_client()

    client['produtos'] = [p for p in client['produtos'] if p['_id'] != ObjectId(product['_id'])]

    self.Service.update_client_by_id(client['_id'], {'produtos': client['produtos']})
    self.Events.open_client(client['_id'])

  def clickTableProductToAddInClient(self, id):
    self.Events.open_product_to_add_in_client(id)

  def listProductsToAddInClient(self):
    self.Events.open_list_products_to_client()

  def addProductInClient(self, product):
    client = get_client_for_client_page()
    product['id'] = get_product_for_client()['_id']
    splitDate = product['date_renovation'].split('-')
    product['date_renovation']  = f"{splitDate[2]}/{splitDate[1]}/{splitDate[0]}"
    self.Service.add_product_to_client(client['domain'], product['id'], product['date_renovation'], int(product['licenses']), float(product['price']))
    self.Events.open_client(client['_id'])

  def open_register_client(self):
    self.Events.open_register_client()

  def registerClient(self, client):
    client = self.Service.register_client(client)
    self.Events.open_client(client.inserted_id)

  def click_table_product(self, product_id):
    self.Events.open_product(product_id)

  def delete_client(self):
    client = get_client_for_client_page()
    self.Service.delete_client_by_id(client['_id'])
    self.Events.open_clients()

  def update_product(self, value):
    product = get_product_for_product_page()
    name, price = value['name'], value['price']

    updates = {}
    if name != product['name']:
      updates['name'] = name

    if price != product['price']:
      updates['price'] = float(price)

    self.Service.update_product_by_id(product['_id'], updates)

  def delete_product(self):
    product = get_product_for_product_page()
    self.Service.delete_product_by_id(product['_id'])
    self.Events.open_products()

  def open_register_product(self):
    self.Events.open_register_product()
  
  def register_product(self, product):
    name, price = product['name'], product['price']
    price = float(price)
    product = self.Service.register_product(name, price)
    self.Events.open_product(product.inserted_id)

