from app.main.model.models import Order, Driver
from ..model.models import db
from typing import Dict, Tuple
from geopy.geocoders import Nominatim
import geopy.distance
from .driver_service import driver_is_free
import math
import datetime
from flask import request
import pandas as pd
from sqlalchemy import func


def update_date():
    return datetime.datetime.today()


def update_driver_status(order):
    driver = Driver.query.filter_by(order_id=order.id).first()
    if driver:
        driver.free = True
        driver.order_id = None
        driver.location = order.delivery_address
        db.session.commit()


def create_order_service(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    try:
        new_order = Order(status=data['status'],
                          stock_address=data['stock_address'],
                          delivery_address=data['delivery_address'],
                          cargo_type=data['cargo_type'])
        new_order.update_status_date = update_date()
        db.session.add(new_order)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully created.'
        }
        return response_object, 201
    except:
        response_object = {
            'status': 'fail',
            'message': 'Error creating an order.',
        }
        return response_object, 500


def get_orders_service():
    return Order.query.all()


def get_order_service(id):
    return Order.query.filter_by(id=id).first()


def update_order_service(id, data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    try:
        order = Order.query.filter_by(id=id).first()
        if order:
            cur_order_status = order.status
            order.status = data['status']
            order.stock_address = data['stock_address']
            order.delivery_address = data['delivery_address']
            order.cargo_type = data['cargo_type']
            if cur_order_status != order.status:
                order.update_status_date = update_date()
            if order.status == 'завершен':
                update_driver_status(order)
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': 'Order updated.',
            }
            return response_object, 200
        response_object = {
            'status': 'fail',
            'message': 'Order not found.',
        }
        return response_object, 404
    except:
        response_object = {
            'status': 'fail',
            'message': 'Error updating an order.',
        }
        return response_object, 500


def delete_order_service(id) :
    try:
        order = Order.query.filter_by(id=id).first()
        if order:
            db.session.delete(order)
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': 'Order deleted.',
            }
            return response_object, 200
        response_object = {
            'status': 'fail',
            'message': 'Order not found.',
        }
        return response_object, 404
    except:
        response_object = {
            'status': 'fail',
            'message': 'Error deleting an order.',
        }
        return response_object, 500


def min_distance(stock_address, drivers):
    min_dist = math.inf
    cur_driver = None
    loc = Nominatim(user_agent="Geopy Library")
    get_order_loc = loc.geocode(stock_address)
    coords_order = (get_order_loc.latitude, get_order_loc.longitude)
    for driver in drivers:
        get_driver_loc = loc.geocode(driver.location)
        coords_driver = (get_driver_loc.latitude, get_driver_loc.longitude)
        dist = geopy.distance.geodesic(coords_order, coords_driver).km
        if dist < min_dist:
            min_dist = dist
            cur_driver = driver
    return cur_driver


def appoint_order_service(id) -> Tuple[Dict[str, str], int]:
    try:
        order = get_order_service(id)
        drivers = driver_is_free('true')
        if order.status == "новый" and drivers:
            appointment_driver = min_distance(order.stock_address, drivers)
            order.status = 'выполняется'
            order.update_status_date = update_date()
            appointment_driver.free = False
            appointment_driver.order_id = id
            # db.session.add(order)
            # db.session.add(appointment_driver)
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': f'Driver {appointment_driver.fio} started order {id}'
            }
            return response_object, 200
        else:
            response_object = {
                'status': 'fail',
                'message': f"You can't appoint driver on order {id}, because order status is {order.status}"
            }
            return response_object, 404
    except:
        response_object = {
            'status': 'fail',
            'message': 'Error appointing driver',
        }
        return response_object, 500


def get_orders_status_service():
    orders = Order.query.all()
    if request.args.get('status'):
        status = request.args.get('status')
        orders = get_orders_by_status_service(status)
    return orders


def status_by_date(status):
    start_date = datetime.datetime.strptime(request.args.get('start-date'), "%Y-%m-%d")
    end_date = datetime.datetime.strptime(request.args.get('end-date'), "%Y-%m-%d")
    orders = Order.query.filter(Order.status == status,
                                func.date(Order.update_status_date) >= start_date,
                                func.date(Order.update_status_date) <= end_date).all()
    return orders


def make_report_service():
    orders = status_by_date('завершен')
    df = pd.DataFrame([order.__dict__ for order in orders])
    columns_to_display = ['status', 'stock_address', 'delivery_address', 'cargo_type', 'update_status_date']
    df = df[columns_to_display]
    df['update_status_date'] = pd.to_datetime(df['update_status_date'])
    df['update_status_date'] = df['update_status_date'].dt.strftime('%Y-%m-%d')
    df.columns = ['Статус заказа', 'Адрес склада', 'Адрес доставки', 'Тип груза', 'Дата завершения зказа']
    with pd.ExcelWriter('orders_report.xlsx', engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Sheet1', startrow=2)
        book = writer.book
        sheet = writer.sheets['Sheet1']
        bold = book.add_format({'bold': True, 'size': 24})
        sheet.write('A1', 'Отчет по выполненным заказам', bold)

    return "Отчет успешно сохранен в файл 'orders_report.xlsx'"


def get_orders_by_status_service(status):
    if request.args.get('start-date') and request.args.get('end-date'):
        return status_by_date(status)

    else:
        orders = Order.query.filter_by(status=status).all()
    return orders


def get_order_status_service(id):
    order = Order.query.filter_by(id=id).first()
    if order:
        return {id: order.status}
    else:
        return {"error": "Order not found"}


def update_order_status_service(id, data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    try:
        order = Order.query.filter_by(id=id).first()
        if order:
            order.status = data['status']
            order.update_status_date = update_date()
            if order.status == 'завершен':
                update_driver_status(order)
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': 'Order status updated.',
            }
            return response_object, 200
        response_object = {
            'status': 'fail',
            'message': 'Order not found.',
        }
        return response_object, 404
    except:
        response_object = {
            'status': 'fail',
            'message': 'Error updating an order status.',
        }
        return response_object, 500


def save_changes_order(data: Order) -> None:
    db.session.add(data)
    db.session.commit()


def save_changes_driver(data: Driver) -> None:
    db.session.add(data)
    db.session.commit()
