from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.user import get_current_user
from twilio.rest import Client
from config import twilio_config
from random import randint
from models import db
from models.user import User

notification_bp=Blueprint('notification_bp',__name__)

rain_condition=[
    {
        'condicao':'Normal',
        'altura':[0, 20],
        'fluxo':[0, 0.5],
        'status':'Sem-Risco',
        'msg':''
    },
    {
        'condicao':'Chuva Moderada',
        'altura':[20, 40],
        'fluxo':[0.5, 1.0],
        'status':'Monitoramento',
        'msg':''
    },
    {
        'condicao':'alerta',
        'altura':[40, 60],
        'fluxo':[1.0, 1.5],
        'status':'Risco-Alagamento',
        'msg':'Alerta, risco de Alagamento'
    },
    {
        'condicao':'Enchente',
        'altura':[60, 200],
        'fluxo':[1.5, 2.5],
        'status':'Risco-Enchente',
        'msg':'Alerta, risco de enchente'
    }
]

def simulate_get_esp_data():
    current_rain_condition=rain_condition[randint(0,len(rain_condition)-1)]
    altura_min=current_rain_condition['altura'][0]
    altura_max=current_rain_condition['altura'][1]
    altura=randint(altura_min, altura_max)
    return {
        "status":current_rain_condition['status'],
        "altura":altura,
        "fluxo_de_agua":current_rain_condition['fluxo'][randint(0,1)],
        "msg":current_rain_condition['msg']
    }

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
@notification_bp.route('/', methods=['POST'])
def index():
    request_body=request.get_json()
    send_sms(request_body['telephone'])
    return jsonify({
        'response':'SMS enviado'
    })

@notification_bp.route('/simulate',methods=['GET'])
def simulate():
    users=db.session.execute(db.select(User).order_by(User.id)).scalars()
    data=simulate_get_esp_data()
    if data['status'] == 'Risco-Enchente' or data['status'] == 'Risco-Alagamento':
        for user in users:
            send_sms(user.telephone, data['msg'])
    return jsonify(data)