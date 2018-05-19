# ledger-web

## Installation

Prerequisites:

- `virtualenv`
- `yarn` (or `npm`)

In your shell run from the project root:

``` sh
# Install Python dependencies
cd server
virtualenv -p python3 venv
venv/bin/pip install -r requirements.txt

# Install and compile front-end dependencies
cd ../ui
yarn install
yarn run build
cd ..
```

## Running the App

In your shell run:

``` sh
FLASK_APP=run.py server/venv/bin/flask run
```

Then open <http://localhost:5000> in your browser.
