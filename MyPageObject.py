class MyPageObject(object):
    text_field_xpath = "//input[@name='text' and @type='text']"
    textarea_field_xpath = "//textarea[@name='textarea']"
    dropdown_field_xpath = "//select[@name='numeros']"
    radiobuttons_field_xpath = "//input[@name='numero' and @type='radio']"
    radiobutton_by_value_xpath = "//input[@name='numero' and @type='radio' and @value='%s']"
    checkbox_field_xpath = "//input[@name='likeNumbers' and @type='checkbox']"

    def __init__(self, webdriver):
        self.webpage_url = "http://bitacoraderobertotorres.blogspot.com/p/blog-page.html"
        self.webdriver = webdriver

    def goto_page(self, wait=True):
        self.webdriver.get(self.webpage_url)
        if wait:
            pass

    def get_title(self):
        return self.webdriver.title

    @property
    def text_field_web_element(self):
        return self.webdriver.find_element_by_xpath(self.text_field_xpath)

    def get_text_field_value(self):
        return self.text_field_web_element.get_attribute("value")

    def set_value_to_text_field(self, value):
        self.text_field_web_element.send_keys(value)

    @property
    def textarea_web_element(self):
        return self.webdriver.find_element_by_xpath(self.textarea_field_xpath)

    def get_textarea_value(self):
        return self.textarea_web_element.get_attribute("value")

    def set_value_to_textarea(self, value):
        self.textarea_web_element.send_keys(value)

    @property
    def checkbox_web_element(self):
        return self.webdriver.find_element_by_xpath(self.checkbox_field_xpath)

    def is_checkbox_selected(self):
        return self.checkbox_web_element.is_selected()

    def switch_checkbox(self, turn_on):
        if turn_on and not self.is_checkbox_selected():
            self.checkbox_web_element.click()
        elif not turn_on and self.is_checkbox_selected():
            self.checkbox_web_element.click()

    @property
    def radiobutton_web_elements(self):
        return self.webdriver.find_elements_by_xpath(self.radiobuttons_field_xpath)

    def get_checked_radiobutton_value(self):
        for radiobutton in self.radiobutton_web_elements:
            if radiobutton.is_selected():
                return radiobutton.get_attribute('value')
        return None

    def select_radiobutton_by_value(self, value):
        self.webdriver.find_element_by_xpath(self.radiobutton_by_value_xpath % value).click()

    @property
    def dropdown_web_element(self):
        from selenium.webdriver.support.ui import Select
        return Select(self.webdriver.find_element_by_xpath(self.dropdown_field_xpath))

    def get_selected_dropdown_text(self):
        return self.dropdown_web_element.first_selected_option.text

    def get_selected_dropdown_value(self):
        return self.dropdown_web_element.first_selected_option.get_attribute('value')

    def set_dropdown_option_by_text(self, text):
        self.dropdown_web_element.select_by_visible_text(text)

    def set_dropdown_option_by_value(self, value):
        self.dropdown_web_element.select_by_value(value)

    def set_dropdown_option_by_index(self, index):
        self.dropdown_web_element.select_by_index(index)
