from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_css_selector('.trollface.btn.btn-primary').click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element_by_css_selector('.form-group #input_value')
    x = x_element.text
    print(x)
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer").send_keys(y)

    button = browser.find_element_by_css_selector('.btn.btn-primary').click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файл