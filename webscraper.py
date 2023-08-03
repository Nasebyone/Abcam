from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import sys 

sys.setrecursionlimit(10**8)  #increase repition limit for loops 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options) #seperates the web instance from the script
driver.get("https://www.abcam.com/products") #launch the abcam website
driver.maximize_window()


def pageLoad(): # a function which checks if the page has loaded
    try:
        driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click() #checks for the cookie notice and accepts it
    except: #if 
        pageLoad() #loops the function if page hasn't reloaded


def NewDataLoad(): #a function to check if more product data has been loaded
    try:
        driver.find_element(By.XPATH,'//*[@id="search_result_container"]/div[3]/div[2]/div[2]/div[' + str(count) + ']') #searches for a 
    except:
        NewDataLoad() #loops the function if the data hasn't reloaded

product_list = [] #creates a list to hold the scoured data

pageLoad() # checks if the page has loaded
count = 1 # initiate a counter which will be used to iterate through the products
product = ()
while count <= 95447: #maximum number of products to scoure
    try:
        driver.find_element(By.XPATH,'//*[@id="search_result_container"]/div[3]/div[2]/div[3]/button').click() #if a next page button appears - click it
        count+1
        NewDataLoad() #wait for the new data to load before proceeding
    except:
        pass
    if count % 20 == 0: #the website display data into groups of 20, when reached the bottom of the page scroll down to load more data
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll to the bottom of the page
        count += 1    
        NewDataLoad() # wait for the new data to load before proceeding


    path = '//*[@id="search_result_container"]/div[3]/div[2]/div[2]/div[' + str(count) + ']' #create a path to the product data using the count to select the correct div


    product_name = driver.find_element(By.XPATH, path).get_attribute("data-productname") #get the product name from the div and remove the Abcam id
    product_name = product_name.split() # Split the string
    product_name = ' '.join(product_name[:-1]) # Join the words

    product_code = driver.find_element(By.XPATH, path).get_attribute("data-productcode") #find the product code from the div

    try: #not all  products have descriptions so this code stops errors
        product_description = driver.find_element(By.XPATH, '//*[@id="search_result_container"]/div[3]/div[2]/div[2]/div[' + str(count) +   ']/div[3]/div/div[3]/div[2]').text #find the product description from the div
                                                            
    except:
        product_description = "" #html cant display a NONE value so an empty string is used instead

    try:
        product_image_link = driver.find_element(By.XPATH, '//*[@id="search_result_container"]/div[3]/div[2]/div[2]/div[' + str(count) +   ']/div[2]/div/img').get_attribute("src") 
    except:
        product_image_link = ""

    product = (count, product_name, product_code, product_image_link, product_description, "https://www.abcam.com/products/" + product_code)
    product_list.append(product)
    print(product_code + ":", product_name + ":", product_description)
    print("-----------------------------------------------------------------------", count, "-----------------------------------------------------------------------")
    count += 1


print(product_list)
import csv
with open('Scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(product_list)
