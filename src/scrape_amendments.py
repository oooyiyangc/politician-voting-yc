from selenium import webdriver
from bs4 import BeautifulSoup
import re
import pandas as pd

class Amendments:

	PATH = "assets/chromedriver_v110.exe"

	def __init__(self, url):
		self.url = url
		self.driver = webdriver.Chrome(self.PATH)
		self.driver.get(self.url)

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
		for amendment_selector in amendments_selector:
		    heading_span = amendment_selector.find('span', class_='result-heading amendment-heading')
		    heading_text = heading_span.find('a', href=True).text
		    print(heading_text)
		    heading_href = heading_span.find('a', href=True)['href']
		    print(heading_href)
		    heading_congress = re.sub(r'\s—\s', '', heading_span.find('a', href=True).next_sibling)
		    print(heading_congress)

		    content_span = amendment_selector.find_all('span', class_='result-item')

		    # Purpose span
		    purpose_span = content_span[0]
		    purpose_text = re.sub(r'\s\s+', '', purpose_span.find('strong').next_sibling)
		    print(purpose_text)
		    purpose_href_a = purpose_span.find('a', href=True)
		    if purpose_href_a:
		    	purpose_href = purpose_href_a['href']
		    else:
		    	purpose_href = None
		    print(purpose_href)

		    # Sponsor span
		    sponsor_span = content_span[1]
		    sponsor_text = sponsor_span.find('a', href=True).text
		    print(sponsor_text)
		    sponsor_href = sponsor_span.find('a', href=True)['href']
		    print(sponsor_href)
		    sponsor_dates = sponsor_span.find('a', href=True).next_sibling
		    print(sponsor_dates)

		    # Latest action span
		    if len(content_span) > 2:
		    	latest_action_span = content_span[2]
		    	latest_action_text = latest_action_span.find('a', href=True).next_sibling
		    	print(latest_action_text)
		    	latest_action_href = latest_action_span.find_all('a', href=True)[-1]['href']
		    	print(latest_action_href)
		    else:
		    	latest_action_text = None
		    	latest_action_href = None

		    print("================================")

		    amendment_data = {
		        'name': heading_text,
		        'href': heading_href,
		        'congress':  heading_congress,
		        'purpose': purpose_text,
		        'purpose_href': purpose_href, 
		        'sponsor': sponsor_text,
		        'sponsor_href':  sponsor_href,
		        'dates': sponsor_dates,
		        'latest_action': latest_action_text, 
		        'latest_action_href': latest_action_href
		    }

		    amendments.append(amendment_data)

		amendments_df = pd.DataFrame(amendments)
		amendments_df.to_csv("amendments_test.csv", index=False)

if __name__ == '__main__':
	test_run = Amendments("https://www.congress.gov/bill/117th-congress/house-bill/2471/amendments")
	print(test_run.get_title())
	test_run.scrape_all_amendments()