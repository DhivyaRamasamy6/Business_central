import logging
import os
import sys
from datetime import datetime
LOG_DIR="logs"
#log folder creation
os.makedirs(LOG_DIR,exist_ok=True)
LOG_FILE=os.path.join(LOG_DIR,f"log_ {datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
      handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stderr)
        ]
)
#logger
def get_logger(name):
    logger=logging.getLogger(name)
    return logger


# Reduce third-party library logs
logging.getLogger("azure").setLevel(logging.WARNING)
logging.getLogger("azure.identity").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("openai").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

