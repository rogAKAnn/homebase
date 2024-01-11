from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


BASE_URL = 'https://batdongsan.com.vn' # for the prefix URL
NUM_OF_CLICK_TO_NEXT_PAGE = 10

options = uc.ChromeOptions() 
options.headless = False  # Set headless to False to run in non-headless mode

driver = uc.Chrome(use_subprocess=True, options=options) 

suffixes = ['nha-dat-ban','nha-dat-cho-thue']

for suffix_url in suffixes:  
    res = []

    print(f"Start crawling for {BASE_URL}/{suffix_url}")
    
    driver.get(f"{BASE_URL}/{suffix_url}")

    for i in range(NUM_OF_CLICK_TO_NEXT_PAGE):

        WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.CLASS_NAME, 're__main-content'))
        )

        list_ads = driver.find_element(By.ID, 'product-lists-web')

        ads = list_ads.find_elements(By.XPATH, "//*[@class='js__card js__card-full-web\n     pr-container re__card-full  re__vip-diamond']")


        print(f"START TO PROCESS {len(ads)} ads")
        for ad in ads:
            product = ad.find_element(By.CLASS_NAME, "js__product-link-for-product-id")
            product_info = product.find_element(By.CLASS_NAME, "re__card-info").find_element(By.CLASS_NAME, 're__card-info-content')
            title = product_info.find_element(By.CLASS_NAME, 're__card-title').get_attribute('innerHTML')

            configurations = product_info.find_element(By.TAG_NAME, 'div')    
            configurations = configurations.find_element(By.XPATH, "//*[@class='re__card-config js__card-config']")
            
            price = configurations.find_element(By.XPATH, "//*[@class='re__card-config-price js__card-config-item']").get_attribute('innerText')
            
            area = configurations.find_element(By.XPATH, "//*[@class='re__card-config-area js__card-config-item']")\
                        .get_attribute('innerHTML').replace('\n','')
            num_of_bedroom = configurations.find_element(By.XPATH, "//*[@class='re__card-config-bedroom js__card-config-item']")\
                        .get_attribute('innerText').replace('\n','')
            num_of_wc = configurations.find_element(By.XPATH, "//*[@class='re__card-config-toilet js__card-config-item']")\
                        .get_attribute('innerText').replace('\n','')

            location = product_info.find_element(By.CLASS_NAME, 're__card-location')\
                        .get_attribute('innerText').replace('\n','')

            res += [[price, area, num_of_bedroom, num_of_wc, location]]

        with open(f'./task3_result/{suffix_url}.csv', '+w') as f:
            f.write(f"{','.join(['price','area','num_of_bedroom,num_of_wc,location'])}\n")
            [f.write(f"{','.join(row)}\n") for row in res]

        # click to new element
        button = driver.find_element(By.XPATH, "//*[@class='re__pagination-group']")
        buttons = button.find_elements(By.TAG_NAME, 'a')
        buttons[-1].click()

    
print(f"Finish crawling")
print(len(res))