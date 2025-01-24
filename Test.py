import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from main import UrbanRoutesConfortOptions,UrbanRoutesPageInicial,UrbanRoutesPaymentMethod, UrbanRoutesNumberPhone


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPageInicial(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.travel_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_comfort_taxi_form(self):
        confort_form = UrbanRoutesConfortOptions(self.driver)
        confort_form.get_look_confort_taxi(data.message_for_driver)
        actual_message_for_driver = confort_form.get_comment()
        actual_ice_cream_number = confort_form.get_ice_cream_number()
        assert actual_message_for_driver == data.message_for_driver
        assert actual_ice_cream_number == data.number_of_ice_creams

    def test_add_phone(self):
        add_phone_number = UrbanRoutesNumberPhone(self.driver)
        add_phone_number.add_new_phone_number(data.phone_number)
        actual_phone_number = add_phone_number.get_phone_number()
        assert actual_phone_number == data.phone_number

    def test_add_new_payment(self):
        add_new_card = UrbanRoutesPaymentMethod(self.driver)
        add_new_card.add_new_payment(data.card_number,data.card_code)
        actual_card_number = add_new_card.get_card_number()
        actual_card_code = add_new_card.get_card_code()
        assert actual_card_number == data.card_number
        assert actual_card_code == data.card_code


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()




