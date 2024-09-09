import datetime
from bson import ObjectId
import pytz
from backend.repository import Repository

class Service(Repository):
  def __init__(self):
    super().__init__()

  # Clients Service

  def register_client(self, client):
    if self._find_client_by_domain(client['domain']):
      raise Exception('Client already exists')
    
    gdap = True if client['gdap'] == 'sim' else False
    cobranca_recorrente = True if client['cobrancaRecorrente'] == 'sim' else False
    tenant_creation = datetime.datetime.strptime(client['date_tenant'], '%Y-%m-%d')

    client = {
      'domain'            : client['domain'],
      'tenantCreation'    : tenant_creation,
      'produtos'          : [],
      'gdap'              : gdap,
      'cobrancaRecorrente': cobranca_recorrente,
      'info'              : client['info'],
      'obs'               : client['obs'],
      'emailAdmin'        : client['email']
    }

    return self._create_client(client)

  def list_clients(self):
    return self._find_clients()

  def find_client_with_domain(self, domain):
    return self._find_client_by_domain(domain)

  def find_client_with_id(self, id):
    return self._find_client_by_id(id)

  def update_client_by_id(self, id, fields):
    id = ObjectId(id)
    self._update_client({'_id': id}, {'$set': fields})

  def add_product_to_client(self, domain, id_product, date_renovation, licenses, price = None):
    product = self._find_product_by_id(id_product)

    if not product:
      raise Exception('Product not found')

    date = self._convert_date_time(date_renovation)
    product['_id'] = ObjectId()
    product['product_id'] = product['_id']
    product['date_renovation'] = date
    product['licenses'] = licenses
    product['price'] = price if price else product['price']
    product['expired'] = False

    client = self._find_client_by_domain(domain)
    client['produtos'].append(product)
    self._update_client({'domain': domain}, {'$set': {'produtos': client['produtos']}})

  def remove_product_from_client(self, domain, id_product):
    client = self._find_client_by_domain(domain)
    client['produtos'] = list(filter(lambda product: product['_id'] != id_product, client['produtos']))
    self._update_client({'domain': domain}, {'$set': {'produtos': client['produtos']}})

  def get_clients_by_date_products(self) -> list[object]:
    clients = [clients for clients in self._find_clients() if len(clients["produtos"]) > 0]

    def get_min_date(client):
      product_dates = [product['date_renovation'] for product in client['produtos']]
      return min(product_dates)

    clients.sort(key=lambda client: get_min_date(client))
    return clients

  def delete_client_by_id(self, id):
    self._delete_client(ObjectId(id))
 
  # Products Service

  def register_product(self, name, price):
    if self._find_product_by_name(name):
      raise Exception('Product already exists')

    product = {"name": name, "price": price}

    return self._create_product(product)

  def update_product_by_id(self, id, fields):
    id = ObjectId(id)
    self._update_product({'_id': id}, {'$set': fields})

  def list_products(self):
    return self._find_products()

  def find_product_by_id(self, _id):
    return self._find_product_by_id(ObjectId(_id))

  def delete_product_by_id(self, id):
    self._delete_product(ObjectId(id))

  # Private methods

  def _convert_date_time(self, date):
    date_obj = datetime.datetime.strptime(date, '%d/%m/%Y')
    date_utc = date_obj.replace(tzinfo=pytz.UTC)
    return date_utc

