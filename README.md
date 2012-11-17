This is a basic Flask project with all the fixins that's ready to be pushed to Heroku.

SETUP
-----
(Soon I'll turn this into a script.. probably)

 1. Go to an empty folder

    mkdir [sitename] && cd [sitename]
 
 2. Download all of this and remove the .git stuff.

    git clone git://github.com/gkoberger/flask-heroku.git . && rm -rf .git

 3. Create a virtualenv

    mkvirtualenv [sitename]

 4. Install all requirements

    pip -E MyProject install -r requirements.txt

 5. Install and open [PosgressApp](http://postgresapp.com/)

 6. Create the database
    
    psql -h localhost
    CREATE DATABASE [DATABASE_NAME]

 7. Open `$VIRTUAL_ENV/bin/postactivate` and add the following:

    export APP_CONFIG='settings_local.cfg'
    export DATABASE_URL='postgresql://localhost/[DATABASE_NAME]'

