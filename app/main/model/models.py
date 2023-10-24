from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(40), nullable=False)
    stock_address = db.Column(db.String(120), nullable=False)
    delivery_address = db.Column(db.String(120), nullable=False)
    cargo_type = db.Column(db.String(40), nullable=False)
    update_status_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, status: str, stock_address: str, delivery_address: str, cargo_type: str):
        self.status = status
        self.stock_address = stock_address
        self.delivery_address = delivery_address
        self.cargo_type = cargo_type

    def json(self):
        return {'id': self.id, 'status': self.status,
                'stock_address': self.stock_address,
                'delivery_address': self.delivery_address,
                'cargo_type': self.cargo_type,
                'update_status_date': self.update_status_date}


class Driver(db.Model):
    __tablename__ = 'drivers'

    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(120), nullable=False, unique=True)
    free = db.Column(db.Boolean, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=True)

    def __init__(self, fio: str, free: bool, location: str):
        self.fio = fio
        self.free = free
        self.location = location

    def json(self):
        return {'id': self.id, 'fio': self.fio,
                'free': self.free,
                'location': self.location, 'order_id': self.order_id}
