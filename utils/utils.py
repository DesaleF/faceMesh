import os
import json
import logging
import colorlog


# ++++++++++++++++++ # 
##  setup logging   ##
# ++++++++++++++++++ # 
log=logging.getLogger()
def setup_logging(folder="log", filename="log_info.log", default_level=logging.DEBUG):
    """Setup logging configuratio

    Args:
        folder (str, optional): path to save logs. default log.
        filename (str, optional): filenames to save the logs.
    """

    log_colors = {
        'DEBUG': 'blue',
        'INFO': 'white',
        'WARNING': 'green',
        'ERROR': 'red',
        'CRITICAL': 'yellow',
    }
    logger = logging.getLogger('FACEMESH')
    LOGFORMAT = "%(log_color)s%(asctime)s [%(log_color)s%(filename)s:%(lineno)d] | %(log_color)s%(message)s%(reset)s |"
    LOG_LEVEL = default_level
    if not os.path.isdir(folder):
        os.makedirs(folder)
        
    logging.root.setLevel(LOG_LEVEL)
    stream = logging.StreamHandler()
    stream.setLevel(LOG_LEVEL)
    stream.setFormatter(colorlog.ColoredFormatter(LOGFORMAT, datefmt='%d %H:%M', log_colors=log_colors))

    # print to log file
    hdlr = logging.FileHandler(os.path.join(folder, filename))
    hdlr.setLevel(LOG_LEVEL)
    hdlr.setFormatter(logging.Formatter("[%(asctime)s] %(message)s"))

    logger.addHandler(hdlr)
    logger.addHandler(stream)
    return logger


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
    