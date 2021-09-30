# mrff-api

Python / Flask Based API

## Setting up the project

### Requirements

**Python can suddenly betray a user if the apt installed python3 version and apt installed python3 packages go out of sync. Take precautions before upgrading a working install (backups, a rollback snapshot, etc) so you can revert to a known good state if an update goes bad**

- Ubuntu 20.04
- Python >= 3.8.5

### Installing requirements

1. Create a new non root user **important, for security, and because pipenv doesn't run well as root**. Log in from root `sudo adduser --system --group api`
2. Run `sudo apt update && apt upgrade` to update to the latest release
3. Install pipenv `sudo apt install pipenv`
4. Set the profile: `echo 'export PIPENV_VENV_IN_PROJECT=1' >> ~/.profile` so the venv dir is created in the project directory
5. Install psycopg2 for access to postgres: `sudo apt install python3-psycopg2`
6. Install virtualenv: `sudo apt install virtualenv`

### Setting up the API

1. Clone the repo and cd into the new local repo: `git clone git@github.com:bitcoinbrisbane/mrff-api.git && cd mrff-api`
2. Create the `.env` file by `cp .env.example .env`
3. Install the virtual env  `python3 -m venv venv`
4. Activate `source venv/bin/activate`
5. Install project dependancies with pipenv: `pip install -r requirements.txt`
6. Run `app --socket 0.0.0.0:5000 --protocol=http -w wsgi:app`
7. `deactivate`
8. Copy the api.service file `cp api.service /etc/systemd/system`
9. `systemctl enable api`
10. `systemctl start api`

Instructions can be found at `https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-20-04`

### Setting up the API with pipenv

1. Clone the repo and cd into the new local repo: `git clone git@github.com:bitcoinbrisbane/mrff-api.git && cd  mrff-api`
2. Install project dependancies with pipenv: `pipenv install`
3. Create the `.env` file
4. Install the virtual env `pipenv shell`

### Applying database migrations to a new database

```bash
pipenv run flask db upgrade
```

## Environment Variables

`CONN_STRING` is the connection string for the database
`FLASK_APP` is the location of the app, and shouldn't be modified
`FLASK_ENV` specifies production or development environments.
`PORT`, `DEBUG`, and `IP_ADDRESS` configure start options for the server

An example `.env` file:

```toml
FLASK_APP=app:init_app
FLASK_ENV=development
CONN_STRING='postgresql://xxx:25061/firmus?sslmode=require'
PORT=5000
DEBUG=True
IP_ADDRESS=127.0.0.1
```


## Unit tests
To run the unit tests from terminal `python -m unittest tests/calctests.py`

### Hosting

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04#prerequisites


## Notes

When os cant be found `export $(cat .env | xargs)`