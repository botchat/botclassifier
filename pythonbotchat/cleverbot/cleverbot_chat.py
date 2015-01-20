"""
It is very simple selnium based code which cat with clevarbot and genrate log from chat
"""
import time
from datetime import datetime
from selenium import webdriver

def botcollectlog(url,name):
    browser = webdriver.Firefox()
    browser.get(url)
    name_of_log = datetime.now().strftime(name+"_%Y_%m_%d_%H_%M_%S.log")
    writelog = open(name_of_log,'w')
    # below list will change after based on db creation current it is static.list should have at least 20-25 questions
    list_q = ["how are you?" ,"are you good thinker?", "well me absolutly fine ","yes","i like know more about you"]
    submit = browser.find_element_by_css_selector("input.bb#sayit")
    submit.click()
    submit = browser.find_element_by_css_selector(".obscure.extend.show")
    submit.click()
    for line in list_q:
        input = browser.find_element_by_id("stimulus")
        input.send_keys(line)
        time.sleep(2)
        submit = browser.find_element_by_css_selector("input.bb#sayit")
        submit.click()
        writelog.write("["+time.strftime("%H:%M:%S:%s")+"]code: "+line+"\n") 
        time.sleep(5)
        text = browser.find_element_by_id("typArea")
        while text.text.strip() == "":
          time.sleep(1)
          text = browser.find_element_by_id("typArea")
        writelog.write("["+time.strftime("%H:%M:%S:%s")+"]bot: "+text.text+"\n")
    writelog.close()

if __name__ == "__main__":
    url = "http://www.cleverbot.com/"
    name = "cleverbot"
    botcollectlog(url,name)
