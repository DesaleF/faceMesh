import os
import json
import yaml
import logging


# ++++++++++++++++++ # 
##  setup logging   ##
# ++++++++++++++++++ # 
log=logging.getLogger()
def setup_logging(default_path='logging.yaml', default_level=logging.DEBUG, env_key='LOG_CFG'):
    """Setup logging configuratio

    Args:
        default_path (str, optional): config file path. Defaults to 'logging.yaml'.
        default_level ([type], optional): logging level. Defaults to logging.DEBUG.
        env_key (str, optional): . Defaults to 'LOG_CFG'.
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
    
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


# +++++++++++++++++++ # 
##  save into json   ##
# +++++++++++++++++++ # 
def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f)
        
    
# +++++++++++++++++++ # 
##  load from json   ##
# +++++++++++++++++++ # 
def load_json(path):
    with open(path, "r") as f:
        return json.loads(f)
    

# ++++++++++++++++++++++++++++++ # 
##  create directory properly   ##
# ++++++++++++++++++++++++++++++ #  
def create_dir(path):    
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print("Path: {} already exists.",format(path))
    