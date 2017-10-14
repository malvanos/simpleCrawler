import sys
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


if (len(sys.argv) != 2):
    print "Please run the script using simple.py <site>"
    exit(0)

url = str(sys.argv[1])
if ("http" not in url):
    url = "http://" + url

print 'Extracting text from url:', url

pathname = os.path.dirname(sys.argv[0])        
path_to_chromedriver =  os.path.abspath(pathname)+ '/driver/chromedriver' # change path as needed

if(not os.path.isfile(path_to_chromedriver)):
    print "ERROR: Didn't find the chrome driver in " + path_to_chromedriver +"."
    print "ERROR: Please download from http://chromedriver.storage.googleapis.com/index.html "
    print "       and unzip it to the driver directory."
    exit(0)


browser = webdriver.Chrome(executable_path = path_to_chromedriver)
browser.get(url)

# You can change also the frame:
# browser.switch_to_frame('mainFrame')
# You can also use actions such as:
# browser.find_elements_by_xpath('//input[@value="Download"]').click()

page = browser.find_element(By.XPATH, '//body').text
browser.quit()
soup = BeautifulSoup(page, 'html.parser')

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

extractedText = soup.get_text()
extractedText = extractedText.encode('ascii', errors='ignore')

for rmtext in ('\n','\r','\t',' | ', ' , ', ' : ', ' / ','    ', '   ', '  ', ):
    extractedText = extractedText.replace(rmtext, ' ')

print extractedText
