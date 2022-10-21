# Politician voting data
- Stockwatcher and CRSP
	- `house_all_transactions`: original dataset from housestockwatcher.com
	- `house_all_transactions_fixed`: fixed some typo with dates (to replicate: src/fix_house_sw(house_all_transactions) -> house_all_transactions_fixed)
	- `senate_all_transactions`: original dataset from senatestockwatcher.com
	- `house_crsp`: CRSP data (from WRDS crsp.wrds_dsfv2_query) for relevant ticker (to replicate: generate-crsp-sql-queries -> execute-crsp-sql-queries)
	- `senate_crsp`: CRSP data (from WRDS crsp.wrds_dsfv2_query) for relevant ticker (to replicate: generate-crsp-sql-queries -> execute-crsp-sql-queries)
	- `sw_crsp_house`: Merge CRSP with housestockwatcher (to replicate: merge-sw-crsp)
	- `sw_crsp_senate`: Merge CRSP with senatestockwatcher (to replicate: merge-sw-crsp)
