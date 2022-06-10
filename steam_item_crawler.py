import dotenv
import json
import logging
import math
import random
from database import Database
from steam_request import SteamRequest
from timer import Timer

class SteamItemCrawler():

    def __init__(self, steam_api_key, batch_size, database_url, env_file_name):
        self.steam_api_key = steam_api_key
        self.batch_size = batch_size
        self.env_file_name = env_file_name
        self.db = Database(database_url)


    def enrich_item_list(self, query_item, item_list, last_processed_page, control_env_variable_processed_page, type, subtype, file_name):
        steam_request = SteamRequest(self.steam_api_key)
        total_items = steam_request.make_request(query=query_item, max_results=1)['total_count']

        total_pages = math.ceil(total_items / self.batch_size)

        logging.info(f'Total Items: {total_items}')
        logging.info(f'Pages: {total_pages}')

        page_to_process = last_processed_page + 1
    
        for i in range(page_to_process * self.batch_size, total_items+self.batch_size, self.batch_size):
            Timer.pause(random.uniform(10, 30))
       
            page_to_process = math.ceil(i / self.batch_size)
            dotenv.set_key('.env', control_env_variable_processed_page, str(page_to_process))

            batch_start = i
            batch_end = i + self.batch_size

            logging.info(f'Fetching items of page {page_to_process}/{total_pages}')
        
            items = steam_request.make_request(query=f'start={batch_start}{query_item}', max_results=self.batch_size)
    
            logging.info(f'Items: {batch_start} - {batch_end}')

            result_list = items['results']
    
            for item in result_list:
                item_list.append({
                    'name': item['name'],
                    'type': type,
                    'subtype': subtype,
                    'game_type': item['asset_description']['type']
                })


    def enrich_data(self, query_item, last_processed_page, control_env_variable_processed_page, type, subtype):
        steam_request = SteamRequest(self.steam_api_key)
        total_items = steam_request.make_request(query=query_item, max_results=1)['total_count']

        total_pages = math.ceil(total_items / self.batch_size)

        logging.info(f'Total Items: {total_items}')
        logging.info(f'Pages: {total_pages}')

        page_to_process = last_processed_page + 1
    
        for i in range(page_to_process * self.batch_size, total_items+self.batch_size, self.batch_size):
            Timer.pause(random.uniform(10, 30))
       
            page_to_process = math.ceil(i / 50)
            dotenv.set_key('.env', control_env_variable_processed_page, str(page_to_process))

            batch_start = i
            batch_end = i + self.batch_size

            logging.info(f'Fetching items of page {page_to_process}/{total_pages}')
        
            items = steam_request.make_request(query=f'start={batch_start}{query_item}', max_results=self.batch_size)
    
            logging.info(f'Items: {batch_start} - {batch_end}')

            result_list = items['results']
    
            for steam_item in result_list:
                item = {
                    'name': steam_item['name'],
                    'type': type,
                    'subtype': subtype,
                    'game_type': steam_item['asset_description']['type']
                }
                self.db.insert_item(item)