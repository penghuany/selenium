#coding=utf-8
import sys
sys.path.append('F:\myfile\python\code\seleniumpython')
import traceback
from business.register_business import RegisterBusiness
from selenium import webdriver
from log.user_log import UserLog
import HTMLTestRunner
import unittest
import os
import time

class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
	'''在所有用例执行前执行一次，只执行一次'''
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        cls.file_name = "F:\\myfile\\python\\code\\seleniumpython\\Image\\test001.png"
		#在jenkins中构建项目，如果浏览器和jenkins安装在不同的目录，就会出现找不到浏览器，所以打开浏览器的时候需要指定浏览器的路径
        cls.driver = webdriver.Chrome("C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
        cls.driver.get('http://www.5itest.cn/register')
        
        cls.driver.maximize_window()
    def setUp(self):
        '''每个用例执行的前都会执行一次'''
        self.driver.refresh()
        
        self.logger.info("this is chrome!!!")
        
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
		'''每个用例执行后都会执行一次'''
		time.sleep(2)
        #if sys.exc_info()[0]:
        #for method_name,error in self._outcome.errors:
              #if error:
                  #case_name = self._testMethodName
                  #file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                  #self.driver.save_screenshot(file_path)
		if sys.exc_info()[1]:
			file_path = os.path.join(os.path.dirname(os.getcwd())+"\\report\\"+ "1"+".png")
			#print(file_path)
			self.driver.save_screenshot(file_path)
        #print("这个是case的后置调键1")
        
    @classmethod
    def tearDownClass(cls):
		'''所有用例执行后执行一次'''
		cls.log.close_handle()
		cls.driver.close()
    
    #邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息

    def test_login_email_error(self):
		email_error = self.login.login_email_error('19','user1111','111111',self.file_name)
		return self.assertFalse(email_error,"测试失败")
        
    def test_login_username_error(self):
		username_error = self.login.login_name_error('1212003@qq.com','t3','111111',self.file_name)
		self.assertTrue(username_error)

    def test_login_code_error(self):
		code_error = self.login.login_name_error('11121@qq.com','ss22212','111111',self.file_name)
		self.assertFalse(code_error)
    
    def test_login_password_error(self):
		password_error = self.login.login_name_error('11311@qq.com','ss23222','111111',self.file_name)
		self.assertFalse(password_error)

    def test_login_success(self):
		success = self.login.user_base('122210444@qq.com','2321000','111111',self.file_name)
		self.assertFalse(success)
        #self.assert

'''    
def main():
    first = FirstCase()
    first.test_login_code_error()
    first.test_login_email_error()
    first.test_login_password_error()
    first.test_login_username_error()
    first.test_login_success()
'''

if __name__ == '__main__':
	#在jenkins 中项目配置的工程路径的目录就是os.getcwd()的目录，所以工程路径最好设置为执行文件py的目录，不然会导致jenkins和cmd中运行后出现文件路径不一致问题。目前工程路径设置的是F:\myfile\python\code\seleniumpython\case
	#os.chdir(os.path.dirname(os.getcwd()))    #切换到上一级目录
	#print(os.path.dirname(os.getcwd())) 
	file_path = os.path.join(os.path.dirname(os.getcwd())+"\\report\\"+"first_case.html")
	#print(file_path)
	with open(file_path,"wb") as f:
		suite = unittest.TestSuite()
		#suite.addTest(FirstCase('test_login_success'))
		#suite.addTest(FirstCase('test_login_code_error'))
		suite.addTest(FirstCase('test_login_email_error'))
		suite.addTest(FirstCase('test_login_username_error'))
		unittest.TextTestRunner().run(suite)
		suite = unittest.TestLoader().loadTestsFromTestCase(FirstCase)
		#runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is first123 report",description=u"这个是我们第一次测试报告",verbosity=2)
		#runner.run(suite)
