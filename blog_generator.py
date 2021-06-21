import sys,csv,winsound,os,platform,json,time,webbrowser

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import itertools
import threading
import time
import sys

"""Declaring Version"""
ver = 1.1
"""Getting Category Name"""

category = input("\nPlease enter the category name and press enter ")
category = category.strip()

"""declaring sound config"""

duration = 250  # milliseconds
freq = [440,880,440,880]  # Hz

captcha_xpath = "//div[@class = 'h-captcha']"

"""Declaring chromepath"""
chromepath = ""
if platform.system() == "Darwin":
    chromepath = os.path.abspath("drivers/chromedriver")
elif platform.system() == "Windows":
    chromepath = os.path.abspath("drivers/chromedriver.exe")
elif platform.system() == 'Linux':
    chromepath = os.path.abspath("drivers/chromedriver_linux")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = ""
url = "https://nichesss.com/home"
try:
    driver = webdriver.Chrome(executable_path=chromepath, chrome_options=chrome_options)
except Exception as e:
    if "Message: 'chromedriver.exe' executable needs to be in PATH" in str(e):
        print("Chrome driver path is incorrect, \nPlease check and try again.")
    elif "Message: session not created: This version of ChromeDriver only supports Chrome version" in str(e):
        print(
            "Chrome driver needs to be updated, \nPlease follow the instructions specified in recently opened PDF file...")
        webbrowser.open_new(r'Chrome driver update instruction.pdf')
    exit()
driver.maximize_window()

"""Declaring Introduction"""

int_name = ['{}','{}','{}','{}','{}']
int_cat = ['Overview,'+'"'+'{}'+'"','Overview,'+'"'+'{}'+'"','Overview,'+'"'+'{}'+'"','Overview,'+'"'+'{}'+'"','Overview,'+'"'+'{}'+'"']
int_about = ['We explain what is {} used for','We explain why people use {}','We explain what is {}','We explain what is {}?','We explain the use of {}?']
int_title = ['What are {} used for?','We explain why people use {}','What are {}','We explain what is {}?','We explain the use of {}?']

"""Declaring Factors"""

fac_name = ['Factors to consider before buying {}','What people discuss before buying {}','All we need to consider while buying {}','What buyers discuss while buying {} on amazon','What factors users consider before buying {} on amazon']
fac_cat = ['{}, "Factors to consider before buying"','mp3 player cases covers, "What people discuss before buying {}"','mp3 player cases covers, "All we need to consider while buying {}"','mp3 player cases covers, "What buyers discuss while buying {} on amazon"','mp3 player cases covers, "What factors users consider before buying {} on amazon"']
fac_about = ['Factors to consider before buying {}','What people discuss before buying {}','All we need to consider while buying {}','What buyers discuss while buying {} on amazon','What factors users consider before buying {} on amazon']
fac_title = ['Factors to consider before buying {}','What people discuss before buying {}','All we need to consider while buying {}','What buyers discuss while buying {} on amazon','What factors users consider before buying {} on amazon']

"""Declaring Factors to consider"""

fac_to_c_name = ['{} in {}','Why {} are essential in {}','Importance of {} in {}','{} is a very important factor while buying {}']
fac_to_c_cat = ['{},"{}"','{},"{}"','{},"{}"','{},"{}"']
fac_to_c_about = ['We explain what are {} in {}','We explain Why {} are essential in {}','We explain the Importance of {} in {}','We explain why the {} is a very important factor while buying {}']
fac_to_c_title = ['We explain what are {} in {}','We explain Why {} are essential in {}','We explain the Importance of {} in {}','We explain why the {} is a very important factor while buying {}']

"""Declaring benefits"""

ban_of_item_name = ['How {} enhances {}','How {} enhances the {}','How {} enhances {}','How {} enhances {}','How {} enhances {}']
ban_of_item_cat =['{}, "{}"','{}, "{}"','{} , "{}"','{}, "good {}"','{}, "{}"']
ban_of_item_about = ['{} enhances {}','How {} enhances the {}.','How {} enhances {}','How {} enhances {}','How {} enhances {}.']
ban_of_item_title = ['{} enhances {}','How {} enhances the {}.','How {} enhances {}','How {} enhances {}','How {} enhances {}.']

"""Declaring Conclusion"""
con_name = ['Overview, "{}"','Overview, "{}"']
con_cat = ['We explain a brief summary of {}','We explain a summary of {}','']
con_about = ['Brief summary of {}','Summary of {}']
con_title = ['Brief summary of {}','Summary of {}']

def login():
    sys.stdout.write("\rLogging in...")
    sys.stdout.flush()
    driver.get(url=url)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "email")))
    driver.find_element_by_name("email").send_keys("paramdeep@shorthillstech.com")
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "password")))
    driver.find_element_by_name("password").send_keys("nichesss@sht123")
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@type = 'submit']")))
    driver.find_element_by_xpath("//button[@type = 'submit']").click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Blogs 📝 ')]")))
    driver.find_element_by_xpath("//h2[contains(text(), 'Blogs 📝 ')]").click()
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
done = False
def play_sound():
    for i in range(4):
        winsound.Beep(freq[i], duration)
    sys.stdout.flush()
def introduction():
    sys.stdout.write("\rGenerating Introduction")
    sys.stdout.flush()
    with open(category+'.csv', 'a', newline='', encoding="utf-8-sig") as file:
        fieldnames = ['Introduction', 'output 1', 'output 2','output 3', 'output 4','output 5', 'output 6','output 7', 'output 8','output 9', 'output 10']
        writer = csv.writer(file, delimiter=',')
        writer.writerow(fieldnames)

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Blogs 📝 ')]")))
        driver.find_element_by_xpath("//h2[contains(text(), 'Blogs 📝 ')]").click()
        if check_exists_by_xpath(captcha_xpath) ==  True:
            play_sound()
            input("\nPlease handle the captcha and press enter")
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@role = 'searchbox']")))
        driver.find_element_by_xpath("//input[@role = 'searchbox']").send_keys(category)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Intro')]")))
        driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Intro')]").click()
        time.sleep(3)

        blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
        blog_name.clear()
        blog_name.send_keys(category)
        blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
        blog_cat.clear()
        blog_cat.send_keys('Overview,'+'"'+category+'"')
        about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
        about.clear()
        about.send_keys('We explain what is '+category + ' used for')
        title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
        title.clear()
        title.send_keys("What are "+category+" used for?")
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Generate')]")))
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(text(), 'Generate')]").click()
        WebDriverWait(driver, 62).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[class = 'ml-2 waiting-plans']")))
        driver.refresh()
        try:
            els = driver.find_elements_by_xpath("//a[@class = 'a--underline font--900']")
            els[0].click()
        except:
            driver.get('https://nichesss.com/home/marketing-plans')
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//a[@class = 'a--underline font--900']")))
            els = driver.find_elements_by_xpath("//a[@class = 'a--underline font--900']")
            els[0].click()
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
        except:
            driver.refresh()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
        add_more = driver.find_element_by_xpath("//i[@class = 'fa fa-plus mr-2 dim']")
        driver.execute_script("arguments[0].scrollIntoView();", add_more)
        try:
            add_more.click()
        except:
            time.sleep(1)
            add_more.click()
        ###
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@role = 'combobox']")))
        if check_exists_by_xpath(captcha_xpath) ==  True:
            play_sound()
            input("\nPlease handle the captcha and press enter")
        driver.find_element_by_xpath("//span[@role = 'combobox']").click()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Intro')]")))
        driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Intro')]").click()
        time.sleep(3)

        blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
        blog_name.clear()
        blog_name.send_keys(category)
        blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
        blog_cat.clear()
        blog_cat.send_keys('Overview,' + '"' + category + '"')
        about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
        about.clear()
        about.send_keys('We explain why people use ' + category)
        title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
        title.clear()
        title.send_keys('We explain why people use ' + category)
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Generate more Now')]")))
        time.sleep(1)
        driver.find_element_by_xpath("//a[contains(text(), 'Generate more Now')]").click()
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
        except:
            driver.refresh()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
        driver.execute_script("arguments[0].scrollIntoView();", add_more)
        try:
            add_more.click()
        except:
            time.sleep(1)
            add_more.click()
        ###
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@role = 'combobox']")))
        if check_exists_by_xpath(captcha_xpath) ==  True:
            play_sound()
            input("\nPlease handle the captcha and press enter")
        driver.find_element_by_xpath("//span[@role = 'combobox']").click()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Intro')]")))
        driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Intro')]").click()
        time.sleep(3)

        blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
        blog_name.clear()
        blog_name.send_keys(category)
        blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
        blog_cat.clear()
        blog_cat.send_keys('Overview,' + '"' + category + '"')
        about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
        about.clear()
        about.send_keys('We explain what is ' + category)
        title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
        title.clear()
        title.send_keys('What are ' + category)
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Generate more Now')]")))
        time.sleep(1)
        driver.find_element_by_xpath("//a[contains(text(), 'Generate more Now')]").click()
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
        except:
            driver.refresh()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
        driver.execute_script("arguments[0].scrollIntoView();", add_more)
        try:
            add_more.click()
        except:
            time.sleep(1)
            add_more.click()
        ###
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@role = 'combobox']")))
        if check_exists_by_xpath(captcha_xpath) == True:
            play_sound()
            input("\nPlease handle the captcha and press enter")
        driver.find_element_by_xpath("//span[@role = 'combobox']").click()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Intro')]")))
        driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Intro')]").click()
        time.sleep(3)

        blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
        blog_name.clear()
        blog_name.send_keys(category)
        blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
        blog_cat.clear()
        blog_cat.send_keys('Overview,' + '"' + category + '"')
        about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
        about.clear()
        about.send_keys('We explain what is ' + category+"?")
        title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
        title.clear()
        title.send_keys('We explain what is ' + category+'?')
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Generate more Now')]")))
        time.sleep(1)
        driver.find_element_by_xpath("//a[contains(text(), 'Generate more Now')]").click()
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
        except:
            driver.refresh()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
        driver.execute_script("arguments[0].scrollIntoView();", add_more)
        try:
            add_more.click()
        except:
            time.sleep(1)
            add_more.click()
        ###
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@role = 'combobox']")))
        if check_exists_by_xpath(captcha_xpath) == True:
            play_sound()
            input("\nPlease handle the captcha and press enter")
        driver.find_element_by_xpath("//span[@role = 'combobox']").click()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Intro')]")))
        driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Intro')]").click()
        time.sleep(3)
        blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
        blog_name.clear()
        blog_name.send_keys(category)
        blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
        blog_cat.clear()
        blog_cat.send_keys('Overview,' + '"' + category + '"')
        about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
        about.clear()
        about.send_keys('We explain the use of ' + category + "?")
        title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
        title.clear()
        title.send_keys('We explain the use of ' + category + "?")
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Generate more Now')]")))
        time.sleep(1)
        driver.find_element_by_xpath("//a[contains(text(), 'Generate more Now')]").click()
        time.sleep(3)
        driver.refresh()
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//div[@class = 'col nl-to-br']")))
        except:
            driver.refresh()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//div[@class = 'col nl-to-br']")))
        blog_text = driver.find_elements_by_xpath("//div[@class = 'col nl-to-br']")
        data = ['Introduction',blog_text[0].text,blog_text[1].text,blog_text[2].text,blog_text[3].text,blog_text[4].text,blog_text[5].text,blog_text[6].text,blog_text[7].text,blog_text[8].text,blog_text[9].text]
        writer.writerow(data)

