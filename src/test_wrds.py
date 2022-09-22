import wrds
import time

if __name__ == '__main__':

	command_log = ""
	db = wrds.Connection(wrds_username='yiyangc')

	print()
	command = "print('\u001b[7m WRDS Interactive Session \u001b[0m')"
	while command != "q":

		if command == "s":
			f = open(f"logs/log-{time.strftime('%Y%m%d-%H%M%S', time.localtime())}.txt", "w")
			f.write(command_log)
			f.close()
			print('\u001b[93m'+"Commands saved. "+'\u001b[0m')

			command = input(">>> ")
			continue;

		try:
			if "db.get_table" in command or "db.raw_sql" in command:
				print('\u001b[93m'+"Fetching data..."+'\u001b[0m')
			exec(command)

			command_log += "[Executed] " + command + "\n"

		except Exception as e:
			print('\u001b[91m'+"An error occurred during execution. "+'\u001b[0m')
			print('\u001b[91m'+str(e)+'\u001b[0m')

			command_log += "[Failed] " + command + "\n"

		command = input(">>> ")

	db.close()

