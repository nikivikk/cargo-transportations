from ..model.models import Order, Driver, db
from ..service.order_service import update_date
from ..service.driver_service import create_driver_service


class OrderHelper:
    def add_order_data(seed_data):
        for data in seed_data:
            order = Order(*data)
            order.update_status_date = update_date()
            db.session.add(order)
            db.session.commit()
        print("Orders successfully Added")


class DriverHelper:
    def add_driver_data(seed_data):
        for data in seed_data:
            driver = Driver(*data)
            db.session.add(driver)
            db.session.commit()
        print("Drivers successfully Added")
