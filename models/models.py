from app import db


class Exchange(db.Model):
    __tablename__ = 'exchange'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    r030 = db.Column(db.Integer, nullable=False)
    txt = db.Column(db.String, nullable=False)
    rate = db.Column(db.Float, nullable=False)
    cc = db.Column(db.String, nullable=False)
    exchangedate = db.Column(db.String, nullable=False)

    def __init__(self, r030, txt, rate, cc, exchangedate):
        self.r030 = r030
        self.txt = txt
        self.rate = rate
        self.cc = cc
        self.exchangedate = exchangedate
