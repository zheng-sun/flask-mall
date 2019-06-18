from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import Flask
import config

from exts import db
import polls.apps as poll_app

# 实例化
app = Flask(__name__)
manager = Manager(app)

for item in config.APP_ITEM:
    __import__(item)

#poll_app.init_app(app)
#poll_app.init_command(manager)

#manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
