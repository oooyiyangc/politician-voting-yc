# Scripts
- Stockwatcher
	- [`eda.ipynb`](eda.ipynb) A general EDA for stockwatcher data
	- [`generate-crsp-sql-queries.ipynb`](generate-crsp-sql-queries.ipynb), [`execute-crsp-sql-queries.ipynb`](execute-crsp-sql-queries.ipynb), [`merge-sw-crsp.ipynb`](merge-sw-crsp.ipynb) Fetch CRSP stock data from WRDS and merge with raw stockwatcher
	- [`fix_house_sw.py`](fix_house_sw.py) Fixes some data entry errors in raw house stockwatcher dataset
	- [`setup_wrds.py`](setup_wrds.py), [`test_wrds.py`](test_wrds.py) Scripts to setup and test (with an interactive session) WRDS connection
	- [`generate-involvement-factor.ipynb`](generate-involvement-factor.ipynb) First-stage exercise to produce single factor for feasibility analysis

- OpenSecrets
	- [`pfd.ipynb`](pfd.ipynb) Exploratory data exercise with OpenSecrets Personal Finance Disclosure (PFD) data

- Sacerdote
	- [`bs-data-cleaning.ipynb`](sacerdote_data.ipynb) Extract relevant columns from [Belmont and Sacerdote (2022)](https://doi.org/10.1016/j.jpubeco.2022.104602) data with some preliminary coverage report. 
	- [`bs-sp500esg.ipynb`](bs-sp500esg.ipynb) Produce single ESG-investment regressor for feasibility exercise with SP500 ESG Index
