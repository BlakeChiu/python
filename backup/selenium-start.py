#載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#建立Driver物件實體，用程式操作瀏覽器運作 
driver=webdriver.Chrome() #不要做Options的設定，讓他去抓預設值
driver.maximize_window() #視窗最大化
driver.get("http:WWW.google.com/")
driver.save_screenshot("screenshow-google.png") #做網頁截圖
driver.get("https://WWW.ntu.edu.tw/")
driver.save_screenshot("screenshot-ntu.png")
driver.close()