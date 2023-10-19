from flask import request, Blueprint, jsonify
from ..service.order_service import create_order_service, get_orders_service, get_order_service, update_order_service, \
    delete_order_service, appoint_order_service, get_orders_status_service, get_order_status_service, \
    update_order_status_service, make_report_service
from ..service.driver_service import create_driver_service, get_drivers_service, get_driver_service, \
    update_driver_service, \
    delete_driver_service

controller_blueprint = Blueprint('controller', __name__)


@controller_blueprint.route('/api/v1/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    return create_order_service(data=data)


@controller_blueprint.route('/api/v1/orders', methods=['GET'])
def get_orders():
    return jsonify([order.json() for order in get_orders_service()])


@controller_blueprint.route('/api/v1/orders/<int:id>', methods=['GET'])
def get_order(id):
    return jsonify(get_order_service(id).json())


@controller_blueprint.route('/api/v1/orders/<int:id>', methods=['PUT'])
def update_order(id):
    data = request.get_json()
    return update_order_service(id, data=data)


@controller_blueprint.route('/api/v1/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    return delete_order_service(id)


@controller_blueprint.route('/api/v1/drivers', methods=['POST'])
def create_driver():
    data = request.get_json()
    return create_driver_service(data=data)


@controller_blueprint.route('/api/v1/drivers', methods=['GET'])
def get_drivers():
    return jsonify([driver.json() for driver in get_drivers_service()])


@controller_blueprint.route('/api/v1/drivers/<int:id>', methods=['GET'])
def get_driver(id):
    return jsonify(get_driver_service(id).json())


@controller_blueprint.route('/api/v1/drivers/<int:id>', methods=['PUT'])
def update_drivers(id):
    data = request.get_json()
    return update_driver_service(id, data=data)


@controller_blueprint.route('/api/v1/drivers/<int:id>', methods=['DELETE'])
def delete_driver(id):
    return delete_driver_service(id)


@controller_blueprint.route('/api/v1/appoint-order/<int:id>', methods=['POST'])
def appoint_order(id):
    return appoint_order_service(id)


@controller_blueprint.route('/api/v1/orders-status', methods=['GET'])
def get_orders_status():
    return jsonify([order.json() for order in get_orders_status_service()])


@controller_blueprint.route('/api/v1/orders-status/<int:id>', methods=['GET'])
def get_order_status(id):
    return jsonify(get_order_status_service(id))


@controller_blueprint.route('/api/v1/orders-status/<int:id>', methods=['PUT'])
def update_order_status(id):
    data = request.get_json()
    return update_order_status_service(id, data=data)


@controller_blueprint.route('/api/v1/make-report')
def make_report():
    return make_report_service()
