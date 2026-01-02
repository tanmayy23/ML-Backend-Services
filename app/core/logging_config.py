import logging
# import os
from dotenv import load_dotenv

load_dotenv()

def setup_logging():
    logging.basicConfig(level = logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")

