from flask import jsonify, request
from sqlalchemy import and_
import requests

from models.models import *
from app import app
from serializers.serializer import exchanges_schema


@app.route('/api/exchanges', methods=['GET'])
def get_exchanges_all():
    exchanges = Exchange.query.all()
    response = exchanges_schema.dump(exchanges)

    return jsonify(response)


@app.route('/api/exchanges/history', methods=['GET'])
def get_exchange_filter():
    filter_args = []
    if request.args.get('valcode'):
        filter_args.append(Exchange.cc.like(request.args.get('valcode')))
    if request.args.get('date'):
        filter_args.append(Exchange.exchangedate.like(request.args.get('date')))

    exchanges = Exchange.query.filter(and_(*filter_args))
    response = exchanges_schema.dump(exchanges)

    return jsonify(response)


@app.route('/api/exchanges/current_rate', methods=['GET'])
def get_current_rate():
    valcode = request.args.get('valcode')
    api_nbu = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&json'

    response = requests.get(api_nbu)
    data = response.json()

    return jsonify(data)
