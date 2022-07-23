import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    # Nasa Mars News
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL to scrape
    url_news = 'https://redplanetscience.com/'
    browser.visit(url_news)
    # Let it sleep for 1 second
    time.sleep(1)
    # html object
    html_news = browser.html
    # Create BeautifulSoup object; parse with 'html.parser'
    soup_news = BeautifulSoup(html_news, 'html.parser')

    # find first/most recent title
    results_news = soup_news.find('div', class_='content_title')
    news_title = results_news.text
    
    # find paragraph text for article
    results_news_p = soup_news.find('div', class_="article_teaser_body")
    news_p = results_news_p.text
    
    # quit browser scraping for Mars News Site
    # browser.quit()
    
    # JPL Mars Space Images—Featured Image
    
    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # browser = Browser('chrome', **executable_path, headless=False)

    # URL to scrape
    url_image = 'https://spaceimages-mars.com/'
    browser.visit(url_image)
    # Let it sleep for 1 second
    time.sleep(1)
    # html object
    html_image = browser.html
    # Create BeautifulSoup object; parse with 'html.parser'
    soup_image = BeautifulSoup(html_image, 'html.parser')
    
    #find img src and build full url string
    results_img = soup_image.find('img', class_="headerimage")
    featured_image_url = f"{url_image}{results_img['src']}"
    
    # quit browser scraping for JPL Mars Space Images
    # browser.quit()
    
    # Mars Facts
    
    # URL to scrape
    url_facts = 'https://galaxyfacts-mars.com/'
    
    # Mars facts table
    tables = pd.read_html(url_facts)
    mars_facts = tables[1]
    #getting rid of column headers
    mars_facts = mars_facts.rename(columns = {0:'',1:''})

    #convert to html string for table
    mars_facts_table = mars_facts.to_html(index=False)
    
    # Mars Hemispheres
    
    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # browser = Browser('chrome', **executable_path, headless=False)

    url_hemispheres = 'https://marshemispheres.com/'
    browser.visit(url_hemispheres)
    # Let it sleep for 1 second
    time.sleep(1)
    html_hemispheres = browser.html
    soup_hemispheres = BeautifulSoup(html_hemispheres, 'html.parser')

    headers=[]
    titles = soup_hemispheres.find_all('h3')
    #removing the last header 'Back' that we don't need
    titles = titles[:-1]

    for title in titles:
        headers.append(title.text)

    #empty list to store image src urls in
    images=[]
    count=0
    for h in headers:
        #using splinter to find thumbnail images, click through to each link,
        #then find the src link for each image with class "wide-image"
        browser.find_by_css('img.thumb')[count].click()
        images.append(browser.find_by_css('img.wide-image')['src'])
        browser.back()
        #counter used to loop through each thumbnail image
        count=count+1

    #list to store dictionaries in
    hemisphere_image_urls = []
    counter = 0
    for i in images:
        #appending each title and url to the list of dictionaries
        hemisphere_image_urls.append({"title":headers[counter],"img_url":images[counter]})
        counter = counter+1

    mars_data = {"newsTitle":news_title, "newsParagraph":news_p, "image_url":featured_image_url, "marsTable":mars_facts_table, "hemisphereImages":hemisphere_image_urls}

    browser.quit()

    return mars_data
# mars_data = scrape()