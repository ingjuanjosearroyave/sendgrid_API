import os
from dotenv import load_dotenv
load_dotenv()

SENDGRID_API_KEY = os.getenv('API_KEY')
FROM_EMAIL = 'juanjosearroyave0401@gmail.com'
TO_EMAIL = ''