from selenium.webdriver.common.by import By


class UrbanRoutesPage:
    From_Box = (By.ID,'from')
    To_Box = (By.ID,'to')

class UrbanRoutesOrderRequirementOptions:
    Flash_option_Button=(By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[1]/div[2]')
    Order_Taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[2]/div[3]')
    look_for_taxi_button = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    Confort_tariff = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    Message_For_Driver = (By.XPATH, '//*[@id="comment"]')
    Blankets_And_Tissue_Slider = (
    By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    Ice_Cream_Counter = (By.XPATH,
                         '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    Number_Ice_Cream = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')
    actual_tariff_selection = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.tariff-cards > div.tcard.active > div.tcard-title')
    option_switches = (By.CLASS_NAME, 'switch')
    option_switches_inputs = (By.CLASS_NAME, 'switch-input')

class UrbanRoutesAddNumberPhone:
    Button_number_phone= (By.CLASS_NAME,'np-text')
    Add_number_phone= (By.XPATH,'//*[@id="phone"]')
    Button_next=(By.XPATH,'/html/body/div/div/div[1]/div[2]/div[1]/form/div[2]/button')
    Confirmation_code = (By.ID,'code')
    Button_confirmation = (By.XPATH,'/html/body/div/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    Ask_for_Taxi=(By.XPATH,'//*[@id="root"]/div/div[3]/div[4]/button/span[2]')

class UrbanRoutesPaymentMethods:
    Payment_Methods = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]')
    Add_Information_card = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]')
    Card_Number_Box = (By.XPATH,'//*[@id="number"]')
    Card_Code_Box = ( By.XPATH, "//input[@id='code'][@class='card-input']")
    Another_Place_On_Card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[1]')
    Button_Add_Card= (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    Close_Button_Section_Payment = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    star_route= (By.XPATH,'//*[@id="root"]/div/div[3]/div[4]/button/span[1]')
    see_driver = (By.XPATH,'//*[@id="root"]/div/div[5]/div[2]/div[1]/div/div[1]')



