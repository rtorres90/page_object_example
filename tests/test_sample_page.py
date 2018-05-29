import unittest

from selenium import webdriver

from MyPageObject import MyPageObject


class TestMyPageObject(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.page_object = MyPageObject(webdriver=cls.driver)
        cls.page_object.goto_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_input_text_field(self):
        test_string = "test1"
        self.page_object.set_value_to_text_field(test_string)

        obtained_value = self.page_object.get_text_field_value()
        self.assertEquals(test_string, obtained_value)

    def test_text_area_field(self):
        test_string = "test2"
        self.page_object.set_value_to_textarea(test_string)

        obtained_value = self.page_object.get_textarea_value()
        self.assertEquals(test_string, obtained_value)

    def test_checkbox(self):
        self.page_object.switch_checkbox(turn_on=True)

        self.assertTrue(self.page_object.is_checkbox_selected())

    def test_radiobutton(self):
        test_value = "1"
        self.page_object.select_radiobutton_by_value(test_value)

        obtained_value = self.page_object.get_checked_radiobutton_value()
        self.assertEquals(test_value, obtained_value)

    def test_dropdown_with_text(self):
        test_value = "Two"
        self.page_object.set_dropdown_option_by_text(test_value)

        obtained_value = self.page_object.get_selected_dropdown_text()
        self.assertEquals(test_value, obtained_value)

    def test_dropdown_with_value(self):
        test_value = "3"
        self.page_object.set_dropdown_option_by_value(test_value)

        obtained_value = self.page_object.get_selected_dropdown_value()
        self.assertEquals(test_value, obtained_value)
