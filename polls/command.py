from flask_script import Manager

PollsManager = Manager()

@PollsManager.command
def init():
    return 'init_app_command init'