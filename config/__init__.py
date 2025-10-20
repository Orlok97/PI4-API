import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

twilio_config={
            "ACCOUNT_SID":os.getenv('ACCOUNT_SID'),
            "TOKEN":os.getenv('TWILIO_TOKEN'),
            "PHONE":os.getenv('TWILIO_TELEPHONE_NUMBER')
        }

class Config:
    def __init__(self, app):
        self.app=app
        self.config()
    def config(self):
        self.app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv('DATABASE_URI')
        self.app.config['JWT_SECRET_KEY']=os.getenv('SECRET_KEY')
        self.app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(weeks=4)
        self.app.json.sort_keys=False
        print("app configurado")
