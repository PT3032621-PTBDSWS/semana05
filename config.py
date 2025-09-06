import os
from dotenv import load_dotenv


# Carrega variáveis de ambiente
load_dotenv()


class Config:
SECRET_KEY = os.getenv("SECRET_KEY", "change-this-in-production")
WTF_CSRF_TIME_LIMIT = None # evita expiração curta em dev
