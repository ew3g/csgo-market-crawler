import logging
from typing import NamedTuple
import os
import dotenv
from item_subtype import ItemSubType
from steam_item_crawler import SteamItemCrawler

dotenv.load_dotenv()
logging.basicConfig(level=logging._nameToLevel[os.getenv('LOG_LEVEL')])

class ConfigParameters(NamedTuple):
    page_control_var_name: str
    item_query: str
    item_type: str
    item_subtype: str

def get_config_parameters(item_subtype):
    if ItemSubType.KNIFE == item_subtype:
        config_parameters = ConfigParameters(page_control_var_name='LAST_PROCESSED_PAGE_KNIFE', 
                                            item_query='&category_730_Type[]=tag_CSGO_Type_Knife', item_type='weapon', item_subtype='knife')
    elif ItemSubType.PISTOL == item_subtype:
        config_parameters = ConfigParameters(page_control_var_name='LAST_PROCESSED_PAGE_PISTOL', 
                                            item_query='&category_730_Type[]=tag_CSGO_Type_Pistol', item_type='weapon', item_subtype='pistol')
    elif ItemSubType.RIFLE == item_subtype:
        config_parameters = ConfigParameters(page_control_var_name='LAST_PROCESSED_PAGE_RIFLE', 
                                            item_query='&category_730_Type[]=tag_CSGO_Type_Rifle', item_type='weapon', item_subtype='rifle')
    elif ItemSubType.SHOTGUN == item_subtype:
        config_parameters = ConfigParameters(page_control_var_name='LAST_PROCESSED_PAGE_SHOTGUN', 
                                            item_query='&category_730_Type[]=tag_CSGO_Type_Shotgun', item_type='weapon', item_subtype='shotgun')
    elif ItemSubType.SNIPER == item_subtype:
        config_parameters = ConfigParameters(page_control_var_name='LAST_PROCESSED_PAGE_SNIPER', 
                                            item_query='&category_730_Type[]=tag_CSGO_Type_SniperRifle', item_type='weapon', item_subtype='sniper')
    elif ItemSubType.MACHINEGUN == item_subtype:
        config_parameters = ConfigParameters(page_control_var_name='LAST_PROCESSED_PAGE_MACHINEGUN', 
                                            item_query='&category_730_Type[]=tag_CSGO_Type_Machinegun', item_type='weapon', item_subtype='machinegun')
    elif ItemSubType.SMG == item_subtype:
        config_parameters = ConfigParameters(page_control_var_name='LAST_PROCESSED_PAGE_SMG', 
                                            item_query='&category_730_Type[]=tag_CSGO_Type_SMG', item_type='weapon', item_subtype='smg')
    elif ItemSubType.GLOVE == item_subtype:
        config_parameters = ConfigParameters(page_control_var_name='LAST_PROCESSED_PAGE_GLOVE', 
                                            item_query='LAST_PROCESSED_PAGE_GLOVE', item_type='weapon', item_subtype='glove')
    return config_parameters

def crawl(config_parameters: ConfigParameters):    
    last_processed_page = int(os.getenv(config_parameters.page_control_var_name))

    steam_item_crawler = SteamItemCrawler(os.getenv('STEAM_API_KEY'), int(os.getenv('BATCH_SIZE')), os.getenv('DATABASE_URL'), '.env')
    steam_item_crawler.enrich_data(config_parameters.item_query, last_processed_page, config_parameters.page_control_var_name, 
                                   config_parameters.item_type, config_parameters.item_subtype)

crawl(get_config_parameters(ItemSubType.KNIFE))
crawl(get_config_parameters(ItemSubType.PISTOL))
crawl(get_config_parameters(ItemSubType.RIFLE))
crawl(get_config_parameters(ItemSubType.SHOTGUN))
crawl(get_config_parameters(ItemSubType.SNIPER))
crawl(get_config_parameters(ItemSubType.MACHINEGUN))
crawl(get_config_parameters(ItemSubType.SMG))
crawl(get_config_parameters(ItemSubType.GLOVE))