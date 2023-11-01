# -*-coding:utf-8-*-
# @Time    :2023/10/3014:28
# @Author  :jzw
# @Email   :1615573929@qq.com
# @File    :ceshi.py
# @Software:PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
import ddt
from parameterized import parameterized,param
from hanshu import hanshu_csv
from time import sleep



class DingWei():
    UserName=(By.ID,"inputUsername")
    PassWord=(By.ID,"inputPassword")
    AnNiu=(By.XPATH,"/html/body/div/form/button")
    CuoWu=(By.XPATH,"/html/body/div/form/p")


class AddEvent():
    addbtu = (By.XPATH, "/html/body/div/div[1]/div[2]/button")
    addname = (By.XPATH, '//*[@id="id_name"]')
    address = (By.XPATH, '//*[@id="id_address"]')
    numbers = (By.XPATH, '//*[@id="id_limit"]')
    datetm = (By.XPATH, '//*[@id="id_start_time"]')
    submitbtu = (By.XPATH, '/html/body/div[1]/div[2]/form/div[7]/div/button')

class AddJiaBin():
    addjiabin=(By.XPATH,'//*[@id="navbar"]/ul[1]/li[2]/a')
    addtianjia=(By.XPATH,'/html/body/div/div[1]/div[2]/button')
    addfabuhui=(By.XPATH,'//*[@id="id_event"]')
    addshoujihao=(By.XPATH,'//*[@id="id_phone"]')
    addEmail=(By.XPATH,'//*[@id="id_email"]')
    addxingming=(By.XPATH,'//*[@id="id_realname"]')
    addtijiao=(By.XPATH,'/html/body/div[1]/div[2]/form/div[7]/div/button')

class ChuShiHua():
    def __init__(self,driver):
        self.driver=driver


class CaoZuo(ChuShiHua):
    def name(self,username):
        ele=self.driver.find_element(*DingWei.UserName)
        ele.clear()
        ele.send_keys(username)
    def pwd(self,password):
        ele=self.driver.find_element(*DingWei.PassWord)
        ele.clear()
        ele.send_keys(password)
    def an(self):
        ele=self.driver.find_element(*DingWei.AnNiu)
        ele.click()
    def cw(self):
        ele=self.driver.find_element(*DingWei.CuoWu)
        print(ele.text)

class AddEventcaozuo(ChuShiHua):
    def tj(self):
        ele = self.driver.find_element(*AddEvent.addbtu)
        ele.click()
    def addname(self,eventname):
        ele=self.driver.find_element(*AddEvent.addname)
        ele.clear()
        ele.send_keys(eventname)
    def add_address(self,address):
        ele=self.driver.find_element(*AddEvent.address)
        ele.clear()
        ele.send_keys(address)
    def add_nums(self,nums):
        ele=self.driver.find_element(*AddEvent.numbers)
        ele.clear()
        ele.send_keys(nums)
    def add_date(self,datetm):
        ele=self.driver.find_element(*AddEvent.datetm)
        ele.clear()
        ele.send_keys(datetm)
    def submit_btu(self):
        ele=self.driver.find_element(*AddEvent.submitbtu)
        ele.click()

class AddJiaBinCaoZuo(ChuShiHua):
    def jb(self):
        ele=self.driver.find_element(*AddJiaBin.addjiabin)
        ele.click()
    def tj(self):
        ele=self.driver.find_element(*AddJiaBin.addtianjia)
        ele.click()
    def fbh(self):
        ele=Select(self.driver.find_element(*AddJiaBin.addfabuhui))
        ele.select_by_index(3)
    def sjh(self,shj):
        ele=self.driver.find_element(*AddJiaBin.addshoujihao)
        ele.clear()
        ele.send_keys(shj)
    def Em(self,Em):
        ele=self.driver.find_element(*AddJiaBin.addEmail)
        ele.clear()
        ele.send_keys(Em)
    def xm(self,xm):
        ele=self.driver.find_element(*AddJiaBin.addxingming)
        ele.clear()
        ele.send_keys(xm)
    def tij(self):
        ele=self.driver.find_element(*AddJiaBin.addtijiao)
        ele.click()


@ddt.ddt()
class TestYeMian(unittest.TestCase):
    data=hanshu_csv(r"C:\Users\JZW\Desktop\datas.csv")
    print(data)
    @ddt.data(*data)
    @ddt.unpack
    def test_denglu(self,username,password,status):
        self.driver=webdriver.Edge()
        self.driver.get("http://150.109.156.47:8000/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        CaoZuo(self.driver).name(username)
        CaoZuo(self.driver).pwd(password)
        CaoZuo(self.driver).an()

        if status=="0":
            CaoZuo(self.driver).cw()
            self.assertEqual(status,"0")
        elif status=="1":
            sleep(3)
            AddEventcaozuo(self.driver).tj()
            sleep(3)
            AddEventcaozuo(self.driver).addname("苹果17")
            AddEventcaozuo(self.driver).add_address("鸟巢")
            AddEventcaozuo(self.driver).add_date("2023-10-21")
            AddEventcaozuo(self.driver).add_nums("1000")
            AddEventcaozuo(self.driver).submit_btu()
            sleep(3)
            xinxi = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[6]/div/p')
            print(xinxi.text)
            print(self.driver.page_source)
            self.assertIn(x , self.driver.page_source)

            sleep(3)





            self.driver.back()
            AddJiaBinCaoZuo(self.driver).jb()
            AddJiaBinCaoZuo(self.driver).tj()   #tuichu
            sleep(3)
            AddJiaBinCaoZuo(self.driver).fbh()
            AddJiaBinCaoZuo(self.driver).sjh("123456")
            AddJiaBinCaoZuo(self.driver).Em("2654@qq.com")
            AddJiaBinCaoZuo(self.driver).xm("李四")
            AddJiaBinCaoZuo(self.driver).tij()
            sleep(3)




if __name__ == '__main__':
    unittest.main()