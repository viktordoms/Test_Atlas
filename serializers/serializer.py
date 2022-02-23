from app import marshmalow
from models.models import *


class ExchangeSchema(marshmalow.Schema):
    class Meta:

        fields = ['id', 'r030', 'txt', 'rate', 'cc', 'exchangedate']


exchanges_schema = ExchangeSchema(many=True)
