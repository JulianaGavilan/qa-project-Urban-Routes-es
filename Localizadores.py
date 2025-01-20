from selenium.webdriver.common.by import By


class UrbanRoutesPage:
    From_Box = (By.ID,'from')
    To_Box = (By.ID,'to')
    Order_Taxi = (By.CLASS_NAME,'button round')

class UrbanRoutesConfortOptions:
    Confort_tariff = (By.CLASS_NAME,'tariff-card-4')
    


