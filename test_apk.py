from appium import webdriver

desired_caps = {
    "platformName": "android",
    "platformVersion": "8.1",
    "deviceName": "Nexus 6 API 27",
    "app": "C:\\Users\\Evgeniy\\Downloads\\Calculator.apk"
}


def test_mult():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.find_element_by_id('com.google.android.calculator:id/digit_4').click()
    driver.find_element_by_id('com.google.android.calculator:id/op_mul').click()
    driver.find_element_by_id('com.google.android.calculator:id/digit_6').click()
    driver.find_element_by_id('com.google.android.calculator:id/eq').click()
    result = driver.find_element_by_id('com.google.android.calculator:id/result_final')
    assert int(result.text) == 24, "Multiplication does not work correctly"
    driver.quit()


def test_sum():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.find_element_by_id('com.google.android.calculator:id/digit_3').click()
    driver.find_element_by_id('com.google.android.calculator:id/op_add').click()
    driver.find_element_by_id('com.google.android.calculator:id/digit_7').click()
    driver.find_element_by_id('com.google.android.calculator:id/eq').click()
    result = driver.find_element_by_id('com.google.android.calculator:id/result_final')
    assert int(result.text) == 10, "Addition does not work correctly"
    driver.quit()


def test_division_by_zero():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.find_element_by_id('com.google.android.calculator:id/digit_5').click()
    driver.find_element_by_id('com.google.android.calculator:id/op_div').click()
    driver.find_element_by_id('com.google.android.calculator:id/digit_0').click()
    driver.find_element_by_id('com.google.android.calculator:id/eq').click()
    numbers_field = driver.find_element_by_id('com.google.android.calculator:id/result_preview')
    assert numbers_field.text == 'Can\'t divide by 0', "Division by 0!!!"
    driver.quit()


def test_send_keys():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.find_element_by_id('com.google.android.calculator:id/formula').send_keys('10+0')
    driver.find_element_by_id('com.google.android.calculator:id/eq').click()
    result = driver.find_element_by_id('com.google.android.calculator:id/result_final')
    assert int(result.text) == 10, "Addition does not work correctly"
    driver.quit()