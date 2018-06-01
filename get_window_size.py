from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://192.168.8.13:9090")
size=driver.get_window_size()
print(size)
