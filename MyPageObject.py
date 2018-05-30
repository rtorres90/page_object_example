class MyPageObject(object):
    """This is a page object to interact with a sample page."""
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
        """Goes to the sample page."""
        self.webdriver.get(self.webpage_url)
        if wait:
            pass

    def get_title(self):
        """Returns the title of the sample page."""
        return self.webdriver.title

    @property
    def text_field_web_element(self):
        return self.webdriver.find_element_by_xpath(self.text_field_xpath)

    def get_text_field_value(self):
        """Returns the value of the text field."""
        return self.text_field_web_element.get_attribute("value")

    def set_value_to_text_field(self, value):
        """Set the value passed as a parameter to the text field."""
        self.text_field_web_element.send_keys(value)

    @property
    def textarea_web_element(self):
        return self.webdriver.find_element_by_xpath(self.textarea_field_xpath)

    def get_textarea_value(self):
        """Returns the value of the text area."""
        return self.textarea_web_element.get_attribute("value")

    def set_value_to_textarea(self, value):
        """Sets the value passed as a parameter to the text area."""
        self.textarea_web_element.send_keys(value)

    @property
    def checkbox_web_element(self):
        return self.webdriver.find_element_by_xpath(self.checkbox_field_xpath)

    def is_checkbox_selected(self):
        """Returns a True if the checkbox is seleted. Otherwise the response will be False"""
        return self.checkbox_web_element.is_selected()

    def switch_checkbox(self, turn_on):
        """Switch on the checkbox if the parameter is True, Otherwise it will switch off the element."""
        if turn_on and not self.is_checkbox_selected():
            self.checkbox_web_element.click()
        elif not turn_on and self.is_checkbox_selected():
            self.checkbox_web_element.click()

    @property
    def radiobutton_web_elements(self):
        return self.webdriver.find_elements_by_xpath(self.radiobuttons_field_xpath)

    def get_checked_radiobutton_value(self):
        """Returns the value of the radiobutton selected."""
        for radiobutton in self.radiobutton_web_elements:
            if radiobutton.is_selected():
                return radiobutton.get_attribute('value')
        return None

    def select_radiobutton_by_value(self, value):
        """Selects the radio button which matches with the value passed as a parameter."""
        self.webdriver.find_element_by_xpath(
            self.radiobutton_by_value_xpath % value).click()

    @property
    def dropdown_web_element(self):
        from selenium.webdriver.support.ui import Select
        return Select(self.webdriver.find_element_by_xpath(self.dropdown_field_xpath))

    def get_selected_dropdown_text(self):
        """Returns the text of the option selected on the dropdown."""
        return self.dropdown_web_element.first_selected_option.text

    def get_selected_dropdown_value(self):
        """Returns the value of the option selected on the dropdown."""
        return self.dropdown_web_element.first_selected_option.get_attribute('value')

    def set_dropdown_option_by_text(self, text):
        """Selects the option of the dropdown which matches by text"""
        self.dropdown_web_element.select_by_visible_text(text)

    def set_dropdown_option_by_value(self, value):
        """Selects the option of the dropdown which matches by value"""
        self.dropdown_web_element.select_by_value(value)

    def set_dropdown_option_by_index(self, index):
        """Selects the option of the dropdown which matches by index"""
        self.dropdown_web_element.select_by_index(index)
