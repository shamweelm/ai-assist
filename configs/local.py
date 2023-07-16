import os
from dotenv import load_dotenv
load_dotenv('.env')

CONNECTION_URL = os.getenv('CONNECTION_URL')