def factors():
    sys.stdout.write("\rGenerating Factors          ")
    sys.stdout.flush()
    driver.get(url=url)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Blogs 📝 ')]")))
    driver.find_element_by_xpath("//h2[contains(text(), 'Blogs 📝 ')]").click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@role = 'searchbox']")))
    if check_exists_by_xpath(captcha_xpath) == True:
        play_sound()
        input("\nPlease handle the captcha and press enter")
    driver.find_element_by_xpath("//input[@role = 'searchbox']").send_keys(category)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Outline')]")))
    driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Outline')]").click()
    time.sleep(3)

    blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
    blog_name.clear()
    blog_name.send_keys("Factors to consider before buying "+category)
    blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
    blog_cat.clear()
    blog_cat.send_keys(category+', "Factors to consider before buying"')
    about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
    about.clear()
    about.send_keys("Factors to consider before buying "+category)
    title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
    title.clear()
    title.send_keys("Factors to consider before buying "+category)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Generate')]")))
    time.sleep(1)
    driver.find_element_by_xpath("//button[contains(text(), 'Generate')]").click()
    WebDriverWait(driver, 62).until(
        EC.invisibility_of_element_located((By.XPATH, "//span[class = 'ml-2 waiting-plans']")))
    ###
    driver.refresh()
    try:
        els = driver.find_elements_by_xpath("//a[@class = 'a--underline font--900']")
        els[0].click()
    except:
        driver.get('https://nichesss.com/home/marketing-plans')
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//a[@class = 'a--underline font--900']")))
        els = driver.find_elements_by_xpath("//a[@class = 'a--underline font--900']")
        els[0].click()
    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
    except:
        driver.refresh()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
    add_more = driver.find_element_by_xpath("//i[@class = 'fa fa-plus mr-2 dim']")
    driver.execute_script("arguments[0].scrollIntoView();", add_more)
    try:
        add_more.click()
    except:
        time.sleep(1)
        add_more.click()
    ###
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@role = 'combobox']")))
    if check_exists_by_xpath(captcha_xpath) == True:
        play_sound()
        input("\nPlease handle the captcha and press enter")
    driver.find_element_by_xpath("//span[@role = 'combobox']").click()
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Outline')]")))
    driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Outline')]").click()
    time.sleep(3)

    blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
    blog_name.clear()
    blog_name.send_keys("What people discuss before buying "+category)
    blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
    blog_cat.clear()
    blog_cat.send_keys(category+','+'"'+'What people discuss before buying '+category+'"')
    about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
    about.clear()
    about.send_keys('What people discuss before buying ' + category)
    title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
    title.clear()
    title.send_keys('What people discuss before buying ' + category)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Generate more Now')]")))
    time.sleep(1)
    driver.find_element_by_xpath("//a[contains(text(), 'Generate more Now')]").click()
    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
    except:
        driver.refresh()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
    driver.execute_script("arguments[0].scrollIntoView();", add_more)
    try:
        add_more.click()
    except:
        time.sleep(1)
        add_more.click()
    ###
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@role = 'combobox']")))
    if check_exists_by_xpath(captcha_xpath) == True:
        play_sound()
        input("\nPlease handle the captcha and press enter")
    driver.find_element_by_xpath("//span[@role = 'combobox']").click()
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Outline')]")))
    driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Outline')]").click()
    time.sleep(3)

    blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
    blog_name.clear()
    blog_name.send_keys("All we need to consider while buying " + category)
    blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
    blog_cat.clear()
    blog_cat.send_keys(category + ',' + '"' + 'All we need to consider while buying ' + category + '"')
    about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
    about.clear()
    about.send_keys('All we need to consider while buying ' + category)
    title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
    title.clear()
    title.send_keys('All we need to consider while buying' + category)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Generate more Now')]")))
    time.sleep(1)
    driver.find_element_by_xpath("//a[contains(text(), 'Generate more Now')]").click()
    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
    except:
        driver.refresh()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
    driver.execute_script("arguments[0].scrollIntoView();", add_more)
    try:
        add_more.click()
    except:
        time.sleep(1)
        add_more.click()
    ###
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@role = 'combobox']")))
    if check_exists_by_xpath(captcha_xpath) == True:
        play_sound()
        input("\nPlease handle the captcha and press enter")
    driver.find_element_by_xpath("//span[@role = 'combobox']").click()
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Outline')]")))
    driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Outline')]").click()
    time.sleep(3)

    blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
    blog_name.clear()
    blog_name.send_keys("What buyers discuss while buying " + category+" on amazon")
    blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
    blog_cat.clear()
    blog_cat.send_keys(category + ',' + '"' + 'What buyers discuss while buying ' + category+' on amazon' + '"')
    about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
    about.clear()
    about.send_keys('What buyers discuss while buying ' + category+' on amazon')
    title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
    title.clear()
    title.send_keys('What buyers discuss while buying ' + category+' on amazon')
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Generate more Now')]")))
    time.sleep(1)
    driver.find_element_by_xpath("//a[contains(text(), 'Generate more Now')]").click()
    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
    except:
        driver.refresh()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
    driver.execute_script("arguments[0].scrollIntoView();", add_more)
    try:
        add_more.click()
    except:
        time.sleep(1)
        add_more.click()
    ###
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@role = 'combobox']")))
    if check_exists_by_xpath(captcha_xpath) == True:
        play_sound()
        input("\nPlease handle the captcha and press enter")
    driver.find_element_by_xpath("//span[@role = 'combobox']").click()
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Outline')]")))
    driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Outline')]").click()
    time.sleep(3)

    blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
    blog_name.clear()
    blog_name.send_keys("What factors users consider before buying " + category + " on amazon")
    blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
    blog_cat.clear()
    blog_cat.send_keys(category + ',' + '"' + 'What factors users consider before buying ' + category + ' on amazon' + '"')
    about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
    about.clear()
    about.send_keys('What factors users consider before buying ' + category + ' on amazon')
    title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
    title.clear()
    title.send_keys('What factors users consider before buying ' + category + ' on amazon')
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Generate more Now')]")))
    time.sleep(1)
    driver.find_element_by_xpath("//a[contains(text(), 'Generate more Now')]").click()
    WebDriverWait(driver, 62).until(
        EC.invisibility_of_element_located((By.XPATH, "//span[class = 'ml-2 waiting-plans']")))
    driver.refresh()
def factor_to_consider():
    sys.stdout.write("\rGenerating factors to consider")
    sys.stdout.flush()
    with open(category + '.csv', 'a', newline='', encoding='utf-8-sig') as file:
        fieldnames = ['', '', '', '', '', '', '',
                      '', '', '', '']
        writer = csv.writer(file, delimiter=',')
        writer.writerow(fieldnames)
        for factor in fc_list:
            for j in range(4):
                driver.get("https://nichesss.com/home")
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Blogs 📝 ')]")))
                driver.find_element_by_xpath("//h2[contains(text(), 'Blogs 📝 ')]").click()
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//input[@role = 'searchbox']")))
                if check_exists_by_xpath(captcha_xpath) == True:
                    play_sound()
                    input("\nPlease handle the captcha and press enter")
                driver.find_element_by_xpath("//input[@role = 'searchbox']").send_keys(category)
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Intro')]")))
                driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Intro')]").click()
                time.sleep(3)

                blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
                blog_name.clear()
                blog_name.send_keys(fac_to_c_name[j].format(factor,category))
                blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
                blog_cat.clear()
                blog_cat.send_keys(fac_to_c_cat[j].format(category,factor))
                about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
                about.clear()
                about.send_keys(fac_to_c_about[j].format(factor,category))
                title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
                title.clear()
                title.send_keys(fac_to_c_title[j].format(factor,category))
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Generate')]")))
                time.sleep(1)
                driver.find_element_by_xpath("//button[contains(text(), 'Generate')]").click()
                WebDriverWait(driver, 62).until(
                    EC.invisibility_of_element_located((By.XPATH, "//span[class = 'ml-2 waiting-plans']")))
                driver.refresh()
                try:
                    els = driver.find_elements_by_xpath("//a[@class = 'a--underline font--900']")
                    els[0].click()
                except:
                    driver.get('https://nichesss.com/home/marketing-plans')
                    WebDriverWait(driver, 20).until(
                        EC.visibility_of_all_elements_located((By.XPATH, "//a[@class = 'a--underline font--900']")))
                    els = driver.find_elements_by_xpath("//a[@class = 'a--underline font--900']")
                    els[0].click()
                try:
                    WebDriverWait(driver, 20).until(
                        EC.visibility_of_all_elements_located((By.XPATH, "//div[@class = 'col nl-to-br']")))
                except:
                    driver.refresh()
                    WebDriverWait(driver, 20).until(
                        EC.visibility_of_all_elements_located((By.XPATH, "//div[@class = 'col nl-to-br']")))

                blog_text = driver.find_elements_by_xpath("//div[@class = 'col nl-to-br']")
                data = ['Factors to consider ('+factor+")", blog_text[0].text, blog_text[1].text]
                writer.writerow(data)
            ###


def benefit():
    sys.stdout.write("\rGenerating benefits                 ")
    sys.stdout.flush()
    driver.get(url=url)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Blogs 📝 ')]")))
    driver.find_element_by_xpath("//h2[contains(text(), 'Blogs 📝 ')]").click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@role = 'searchbox']")))
    if check_exists_by_xpath(captcha_xpath) == True:
        play_sound()
        input("\nPlease handle the captcha and press enter")
    driver.find_element_by_xpath("//input[@role = 'searchbox']").send_keys(category)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Outline')]")))
    driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Outline')]").click()
    time.sleep(3)

    blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
    blog_name.clear()
    blog_name.send_keys("What are the benefits of "+category)
    blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
    blog_cat.clear()
    blog_cat.send_keys("Benefits" + ',' + '"' + category + '"')
    about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
    about.clear()
    about.send_keys("What are the benefits of "+category)
    title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
    title.clear()
    title.send_keys("What are the benefits of "+category)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Generate')]")))
    time.sleep(1)
    driver.find_element_by_xpath("//button[contains(text(), 'Generate')]").click()
    WebDriverWait(driver, 62).until(
        EC.invisibility_of_element_located((By.XPATH, "//span[class = 'ml-2 waiting-plans']")))
    ###
    driver.refresh()
    try:
        els = driver.find_elements_by_xpath("//a[@class = 'a--underline font--900']")
        els[0].click()
    except:
        driver.get('https://nichesss.com/home/marketing-plans')
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//a[@class = 'a--underline font--900']")))
        els = driver.find_elements_by_xpath("//a[@class = 'a--underline font--900']")
        els[0].click()
    time.sleep(3)
    driver.refresh()
    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
    except:
        driver.refresh()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
    add_more = driver.find_element_by_xpath("//i[@class = 'fa fa-plus mr-2 dim']")
    driver.execute_script("arguments[0].scrollIntoView();", add_more)
    try:
        add_more.click()
    except:
        time.sleep(1)
        add_more.click()
    ###
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@role = 'combobox']")))
    if check_exists_by_xpath(captcha_xpath) == True:
        play_sound()
        input("\nPlease handle the captcha and press enter")
    driver.find_element_by_xpath("//span[@role = 'combobox']").click()
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Outline')]")))
    driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Outline')]").click()
    time.sleep(3)

    blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
    blog_name.clear()
    blog_name.send_keys("Benefits of "+category)
    blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
    blog_cat.clear()
    blog_cat.send_keys("Benefits" + ',' + '"' + category + '"')
    about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
    about.clear()
    about.send_keys('Benefits of ' + category)
    title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
    title.clear()
    title.send_keys('Benefits of ' + category)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Generate more Now')]")))
    time.sleep(1)
    driver.find_element_by_xpath("//a[contains(text(), 'Generate more Now')]").click()
    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
    except:
        driver.refresh()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
    driver.execute_script("arguments[0].scrollIntoView();", add_more)
    try:
        add_more.click()
    except:
        time.sleep(1)
        add_more.click()
    ###
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@role = 'combobox']")))
    if check_exists_by_xpath(captcha_xpath) == True:
        play_sound()
        input("\nPlease handle the captcha and press enter")
    driver.find_element_by_xpath("//span[@role = 'combobox']").click()
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Outline')]")))
    driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Outline')]").click()
    time.sleep(3)

    blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
    blog_name.clear()
    blog_name.send_keys("Advantages of " + category)
    blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
    blog_cat.clear()
    blog_cat.send_keys("Benefits" + ',' + '"' + category + '"')
    about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
    about.clear()
    about.send_keys('Advantages of ' + category)
    title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
    title.clear()
    title.send_keys('Advantages of ' + category)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Generate more Now')]")))
    time.sleep(1)
    driver.find_element_by_xpath("//a[contains(text(), 'Generate more Now')]").click()
    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
    except:
        driver.refresh()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
    driver.execute_script("arguments[0].scrollIntoView();", add_more)
    try:
        add_more.click()
    except:
        time.sleep(1)
        add_more.click()
    ###
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@role = 'combobox']")))
    if check_exists_by_xpath(captcha_xpath) == True:
        play_sound()
        input("\nPlease handle the captcha and press enter")
    driver.find_element_by_xpath("//span[@role = 'combobox']").click()
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Outline')]")))
    driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Outline')]").click()
    time.sleep(3)

    blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
    blog_name.clear()
    blog_name.send_keys("What benefits do people seek in " + category)
    blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
    blog_cat.clear()
    blog_cat.send_keys("Benefits" + ',' + '"' + category + '"')
    about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
    about.clear()
    about.send_keys('What benefits do people seek in ' + category)
    title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
    title.clear()
    title.send_keys('What benefits do people seek in ' + category)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Generate more Now')]")))
    time.sleep(1)
    driver.find_element_by_xpath("//a[contains(text(), 'Generate more Now')]").click()
    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
    except:
        driver.refresh()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
    driver.execute_script("arguments[0].scrollIntoView();", add_more)
    try:
        add_more.click()
    except:
        time.sleep(1)
        add_more.click()
    ###
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@role = 'combobox']")))
    if check_exists_by_xpath(captcha_xpath) == True:
        play_sound()
        input("\nPlease handle the captcha and press enter")
    driver.find_element_by_xpath("//span[@role = 'combobox']").click()
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Outline')]")))
    driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Outline')]").click()
    time.sleep(3)

    blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
    blog_name.clear()
    blog_name.send_keys("What benefits does " + category + " provide")
    blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
    blog_cat.clear()
    blog_cat.send_keys("Benefits" + ',' + '"' + category + '"')
    about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
    about.clear()
    about.send_keys('What benefits does ' + category + ' provide')
    title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
    title.clear()
    title.send_keys('What benefits does ' + category + ' provide')
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Generate more Now')]")))
    time.sleep(1)
    driver.find_element_by_xpath("//a[contains(text(), 'Generate more Now')]").click()
    WebDriverWait(driver, 62).until(
        EC.invisibility_of_element_located((By.XPATH, "//span[class = 'ml-2 waiting-plans']")))
    driver.refresh()

