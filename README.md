# whatsapp-automation
A simple Python Script for whatsapp automation.

## Requirements.
- Selenium
- Python 2.7 > or Python 3 or Greater. (Preferably Python3)
- Chromium Browser
- Chrome web driver

## Steps
### 1. Install Python 3
Check for the default version of Python which you have in your system by the following command.

 `python --version`
 
 You will get the Default version as ` Python 2.7.5` which will be your default version of python in yout system.
 We have to download the Python 3 version as that will only have the pip command which comes with Python3.
 
 Go to this [page](https://www.python.org/downloads/) for downloading the latest version of Python 3.
 Extract and install it. Run the shell script to update the path and restart your default terminal.
 
 Now if you go and type the following command you will get the verstion number.
 
 `python3 --version`
 
 ### 2. Install Selenium
 Once python3 is installed the `pip` command will be activated. Its a package for installing other modules.
 With pip you can install Selenium with the following command.
 
 `pip install -U selenium`
 
 Selenium will be installed.
 
 ### 3. Install Chromium Browser
 
Chromium Browser can be installed from this [link](https://chromium.woolyss.com/download/en/).

### 4. Install the Chrome web driver

Install the chromewebdriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
**NOTE : Get the version which is similar to the chrome browser. This is required for the webdriver to work properly.**

Extract and make note of the folder in which the driver is installed. It is required to modify the code accordingly.



### Make changes in the code accroding to your need. Refer the comments in the code for any doubt.


### 5. Run the Code

In your terminal run the following command to execute the script.

`python3 whatsapp.py` 

Make sure to use python3 and not python.

A new instance of the browser will start and you might need to login to your whatsapp account using the QR code and the code will execute automatically.
