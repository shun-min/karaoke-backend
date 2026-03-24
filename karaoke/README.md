# Setup backend
### Notes:
1. Top level `karaoke` folder is the django project root, which contains a `core` app and `backend` app.
2. `pyproject.toml` and `env` virtualenv folder are outside of the django project root, but does not affect the frontend folder.

## Pre-requisites:
1. Have pyenv installed
2. use python 3.12.1

## Instructions (Linux only)
1. git clone kara-no-kyoukai project
2. cd into cloned `kara-no-kyoukai` folder
3. Execute the following lines:
```shell
pyenv local 3.12.1
python -m venv env
source env/bin/activate
pip install -e .
pip install -e .[dev]
pip install -e .[dev-lint]
```
4. `cd karaoke`
5. create `.env` file, add `DJANGO_SECRET` value. Re-generate it if you don't have one
6. `python manage.py runserver` to test

## Database: 
This project uses sqlite, controls db data with django-seed module. \
(https://medium.com/@anindya.lokeswara/django-data-seeding-a-quick-guide-b8cfd72be4cc)
(https://github.com/Brobin/django-seed)

### Seed database: 
```shell
cd karaoke
python manage.py loaddata core/manage/seed.json
```

### Dump database: 
```shell
cd karaoke
python manage.py dumpdata core --indent 2 > core/manage/seed.json
```

# Setup frontend
1. Download nvm through curl. NVM will be used to manage node and npm versions
```shell
cd karaoke-nextjs
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
```

2. Execute the following etup nvm env vars. You can paste them into ~/.bash_profile so it auto loads upon WSL start up
```
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

3.Install Node and npmq
`nvm install 24.13.0`
`nvm use 24.13.0`

4. Check versions
```
node -v
npm -v
```

5. Install packages into node_modules folder, based on package.json
`npm install`

6. cd into `karaoke-nextjs`, create a .env file, add `NEXT_PUBLIC_PROD_HOST` value (localhost or prod domain)

# Run nextJS server
`npm run dev`
