from bson import ObjectId
from frontend.events import Events
import sys
from globals import get_client_for_client_page, get_service, get_product_for_client
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
    domain, attInfo, attObs, attEmail, attGDAP, attCobrancaRecorrente = value['domain'], value['info'], value['obs'], value['email'], value['GDAP'], value['cobrancaRecorrente']
    client = get_client_for_client_page()
    updates = {}
 
    if domain != client['domain']:
      updates['domain'] = domain

    if attInfo != client['Info']:
      updates['Info'] = attInfo
    
    if attObs != client['Obs']:
      updates['Obs'] = attObs
    
    if attEmail != client['emailAdmin']:
      updates['emailAdmin'] = attEmail

    attGDAP = True if attGDAP == 'sim' else False
    if attGDAP != client['GDAP']:
      updates['GDAP'] = attGDAP

    attCobrancaRecorrente = True if attCobrancaRecorrente == 'sim' else False
    if attCobrancaRecorrente != client['cobrancaRecorrente']:
      updates['cobrancaRecorrente'] = attCobrancaRecorrente

    self.Service.update_client_by_id(client['_id'], updates)

  def clickTableProductInClient(self, id):
    self.Events.open_product(id)

  def update_product_by_client(self, value):
    price, licenses, date_renovation = value['price'], value['licenses'], value['date_renovation']

    client = get_client_for_client_page()
    product = get_product_for_client()

    product_index = next((i for i, p in enumerate(client['produtos']) if p['_id'] == ObjectId(product['_id'])), None)

    if product_index is not None:
      client['produtos'][product_index]['price'] = float(price)
      client['produtos'][product_index]['licenses'] = int(licenses)

      if date_renovation.strip() != '':
        date_renovation = datetime.datetime.strptime(date_renovation, '%Y-%m-%d')
        client['produtos'][product_index]['date_renovation'] = date_renovation

    self.Service.update_client_by_id(client['_id'], {'produtos': client['produtos']})

  def remove_product_by_client(self):
    client = get_client_for_client_page()
    product = get_product_for_client()

    client['produtos'] = [p for p in client['produtos'] if p['_id'] != ObjectId(product['_id'])]

    self.Service.update_client_by_id(client['_id'], {'produtos': client['produtos']})
    self.Events.open_client(client['_id'])

  def clickTableProductInClient(self, id):
    self.Events.open_product_to_add_in_client(id)

  def addProductInClient(self):
    #client = get_client_for_client_page()
    self.Events.open_list_products_to_client()