from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


def upVote():

    linkOfThePost = input("Enter URL of the post: ")

    caps = webdriver.DesiredCapabilities.CHROME.copy()
    caps['acceptInsecureCerts'] = True
    caps['acceptSslCerts'] = True
    browser = webdriver.Chrome(desired_capabilities=caps)
    
    df = pd.read_csv("accounts.csv")
    userNamesOfAccounts = df.loc[:]["username"];
    passwordsOfAccounts = df.loc[:]["password"];
    
    print(df)
    print(userNamesOfAccounts)
    i = 0

    while(i<len(df)):
        print(type(userNamesOfAccounts)) 

        browser.get("https://www.reddit.com/")
        time.sleep(3)

        browser.get("https://www.reddit.com/login/")
        time.sleep(3)

        usernameInfo = userNamesOfAccounts[i]
        passwordInfo = passwordsOfAccounts[i]

        usernameInput = browser.find_element_by_id('loginUsername')
        passwordInput = browser.find_element_by_id('loginPassword')
        usernameInput.send_keys(usernameInfo)       
        passwordInput.send_keys(passwordInfo)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)

        browser.get(linkOfThePost)
        time.sleep(3)    
        upVoteButton = browser.find_element_by_css_selector(".voteButton")
        time.sleep(3)
        upVoteButton.click()
        time.sleep(3)
        
        i+=1
    
    browser.close()

upVote()