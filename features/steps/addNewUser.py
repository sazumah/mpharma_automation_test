from behave import given, when, then
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService

browser = webdriver.Chrome(ChromeDriverManager().install())

firstName = 'mario'
middleName= 'senior'
lastName = 'tester'
phoneNumber = '0000000000'
dob = '01/10/2020'
address = 'BQ88'

@given(u'A user navigates to the url')
def vist_url(context):
    browser.get('http://localhost:3000/')


@when(u'A user enters the patient\'s firstName')
def type_first_name(context):
    browser.find_element_by_xpath('//*[@data-test-id="first-name"]').send_keys(firstName)


@when(u'A user enters the patient\'s middleName')
def type_middle_name(context):
    browser.find_element_by_xpath('//*[@data-test-id="middle-name"]').send_keys(middleName)


@when(u'A user enters the patient\'s lastName')
def type_last_name(context):
   browser.find_element_by_xpath('//*[@data-test-id="last-name"]').send_keys(lastName)


@when(u'A user enters  the patient\'s phoneNumber')
def type_last_name(context):
    browser.find_element_by_xpath('//*[@data-test-id="phone-number"]').send_keys(phoneNumber)


@when(u'A user enters  the patient\'s dob')
def choose_date_of_birth(context):
    browser.find_element_by_xpath('//*[@data-test-id="dob"]').send_keys(dob)


@when(u'A user enters the patient\'s address')
def type_address(context):
    browser.find_element_by_xpath('//*[@data-test-id="address"]').send_keys(address)


@when(u'A user clicks on the Add New User button')
def click_on_add_new_user_button(context):
    browser.find_element_by_xpath('//*[@data-test-id="submit-btn"]').click()


@then(u'A patient account should be created with the details provided.')
def see_added_patient(context):
    new_user = browser.find_element_by_xpath('//*[@data-test-id="user-card"]')
    assert firstName in new_user.text
    assert middleName in new_user.text
    assert lastName in new_user.text
    assert address in new_user.text
