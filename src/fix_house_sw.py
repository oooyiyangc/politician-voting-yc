import numpy as np
import pandas as pd

"""
Fixes House Stockwatcher data
In transaction_date, replace instances of "20222-xx-xx" with "2022-xx-xx"
"""

if __name__ == '__main__':

	house = pd.read_csv("../data/house_all_transactions.csv")

	house["transaction_date"] = house["transaction_date"].str.replace(r"20222-", "2022-")
	house["transaction_date"] = house["transaction_date"].str.replace(r"20221-", "2021-")

	house.to_csv("../data/house_all_transactions_fixed.csv", index=False)