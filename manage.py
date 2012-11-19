# manage.py

from flask.ext.script import Manager

from app import app

manager = Manager(app)

@manager.command
def migrate(action):
    from flask.ext.evolution import Evolution
    evolution = Evolution(app)
    evolution.manager(action)

if __name__ == "__main__":
    manager.run()


