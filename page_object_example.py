from selenium import webdriver

from MyPageObject import MyPageObject

driver = webdriver.Chrome()

mpo = MyPageObject(webdriver=driver)

mpo.goto_page()

mpo.set_value_to_text_field("xxx")
mpo.set_value_to_textarea("yyy")

