from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

# All time.sleep sentence could be replaced by driver.implicitly_wait(n) which is more quickly in speed.  time.sleep(n) only for observer the test result


driver = webdriver.Chrome()
first_url = 'http://automationpractice.com/'


driver.get(first_url)

driver.find_element_by_class_name('login').click()
driver.maximize_window()


driver.find_element_by_id('email').click()
driver.find_element_by_id('email').send_keys('lyfyxy66@gmail.com')
driver.find_element_by_id('passwd').click()
driver.find_element_by_id('passwd').send_keys('DellaLi')


driver.find_element_by_name('SubmitLogin').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="search_query_top"]').click()
driver.find_element_by_xpath('//*[@id="search_query_top"]').send_keys('dresses')
driver.find_element_by_name('submit_search').click()


sel = driver.find_element_by_id('selectProductSort')
Select(sel).select_by_value('price:desc')

selectUrl = driver.current_url
print(selectUrl)

time.sleep(5)

'''
following are two methods to see the element: 
1) poistion the element and drag to make it visible
2) scroll the mouse to make the element visible

'''
'''
target = driver.find_element_by_xpath("//*[@id='color_16']")
driver.execute_script("arguments[0].scrollIntoView();", target) #拖动到可见的元素去
time.sleep(3)

target.click()

'''
driver.execute_script("window.scrollBy(0,600)")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='color_16']").click()
driver.execute_script("window.scrollBy(0,300)")
time.sleep(5)


driver.find_element_by_css_selector('#uniform-group_1').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="group_1"]/option[2]').click()
time.sleep(5)

driver.find_element_by_css_selector('#uniform-group_1').click()

time.sleep(5)
driver.find_element_by_name('Submit').click()

time.sleep(5)

driver.find_element_by_xpath("//span[@title='Continue shopping']/span").click()

time.sleep(5)



driver.get(selectUrl)

driver.execute_script("window.scrollBy(0,600)")
time.sleep(5)

driver.find_element_by_xpath("//*[@id='color_19']").click()
driver.find_element_by_xpath("//*[@id='color_19']").click()
driver.execute_script("window.scrollBy(0,300)")
time.sleep(6)



selAnother = driver.find_element_by_id('group_1')
time.sleep(5)

Select(selAnother).select_by_value('2')

driver.find_element_by_name('Submit').click()

time.sleep(2)


driver.execute_script("window.scrollBy(0,300)")

time.sleep(6)

driver.find_element_by_xpath('//*[@id="center_column"]/p[2]/a[1]/span').click

