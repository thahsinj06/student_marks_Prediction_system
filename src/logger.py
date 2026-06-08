import logging
import os
from datetime import datetime

# log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# logs folder path
logs_dir = os.path.join(os.getcwd(), "logs")

# create logs folder
os.makedirs(logs_dir, exist_ok=True)

# full log file path
log_file_path = os.path.join(logs_dir, LOG_FILE)

# logging config
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger()