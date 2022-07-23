import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import os
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    # Nasa Mars News
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL to scrape
    url_news = 'https://redplanetscience.com/'
    browser.visit(url_news)
    # html object
    html_news = browser.html
    # Create BeautifulSoup object; parse with 'html.parser'
    soup_news = BeautifulSoup(html_news, 'html.parser')

    # find first/most recent title
    results_news = soup_news.find('div', class_='content_title')
    news_title = results_news.text
    
    # find paragraph text for article
    results_news_p = soup.find('div', class_="article_teaser_body")
    news_p = results_news_p.text
    
    # quit browser scraping for Mars News Site
    browser.quit()
    
    # JPL Mars Space Images—Featured Image
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL to scrape
    url_image = 'https://spaceimages-mars.com/'
    browser.visit(url_image)

    # html object
    html_image = browser.html
    # Create BeautifulSoup object; parse with 'html.parser'
    soup_image = BeautifulSoup(html_image, 'html.parser')
    
    #find img src and build full url string
    results_img = soup.find('img', class_="headerimage")
    featured_image_url = f"{url}{results_img['src']}"
    
    # quit browser scraping for JPL Mars Space Images
    browser.quit()
    
    # Mars Facts
    
    # URL to scrape
    url_facts = 'https://galaxyfacts-mars.com/'
    # Retrieve page with the requests module
    html_facts = requests.get(url_facts)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup_facts = BeautifulSoup(html_facts.text, 'html.parser')
    results_facts = soup_facts.find('table', class_="table-striped")
    
    # Mars facts table
    tables = pd.read_html(url)
    mars_facts = tables[1]

    #convert to html string for table
    mars_facts.to_html()
    
    # Mars Hemispheres
    
    # https://marshemispheres.com/
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"},
    ]

    


