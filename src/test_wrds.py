import wrds

if __name__ == '__main__':

	db = wrds.Connection(wrds_username='yiyangc')

	command = "print('WRDS Interactive Session...')"
	while command != "q":
		try:
			exec(command)
		except:
			print('\033[91m'+"An error occurred during execution. "+'\033[0m')
		command = input(">>> ")

