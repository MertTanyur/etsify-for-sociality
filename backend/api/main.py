from selenium import webdriver
from fastapi import FastAPI, HTTPException
from api.functions import *
import api.config as config
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
if config.dockerized:
    print('app running on guvicorn fastapi')
    origins = [
        "https://etsify-for-sociality.netlify.app",
        "http://localhost",
        "http://localhost:8080",
        "https://localhost:8080",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def open_driver():
    if config.dockerized:
        print('app running on docker')
        chrome_opt = webdriver.ChromeOptions()
        chrome_opt.add_argument('--headless')
        chrome_opt.add_argument('--no-sandbox')

        return webdriver.Chrome(
            './applications/chromedriver', options=chrome_opt)
    else:
        return webdriver.Chrome(
            'D:/chromedriver_win32/chromedriver')


@app.get("/")
async def root():
    return {"welcome": "to etsify"}


@app.get('/adding_product')
def get_product_from_link(product_link: str):
    # driver = open_driver()
    result = addingProduct(product_link)
    # driver.close()
    return result


@app.get('/product_details')
def show_product_details(product_id: int):

    result = showProductDetails(product_id)

    return result


@app.get('/list_products')
def list_previously_searched_products():

    result = listProducts()

    return result
