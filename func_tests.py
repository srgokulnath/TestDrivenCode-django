from selenium import webdriver

brouser = webdriver.Firefox()
brouser.get('http://localhost:8000')

assert brouser.page_source.find('install')