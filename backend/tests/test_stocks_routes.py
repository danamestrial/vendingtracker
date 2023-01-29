import requests
import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv('HOST', '127.0.0.1')
port = os.getenv('PORT', '5000')