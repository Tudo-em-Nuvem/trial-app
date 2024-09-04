import datetime
from bson import ObjectId
import pytz
from backend.repository import Repository

class Service(Repository):
  def __init__(self):
    super().__init__()

  def register_client(self, domain, tenantCreation, GDAP, CobrançaRecorrente, Info, Obs, emailAdmin):
    if self._find_client_by_domain(domain):
      raise Exception('Client already exists')
    self._create_client(domain, tenantCreation, GDAP, CobrançaRecorrente, Info, Obs, emailAdmin)

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

    date =self._convert_date_time(date_renovation)
    product['date_renovation'] = date

    product['licenses'] = licenses
    product['price'] = price if price else product['price']

    client = self._find_client_by_domain(domain)
    client['produtos'].append(product)
    self._update_client({'domain': domain}, {'$set': {'produtos': client['produtos']}})

  def remove_product_from_client(self, domain, id_product):
    client = self._find_client_by_domain(domain)
    client['produtos'] = list(filter(lambda product: product['_id'] != id_product, client['produtos']))
    self._update_client({'domain': domain}, {'$set': {'produtos': client['produtos']}})

  def register_product(self, name, price):
    if self._find_product_by_name(name):
      raise Exception('Product already exists')

    self._create_product(name, price)

  def list_products(self):
    return self._find_products()

  def _convert_date_time(self, date):
    date_obj = datetime.datetime.strptime(date, '%d/%m/%Y')
    date_utc = date_obj.replace(tzinfo=pytz.UTC)
    return date_utc

  def get_clients_by_date_products(self) -> list[object]:
    clients = self._find_clients()

    def get_min_date(client):
      product_dates = [product['date_renovation'] for product in client['produtos']]
      return min(product_dates)

    clients.sort(key=lambda client: get_min_date(client))
    return clients
