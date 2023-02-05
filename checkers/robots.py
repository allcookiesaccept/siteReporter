import requests
import pandas as pd
from sitemap import Sitemap

class Robots:

    def __init__(self):

        self.sitemap_link = None

    def check_robots(self, site):

        self.get_robots(site)
        self.count_user_agents()
        # self.group_lines_by_user_agents()
        # self.is_site_blocked()
        self.find_sitemap_link()
        # self.get_sitemap_link()


    def get_robots(self, site):

        url = f'{site}robots.txt'
        self.robots = requests.get(url).text.lower()

        return self.robots

    def count_user_agents(self):

        self.ua_counter = self.robots.count('user-agent')

        return self.ua_counter

    def find_sitemap_link(self):

        if self.robots.find('sitemap:') > -1:
            self.sitemap_link = self.robots.split('sitemap:')[1].strip()
            return True

        else:
            return False
