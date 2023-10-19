from app.main.utils.helper import OrderHelper, DriverHelper
from app.main.utils.data import order_data, driver_data


def migrate_data():
    OrderHelper.add_order_data(order_data)
    DriverHelper.add_driver_data(driver_data)
