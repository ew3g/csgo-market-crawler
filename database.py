import logging
import pymongo

class Database():
    
    def __init__(self, database_url):
        client = pymongo.MongoClient(database_url)
        db = client['cs-info']
        if 'name_idx' not in db.profiles.index_information():
            db.profiles.create_index([('name', pymongo.TEXT)], unique=True, name='name_idx')
        self.db = db
    
    def insert_item(self, item):
        item_collection = self.db['item']
        existing_item = item_collection.find_one({'name': item['name']})
        if not existing_item:
            logging.info(f'Saving {item} to collection item')
            item_collection.insert_one(item)