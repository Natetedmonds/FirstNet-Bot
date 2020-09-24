from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as xC
import time
import tkinter as tk

#********* Actual App ***********#

def iotCancelRequest():

  iccid = ent_iccid.get()

  #options = Options()
  #options.headless = True
  browser = webdriver.Chrome(ChromeDriverManager().install())#, chrome_options = options)
  #browser = webdriver.Firefox()
  browser.maximize_window()
  browser.get("https://localcontrol.firstnet.att.com/admin")

  try:
    text = WebDriverWait(browser, 10).until(xC.presence_of_element_located((By.ID, "username")))

  finally:
    print ("Login Page Loaded")

  time.sleep(2)
  elm = browser.find_element_by_id("username")
  elm.clear()
  elm.send_keys("youremail@domain.org")

  elm = browser.find_element_by_id("password")
  elm.clear()
  elm.send_keys("yourpass")
  elm.send_keys(Keys.RETURN)

  try:
    text = WebDriverWait(browser, 10).until(xC.presence_of_element_located((By.ID, "tour-intro-modal")))

  finally:
    print ("Admin Options Page Loaded")

  time.sleep(3)
  elm = browser.find_element_by_class_name("fn-modal-close")
  elm.click()

  time.sleep(2)
  elm = browser.find_element_by_class_name("joyride-tooltip__close--header")
  elm.click()

  elm = browser.find_element_by_class_name("manage-iot")
  elm.click()

  time.sleep(3)
  browser.execute_script("window.open('');")
  browser.switch_to.window(browser.window_handles[1])
  browser.get("https://cc19.jasper.com/provision/ui/terminals/sims/sims.html")
  print("IOT Page Loaded")

  time.sleep(2)

  elm = browser.find_element_by_id("jw-searchfield-1066-inputEl")
  elm.send_keys(iccid)
  elm.send_keys(Keys.RETURN)
  time.sleep(1)

  elm = browser.find_element_by_link_text(iccid)
  elm.click()

  time.sleep(2)
  elm = browser.find_element_by_id("jw-button-1029")
  elm.click()
  print("SIM Page Loaded")

  time.sleep(2)
  elm = browser.find_element_by_id("jw-button-1399") #firefox is 1401
  elm.click()
  time.sleep(6)
  print("Cancel Request Sent")

  lbl_resetFin["text"] = "Cancel Request Sent!"

  browser.quit()

  lbl_resetFin ["text"] = "Ready for request"

  
  
  
  
  

  

#******** GUI ******************

window = tk.Tk()
window.title("IoT Tools Automate")

frm_entry = tk.Frame(master=window)
ent_iccid = tk.Entry(master=frm_entry, width = 40)
lbl = tk.Label(master=frm_entry, text="ICCID")

ent_iccid.grid(row=0, column=0, sticky="e")
lbl.grid(row=0, column=1, sticky="w")


btn = tk.Button(master=window, text="Send Cancel Request", command=iotCancelRequest)
lbl_resetFin = tk.Label(master=window, text="Ready for request ")
frm_entry.grid(row=0, column=0, padx=10)
btn.grid(row=0, column=1, pady=10, padx=10)
lbl_resetFin.grid(row=1, column=1, padx=10)

window.mainloop()


#********************************#








