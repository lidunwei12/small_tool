# -*- coding: utf-8 -*-
"""
Created on Thu Sep 7 14:21:28 2018

@author: bob.lee
"""
from selenium import webdriver
import win32gui
import win32con
import time
import os
import re

DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/'))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)


def pdf_word(driver_home, file_home):
    driver = webdriver.Chrome(driver_home)
    driver.get('https://pdf2docx.com/zh/')
    for file in os.listdir(file_home):
        driver.find_element_by_xpath('//*[@id="pick-files"]').click()
        time.sleep(1)
        filename = file_home + re.findall(r'\\', '\\\\')[0] + file
        print(filename)
        dialog = win32gui.FindWindow(None, '打开')  # 对话框
        combo_box_ex32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        com_bo_box = win32gui.FindWindowEx(combo_box_ex32, 0, 'ComboBox', None)
        edit = win32gui.FindWindowEx(com_bo_box, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filename)  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
    temp = driver.find_element_by_xpath('//*[@id="download-all"]').is_enabled()
    while temp is False:
        temp = driver.find_element_by_xpath('//*[@id="download-all"]').is_enabled()
    driver.find_element_by_xpath('//*[@id="download-all"]').click()
    driver.quit()
