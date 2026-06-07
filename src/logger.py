import logging 
import os
from datetime import datetime
Log=f"{datetime.now().strftime('%m_%d_%Y_%H_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",Log)
os.makedirs(logs_path,exist_ok=True)
log_file_path=os.path.join(logs_path,Log)
logging.basicConfig(filename=log_file_path,
                    format="[%(asctime)s ] %(lineno)d %(name)s- %(levelname)s- %(message)s",
                    level=logging.INFO,
)
