import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException



def scrape_legrand_websites(legrand_input, first_url, second_url):
    #  chrome driver
    # browser = webdriver.Chrome()
    # web driver path /Users/kevintivert/Documents/web_driver/chromedriver
    PATH = r'/usr/local/bin/chromedriver'

    is_product_found = False
    # chrome driver load
    driver = webdriver.Chrome(executable_path=PATH)

    for index in range(legrand_input):
        driver.get(first_url+str(legrand_input[index]))
        accept_button = driver.find_element_by_id('popin_tc_privacy_button')
        time.sleep(2.5)
        accept_button.click()
        check_if_prod_is_found = driver.find_element_by_xpath('//*[@id="results"]/div/div/div/p')
        is_product_found = check_exists_by_xpath(check_if_prod_is_found)
        if(is_product_found == False):
            # find needed elements
            img_element = driver.find_elements_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/a/img')
            caract_prd = driver.find_elements_by_xpath('//*[@id="caracteristiques-produit"]/div')
            caract_general = driver.find_elements_by_xpath('//*[@id="caracteristiques-techniques"]/div')
            #test
            for my_src in img_element:
                print(my_src.get_attribute("src"))
            for my_prd_caract in caract_prd:
                print(my_prd_caract.text)
            for my_gnrl_caract in caract_general:
                print(my_gnrl_caract.text)

        else:
            #print row red
            driver.quit()


def check_exists_by_xpath(is_prd_found):
    try:
        webdriver.find_element_by_xpath(is_prd_found)
    except NoSuchElementException:
        return False
    return True

def legrand_ref_input_function():
    # open legrand reference input text file &
    # insert reference in an array
    input_file = open("legrand_ref_input.txt", "r")
    ref_input_array = input_file.read().splitlines()
    input_file.close()
    return ref_input_array


def main():
     # First legrand URL
    first_legrand_url= 'https://www.legrand.fr/pro/recherche?s='
    # Second legrand URL
    second_legrand_url = 'https://www.export.legrand.com/search/fr?words='

    legrand_ref_inputs = legrand_ref_input_function()

    scrape_legrand_websites(legrand_ref_inputs, first_legrand_url, second_legrand_url)

if __name__ == "__main__":
    main()
