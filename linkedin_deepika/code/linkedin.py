#DataFlair's Guide to Automating LinkedIn Connections using Python 
#Import libraries
from selenium import webdriver

#-------------------------------------------------------------------------------------#
def login_to_linkedin():
    #Find username
    Username=browser.find_element_by_name("session_key")
    #Send username details
    Username.send_keys("enter username")
    #Find password
    password=browser.find_element_by_name("session_password")
    #Send password details
    password.send_keys("enter password")
    #Submit button
    browser.find_element_by_xpath("//button[@type='submit']").click()
#-------------------------------------------------------------------------------------#

def navigate_to_network_and_connect():
    #Navigate to the network page
    browser.find_element_by_xpath('//*[@id="ember21"]').click()
    #Cause a delay so it does not throw an error
    browser.implicitly_wait(5)
    #Select 'See All'
    browser.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[2]/div/div/main/ul/li[1]/div/button/span').click()
    #Obtain the number of items containing the same path 
    elements = browser.find_elements_by_xpath('/html/body/div[3]/div/div/div[2]/section/div/ul/li')
    for i in range(1,len(elements)+1):
        #Send connection request
        browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/section/div/ul/li[{}]/div/section/div[2]/footer/button/span'.format(str(i))).click()
        #Connections send to 13 people at a time
        print('Connection request sent to person {}'.format(str(i)))
        #Cause a time delay before progressing to next person
        browser.implicitly_wait(1)
#-------------------------------------------------------------------------------------# 

#Open the webbrowser and use it for autonomous control
browser = webdriver.Firefox(executable_path='/home/deepika/Downloads/internship/instagram/geckodriver')
#Open the URL in the opened webbrowser
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
#Start using the functions after a delay
browser.implicitly_wait(5)
#Call all the functions in order based on webpages
login_to_linkedin()
navigate_to_network_and_connect()
