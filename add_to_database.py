import requests
from flask import jsonify
from sqlalchemy import and_
from celery import Celery

import config
from models.models import *
from app import db, app
from serializers.serializer import exchanges_schema


celery_beat_schedule = {
      "time_scheduler": {
          "task": "add_to_database.save_to_db",
          "schedule": 30.0,
      }
  }

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(
    result_backend=app.config["CELERY_RESULT_BACKEND"],
    timezone="UTC",
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    beat_schedule=celery_beat_schedule,
)


def save(el):
    r030 = el['r030']
    txt = el['txt']
    rate = el['rate']
    cc = el['cc']
    exchangedate = el['exchangedate']

    exchange = Exchange(r030, txt, rate, cc, exchangedate)

    db.session.add(exchange)
    db.session.commit()


@celery.task
def save_to_db():
    api_nbu = config.Config.API_URL

    response = requests.get(api_nbu)
    data = response.json()
    exchange_lst = []
    exchange_code = ['USD', 'RUB', 'PLN', 'EUR', 'CAD']
    for exchange in data:
        if exchange['cc'] in exchange_code:
            exchange_lst.append(exchange)

    database = Exchange.query.all()
    res_database = exchanges_schema.dump(database)
    if not res_database:
        for el in exchange_lst:
            save(el=el)
    else:
        for el in exchange_lst:
            data_el = Exchange.query.filter(and_
                                            (Exchange.cc == el['cc']),
                                            (Exchange.exchangedate == el['exchangedate']))
            data_response_el = exchanges_schema.dump(data_el)

            if not data_response_el:
                print(el['txt'], '--Сьогодні ця валюта не записувалась. Записую ')
                save(el=el)
                continue

            if el['rate'] == data_response_el[0]['rate']:
                print(el['txt'], '--Курс не змінився')
            else:
                print(el['txt'], '--Курс змінився')
                save(el=el)
    return jsonify(exchange_lst)
