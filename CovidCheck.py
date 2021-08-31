import tkinter, requests, tkinter.font, datetime, time, locale, os

from requests.api import options

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from bs4 import BeautifulSoup

from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *


# 언어 형식을 위한 모듈
locale.setlocale(locale.LC_ALL,"")



# 윈도우 창 표시를 위한 모듈
window = Tk()
window.geometry("300x200")
window.title("코로나 확진자 조회")




# 일일 코로나 확진자 수 Beautifulsoup 모듈
url = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=1&acq=zhfhsk+&qdt=0&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90")
Object = BeautifulSoup(url.content,'html.parser')

for result in Object.find_all(attrs={'class':'info_variation'}):
    newCorona = []
    newCorona.append(result.get_text())
    if newCorona[0] is not None:
        break



# selenium chromedriver 옵션 설정
Chrome_options = Options()
Chrome_options.headless = True

'''
# 일일 코로나 확진자 수 selenium 모듈
browser = webdriver.Chrome(executable_path="C:\chromedriver.exe", options=Chrome_options)
Selenium_URL = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=1&acq=zhfhsk+&qdt=0&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90"


tag_names = browser.find_element_by_css_selector("#target2 > dl > div:nth-child(6) > dd:nth-child(2) > span > span")
print(tag_names)
'''

# 위젯에 적용할 폰트에 대한 모듈
TextFont = tkinter.font.Font(size=15, weight="bold")
TimerFont = tkinter.font.Font(size=12, weight="bold")


# 현재 날짜를 처리할 모듈
toDate = datetime.datetime.now()
TimeSet = '%Y년 %m월 %d일 %A'
nowTime = tkinter.Label(window, text=toDate.strftime(TimeSet), font=TimerFont)
nowTime.place(x=0, y=10)



# 현재 시간을 나타내는 모듈
class Clock():
    def __init__(self):
        self.label = tkinter.Label(text="", font=TimerFont)
        self.label.place(x=0, y=35)
        self.update_clock()
        window.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        window.after(1000, self.update_clock)



# 웹 크롤링 결과를 리스트 자료형에서 문자열 자료형으로 변환하기 위한 모듈
newCorona = "".join(newCorona)



'''
# 전날 확진자 수 표시를 위한 모듈
Before_Text = tkinter.Label(window, text="전날 확진자 수:", font = TextFont)
Before_Text.place(x=0, y=70) 
Before_Corona = tkinter.Label(window, text = Before+"명", font = TextFont, foreground="red")
Before_Corona.place(x=150, y=70)
'''

# 일일 확진자 수 표시를 위한 모듈
DateCorona = tkinter.Label(window,text="일일 확진자 수:", font=TextFont)
DateCorona.place(x=0, y=100)
CoronaUp = tkinter.Label(window, text = newCorona+"명", font = TextFont, foreground="red")
CoronaUp.place(x=150, y=100)


Clock()

window.mainloop()
