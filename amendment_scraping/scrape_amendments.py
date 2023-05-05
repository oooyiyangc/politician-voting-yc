from selenium import webdriver
from bs4 import BeautifulSoup
import re
import pandas as pd

class Amendments:

	PATH = "assets/chromedriver_v112.exe"
	congress_base_url = "https://www.congress.gov"

	def __init__(self, url, base_file_path='output/'):
		self.url = url

		options = webdriver.ChromeOptions() 
		options.add_experimental_option('excludeSwitches', ['enable-logging']) # to supress the error messages/logs
		self.driver = webdriver.Chrome(options=options, executable_path=self.PATH)
		self.driver.get(self.url)
		self.base_file_path = base_file_path

	def get_title(self):
		return self.driver.title

	def quit(self):
		self.driver.quit()
		quit()

	def scrape_all_amendments(self):
		page_source = self.driver.page_source
		soup = BeautifulSoup(page_source, 'lxml')

		amendments = []
		amendments_selector = soup.find_all('li', class_="compact")

		if amendments_selector == None:
			print(f"No amendments found for {self.url}.")
			return;
		while True:
			for amendment_selector in amendments_selector:
				heading_span = amendment_selector.find('span', class_='result-heading amendment-heading')
				heading_text = heading_span.find('a', href=True).text
				# print(heading_text)
				heading_href = self.congress_base_url + heading_span.find('a', href=True)['href']
				# print(heading_href)
				heading_congress = re.sub(r'\s—\s', '', heading_span.find('a', href=True).next_sibling)
				# print(heading_congress)

				content_span = amendment_selector.find_all('span', class_='result-item')

				# raise warning to user if content span has length 0
				if len(content_span) < 1:
					print('\u001b[91m'+f"Error: Unexpected content span for {heading_text}"+'\u001b[0m')
					print('\u001b[91m'+f"Content: {content_span}"+'\u001b[0m')
					print('\u001b[91m'+f"URL: {self.url}"+'\u001b[0m')
					continue

				# Purpose span
				if len(content_span) > 1:
					purpose_span = content_span[0]
					purpose_text = re.sub(r'\s\s+', '', purpose_span.find('strong').next_sibling)
					purpose_href_a = purpose_span.find('a', href=True)
					if purpose_href_a:
						purpose_href = self.congress_base_url + purpose_href_a['href']
					else:
						purpose_href = None
				else:
					# if content span only has 1 item, that item is sponsor
					# set purpose to None
					purpose_text = None 
					purpose_href = None

				# Sponsor span
				if len(content_span) > 1:
					sponsor_span = content_span[1]
				else:
					sponsor_span = content_span[0]
				sponsor_text = sponsor_span.find('a', href=True)
				if sponsor_text:
					sponsor_text = sponsor_text.text
					sponsor_href = self.congress_base_url + sponsor_span.find('a', href=True)['href']
					sponsor_dates = sponsor_span.find('a', href=True).next_sibling
				else: 
					sponsor_span_text = re.sub(r'\s\s+', '', sponsor_span.find('strong').next_sibling)
					try: 
						sponsor_text = re.findall(r'(.*)\(', sponsor_span_text)[0]
						sponsor_href = None
						sponsor_dates = re.findall(r'\(.*\)', sponsor_span_text)[0]
					except:
						sponsor_text = None 
						sponsor_dates = None 

				# Latest action span
				if len(content_span) > 2:
					latest_action_span = content_span[2]
					latest_action_text = latest_action_span.find('strong').next_sibling
				else:
					latest_action_text = None

				# print("================================")

				amendment_data = {
					'name': heading_text,
					'href': heading_href,
					'congress':  heading_congress,
					'purpose': purpose_text,
					'purpose_href': purpose_href, 
					'sponsor': sponsor_text,
					'sponsor_href':  sponsor_href,
					'dates': sponsor_dates,
					'latest_action': latest_action_text
				}

				amendments.append(amendment_data)

			# if there's next page
			if soup.find('a', href=True, class_="next"):
				next_page_url = soup.find('a', href=True, class_="next")["href"]
				self.url = "https://www.congress.gov" + next_page_url
				self.driver.get(self.url)
				page_source = self.driver.page_source
				soup = BeautifulSoup(page_source, 'lxml')
				amendments_selector = soup.find_all('li', class_="compact")
			else:
				break;

		amendments_df = pd.DataFrame(amendments)
		amendments_df.to_csv(f"{self.base_file_path}amdt_text_index.csv", index=False)


if __name__ == '__main__':
	# test_run = Amendments("https://www.congress.gov/bill/117th-congress/house-bill/2471/amendments")
	# test_run = Amendments("https://www.congress.gov/bill/117th-congress/house-bill/4502/amendments")
	test_run = Amendments("https://www.congress.gov/bill/108th-congress/house-bill/2657/amendments")
	print(test_run.get_title())
	test_run.scrape_all_amendments()