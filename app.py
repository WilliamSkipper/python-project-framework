from utils.resource_path import resource_path
from utils.os_path import os_path
from utils.log import log
from utils.config import load_config
import os

# Define application name
config = load_config()
version = '.'.join(map(str, config['version']))

log(f"App Started, Version: {version}")