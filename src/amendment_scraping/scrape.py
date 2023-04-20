from selenium import webdriver
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
from scrape_amendments import Amendments
from scrape_amendments_text import AmendmentText
import os
import sys
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

PATH = "assets/chromedriver_v112.exe"

def run(amendment_url, base_file_path='output/'):

	if not os.path.exists(base_file_path):
		os.makedirs(base_file_path)

	test_run = Amendments(amendment_url, base_file_path)
	print(test_run.get_title())
	test_run.scrape_all_amendments()

	index_csv = pd.read_csv(f"{base_file_path}amdt_text_index.csv")
	index_csv["text_scraped?"] = np.zeros(index_csv.shape[0])
	print(f"Found {index_csv.shape[0]} amendements. ")

	# initialize driver
	options = webdriver.ChromeOptions() 
	options.add_experimental_option('excludeSwitches', ['enable-logging']) # to supress the error messages/logs
	driver = webdriver.Chrome(options=options, executable_path=PATH)

	# initialize progress bar
	num_block = 0
	if len(base_file_path) == 7:
		title = "Progress"
	else:
		title = base_file_path[7:-1]
	for i in range(index_csv.shape[0]):

		# create a new driver instance every 20 amendments to 
		# prevent being detected as bot
		if i % 20 == 0:
			driver.quit()
			options = webdriver.ChromeOptions() 
			options.add_experimental_option('excludeSwitches', ['enable-logging']) # to supress the error messages/logs
			driver = webdriver.Chrome(options=options, executable_path=PATH)

		# progress bar
		num_block = int(i / index_csv.shape[0] * 100 * 40 // 100)
		sys.stdout.write(
		"\r" + title + ": |" + "█" * num_block + " " * (40 - num_block) + "|" + " " + f"{i+1}/{index_csv.shape[0]}")
		sys.stdout.flush()

		amendment_url = index_csv.iloc[i, 1]
		# print(amendment_url)
		amendment_text_url = re.sub(r'\?', '/text?', amendment_url)
		try:
			test_run = AmendmentText(amendment_text_url, driver)
			# print(test_run.get_title())
			amendment_text = test_run.scrape_amendment_text()

			with open(f'{base_file_path}amdt_text_{index_csv.iloc[i, 0]}.txt', 'w') as f:
				f.write(amendment_text)

			index_csv.iloc[i, -1] = 1 # indicates success
		except: 
			index_csv.iloc[i, -1] = 2 # indicates error

		# rate limiting
		time.sleep(0.5)

	index_csv.to_csv(f"{base_file_path}amdt_text_index.csv", index=False)

	# end progress bar
	sys.stdout.write(
		"\r" + title + ": |" + "█" * 40 + "|" + " " + f"{i+1}/{index_csv.shape[0]}" + " Done. \n")
	sys.stdout.flush()

	driver.quit()

def run_batch(to_run_file):
	batch_index_df = pd.read_csv(to_run_file)
	for i in range(batch_index_df.shape[0]):
		run(batch_index_df.iloc[i, 1], f'output/{batch_index_df.iloc[i, 0]}/')
		# print(f"Finished scraping all amendments for {batch_index_df.iloc[i, 0]}")
		print()

if __name__ == '__main__':
	
	# run("https://www.congress.gov/bill/113th-congress/house-bill/83/amendments")
	run_batch("amendments_to_run.txt")

		