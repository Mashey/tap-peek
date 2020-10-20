# Peek :: Tap

A Singer tap for Peek.

## Setup :: Developers

If you are already familiar with `Python Poetry` and `singer-python` the next few sections of this `README` do not contain any new information; follow the standard setup process and proceed to the `Tap Documentation` section.

### Dependencies and Virtualenvs

- Install: [Python Poetry](https://python-poetry.org/)
  - Poetry handles dependencies and virtual environments
- After pulling the repo run `poetry install`
  - This ensures all dependencies and virtualenvs are the correct version

### Environment Variables

- The `singer-python` package is included to handle secret environment variables
- There is a `config_tap_<company>.json` file for each company
  - This file contains `partner_id` and `API_KEY`
- The configuration file used is determined by the command line arguments when launching the tap
  - `python tap_peek.py -c config_tap_<company>.json | target-<name> -c config_target_<name>.json`
- The `partner_id` and `API_KEY` are set by the following code:

```python
# peek.py

...

args = singer.utils.parse_args(["token", "partner_id"])
partner_id = args.config['partner_id']
API_KEY = args.config['token']
```

### Add native Poetry virtualenv support to VS Code (optional)

- VS Code can be configured to support Poetry virtual environments natively
  - This only needs to be done once
  - Add the following to the VS Code `settings.json` file, or use the `settings` gui:

```json
{
  "python.poetryPath": "poetry",
  "python.venvPath": "~/.cache/pypoetry/virtualenvs"
}
```

- Add a `.vscode` directory to the root of the project
  - Add a `settings.json` file to the `.vscode` directory
  - Ensure `poetry install` has been completed
  - In the terminal run the command `poetry env info` to display virtual environment information for the project. The results are unqiue to each local user. This is an example of what to expect:

![Virtualenv Info](https://user-images.githubusercontent.com/10391857/94093631-e4b53480-fdda-11ea-8a97-d9f0dc40be65.png)

- Copy and paste the path from `Virtualenv > Path: </copy/your/path/located/here>` to `settings.json` within the `.vscode` directory as follows:

```json
{
  "python.pythonPath": "/paste/your/path/here"
}
```

- Close and reopen the VS Code terminal
- Poetry virtualenvs are now able to be selected as a default interpreter

New to Poetry? The docs are excellent, and there is more information about
managing environments [here](https://python-poetry.org/docs/managing-environments/).

## Tap Documentation

This service is designed to be company agnostic, but it does require the correct company `token` and `partner_id` to be loaded from the `company_name` environment variable.

### Testing :: `partner_id` and `API_KEY`

Passing the normal command line args to the tap in the test environment is not predictable. Uncomment the following code block to use with testing:

```python
# peek.py
...

# The code below is for testing with Pytest.
load_dotenv()
API_KEY = json.loads(os.getenv("company_name"))['token']
partner_id = json.loads(os.getenv("company_name"))['partner_id']

...
```

Then ensure the regular args code block is commented out:

```python
# peek.py
...

# This code is for production.
args = singer.utils.parse_args(["token", "partner_id"])
API_KEY = args.config['token']
partner_id = args.config['partner_id']

...
```

### Endpoints

The available Peek API endpoints.

#### `fetch_transactions(new_start_date, new_end_date)`

This function returns transactions within the given date range. The associated schema is `transactions_schema.json`.

```python
def fetch_transactions(new_start_date="year-month-day", new_end_date="year-month-day"):
    start_date = new_start_date
    end_date = new_end_date
  ...
```

Calling `fetch_transactions()`

```python
fetch_transactions("2020-08-15", "2020-08-25")
```

#### `fetch_core_activities()`

This function returns core activities for a given partner. The associated schema is `activity_info_schema.json`.

```python
def fetch_core_activities():
  ...
```

Calling `fetch_core_activities()`

```python
fetch_core_activities()
```

#### `fetch_core_addons()`

This function returns core addons for a given partner. The associated schema is `core_addons_schema.json`.

```python
def fetch_core_addons():
  ...
```

Calling `fetch_core_addons()`

```python
fetch_core_addons()
```

#### fetch_timeslots(start_date="year-month-day", end_date="year-month-day")

This function returns all timeslots for a given date range. The associated schema is `timeslots_schema.json`.

```python
def fetch_timeslots(start_date="year-month-day", end_date="year-month-day"):
    payload = {
      "start_date": start_date,
      "end_date": end_date
    }
  ...
```

Calling `fetch_timeslots(start_date="year-month-day", end_date="year-month-day")`

```python
fetch_timeslots("2020-08-15", "2020-08-25")
```

## Helpful Documentation

Documentation for packages used in this project.

### `Python Poetry` Package :: Dependency and Environment Management

- [Python Poetry Docs](https://python-poetry.org/docs/)

### `Requests` Package :: Client and Server Requests

- [Requests Docs](https://requests.readthedocs.io/en/master/)

### `VCR.py` Package :: Records API Requests for Testing

- [VCR.py Docs](https://vcrpy.readthedocs.io/en/latest/)

### `Pytest` Package and Plugins :: Testing

- [Pytest Docs](https://docs.pytest.org/en/stable/index.html)
- [Pytest VCR Docs](https://pytest-vcr.readthedocs.io/en/latest/)
- [Pytest Cov Docs](https://pytest-cov.readthedocs.io/en/latest/readme.html)

### `Coverage.py` Package :: Test Coverage

- [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.3/)

### `Python Dotenv` Package :: Environment Variables

- [Python Dotenv Docs](https://pypi.org/project/python-dotenv/)