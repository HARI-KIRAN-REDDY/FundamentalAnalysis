import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class CashflowDataGetter:
    def __init__(self, stock_code):
        self.stock_code = stock_code
        self.driver = Chrome()
        self.driver.get(f'https://www.screener.in/company/{stock_code}/consolidated/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)



    def get_operating_details(self):
        cash_flow_type = 'Cash from Operating Activity'
        self.driver.find_element(By.XPATH, f'//button[contains(text(), "{cash_flow_type}")]/span').click()
        time.sleep(3)
        details = {'cash_flow_type': cash_flow_type, 'company_code': self.stock_code, 'data_items': {}, 'years': []}
        data_item_elements = self.driver.find_elements(By.XPATH, f'//button[contains(text(), "{cash_flow_type}")]/parent::td/parent::tr/following-sibling::tr[contains(@class, "stripe")]')
        for element in data_item_elements:
            item_name = element.find_element(By.XPATH, './td').text
            if item_name == 'Working capital changes':
                continue
            if item_name == 'Cash from Financing Activity +':
                break
            item_values = []
            for value_element in element.find_elements(By.XPATH, './td[not(@class)]'):
                item_values.append(float(value_element.text.replace(',', '')))
            details['data_items'][item_name] = item_values
        details['years'] = self.get_years()
        details['net cashflow'] = self.get_net_cashflow_from_type(cash_flow_type)
        return details
    def get_investment_details(self):
        cash_flow_type = 'Cash from Investing Activity'
        self.driver.find_element(By.XPATH, f'//button[contains(text(), "{cash_flow_type}")]/span').click()
        details = {'cash_flow_type': cash_flow_type, 'company_code': self.stock_code, 'data_items': {}, 'years': []}
        data_item_elements = self.driver.find_elements(By.XPATH, f'//button[contains(text(), "{cash_flow_type}")]/parent::td/parent::tr/following-sibling::tr[@class=""]')
        for element in data_item_elements:
            item_name = element.find_element(By.XPATH, './td').text
            item_values = []
            for value_element in element.find_elements(By.XPATH, './td[not(@class)]'):
                item_values.append(float(value_element.text.replace(',', '')))
            details['data_items'][item_name] = item_values
        details['years'] = self.get_years()
        details['net cashflow'] = self.get_net_cashflow_from_type(cash_flow_type)
        return details
    def get_financing_details(self):
        cash_flow_type = 'Cash from Financing Activity'
        self.driver.find_element(By.XPATH, f'//button[contains(text(), "{cash_flow_type}")]/span').click()
        details = {'cash_flow_type': cash_flow_type, 'company_code': self.stock_code, 'data_items': {}, 'years': []}
        data_item_elements = self.driver.find_elements(By.XPATH, f'//button[contains(text(), "{cash_flow_type}")]/parent::td/parent::tr/following-sibling::tr[@class="stripe"]')
        for element in data_item_elements:
            item_name = element.find_element(By.XPATH, './td').text
            item_values = []
            for value_element in element.find_elements(By.XPATH, './td[not(@class)]'):
                item_values.append(float(value_element.text.replace(',', '')))
            details['data_items'][item_name] = item_values
        details['years'] = self.get_years()
        details['net cashflow'] = self.get_net_cashflow_from_type(cash_flow_type)
        return details

    def get_overall_details(self):
        details = {'cash_flow_type': 'Overall Cashflow',
                   'company_code': self.stock_code,
                   'data_items': {}, 'years': []}
        for item in ('Operating', 'Investing', 'Financing'):
            details['data_items'][f'Cash from {item} Activity'] = (
                self.get_net_cashflow_from_type(f'Cash from {item} Activity'))
        details['years'] = self.get_years()
        details['net cashflow'] = self.get_net_cashflow()
        return details


    def get_years(self):
        values = []
        value_elements = self.driver.find_elements(By.XPATH,
                                                   '//*[@id="cash-flow"]//th/following-sibling::th')
        for element in value_elements:
            values.append(float(element.text.split(' ')[1]))
        return values

    def get_net_cashflow_from_type(self, cash_flow_type):
        values = []
        value_elements = self.driver.find_elements(By.XPATH,
                                                   f'//button[contains(text(), "{cash_flow_type}")]/parent::td/following-sibling::td')
        for element in value_elements:
            values.append(float(element.text.replace(',', '')))
        return values

    def get_net_cashflow(self):
        values = []
        value_elements = (self.driver
                          .find_elements(By.XPATH,
                                         '//td[contains(text(), "Net Cash Flow")]/following-sibling::td'))
        for element in value_elements:
            values.append(float(element.text.replace(',', '')))
        return values
