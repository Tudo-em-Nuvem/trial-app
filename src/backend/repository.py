from bson import ObjectId
from pymongo import MongoClient

class Repository:
  def __init__(self):
    # Conectar ao banco de dados
    client = MongoClient("mongodb+srv://vini:kIBaEiozt0Jq60Jp@cluster0.2zppx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client['Trials']

    self.ClientCollection  = db['Clients']
    self.productCollection = db['Products']

  def _create_client(self, domain, tenantCreation, GDAP, CobrancaRecorrente, Info, Obs, emailAdmin):
    if self.ClientCollection.find_one({'domain': domain}):
      raise Exception('Client already exists')

    self.ClientCollection.insert_one({
      'domain'            : domain,
      'tenantCreation'    : tenantCreation,
      'produtos'          : [],
      'GDAP'              : GDAP,
      'cobrancaRecorrente': CobrancaRecorrente,
      'Info'              : Info,
      'Obs'               : Obs,
      'emailAdmin'        : emailAdmin
    })

  def _find_clients(self):
    return list(self.ClientCollection.find())

  def _find_client_by_domain(self, domain):
    return self.ClientCollection.find_one({'domain': domain})

  def _find_client_by_id(self, _id):
    _id = ObjectId(_id)
    return self.ClientCollection.find_one({'_id': _id})
  
  def _update_client(self, filter, update):
    self.ClientCollection.update_one(filter, update)
    
  def _delete_client(self, _id):
    self.ClientCollection.delete_one({'_id': _id})

  def _delete_client_by_domain(self, domain):
    self.ClientCollection.delete_one({'domain': domain})
  
  def _create_product(self, name, price):
    if self.productCollection.find_one({'name': name}):
      raise Exception('Product already exists')

    self.productCollection.insert_one({
    'name'  : name,
    'price' : price
    })

  def _find_products(self):
    return list(self.productCollection.find())

  def _find_product_by_name(self, name):
    return self.productCollection.find_one({'name': name})
  
  def _find_product_by_id(self, _id):
    return self.productCollection.find_one({'_id': _id})

  def _update_product(self, filter, update):
    self.productCollection.update_one(filter, update)

  def _delete_product(self, _id):
    self.productCollection.delete_one({'_id': _id})
