import requests
import pandas as pd
import xml.etree.ElementTree as ET
# from checkers.robots import Robots
# from checkers.sitemap import Sitemap
import xmltodict


url = 'https://re-store.ru/sitemap.xml'

response = requests.get(url)
dict_data = xmltodict.parse(response.content)

sitemaps_with_links = []
sitemaps_list = []


for item in dict_data['sitemapindex']['sitemap']:
    link = item['loc']
    sitemap_urls = []
    if link.find('.xml'):
        sitemaps_list.append(link)
    sitemap_urls.append(link)
    sitemaps_with_links.append({url: sitemaps_urls})
