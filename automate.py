from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import requests
import os, sys
from selenium import webdriver
import time
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from random import randint
from fake_useragent import UserAgent
import shutil
from pathlib import Path
import fitz
class Property:
    def __init__(self, name):
        self.url = name
    def print_information(self):
        print(f"データ種類: {self.データ種類}")
        print(f"物件種別: {self.物件種別}")
        print(f"登録年月日: {self.登録年月日}")
        print(f"取引態様: {self.取引態様}")
        print(f"価格: {self.価格}")
        print(f"土地面積: {self.土地面積}")
        print(f"私道面積: {self.私道面積}")
        print(f"所在地: {self.所在地}")
        print(f"沿線名: {self.沿線名}")
        print(f"現況: {self.現況}")
        print(f"引渡時期: {self.引渡時期}")
        print(f"都市計画: {self.都市計画}")
        print(f"地目: {self.地目}")
        print(f"建ぺい率: {self.建ぺい率}")
        print(f"地勢: {self.地勢}")
        print(f"接道状況: {self.接道状況}")
        print(f"接道種別: {self.接道種別}")
        print(f"接道位置指定: {self.接道位置指定}")
        print(f"接道１方向: {self.接道１方向}")
        print(f"接道２方向: {self.接道２方向}")

        print(f"m単価: {self.m単価}")
        print(f"坪単価: {self.坪単価}")
        print(f"面積計測方式: {self.面積計測方式}")
        print(f"最寄駅: {self.最寄駅}")
        print(f"用途地域: {self.用途地域}")
        print(f"容積率: {self.容積率}")
        print(f"建築条件: {self.建築条件}")
        print(f"接道接面: {self.接道接面}")
        print(f"接道１幅員: {self.接道１幅員}")
        print(f"接道２幅員: {self.接道２幅員}")
    

def pdf_to_html(name):
    pdf = fitz.open(name + ".pdf")
    page = pdf.load_page(0)
    html = page.get_text("html")
    html_output = open(name + ".html", "w")
    html_output.write(html)
    html_output.close
def delete_html(name):
    try:
        os.remove(f"{name}.html")
        #print("Removed HTML File")
    except Exception as e:
        print(e)
def scrape_from_html(name):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('log-level=3')
    options.add_argument("--headless")
    browser = webdriver.Chrome(options = options)
    browser.maximize_window()
    html_file = os.path.join(Path().resolve(), name + ".html")
    browser.get(html_file)
    plist = browser.find_elements(By.TAG_NAME, "p")
    #print(plist)

    # find_style = browser.find_element(By.XPATH, '//*[@id="page0"]/p[43]').get_attribute('style')
    # print(find_style)
    prop = Property(name)
    prop.データ種類 = None
    prop.物件種別 = None
    prop.登録年月日 = None
    prop.取引態様 = None
    prop.価格 = None
    prop.土地面積 = None
    prop.私道面積 = None #
    prop.所在地 = None #
    prop.沿線名 = None #
    prop.現況 = None #
    prop.引渡時期 = None #
    prop.都市計画 = None #
    prop.地目 = None #
    prop.建ぺい率 = None #
    prop.地勢 = None #
    prop.接道状況 = None #
    prop.接道種別 = None #
    prop.接道位置指定 = None #
    prop.接道１方向 = None #
    prop.接道２方向 = None #
    prop.m単価 = None
    prop.坪単価 = None
    prop.面積計測方式 = None
    prop.最寄駅 = None
    prop.用途地域 = None
    prop.容積率 = None
    prop.建築条件 = None
    prop.接道接面 = None
    prop.接道１幅員 = None
    prop.接道２幅員 = None

    for p in plist:
        tempstyle = p.get_attribute('style')
        if tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 178pt; left: 121pt;':
            prop.価格 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 101pt; left: 127pt;':
            prop.データ種類 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 114pt; left: 127pt;':
            prop.物件種別 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 140pt; left: 127pt;':
            prop.登録年月日 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 153pt; left: 127pt;':
            prop.取引態様 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 216pt; left: 146pt;':
            prop.土地面積 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 229pt; left: 146pt;':
            prop.私道面積 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 255pt; left: 127pt;':
            prop.所在地 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 280pt; left: 127pt;':
            prop.沿線名 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 331pt; left: 186pt;':
            prop.現況 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 344pt; left: 176pt;':
            prop.引渡時期 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 369pt; left: 176pt;':
            prop.都市計画 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 382pt; left: 196pt;':
            prop.地目 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 395pt; left: 191pt;':
            prop.建ぺい率 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 446pt; left: 186pt;':
            prop.地勢 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 472pt; left: 196pt;':
            prop.接道状況 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 484pt; left: 196pt;':
            prop.接道種別 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 497pt; left: 206pt;':
            prop.接道位置指定 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 510pt; left: 196pt;':
            prop.接道１方向 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 522pt; left: 196pt;':
            prop.接道２方向 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 178pt; left: 437pt;':
            prop.m単価 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 191pt; left: 437pt;':
            prop.坪単価 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 229pt; left: 477pt;':
            prop.面積計測方式 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 280pt; left: 408pt;':
            prop.最寄駅 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 369pt; left: 467pt;':
            prop.用途地域 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 395pt; left: 462pt;':
            prop.容積率 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 446pt; left: 487pt;':
            prop.建築条件 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 472pt; left: 462pt;':
            prop.接道接面 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 510pt; left: 462pt;':
            prop.接道１幅員 = p.text.strip()
        elif tempstyle == 'position: absolute; white-space: pre; margin: 0px; padding: 0px; top: 522pt; left: 462pt;':
            prop.接道２幅員 = p.text.strip()
        

        
        






    # print(f"データ種類: {データ種類}")
    # print(f"物件種別: {物件種別}")
    # print(f"登録年月日: {登録年月日}")
    # print(f"取引態様: {取引態様}")
    # print(f"価格: {価格}")
    # print(f"土地面積: {土地面積}")
    # print(f"私道面積: {私道面積}")
    # print(f"所在地: {所在地}")
    # print(f"沿線名: {沿線名}")
    # print(f"現況: {現況}")
    # print(f"引渡時期: {引渡時期}")
    # print(f"都市計画: {都市計画}")
    # print(f"地目: {地目}")
    # print(f"建ぺい率: {建ぺい率}")
    # print(f"地勢: {地勢}")
    # print(f"接道状況: {接道状況}")
    # print(f"接道種別: {接道種別}")
    # print(f"接道位置指定: {接道位置指定}")
    # print(f"接道１方向: {接道１方向}")
    # print(f"接道２方向: {接道２方向}")

    # print(f"m単価: {m単価}")
    # print(f"坪単価: {坪単価}")
    # print(f"面積計測方式: {面積計測方式}")
    # print(f"最寄駅: {最寄駅}")
    # print(f"用途地域: {用途地域}")
    # print(f"容積率: {容積率}")
    # print(f"建築条件: {建築条件}")
    # print(f"接道接面: {接道接面}")
    # print(f"接道１幅員: {接道１幅員}")
    # print(f"接道２幅員: {接道２幅員}")
    prop.print_information()
def run_program(name):
    pdf_to_html(name)
    scrape_from_html(name)
    delete_html(name)

while True:
    try:
        print("Please give the name of the PDF")
        name = input()
        run_program(name)
    except Exception as e:
        print(e)

    