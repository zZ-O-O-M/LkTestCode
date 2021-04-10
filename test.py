import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test1(self):
    self.driver.get("https://student.altstu.ru/login/")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.ID, "id_login").click()
    self.driver.find_element(By.ID, "id_login").send_keys("123123@mail.ru")
    self.driver.find_element(By.CSS_SELECTOR, ".form-signin").click()
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.ID, "id_password").send_keys("1232121213213123213")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Вход по номеру зачётки").click()
    self.driver.find_element(By.ID, "id_reg_number").send_keys("17110762")
    self.driver.find_element(By.CSS_SELECTOR, "label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".navbar-nav > li:nth-child(1) > a").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav > li:nth-child(2) > a").click()
    self.driver.find_element(By.CSS_SELECTOR, ".navbar-brand span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".navbar-nav > li:nth-child(1) > a").click()
    self.driver.find_element(By.LINK_TEXT, "Архивные сообщения").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fi-msg-item:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#accordion1 .fi-sender").click()
    self.driver.find_element(By.LINK_TEXT, "Группа ПИ-72").click()
    self.driver.find_element(By.LINK_TEXT, "Выход").click()
    self.driver.find_element(By.LINK_TEXT, "Регистрация").click()
    self.driver.find_element(By.CSS_SELECTOR, "img").click()
    self.driver.find_element(By.ID, "id_login").send_keys("213123")
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.ID, "id_password").send_keys("213")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Вход по номеру зачётки").click()
    self.driver.find_element(By.ID, "id_reg_number").send_keys("17110762")
    self.driver.find_element(By.ID, "id_reg_number").send_keys(Keys.ENTER)
  
