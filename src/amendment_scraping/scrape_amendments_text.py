from selenium import webdriver
from bs4 import BeautifulSoup
import re
import pandas as pd

class AmendmentText:

	PATH = "assets/chromedriver_v110.exe"

	def __init__(self, url):
		self.url = url
		# self.aid = aid
		self.driver = webdriver.Chrome(self.PATH)
		self.driver.get(self.url)


	def get_title(self):
		return self.driver.title

	def quit(self):
		self.driver.quit()
		quit()

	def scrape_amendment_text(self):
		# amendment_text_link = self.driver.find_element_by_partial_link_text(self.aid)
		# amendment_text_link.click()

		# text_window_link = self.driver.find_element_by_link_text("View TXT in new window")
		# text_window_link.click()

		# self.driver.switch_to.window(self.driver.window_handles[1])
		amendment_text_html = self.driver.page_source
		soup = BeautifulSoup(amendment_text_html,'html.parser')
		try: 
			# Version after 3/16/2023
			amendment_text = soup.find('pre', class_="styled").text
			# print(amendment_text.text)
		except:
			table_block = soup.find('table', class_="item_table")
			articles_table_url = table_block.find('a', href=True)['href']
			self.url = "https://www.congress.gov" + articles_table_url
			self.driver.get(self.url)

			text_window_link = self.driver.find_element_by_link_text("View TXT in new window")
			text_window_link.click()

			self.driver.switch_to.window(self.driver.window_handles[1])
			amendment_text_html = self.driver.page_source
			soup = BeautifulSoup(amendment_text_html,'html.parser')
			amendment_text = soup.text

		return amendment_text

		

if __name__ == '__main__':

	test_run = AmendmentText("https://www.congress.gov/amendment/116th-congress/senate-amendment/1266/text?s=a&r=2")
	# print(test_run.get_title())
	amendment_text = test_run.scrape_amendment_text()
	with open(f'output/amendment_text.txt', 'w') as f:
		f.write(amendment_text)