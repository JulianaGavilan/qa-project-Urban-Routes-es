from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Localizadores import UrbanRoutesPaymentMethods, UrbanRoutesPage,UrbanRoutesAddNumberPhone,UrbanRoutesOrderRequirementOptions
from helpers import retrieve_phone_code

class UrbanRoutesPageInicial:
    from_field = UrbanRoutesPage.From_Box
    to_field = UrbanRoutesPage.To_Box
    flash_button = UrbanRoutesOrderRequirementOptions.Flash_option_Button
    order_a_taxi_button = UrbanRoutesOrderRequirementOptions.Order_Taxi
    look_taxi_button = UrbanRoutesOrderRequirementOptions.look_for_taxi_button
    icon_confort_tariff = UrbanRoutesOrderRequirementOptions.Confort_tariff
    driver_message = UrbanRoutesOrderRequirementOptions.Message_For_Driver
    blanket_and_tissue = UrbanRoutesOrderRequirementOptions.Blankets_And_Tissue_Slider
    counter_of_ice_creams = UrbanRoutesOrderRequirementOptions.Ice_Cream_Counter
    ice_cream_number = UrbanRoutesOrderRequirementOptions.Number_Ice_Cream
    actual_tariff = UrbanRoutesOrderRequirementOptions.actual_tariff_selection
    number_phone_button = UrbanRoutesAddNumberPhone.Button_number_phone
    next_section_button = UrbanRoutesAddNumberPhone.Button_next
    set_confirmation_code = UrbanRoutesAddNumberPhone.Confirmation_code
    confirmation_button = UrbanRoutesAddNumberPhone.Button_confirmation
    ask_for_taxi_button = UrbanRoutesAddNumberPhone.Ask_for_Taxi
    add_number_phone_box = UrbanRoutesAddNumberPhone.Add_number_phone
    payment_methods_section = UrbanRoutesPaymentMethods.Payment_Methods
    add_new_method = UrbanRoutesPaymentMethods.Add_Information_card
    add_card_number = UrbanRoutesPaymentMethods.Card_Number_Box
    add_code_number = UrbanRoutesPaymentMethods.Card_Code_Box
    another_place_in_card = UrbanRoutesPaymentMethods.Another_Place_On_Card
    add_card = UrbanRoutesPaymentMethods.Button_Add_Card
    button_close_section = UrbanRoutesPaymentMethods.Close_Button_Section_Payment
    see_driver_for_route = UrbanRoutesPaymentMethods.see_driver
    take_a_taxi = UrbanRoutesPaymentMethods.star_route

    def __init__(self, driver):
        self.driver = driver

    def wait_for_inicial(self):
        WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located(self.from_field))

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')


    def wait_for_look_taxi_option(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.order_a_taxi_button))

    def click_flash_option(self):
        self.driver.find_element(*self.flash_button).click()

    def order_a_taxi(self):
        self.driver.find_element(*self.order_a_taxi_button).click()

    def click_look_for_taxi_button(self):
        self.driver.find_element(*self.look_taxi_button).click()

    def wait_for_taxi_types(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.icon_confort_tariff))

    def selector_confort_tariff(self):
        self.driver.find_element(*self.icon_confort_tariff).click()

    def wait_for_comfort_form(self):
        WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located(self.driver_message))

    def write_message_to_driver(self, comment):
        self.driver.find_element(*self.driver_message).send_keys(comment)

    def selector_blankets_and_tissue(self):
        self.driver.find_element(*self.blanket_and_tissue).click()

    def add_two_ice_cream(self):
        self.driver.find_element(*self.counter_of_ice_creams).click()
        self.driver.find_element(*self.counter_of_ice_creams).click()

    def wait_for_confirm_information(self):
        WebDriverWait(self.driver,30).until(expected_conditions.visibility_of_element_located(self.ice_cream_number))

    def get_comment(self):
        return self.driver.find_element(*self.driver_message).get_property('value')

    def get_confirmation_blankets_and_tissue (self):
        switch= self.driver.find_element(*self.blanket_and_tissue)
        return switch[0].get_property('checked')

    def get_ice_cream_number(self):
        return self.driver.find_element(*self.ice_cream_number).text

    def get_tariff_comfort(self):
        return self.driver.find_element(*self.actual_tariff).text

    def wait_for_number_form(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(self.number_phone_button))

    def click_number_phone_button(self):
        self.driver.find_element(*self.number_phone_button).click()

    def write_number_phone(self, number_phone):
        self.driver.find_element(*self.add_number_phone_box).send_keys(number_phone)

    def get_phone_number(self):
        return self.driver.find_element(*self.add_number_phone_box).get_property('value')

    def click_set_phone(self):
        self.driver.find_element(*self.next_section_button).click()

    def wait_for_code_confirmation(self):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.set_confirmation_code))

    def write_confirmation_code(self):
        confirmation_code= retrieve_phone_code(self.driver)
        self.driver.find_element(*self.set_confirmation_code).send_keys(confirmation_code)

    def click_on_confirmation_button(self):
        self.driver.find_element(*self.confirmation_button).click()

    def ask_for_taxi(self):
        return self.driver.find_element(*self.ask_for_taxi_button).text

    def click_payment_methods_section(self):
        self.driver.find_element(*self.payment_methods_section).click()

    def wait_for_open_payment_section(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.add_new_method))

    def click_add_new_method(self):
        self.driver.find_element(*self.add_new_method).click()

    def wait_for_add_card(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.add_card_number))

    def write_card_number(self, number_card):
        self.driver.find_element(*self.add_card_number).send_keys(number_card)

    def write_card_code(self, code_number):
        self.driver.find_element(*self.add_code_number).send_keys(code_number)

    def get_card_number(self):
        return self.driver.find_element(*self.add_card_number).get_property('value')

    def get_card_code(self):
        return self.driver.find_element(*self.add_code_number).get_property('value')

    def click_in_another_place(self):
        self.driver.find_element(*self.another_place_in_card).click()

    def click_in_add_payment(self):
        self.driver.find_element(*self.add_card).click()

    def wait_for_add_new_payment(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self.button_close_section))

    def close_button_payment_section(self):
        self.driver.find_element(*self.button_close_section).click()

    def click_in_taxi(self):
        self.driver.find_element(self.take_a_taxi).click()

    def confirm_payment_method(self):
        return self.driver.find_element(*self.add_new_method).text

    def wait_for_information (self):
        WebDriverWait(self.driver ,60).until(expected_conditions.visibility_of_element_located(self.see_driver_for_route))

    def get_information_about_driver(self):
        return self.driver.find_element(*self.see_driver_for_route).text

    def travel_route(self,from_address,to_address,comment,number_card, code_number,number_phone):
        self.wait_for_inicial()
        self.set_from(from_address)
        self.set_to(to_address)
        self.get_from()
        self.get_to()
        self.wait_for_look_taxi_option()
        self.click_flash_option()
        self.order_a_taxi()
        self.click_look_for_taxi_button()
        self.wait_for_taxi_types()
        self.selector_confort_tariff()
        self.wait_for_comfort_form()
        self.write_message_to_driver(comment)
        self.add_two_ice_cream()
        self.wait_for_confirm_information()
        self.get_ice_cream_number()
        self.selector_blankets_and_tissue()
        self.get_confirmation_blankets_and_tissue()
        self.get_tariff_comfort()
        self.wait_for_number_form()
        self.click_number_phone_button()
        self.write_number_phone(number_phone)
        self.get_phone_number()
        self.click_set_phone()
        self.wait_for_code_confirmation()
        self.write_confirmation_code()
        self.click_on_confirmation_button()
        self.click_payment_methods_section()
        self.click_add_new_method()
        self.wait_for_add_card()
        self.write_card_number(number_card)
        self.write_card_code(code_number)
        self.click_in_another_place()
        self.click_in_add_payment()
        self.wait_for_add_new_payment()
        self.close_button_payment_section()
        self.click_in_taxi()
        self.confirm_payment_method()
        self.wait_for_information()
        self.get_information_about_driver()