def benefit_of_item():
    sys.stdout.write("\rGenerating benefits of item   ")
    sys.stdout.flush()
    with open(category + '.csv', 'a', newline='', encoding='utf-8-sig') as file:
        fieldnames = ['', '', '', '', '', '', '',
                      '', '', '', '']
        writer = csv.writer(file, delimiter=',')
        writer.writerow(fieldnames)
        for benefit in bn_list:
            for j in range(5):
                driver.get("https://nichesss.com/home")
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Blogs 📝 ')]")))
                driver.find_element_by_xpath("//h2[contains(text(), 'Blogs 📝 ')]").click()
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//input[@role = 'searchbox']")))
                if check_exists_by_xpath(captcha_xpath) == True:
                    play_sound()
                    input("\nPlease handle the captcha and press enter")
                driver.find_element_by_xpath("//input[@role = 'searchbox']").send_keys(category)
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Intro')]")))
                driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Intro')]").click()
                time.sleep(3)

                blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
                blog_name.clear()
                blog_name.send_keys(ban_of_item_name[j].format(category,benefit))
                blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
                blog_cat.clear()
                blog_cat.send_keys(ban_of_item_cat[j].format(category,benefit))
                about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
                about.clear()
                about.send_keys(ban_of_item_about[j].format(category,benefit))
                title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
                title.clear()
                title.send_keys(ban_of_item_title[j].format(category,benefit))
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Generate')]")))
                time.sleep(1)
                driver.find_element_by_xpath("//button[contains(text(), 'Generate')]").click()
                WebDriverWait(driver, 62).until(
                    EC.invisibility_of_element_located((By.XPATH, "//span[class = 'ml-2 waiting-plans']")))
                driver.refresh()
                try:
                    els = driver.find_elements_by_xpath("//a[@class = 'a--underline font--900']")
                    els[0].click()
                except:
                    driver.get('https://nichesss.com/home/marketing-plans')
                    WebDriverWait(driver, 20).until(
                        EC.visibility_of_all_elements_located((By.XPATH, "//a[@class = 'a--underline font--900']")))
                    els = driver.find_elements_by_xpath("//a[@class = 'a--underline font--900']")
                    els[0].click()
                try:
                    WebDriverWait(driver, 20).until(
                        EC.visibility_of_all_elements_located((By.XPATH, "//div[@class = 'col nl-to-br']")))
                except:
                    driver.refresh()
                    WebDriverWait(driver, 20).until(
                        EC.visibility_of_all_elements_located((By.XPATH, "//div[@class = 'col nl-to-br']")))

                blog_text = driver.find_elements_by_xpath("//div[@class = 'col nl-to-br']")
                data = ['Benefits of the item ('+benefit+")", blog_text[0].text, blog_text[1].text]
                writer.writerow(data)
            ###
