from flask import Blueprint, jsonify

hello_bp=Blueprint('hello_bp',__name__)

@hello_bp.route('/',methods=['GET'])
def hello():
    return jsonify({
        "msg":"hello world"
    })