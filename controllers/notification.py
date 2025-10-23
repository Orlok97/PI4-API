from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.user import get_current_user
from twilio.rest import Client
from config import twilio_config
from random import randint, uniform, choice
from models import db
from models.user import User
from mockdata.data import sensors, rain_condition
import requests

notification_bp=Blueprint('notification_bp',__name__)

def generate_random_weather():
    return choice(rain_condition)

def get_sensor_data():
    response=requests.get('https://pi4univesp.dservicos.online/')
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return {
            'response':'Endpoint não encontrado'
        }
    else:
        return {
            'response':'Sensor desativado no momento',
            'status_code':response.status_code
        }

def simulate_get_esp_data():
    sensor_list=[]
    for i in range(len(sensors)):
        current_condition=generate_random_weather()

        altura_min=current_condition['altura'][0]
        altura_max=current_condition['altura'][1]

        fluxo_min=current_condition['fluxo'][0]
        fluxo_max=current_condition['fluxo'][1]

        sensor_altura=randint(altura_min, altura_max)
        sensor_fluxo=round(uniform(fluxo_min, fluxo_max),2)

        sensors[i]['altura']=sensor_altura
        sensors[i]['fluxo']=sensor_fluxo
        sensors[i]['status']=current_condition['status']
        sensor_list.append(sensors[i])
    return sensor_list
        

def send_sms(tel, msg):
    account_sid=twilio_config['ACCOUNT_SID']
    token=twilio_config['TOKEN']
    client = Client(account_sid, token)
    message = client.messages.create(
        body=msg,
        to=tel,
        from_=twilio_config['PHONE']
    )
    print(message.body)

def sms_to_current_user(msg, user_phone):
    account_sid=twilio_config['ACCOUNT_SID']
    token=twilio_config['TOKEN']
    client = Client(account_sid, token)
    message = client.messages.create(
        body=msg,
        to=user_phone,
        from_=twilio_config['PHONE']
        
    )
@notification_bp.route('/', methods=['GET'])
def index():
    data=get_sensor_data()
    return jsonify(data)

@notification_bp.route('/simulate',methods=['GET'])
def simulate():
    data=simulate_get_esp_data()
    return jsonify(data)