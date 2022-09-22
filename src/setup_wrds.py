import wrds
db = wrds.Connection(wrds_username="yiyangc")
db.create_pgpass_file()