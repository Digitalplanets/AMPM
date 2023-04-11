import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import spacy
import re

def scrape():
    numz = []
    driver = webdriver.Safari()
    driver.maximize_window()
    driver.get("https://app.textdrip.com/login")
    username = driver.find_element(by=By.NAME, value="email")
    username.send_keys("Ashleylynnmiller819@yahoo.com")
    time.sleep(2)
    password = driver.find_element(by=By.NAME, value="password")
    password.send_keys("Jj121218!")
    password.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.get("https://app.textdrip.com/conversations")
    scroll_box = driver.find_element('xpath', '//*[@id="sidechat"]')
    #for i in scroll_box:
        #print(i)
    l = scroll_box.find_elements(by=By.XPATH, value='//*[@id="list-empty-list2"]/div/div[3]/small')
    r = scroll_box.find_elements(by=By.XPATH, value='//*[@id="list-empty-list2"]/div/div[1]')
    g = scroll_box.find_elements(by=By.XPATH, value='//*[@id="list-empty-list2"]/div')

    for i in g:
        vv = i.text
        text = vv.strip()
        name = re.findall(r'\b[A-Z]+\s*[A-Z]+\s*[A-Z]+\s*[A-Z]+\s*', text)[0].strip()
        number = re.findall(r'\+(\d+)\s*', text)[0]
        text = re.sub(r'\s+', ' ', text)
        text = re.findall(r'(?<=\+)[^\n]+', text)[-1].strip()
        result = {'text': text}
        if 'Yes' in result['text']:
            numz.append(result['text'][:11])
        elif 'YES' in result['text']:
            numz.append(result['text'][:11])
        elif 'yes' in result['text']:
            numz.append(result['text'][:11])
        elif 'yea' in result['text']:
            numz.append(result['text'][:11])
        elif 'Sure' in result['text']:
            numz.append(result['text'][:11])
        elif 'sure' in result['text']:
            numz.append(result['text'][:11])
    driver.quit()
    return numz

nlp = spacy.load("en_core_web_sm")

def sim(x,y):
    x = x.lower()
    y = y.lower()
    name01 = nlp(x)
    name02 = nlp(y)
    ss = name01.similarity(name02)
    return ss

def mhquote(x):
    if x > 18 and x < 25:
        qr = "$232-$298"
    if x > 25 and x < 30:
        qr = "$210-$302"
    if x > 30 and x < 35:
        qr = "$236-$318"
    if x > 35 and x < 40:
        qr = "$284-$342"
    if x > 40 and x < 45:
        qr = "$345-$398"
    if x > 45 and x < 50:
        qr = "$364-$442"
    if x > 50 and x < 55:
        qr = "$448-$502"
    if x > 55 and x < 64:
        qr = "$502-$588"
    if x > 64:
        qr = "Age error"
    return qr

def fhquote(x):
    if x > 18 and x < 25:
        qr = "$232-$298"
    if x > 25 and x < 30:
        qr = "$272-$338"
    if x > 30 and x < 35:
        qr = "$304-$362"
    if x > 35 and x < 40:
        qr = "$328-$364"
    if x > 40 and x < 45:
        qr = "$352-$398"
    if x > 45 and x < 50:
        qr = "$398-$452"
    if x > 50 and x < 55:
        qr = "$434-$474"
    if x > 55 and x < 64:
        qr = "$498-$584"
    return qr

def mhdvquote(x):
    if x > 18 and x < 25:
        qr = "$238-$304"
    if x > 25 and x < 30:
        qr = "$262-$318"
    if x > 30 and x < 35:
        qr = "$278-$332"
    if x > 35 and x < 40:
        qr = "$298-$372"
    if x > 40 and x < 45:
        qr = "$326-$398"
    if x > 45 and x < 50:
        qr = "$398-$466"
    if x > 50 and x < 55:
        qr = "$462-$508"
    if x > 55 and x < 64:
        qr = "$544-$598"
    return (qr)


headers = {
    'Authorization': 'Bearer t0pDPeQjnvr3mCkSsWyc0P1qpEhCLYwbwxnxj2gb'
    }

#numbers = numbers in selected dataframe. 


def chckinfo():
    try:
        name = driver.find_element(by=By.XPATH, value='/html/body/main/div/div[2]/div[1]/div[2]/div[1]/div[1]/p')
        return True
    except NoSuchElementException:
        return False
    else:
        print('unknown error, contact hue')



def checkyes():
    hapik = requests.get('http://www.huemanservices.com/19keyscount')
    if hapik.status_code == 200:
        pass
    else:
        return
    numbers = scrape()
    for i in numbers:
        number = i
        chaturl= 'https://api.textdrip.com/api/get-chats'
        gg=requests.post(chaturl, headers=headers, data={'phone':number, "page": "1"})
        gg=json.loads(gg.text)
        chats = gg['chats']['data']
        number = number
        for i in chats:
            if i.get("type") == 'sender' and i.get("message") == 'yes' or i.get("message") == 'Yes' :
                lookup = requests.post("https://api.textdrip.com/api/get-contact-detail", headers = headers, data={"phone": number})
                cont = json.loads(lookup.text)
                name1 = cont['contact']['name']
                driver = webdriver.Safari()
                driver.maximize_window()
                srcnumber = number[1:]
                formattedNumber = '-'.join([srcnumber[:3], srcnumber[3:6], srcnumber[6:]])
                driver.get('https://www.peoplesearchnow.com/phone/' + formattedNumber)
                time.sleep(2)
                if checkinfo() == True:
                    name2 = driver.find_element(by=By.XPATH, value='/html/body/main/div/div[2]/div[1]/div[2]/div[1]/div[1]/p')
                    name2 = name2.text
                else:
                    name2 = 'need name'
                    
                ssc = sim(name1, name2)
                if ssc < 0.4:
                    sndurl = "https://api.textdrip.com/api/send-message"
                    data = {
                        "receiver": number,
                        "message": 'Okay no problem, I just need your Age and Zip code to produce some accurate quotes for you. If you would like a family quote please include their ages as well.'
                        }
                    jj = requests.post(sndurl, headers=headers, data=data)
                    #print('Requested Additional information for: ',number)
                else:
                    age = driver.find_element(by=By.XPATH, value='/html/body/main/div/div[2]/div[1]/div[2]/div[1]/div[2]/p[1]/span[2]')
                    ages=age.text.strip()
                    driver.close()
                    vari = mhquote(int(ages))
                    sndurl = "https://api.textdrip.com/api/send-message"
                    data = {
                        "receiver": number,
                        "message": str(vari)+ ''' Monthly \n United Healthcare Network PPO Nationwide coverage \n $0  Calendar Year Deductible for Day to Day Services Fully Tax Deductible No copays 24 mo. Rate Guarantee Dental/Vision(optional) Does this work for your budget?'''
                        }
                    jj = requests.post(sndurl, headers=headers, data=data)
                    text_display.insert(tk.END, data['message'])
                    text_display.insert(tk.END, number)
                    numbers.remove(number)
            else:
                pass

import tkinter as tk

def run_clicked():
    text_display.insert(tk.END, 'Running...\n')

# Create main window
window = tk.Tk()
window.title('Tylers Interface')

# Create a text widget for displaying results
text_display = tk.Text(window, wrap=tk.WORD, height=10, width=40)
text_display.pack(padx=10, pady=10)

# Create a 'Run' button
run_button = tk.Button(window, text='Run', command=checkyes)
run_button.pack(padx=10, pady=10)

# Start the main loop
window.mainloop()
