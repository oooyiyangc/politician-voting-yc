from selenium import webdriver
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
from scrape_amendments import Amendments
from scrape_amendments_text import AmendmentText

if __name__ == '__main__':
	test_run = Amendments("https://www.congress.gov/bill/116th-congress/house-bill/1158/amendments")
	print(test_run.get_title())
	test_run.scrape_all_amendments()

	test_run_csv = pd.read_csv("amendments_test.csv")
	test_run_csv["text_scraped?"] = np.zeros(test_run_csv.shape[0])
	for i in range(test_run_csv.shape[0]):
		amendment_url = test_run_csv.iloc[i, 1]
		print(amendment_url)
		amendment_text_url = re.sub(r'\?', '/text?', amendment_url)
		try:
			test_run = AmendmentText(amendment_text_url)
			# print(test_run.get_title())
			amendment_text = test_run.scrape_amendment_text()

			with open(f'output/amendment_text_{test_run_csv.iloc[i, 0]}.txt', 'w') as f:
				f.write(amendment_text)

			test_run_csv.iloc[i, -1] = 1
		except: 
			test_run_csv.iloc[i, -1] = 2 # indicates error

	test_run_csv.to_csv("amendments_test.csv", index=False)

		