def conclusion():
    sys.stdout.write("\rGenerating Conclusion         ")
    sys.stdout.flush()
    with open(category + '.csv', 'a', newline='', encoding="utf-8-sig") as file:
        fieldnames = ['', '', '', '', '', '', '',
                      '', '', '', '']
        writer = csv.writer(file, delimiter=',')
        writer.writerow(fieldnames)
        driver.get(url=url)
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Blogs 📝 ')]")))
        driver.find_element_by_xpath("//h2[contains(text(), 'Blogs 📝 ')]").click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@role = 'searchbox']")))
        if check_exists_by_xpath(captcha_xpath) == True:
            play_sound()
            input("\nPlease handle the captcha and press enter")
        driver.find_element_by_xpath("//input[@role = 'searchbox']").send_keys(category)
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Intro')]")))
        driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Intro')]").click()
        time.sleep(3)

        blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
        blog_name.clear()
        blog_name.send_keys(category)
        blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
        blog_cat.clear()
        blog_cat.send_keys('Overview,' + '"' + category + '"')
        about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
        about.clear()
        about.send_keys('We explain what is ' + category + ' used for')
        title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
        title.clear()
        title.send_keys("What are " + category + " used for?")

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Generate')]")))
        time.sleep(1)

        driver.find_element_by_xpath("//button[contains(text(), 'Generate')]").click()
        WebDriverWait(driver, 62).until(
            EC.invisibility_of_element_located((By.XPATH, "//span[class = 'ml-2 waiting-plans']")))
        driver.refresh()
        try:
            els = driver.find_elements_by_xpath("//a[@class = 'a--underline font--900']")
            els[0].click()
        except:
            driver.get('https://nichesss.com/home/marketing-plans')
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//a[@class = 'a--underline font--900']")))
            els = driver.find_elements_by_xpath("//a[@class = 'a--underline font--900']")
            els[0].click()
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
        except:
            driver.refresh()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//i[@class = 'fa fa-plus mr-2 dim']")))
        add_more = driver.find_element_by_xpath("//i[@class = 'fa fa-plus mr-2 dim']")
        driver.execute_script("arguments[0].scrollIntoView();", add_more)
        try:
            add_more.click()
        except:
            time.sleep(1)
            add_more.click()
        ###
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@role = 'combobox']")))
        if check_exists_by_xpath(captcha_xpath) == True:
            play_sound()
            input("\nPlease handle the captcha and press enter")
        driver.find_element_by_xpath("//span[@role = 'combobox']").click()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Blog Post Intro')]")))
        driver.find_element_by_xpath("//strong[contains(text(), 'Blog Post Intro')]").click()
        time.sleep(3)

        blog_name = driver.find_element_by_xpath("//textarea[@name = 'biz_name']")
        blog_name.clear()
        blog_name.send_keys(category)
        blog_cat = driver.find_element_by_xpath("//textarea[@name = 'biz_type']")
        blog_cat.clear()
        blog_cat.send_keys('Overview,' + '"' + category + '"')
        about = driver.find_element_by_xpath("//textarea[@name = 'biz_desc']")
        about.clear()
        about.send_keys('We explain why people use ' + category)
        title = driver.find_element_by_xpath("//textarea[@name = 'post_title']")
        title.clear()
        title.send_keys('We explain why people use ' + category)
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Generate more Now')]")))
        time.sleep(1)

        driver.find_element_by_xpath("//a[contains(text(), 'Generate more Now')]").click()
        time.sleep(3)
        driver.refresh()
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//div[@class = 'col nl-to-br']")))
        except:
            driver.refresh()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//div[@class = 'col nl-to-br']")))
        blog_text = driver.find_elements_by_xpath("//div[@class = 'col nl-to-br']")
        data = ['Conclusion', blog_text[0].text, blog_text[1].text, blog_text[2].text, blog_text[3].text]
        writer.writerow(data)
#
start_time = time.time()
print("Running Blog Generator",ver)
login()
introduction()
factors()
play_sound()
fc_list = input("\nPlease enter the factors separated with ; eq: Style;Quality;Price  and then press Enter key ")
fc_list = fc_list.split(";")
factor_to_consider()
benefit()
play_sound()
bn_list = input("\nPlease enter the benefits separated with ; eq: Style;Quality;Price  and then press Enter key ")
bn_list = bn_list.split(";")
benefit_of_item()
conclusion()
sys.stdout.flush()
print("Process finished in " + str(round((time.time() - start_time) / 60, 2)) + " Minutes")
time.sleep(5)
sys.stdout.flush()
driver.quit()
