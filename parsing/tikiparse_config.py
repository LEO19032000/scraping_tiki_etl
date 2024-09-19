import os
import yaml

class ConfigObject:
    def __init__(self, save_path, website_path, page_number, dataframe):
        self.save_path = save_path
        self.website_path = website_path
        self.page_number = page_number
        self.dataframe = dataframe

    def __str__(self):
        return f"save_path: {self.save_path}, website_path: {self.website_path}, page_number: {self.page_number}, dataframe: {self.dataframe}"
    
# Get the directory of the script
script_dir = os.path.dirname(__file__)
# Construct the path to the YAML file
yaml_path = os.path.join(script_dir, "parse_config.yml")

with open(yaml_path, 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)
    
    config_obj_list = []
    for section in cfg:
        save_path = cfg[section]['path']['save_path']
        website_path = cfg[section]['path']['website_path']
        page_number = cfg[section]['page']['page_number']
        dataframe = cfg[section]['dataframe']
        config_obj_list.append(ConfigObject(save_path, website_path, page_number, dataframe))
        
def get_config():
    return {
        'save_path': save_path,
        'website_path': website_path,
        'page_number': page_number,
        'dataframe': dataframe
    }

