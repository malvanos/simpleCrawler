import requests
from bs4 import BeautifulSoup
import sys

if (len(sys.argv) != 2):
    print "Please run the script using simple.py <site>"
    exit(0)

url = str(sys.argv[1])
if ("http" not in url):
    url = "http://" + url

print 'Extracting text from url:', url


page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out


extractedText = soup.find_all('body')[0].get_text()
extractedText = extractedText.encode('ascii', errors='ignore')

for rmtext in ('\n','\r','\t',' | ', ' , ', ' : ', ' / ','    ', '   ', '  ', ):
    extractedText = extractedText.replace(rmtext, ' ')

print extractedText
