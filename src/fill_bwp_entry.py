import numpy as np
import pandas as pd

FILE_PATH = "bwp_entry_Yiyang_test_output.csv"
OUPUT_PATH = "bwp_entry_Yiyang_test_output.csv"
DICT = {
	'w': "White", 
	'b': "Blue", 
	'p': "Pink", 
	'u': "Unsure"
}


def take_input(df):

	type_list = []
	while True:
		c = input("Layoff type: (w, b, p, u) ")
		while c not in ['w', 'b', 'p', 'u', 'f', 's']:
			c = input("Invalid type, try again: ")

		if c == 's':
			save_progress(df)	
			continue;

		if c == 'f':
			if len(type_list) > 0:
				return type_list
			else: 
				print("No input yet. ")
				continue;

		type_list.append(c)


def find_start_index(df):
	start_index = 0
	while start_index < df.shape[0]:
		if df.iloc[start_index].Filled == 0:
			break;
		start_index += 1
	return start_index


def save_progress(df):
	df.to_csv(OUPUT_PATH, index=False)
	print("Progress saved!")


if __name__ == '__main__':

	df = pd.read_csv(FILE_PATH)

	start_index = find_start_index(df)
	for i in range(start_index, df.shape[0]):
		print("Row", i)
		print(df.iloc[i].situation)
		type_list = take_input(df)
		for c in type_list:
			df.loc[df.index[i], DICT[c]] = 1
		df.loc[df.index[i], "Filled"] = 1
		print("===================")
		print()

	save_progress(df)
	print("Finished")

