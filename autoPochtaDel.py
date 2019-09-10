from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://mail.rambler.ru/"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))
    browser.find_element_by_id("login").send_keys("*********")
    browser.find_element_by_id('password').send_keys("**********")
    browser.find_element_by_class_name('rui-Button-content').click()
    n = True
    while n == True:
        browser.implicitly_wait(5)
        browser.find_element(By.CSS_SELECTOR, 'div.MailListCheckMenu-bird-2r').click()
        browser.find_element(By.CSS_SELECTOR, 'span.Checkbox-root-vD').click()
        browser.find_element(By.CSS_SELECTOR,
                             'div.ButtonWithIcon-root-5K.ButtonWithIcon-themeDark-3m.ToolbarItem-root-20').click()
        #num = browser.find_element(By.CSS_SELECTOR, 'span.rui-Pagination-item').text      #not ready
        #if int(num[2:]) <= 1:                                                             #not ready
        #    print(int(num[2:]))                                                           #not ready
        #    n = False                                                                     #not ready
finally:
    browser.quit()
