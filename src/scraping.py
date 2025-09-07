import os
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

value = 390
driver = webdriver.Chrome()

"""
Section: Banali.am Scraper

- Navigates to Banali.am and applies filters for apartments in Yerevan.
- Iterates over multiple pages and listings, extracting the same fields as above.
- Cleans and converts prices to USD.
- Stores structured data for downstream analysis.
"""

try:
    driver.get(url="https://www.senyak.am/")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#responsive > li:nth-child(1) > a").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,
                        "#titlebar > div > div.row.text-center.big-block > div.col-md-20-percent.col-xs-100-percent.padding-top-10.padding-bottom-10").click()
    time.sleep(3)
    info = [["Տարածաշրջան", "Շինության տիպ", "Սենյակներ", "Մակերես", "Հարկ", "Վերանորոգում", "Գինը"]]
    for i in range(171, 201):
        for j in range(1, 44):
            try:
                new_list = []
                driver.find_element(By.CSS_SELECTOR,
                                    f"#propListContainer > article:nth-child({j}) > div > div > div.listing-title > h2 > a").click()
                time.sleep(1)
                for l in range(1, 8):
                    try:
                        if l == 6:
                            continue
                        content = driver.find_element(By.CSS_SELECTOR,
                                                      f"#wrapper > main > div:nth-child(1) > div > div > div.col-lg-4.col-md-5 > table > tbody > tr:nth-child({l}) > td").text
                        time.sleep(2)
                        if content[-1] == "²":
                            content = content[:-2]
                        if "/" in content:
                            content = content.split("/")[0]
                        new_list.append(content)
                        time.sleep(2)
                    except:
                        continue
                try:
                    try:
                        price = driver.find_element(By.CSS_SELECTOR,
                                                    "#wrapper > main > div:nth-child(1) > div.container > div > div.col-lg-4.col-md-5 > div.h3.text-right.margin-top-0 > span").text
                    except:
                        price = driver.find_element(By.CSS_SELECTOR,
                                                    "#wrapper > main > div:nth-child(1) > div.container > div > div.col-lg-4.col-md-5 > div.h3.text-right.margin-top-0").text
                except:
                    continue
                price = price.replace(" ", "")
                if len(price) > 7 and price[0].isdigit() == False:
                    price = float(int(str(price[1:])) / value)
                    price = "$" + price
                elif len(price) > 7 and price[-1].isdigit() == False:
                    price = float(int(str(price[:-1])) / value)
                    price = "$" + price
                new_list.append(str(price))
                if len(new_list) == 7:
                    info.append(new_list)
                driver.back()
                time.sleep(1)
            except:
                if i == 43:
                    break
                else:
                    continue
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,
                            "#paginationId > nav.pagination-next-prev > ul > li:nth-child(2) > a").click()
        time.sleep(2)
    time.sleep(2)
except Exception as exx:
    print(exx)

"""
Section: Banali.am Scraper

- Navigates to Banali.am and applies filters for apartments in Yerevan.
- Iterates over multiple pages and listings, extracting the same fields as above.
- Cleans and converts prices to USD.
- Stores structured data for downstream analysis.
"""

try:
    driver.get(url="https://banali.am/vachark/ansharzh-guik-yerevanum")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "#app > div.search-page-main.extend-ui > div.search-box > div.search-page-top > div.priority-navigation.main-filters > div > div:nth-child(3) > div > div.filter-summary").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,
                        "#app > div.search-page-main.extend-ui > div.search-box > div.search-page-top > div.priority-navigation.main-filters > div > div:nth-child(3) > div > div.filter-dropdown > div.filter-content.property_type-content > ul > li:nth-child(1) > div").click()
    time.sleep(2)
    info = []
    columns = ["Տարածաշրջան", "Շինության տիպ", "Սենյակներ", "Մակերես", "Հարկ", "Վերանորոգում", "Գինը"]
    for j in range(10):
        for i in range(1, 11):
            time.sleep(2)
            new_listik = []
            try:
                driver.find_element(By.CSS_SELECTOR,
                                    f"#app > div.search-page-main.extend-ui > div.d-flex.results-wrapper.mobile-is-post-view > div.scrolling-view-port > div.post-list > div.posts.layout-search > div:nth-child({i}) > a").click()
                time.sleep(2)
            except:
                continue
            try:
                content = driver.find_element(By.CSS_SELECTOR,
                                              "#router-modal > div > div._199FaV9HklYy0FFuFFXQVE > div.bl_modal_root > div > div > div.post-details > div.post-content > div.post-address").text
                full_address = content
                content = ", ".join(content.split(", ")[:2])
                content = content.replace("-", " ")
                new_listik.append(content)
            except:
                driver.back()
                continue
            try:
                content = driver.find_element(By.CSS_SELECTOR,
                                              "#router-modal > div > div._199FaV9HklYy0FFuFFXQVE > div.bl_modal_root > div > div > div.post-details > div.post-content > div:nth-child(9) > div:nth-child(3) > div > div._1scNe5JZvUHaGWJa_A_StX > div:nth-child(2) > div.amenity-info").text
                new_listik.append(content)
            except:
                driver.back()
                continue
            try:
                content = driver.find_element(By.CSS_SELECTOR,
                                              "#router-modal > div > div._199FaV9HklYy0FFuFFXQVE > div.bl_modal_root > div > div > div.post-details > div.post-content > div:nth-child(9) > div:nth-child(2) > div > div:nth-child(6) > div > div:nth-child(1) > div.amenity-info").text
                new_listik.append(content)
            except:
                driver.back()
                continue
            try:
                content = driver.find_element(By.CSS_SELECTOR,
                                              "#router-modal > div > div._199FaV9HklYy0FFuFFXQVE > div.bl_modal_root > div > div > div.post-details > div.post-content > div:nth-child(9) > div:nth-child(2) > div > div:nth-child(6) > div > div:nth-child(2) > div.amenity-info").text
                new_listik.append(content)
            except:
                driver.back()
                continue
            try:
                content = driver.find_element(By.CSS_SELECTOR,
                                              "#router-modal > div > div._199FaV9HklYy0FFuFFXQVE > div.bl_modal_root > div > div > div.post-details > div.post-content > ul > li:nth-child(3) > span").text
                content = content.split("/")[0]
                new_listik.append(content)
            except:
                driver.back()
                continue
            try:
                content = driver.find_element(By.CSS_SELECTOR,
                                              "#router-modal > div > div._199FaV9HklYy0FFuFFXQVE > div.bl_modal_root > div > div > div.post-details > div.post-content > div:nth-child(9) > div:nth-child(2) > div > div:nth-child(6) > div > div:nth-child(6) > div.amenity-info").text
                new_listik.append(content)
            except:
                driver.back()
                continue
            try:
                content = driver.find_element(By.CSS_SELECTOR,
                                              "#router-modal > div > div._199FaV9HklYy0FFuFFXQVE > div.bl_modal_root > div > div > div.post-details > div.post-content > div.price-section > span.price-val > div").text
                content = content.replace(",", "")
                content = int(int(content) / 390)
                content = "$" + str(content)
                new_listik.append(content)
            except:
                driver.back()
                continue
            time.sleep(2)
            if i > 5:
                driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
            time.sleep(2)
            if new_listik in info == False:
                info.append(new_listik)
            driver.back()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#pagination > a:nth-child(7)").click()
        time.sleep(3)


except Exception as exx:
    print(f"Error: {exx}")

finally:
    driver.close()
    driver.quit()
