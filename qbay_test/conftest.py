import os.path
import time
import pytest
import tempfile
import threading
from werkzeug.serving import make_server
from qbay import app

'''
This file defines what to do BEFORE running any test cases:


'''

base_url = 'http://127.0.0.1:{}'.format(8081)


class ServerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        # import necessary routes
        from qbay import controllers
        self.srv = make_server('127.0.0.1', 8081, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        print('running')
        self.srv.serve_forever()

    def shutdown(self):
        self.srv.shutdown()


@pytest.fixture(scope="session", autouse=True)
def server():
    # create a live server for testing
    # with a temporary file as database
    server = ServerThread()
    server.start()
    time.sleep(5)
    yield
    server.shutdown()
    time.sleep(2)


def pytest_sessionstart():
    '''
    Delete database file if existed. So testing can start fresh.
    '''
    print('Setting up environment..')
    db_file = 'db.sqlite'
    if os.path.exists('qbay/db.sqlite'):
        os.remove('qbay/db.sqlite')
    if os.path.exists("db.sqlite"):
        os.remove('db.sqlite')


def pytest_sessionfinish():
    '''
    Optional function called when testing is done.
    Do nothing for now
    '''
    pass
