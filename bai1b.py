from selenium import webdriver
import time
link = 'http://45.79.43.178/source_carts/wordpress/wp-admin/'
driver = webdriver.Chrome(executable_path='chromedriver_linux64/chromedriver')
driver.maximize_window()
driver.get(link)
driver.find_element_by_id('user_login').send_keys('admin')
driver.find_element_by_id('user_pass').send_keys('123456aA')
driver.find_element_by_id('wp-submit').click()
name = driver.find_element_by_id('wp-admin-bar-my-account').text.split(',')[0]
print(name)
driver.quit()