## This is simple instruction how to run pytest tests for TRN database in MS SQL Server.


## Create virtual environment for tests execution
```cmd
cd pytest_hw
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

## Run pytest tests in verbose mode (in created virtual environment)
```cmd
pytest -v
```

## Run pytest tests in verbose mode for specific table (in created virtual environment)
## Existing tables (table_name): countries, jobs, employees
```cmd
pytest -v -m table_name
```