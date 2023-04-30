from pages.swag_labs import SwagLabs


def test_icon_exist(browser):
    demo_swag_labs = SwagLabs(browser)
    demo_swag_labs.visit()
    assert demo_swag_labs.exist_icon()


def test_name_exist(browser):
    demo_swag_labs = SwagLabs(browser)
    demo_swag_labs.visit()
    assert demo_swag_labs.exist_placeholder_name()


def test_password_exist(browser):
    demo_swag_labs = SwagLabs(browser)
    demo_swag_labs.visit()
    assert demo_swag_labs.exist_placeholder_password()
