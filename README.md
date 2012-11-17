This is a basic Flask project with all the fixins that's ready to be pushed to Heroku.

SETUP
-----
(Soon I'll turn this into a script.. probably)

Go to an empty folder

    mkdir [sitename] && cd [sitename]
 
Download all of this and remove the .git stuff.

    git clone git://github.com/gkoberger/flask-heroku.git . && rm -rf .git

Create a virtualenv

    mkvirtualenv [sitename]

Install all requirements

    pip install -r requirements.txt

Install and open [PosgressApp](http://postgresapp.com/)

Create the database
  
    psql -h localhost
    yourname=# CREATE DATABASE [DATABASE_NAME]

Open `$VIRTUAL_ENV/bin/postactivate` and add the following:

    export APP_CONFIG='settings_local.cfg'
    export DATABASE_URL='postgresql://localhost/[DATABASE_NAME]'

