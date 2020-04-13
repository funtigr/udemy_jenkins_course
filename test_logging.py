import logging
from selenium.webdriver import Chrome

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# Create a file handler
handler_warn = logging.FileHandler('warning_log.txt')
handler_warn.setLevel(logging.WARNING)

handler_info = logging.FileHandler('info_log.txt')
handler_info.setLevel(logging.INFO)

# create a logging format

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_warn.setFormatter(formatter)
handler_info.setFormatter(formatter)

# add the handler to the logger

log.addHandler(handler_warn)
log.addHandler(handler_info)

log.info('Information')
log.warning('warning')

driver = Chrome()
driver.maximize_window()
driver.get("https://www.thetestingworld.com/testings")
driver.find_element_by_xpath("//label[text()='Login']").click()
driver.find_element_by_name("_txtUserName").send_keys("test")
driver.find_element_by_name("_txtPassword").send_keys("test")
driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()
driver.find_element_by_xpath("//a[contains(text(),'My Account')]").click()
log.info("This is log info")