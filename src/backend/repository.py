from bson import ObjectId
from pymongo import MongoClient

class Repository:
  def __init__(self):
    # Conectar ao banco de dados
    client = MongoClient("mongodb+srv://vini:kIBaEiozt0Jq60Jp@cluster0.2zppx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client['Trials']

    self.__ClientCollection  = db['Clients']
    self.__productCollection = db['Products']

  def _create_client(self, client):
    return self.__ClientCollection.insert_one(client)

  def _find_clients(self):
    return list(self.__ClientCollection.find())

  def _find_client_by_domain(self, domain):
    return self.__ClientCollection.find_one({'domain': domain})

  def _find_client_by_id(self, _id):
    _id = ObjectId(_id)
    return self.__ClientCollection.find_one({'_id': _id})
  
  def _update_client(self, filter, update):
    self.__ClientCollection.update_one(filter, update)
    
  def _delete_client(self, _id):
    self.__ClientCollection.delete_one({'_id': _id})

  def _delete_client_by_domain(self, domain):
    self.__ClientCollection.delete_one({'domain': domain})
  
  # Products repository

  def _create_product(self, product):
    self.__productCollection.insert_one(product)

  def _find_products(self):
    return list(self.__productCollection.find())

  def _find_product_by_name(self, name):
    return self.__productCollection.find_one({'name': name})
  
  def _find_product_by_id(self, _id):
    return self.__productCollection.find_one({'_id': _id})

  def _update_product(self, filter, update):
    self.__productCollection.update_one(filter, update)

  def _delete_product(self, _id):
    self.__productCollection.delete_one({'_id': _id})
