#import statements
import requests
from bs4 import BeautifulSoup
import json

#Note p_name, p_img, etc. refer to a single product's attributes


#Get Search String from User
searchstring=input("Enter Your Search String: ")
url=("https://www.amazon.com/s?k="+searchstring)

jsonfilename=searchstring+'.json'

#Establish Connection with Amazon.com

#Headers has been used because Amazon recommends API for scraping. If there is any error during run, replace this header with a new one. New Header is just a google search away!

headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

r = requests.get(url, headers=headers)

#Make the soup!
soup=BeautifulSoup(r.text, 'lxml')

jstring=dict() #string for JSON formation

i=0 #this will act as an index for each product


#extracting data from the soup
for each in soup.findAll('div', class_='sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item s-asin sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32'):

#getting the product name
  i=i+1
  try:
    p_name=each.find('span', class_='a-size-base-plus a-color-base a-text-normal').text
  except:
    p_name='Error!'

#getting the product image link
  try:
    p_img=each.find('img', class_='s-image')['src']
  except:
    p_img='no image available'

#getting the product ratings
  try:
    p_stars=each.find('span', class_='a-icon-alt').text 
  except:
    p_stars='no ratings available'

#getting the number of reviews
  try:
    p_reviews=each.find('span', class_='a-size-base').text
  except:
    p_reviews='no reviews written'


#getting the product price
  try:
    p_price=each.find('span', class_='a-price')
    p_price1=p_price.find('span', class_='a-offscreen').text
  except:
    p_price1='no price quoted'


#converting to JSON
  jstring[i]={"p_name":p_name, "p_img":p_img, "p_stars":p_stars, "p_reviews":p_reviews, "p_price":p_price1}
  with open(jsonfilename, 'w') as outfile:
    json.dump(jstring, outfile, indent=2)

print('Your JSON file titled '+jsonfilename+' has been created!')



        
  

    

  