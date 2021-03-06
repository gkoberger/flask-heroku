This is a basic Flask project with all the fixins that's ready to be pushed to Heroku.

I'll clean it up eventually, move things out of app.py and make a script for 
initiating it. But this is a start, I suppose?

WHAT THIS INCLUDES
------------------

 * Flask
 * ["Real HTML5 Boilerplate"](http://csswizardry.com/2011/01/the-real-html5-boilerplate/)
 * SQL Alchemy
 * WTForms
 * Webassets (compress assets, compile LESS, etc)
 * Flask-Script
 * Flask-Evolution (migrations)

Everything is connected to Flask, and ready to be pushed to Heroku.

LOCAL SETUP
-----------
(Soon I'll turn this into a script.. probably)
(TODO: show difference between initial setup and anyone checking it out)

Go to an empty folder

    mkdir [sitename] && cd [sitename]
 
Download all of this and remove the .git stuff.

    git clone git://github.com/gkoberger/flask-heroku.git . && rm -rf .git

Create a virtualenv

    mkvirtualenv [sitename]

Install all requirements

    pip install -r requirements.txt

Install [PosgressApp](http://postgresapp.com/)

Install all the node dependencies:

    npm install -g uglify-js
    npm install -g less

Create the database
  
    psql -h localhost
    yourname=# CREATE DATABASE [DATABASE_NAME]

Open `$VIRTUAL_ENV/bin/postactivate` and add the following:

    export APP_CONFIG='settings_local.cfg'
    export DATABASE_URL='postgresql://localhost/[DATABASE_NAME]'

Set up migrations (we have to run it to create directories, etc):

    python manage.py migrate run

RUNNING IT
----------

1. `workon [sitename]`

2. Open up Postgres.app

3. Run `foreman start`

CREATING AND RUNNING MIGRATIONS
-------------------------------

Create: `python manage.py migrate create`
Run: `python manage.py migrate run`

Redo: `python manage.py migrate redo`
Undo: `python manage.py migrate undo`

SETTING UP HEROKU
-----------------

Scale things up

    heroku ps:scale web=1

Set settings file

    heroku config:add APP_CONFIG=settings_prod.cfg

Set up Postgres

    heroku addons:add heroku-postgresql:dev
    heroku pg:promote HEROKU_POSTGRESQL_[GET_REST_FROM_OUTPUT_OF_ABOVE_COMMAND]

TODO (So I don't forget)
------------------------
Push script:
 * Compile assets
 * Run migrations

