import os
import logging
from datetime import datetime

#datetime object containing current date and time
Log_file = f"{datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}.log"
#make a directory called logs in the current working directory if it doesn't exist
Log_path = os.path.join(os.getcwd(), "logs", Log_file)
#make a directory called logs in the current working directory if it doesn't exist
os.makedirs(Log_path, exist_ok=True)
#join path to the log file

log_file_path= os.path.join(Log_path, Log_file)
#basic configuration for logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    
)

