#--coding:utf-8--
import sys
sys.path.append("F:\myfile\python\code\seleniumpython")
import os
from selenium import webdriver
from util.get_code import GetCode 
import time

'''os.chdir(os.path.dirname(os.getcwd()))
print(os.getcwd())
file_path = os.path.join(os.getcwd()+"\\report\\"+"first_case.html")
print(file_path)
with open(file_path,'wb') as fd:
	print("hello")'''
	
class Test(object):
	def __init__(self):
		self.driver = webdriver.Chrome("C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
		self.driver.maximize_window()
		self.driver.get("http://www.5itest.cn/register")
			
	def get_code_text(self):
		get_code = GetCode(self.driver)
		time.sleep(5)
		file_name = "F:\\myfile\\python\\code\\seleniumpython\\Image\\test001.png"
		code = get_code.code_online(file_name)
		print(code)
		
	def close_driver(self):
		self.driver.close()
		
	def refresh_driver(self):
		self.driver.refresh()


if __name__ == "__main__":
	test1 = Test()
	test1.get_code_text()
	test1.refresh_driver()
	test1.get_code_text()
	test1.close_driver()

