# pyLaridae (Seagull Helper)

This is a program that helps generate content for Seagull, a SSG built by me (notna888)

This project was originally based off https://github.com/cookiecutter-flask/cookiecutter-flask - I have removed the docker part however, just because I feel it is outside of the scope I'm going for here.

### Running locally

Run the following commands to set up development

```bash
cd pyLaridae
pipenv install --dev
pipenv shell
npm install
npm start  # run the webpack dev server and flask server using concurrently
```

If you aren't developing this project and do not require webpack and are just using the project, all you need is python.

```bash
cd pyLaridae
pipenv install --dev
flask run --host=0.0.0.0
```

You will see a pretty welcome screen.

The default login is: <br/>
Username: laridae
Password: laridae

#### Database Initialization (locally)

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration

```bash
flask db init
flask db migrate
flask db upgrade
```

## Deployment

```bash
export FLASK_ENV=production
export FLASK_DEBUG=0
export DATABASE_URL="<YOUR DATABASE URL>"
npm run build   # build assets with webpack
flask run       # start the flask server
```

## Shell

To open the interactive shell, run

```bash
flask shell
```

By default, you will have access to the flask `app`.

## Running Tests/Linter

To run all tests, run

```bash
flask test
```

To run the linter, run

```bash
flask lint
```

The `lint` command will attempt to fix any linting/style errors in the code. If you only want to know if the code will pass CI and do not wish for the linter to make changes, add the `--check` argument.

## Migrations

Whenever a database migration needs to be made. Run the following commands

```bash
flask db migrate
```

This will generate a new migration script. Then run

```bash
flask db upgrade
```

To apply the migration.

```bash
git add migrations/*
git commit -m "Add migrations"
```

Make sure folder `migrations/versions` is not empty.

## Asset Management

Files placed inside the `assets` directory and its subdirectories
(excluding `js` and `css`) will be copied by webpack's
`file-loader` into the `static/build` directory. In production, the plugin
`Flask-Static-Digest` zips the webpack content and tags them with a MD5 hash.
As a result, you must use the `static_url_for` function when including static content,
as it resolves the correct file name, including the MD5 hash.
For example

```html
<link rel="shortcut icon" href="{{static_url_for('static', filename='build/img/favicon.ico') }}">
```

If all of your static files are managed this way, then their filenames will change whenever their
contents do, and you can ask Flask to tell web browsers that they
should cache all your assets forever by including the following line
in ``.env``:

```text
SEND_FILE_MAX_AGE_DEFAULT=31556926  # one year
```
