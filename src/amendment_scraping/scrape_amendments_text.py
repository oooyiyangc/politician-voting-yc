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

		# Version after 3/16/2023
		amendment_text_html = self.driver.page_source
		soup = BeautifulSoup(amendment_text_html,'html.parser')
		amendment_text = soup.find('pre', class_="styled")
		# print(amendment_text.text)
		# amendment_text = soup.text

		# with open(f'amendment_text_test.txt', 'w') as f:
		# 	f.write(amendment_text.text)
		return amendment_text.text

		

if __name__ == '__main__':
	test_run_csv = pd.read_csv("amendments_test.csv")
	# test_run_csv["text_scraped?"] = np.zeros(test_run_csv.shape[0])
	for i in range(test_run_csv.shape[0]):
		amendment_url = test_run_csv.iloc[i, 1]
		print(amendment_url)
		amendment_text_url = re.sub(r'\?', '/text?', amendment_url)

		test_run = AmendmentText(amendment_text_url)
		# print(test_run.get_title())
		amendment_text = test_run.scrape_amendment_text()
		with open(f'output/amendment_text_{test_run_csv.iloc[i, 0]}.txt', 'w') as f:
			f.write(amendment_text)