
class Login():
    def user_login(self, driver, username, password, validatecode):
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("validatecode").clear()
    driver.find_element_by_id("validatecode").send_keys(validatecode)
