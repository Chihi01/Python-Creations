import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera

from pyzbar.pyzbar import decode
from PIL import Image
import time
from threading import Thread
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from discord_webhook import DiscordWebhook, DiscordEmbed
import random
import datetime

class search(FloatLayout, BoxLayout):
    price = ObjectProperty(None)
    store = ObjectProperty(None)
    date = ObjectProperty(None)

    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
    
    

    def clear(self):
        self.price.text = ""
        self.store.text = ""
        self.date.text = ""
        self.name.text = "Scan Barcode for Name / Size"

    def open(self):
        img = (Image.open('IMG_7605.jpg'))

        for code in decode(img):
            barcode = (code.data.decode("UTF-8"))

        url = "http://www.searchupc.com/default.aspx?q=" + barcode

        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=selenium")
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome("C:/Users/Rik - Desktop/Downloads/chromedriver_win32/chromedriver.exe", options=chrome_options)

        driver.get(url)
        
        time.sleep(2)

        p = self.price.text
        s = self.store.text
        d = self.date.text
        print(self.price.text, self.store.text, self.date.text)

        time.sleep(2)
        try:
            name = driver.find_element_by_xpath('//a[@target="_blank"]').text
            print(name)
        except:
            name = "Shoe not found"

        driver.close()
        print("Closed Driver")

        t = name
        self.ids.name_label.text = name

    def insert(self):

        p = self.price.text
        s = self.store.text
        d = self.date.text
        name = self.name.text
        
        with open("CookbookTest.csv", "a") as f:
                f.write(name + " - " + p + " - " + s + " - " + d + "\n")

        print("Exported to CookBook")
        
class MyApp(App):
    def build(self):
        Window.clearcolor = (0,0.2,0.205,1)
        return search()
        

if __name__ == "__main__":
    MyApp().run()