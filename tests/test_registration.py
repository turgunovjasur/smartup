import random

import pytest
from pages.login_page import LoginPage
from pages.dashboart_page import DashboartPage
from pages.sales_modal import SalesModal
from pages.orders_page import OrdersPage
from pages.goods_page import GoodsPage
from pages.final_page import FinalPage
from pages.create_order_page import CreateOrderPage
from utils.driver_setup import setup_driver


@pytest.fixture(scope="module")
def driver():
    driver = setup_driver()
    driver.get("https://smartup.online/")
    yield driver
    driver.quit()


def test_all(driver):
    login = "admin@test"
    password = 'xxxx'

    login_page = LoginPage(driver)
    login_page.fill_registration_form(login, password)
    login_page.click_sign_up_button()

    dashboard_page = DashboartPage(driver)
    dashboard_page.check_page()
    dashboard_page.click_button()

    sales_modal = SalesModal(driver)
    sales_modal.check_modal()
    sales_modal.click_button()

    orders_page = OrdersPage(driver)
    orders_page.check_page()
    count_orders = orders_page.check_count()
    orders_page.click_create_button()

    workspace = 'Family Group'
    staff_unit = 'BetterCall'
    client = 'debtor'

    create_orders_page = CreateOrderPage(driver)
    create_orders_page.check_page()
    create_orders_page.fill_form(workspace, staff_unit, client)
    create_orders_page.click_next_button()

    name = 'Product 2'
    qty = '3'

    goods_page = GoodsPage(driver)
    goods_page.fill_form(qty)
    goods_page.click_next_button()

    payment_type = 'Наличные деньги'
    status = 'Черновик'

    final_page = FinalPage(driver)
    final_page.fill_form(payment_type, status)
    final_page.click_save_button()

    check_orders_page = OrdersPage(driver)
    check_orders_page.check_page()
    new_count_orders = check_orders_page.check_count()
    assert count_orders == new_count_orders, "FAIL"
