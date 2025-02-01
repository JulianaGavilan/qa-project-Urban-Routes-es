
import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from main import UrbanRoutesPageInicial


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
        comment_for_driver = data.message_for_driver
        number_card = data.card_number
        code_card = data.card_code
        number_phone = data.phone_number
        routes_page.travel_route(address_from, address_to,comment_for_driver,number_card,code_card,number_phone)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to


# Separe los test de número de helados y mensajes al conductor que se encontraban en una sola prueba

    def test_for_ice_creams(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPageInicial(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        comment_for_driver = data.message_for_driver
        number_card = data.card_number
        code_card = data.card_code
        number_phone = data.phone_number
        routes_page.travel_route(address_from, address_to, comment_for_driver, number_card, code_card, number_phone)
        actual_ice_cream_number = routes_page.get_ice_cream_number()
        assert actual_ice_cream_number == data.number_of_ice_creams

    def test_message_for_driver(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPageInicial(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        comment_for_driver = data.message_for_driver
        number_card = data.card_number
        code_card = data.card_code
        number_phone = data.phone_number
        routes_page.travel_route(address_from, address_to, comment_for_driver, number_card, code_card, number_phone)
        actual_message_for_driver = routes_page.get_comment()
        assert actual_message_for_driver == data.message_for_driver


    def test_add_phone(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPageInicial(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        comment_for_driver = data.message_for_driver
        number_card = data.card_number
        code_card = data.card_code
        number_phone = data.phone_number
        routes_page.travel_route(address_from, address_to, comment_for_driver, number_card, code_card, number_phone)
        actual_phone_number = routes_page.get_phone_number()
        assert actual_phone_number == data.phone_number

    def test_add_new_payment(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPageInicial(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        comment_for_driver = data.message_for_driver
        number_card = data.card_number
        code_card = data.card_code
        number_phone = data.phone_number
        routes_page.travel_route(address_from, address_to, comment_for_driver, number_card, code_card, number_phone)
        actual_card_number = routes_page.get_card_number()
        actual_card_code = routes_page.get_card_code()
        assert actual_card_number == data.card_number
        assert actual_card_code == data.card_code

# Formule los test para confirmar la tarifa confort, revisar la solicitud de mantas y pañuelos y lo relacionado con el modal de confirmacion de solicitud de taxi

    def test_comfort_tariff (self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPageInicial(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        comment_for_driver = data.message_for_driver
        number_card = data.card_number
        code_card = data.card_code
        number_phone = data.phone_number
        routes_page.travel_route(address_from, address_to, comment_for_driver, number_card, code_card, number_phone)
        actual_tariff = routes_page.get_tariff_comfort()
        assert actual_tariff == data.actual_tariff_in_page

    def test_for_blankets_and_tissue (self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPageInicial(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        comment_for_driver = data.message_for_driver
        number_card = data.card_number
        code_card = data.card_code
        number_phone = data.phone_number
        routes_page.travel_route(address_from, address_to, comment_for_driver, number_card, code_card, number_phone)
        actual_switch_situation = routes_page.get_confirmation_blankets_and_tissue()
        assert actual_switch_situation == data.blanket_and_tissue

    def test_to_modal_taxi(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPageInicial(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        comment_for_driver = data.message_for_driver
        number_card = data.card_number
        code_card = data.card_code
        number_phone = data.phone_number
        routes_page.travel_route(address_from, address_to, comment_for_driver, number_card, code_card, number_phone)
        take_a_taxi_section = routes_page.get_information()
        assert take_a_taxi_section == data.take_a_taxi_button

    def test_for_final_form(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPageInicial(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        comment_for_driver = data.message_for_driver
        number_card = data.card_number
        code_card = data.card_code
        number_phone = data.phone_number
        routes_page.travel_route(address_from, address_to, comment_for_driver, number_card, code_card, number_phone)
        final_form = routes_page.get_information_about_driver()
        assert final_form == data.driver_information