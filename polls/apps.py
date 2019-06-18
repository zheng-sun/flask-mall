from .controller import bq
from .command import PollsManager

def init_app(app):
    app.register_blueprint(bq)

def init_command(Manager, prefix = 'polls'):
    Manager.add_command(prefix, PollsManager)




