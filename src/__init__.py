import os
import sys
import logging
from pathlib import Path 

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_filepath = os.path.join(log_dir,"running_logs.log")


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(Path(log_filepath)),
        logging.StreamHandler(sys.stdout)
    ]
)


logger = logging.getLogger('loanPrediction')