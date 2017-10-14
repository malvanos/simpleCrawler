# simpleCrawler

Simple python script that uses the bs4 package to extract the text from the
body of a webpage without html tags or Javascript.


## Requirements

Install the following packages:

pip install requests
pip install bs4

For the Selenium crawler you need also the selenium package:

pip install selenium

You have also to download the driver from here and unzip it in a directory
named driver:

http://chromedriver.storage.googleapis.com/index.html


## Instructions

Run python simple.py www.google.com to test it.

Run python simpleSelenium.py www.google.com to test it with the google chrome driver.

