import requests
import xml.etree.ElementTree as ET


class Sitemap:

    def __init__(self):

        self.sitemaps_with_links = []
        self.sitemaps_list = []
        self.xml_reader = ET

    def sitemap_links_scrapper(self):
        ...


    def get_response(self):

        response = requests.get(self.sitemap_link)
        self.tree = ET.fromstring(response.content)

        return self.tree

    def get_links(self):

        self.sitemap_name = self.sitemap_link.split('/')[-1]
        xml_file = ET.parse(self.tree)
        self.xml_links = {self.sitemap_name: []}

        for loc in xml_file.findall('sitemap'):
            url = loc.find('loc').text

            if url.find('.xml') > -1:
                self.sitemaps_list.append(url)

            self.sitemaps_with_links.append(self.xml_links)


