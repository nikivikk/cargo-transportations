from app.main.model.models import Driver
from ..model.models import db
from typing import Dict, Tuple
from flask import request


def create_driver_service(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    try:
        new_driver = Driver(fio=data['fio'],
                            free=data['free'],
                            location=data['location'])
        db.session.add(new_driver)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully created.'
        }
        return response_object, 201
    except:
        response_object = {
            'status': 'fail',
            'message': 'Error creating a driver.',
        }
        return response_object, 500


def get_drivers_service():
    if request.args.get('free'):
        return driver_is_free(request.args.get('free'))
    else:
        return Driver.query.all()


def get_driver_service(id):
    return Driver.query.filter_by(id=id).first()


def update_driver_service(id, data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    try:
        driver = Driver.query.filter_by(id=id).first()
        if driver:
            data = request.get_json()
            driver.fio = data['fio']
            driver.free = data['free']
            driver.location = data['location']
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': 'Driver updated.',
            }
            return response_object, 200
        response_object = {
            'status': 'fail',
            'message': 'Driver not found.',
        }
        return response_object, 404
    except:
        response_object = {
            'status': 'fail',
            'message': 'Error updating a driver.',
        }
        return response_object, 500


def delete_driver_service(id):
    try:
        driver = Driver.query.filter_by(id=id).first()
        if driver:
            db.session.delete(driver)
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': 'Driver deleted.',
            }
            return response_object, 200
        response_object = {
            'status': 'fail',
            'message': 'Driver not found.',
        }
        return response_object, 404
    except:
        response_object = {
            'status': 'fail',
            'message': 'Error deleting a driver.',
        }
        return response_object, 500


def driver_is_free(status):
    if status.lower() == 'true':
        return Driver.query.filter_by(free=True).all()
    else:
        return Driver.query.filter_by(free=False).all()


def save_changes(data: Driver) -> None:
    db.session.add(data)
    db.session.commit()
