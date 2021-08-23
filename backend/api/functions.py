
# remove this
from selenium import webdriver
import time
import pymongo
import copy
import requests
from bs4 import BeautifulSoup

client = pymongo.MongoClient(
    "mongodb+srv://sociality:sociality@cluster0.bvjnq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['sociality_db']
product_col = db['products']


def generateProductId():
    document = product_col.find_one({'_id': 'last_product_id'})
    if document:
        product_col.find_one_and_update(
            {'_id': 'last_product_id'}, {'$inc': {'last': 1}})
        return document['last'] + 1
    else:
        product_col.insert_one({'_id': 'last_product_id', 'last': 1})
        return 1

# the function below is suspended bcz it doesn't work on google cloud run


def addingProductOlder(product_link, driver):

    result = {}
    driver.get(product_link)
    try:
        result['_id'] = generateProductId()

    except Exception as e:
        result['_id'] = f'cant be fetched because of {e}'

    try:
        result['name'] = driver.find_element_by_xpath(
            '//*[@id="listing-page-cart"]/div[2]/h1').text

    except Exception as e:
        result['name'] = f'cant be fetched because of {e}'

    try:
        result['image'] = driver.find_element_by_xpath(
            '//*[@id="listing-right-column"]/div/div[1]/div[1]/div/div/div/div/div[1]/ul/li[1]/img').get_attribute('src')

    except Exception as e:
        result['image'] = f'cant be fetched because of {e}'

    try:
        result['price'] = driver.find_element_by_xpath(
            '//*[@id="listing-page-cart"]/div[3]/div[1]/div[1]/div/div[1]/p').text.replace('Price:', '')

    except Exception as e:
        result['price'] = f'cant be fetched because of {e}'

    filter = copy.deepcopy(result)
    del filter['_id']

    is_a_clone = product_col.find_one(filter)

    if not is_a_clone:
        product_col.insert_one(result)
    else:
        result['_id'] -= 1
        product_col.find_one_and_update(
            {'_id': 'last_product_id'}, {'$inc': {'last': -1}})

    return result


def addingProduct(product_link):

    result = {}
    page = requests.get(product_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        result['_id'] = generateProductId()

    except Exception as e:
        result['_id'] = f'cant be fetched because of {e}'

    try:
        result['name'] = soup.find(
            'h1', {'class': 'wt-text-body-03 wt-line-height-tight wt-break-word wt-mb-xs-1'}).text

    except Exception as e:
        result['name'] = f'cant be fetched because of {e}'

    try:
        result['image'] = soup.find('img', {
                                    'class': 'wt-max-width-full wt-horizontal-center wt-vertical-center carousel-image wt-rounded'})['src']

    except Exception as e:
        result['image'] = f'cant be fetched because of {e}'

    try:
        result['price'] = soup.find(
            'p', {'class': 'wt-text-title-03 wt-mr-xs-2'}).text.replace('+', '')

    except Exception as e:
        result['price'] = f'cant be fetched because of {e}'

    filter = copy.deepcopy(result)
    del filter['_id']

    is_a_clone = product_col.find_one(filter)

    if not is_a_clone:
        product_col.insert_one(result)
    else:
        result['_id'] -= 1
        product_col.find_one_and_update(
            {'_id': 'last_product_id'}, {'$inc': {'last': -1}})

    return result


def showProductDetails(product_id):
    try:
        result = product_col.find_one({'_id': product_id})

    except Exception as e:
        print('couldnt reach to database')
        result = 'couldnt reach to database'
    # if not result:
    #     result = 'there isnt such a product in database'
    return result


def listProducts():
    result = {}
    try:
        for document in product_col.find():
            doc_id = document['_id']
            if doc_id != 'last_product_id':
                result[doc_id] = document
    except Exception as e:
        result[0] = e
    return result
