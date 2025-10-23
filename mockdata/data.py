rain_condition = [
    {
        'condicao': 'Normal',
        'altura': [0, 20],
        'fluxo': [0, 0.5],
        'status': 'Sem-Risco',
        'msg': ''
    },
    {
        'condicao': 'Chuva Moderada',
        'altura': [20, 40],
        'fluxo': [0.5, 1.0],
        'status': 'Monitoramento',
        'msg': ''
    },
    {
        'condicao': 'Chuva Forte',
        'altura': [40, 60],
        'fluxo': [1.0, 1.5],
        'status': 'Risco-Alagamento',
        'msg': 'Alerta: risco de alagamento.'
    },
    {
        'condicao': 'Enchente',
        'altura': [60, 300],
        'fluxo': [1.5, 2.5],
        'status': 'Risco-Enchente',
        'msg': 'Alerta máximo: risco de enchente!'
    }
]

sensors=[
    {
        "nome":"Estação 1",
        "local":"Canal 1",
        "altura":0,
        "fluxo":0,
        "nivel_maximo":150
    },
    {
        "nome":"Estação 2",
        "local":"Canal 2",
        "altura":0,
        "fluxo":0,
        "nivel_maximo":400
    },
    {
        "nome":"Estação 3",
        "local":"Canal 3",
        "altura":0,
        "fluxo":0,
        "nivel_maximo":200
    },
    {
        "nome":"Estação 4",
        "local":"Canal 4",
        "altura":0,
        "fluxo":0,
        "nivel_maximo":300
    }
]