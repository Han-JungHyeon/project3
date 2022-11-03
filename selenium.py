from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd


URL = "https://www.wart.or.kr/product/list.html?cate_no=58" #동양화
URL2 = "https://www.wart.co.kr/product/list.html?cate_no=380" #명화
URL3 = "https://www.wart.co.kr/product/list.html?cate_no=35" #추상화
URL4 = "https://www.wart.co.kr/product/list.html?cate_no=61" #현대미술
URL5 = "https://www.wart.co.kr/product/list.html?cate_no=62" #사진
URL6 = "https://www.wart.co.kr/product/list.html?cate_no=64" #일러스트
driver = webdriver.Chrome("./chromedriver")
driver.get(URL6)
sleep(5)

# driver.find_element(By.CSS_SELECTOR, "#closing_close").click() # 팝업창 닫기

# 더보기 클릭
while True:
    try:
        driver.find_element(By.CSS_SELECTOR, "a.btnMore").click()
        sleep(1)
    except:
        break
sleep(5)

# 데이터 수집
art_list = []
arts = driver.find_elements(By.CSS_SELECTOR, "#product_list_section > div.xans-element-.xans-product.xans-product-normalpackage.product_area_container > div.product_area > div.xans-element-.xans-product.xans-product-listnormal.ec-base-product > ul")
arts_li = arts[0].find_elements(By.TAG_NAME, "li")
for art in arts_li:
    try:
        title = art.find_element(By.CSS_SELECTOR, "div > div.description > strong > a > span:nth-child(2)").text
        artist = art.find_element(By.CSS_SELECTOR, "div > div.description > p.model").text
        hash_tag = art.find_element(By.CSS_SELECTOR, "div > div.description > div.hash_tag").text
        price = art.find_element(By.CSS_SELECTOR, "div > div.description > p.price > span:nth-child(2)").text
        art_url = art.find_element(By.CSS_SELECTOR, "div > div.thumbnail > a").get_attribute('href')
        img_url = art.find_element(By.CSS_SELECTOR, "div > div.thumbnail > a > img").get_attribute('src')
        art_list.append(
            {
                'Title' : title,
                'Artist' : artist,
                'Hash_tag' : hash_tag,
                'Price' : price,
                'URL' : art_url,
                'img' : img_url
            }
        )
        sleep(1)
    except:
        break


sleep(5)
df = pd.DataFrame(art_list)
df.to_csv('Illust.csv', encoding = 'utf-8-sig')

driver.close()