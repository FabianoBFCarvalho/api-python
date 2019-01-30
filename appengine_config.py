import os
import google
from google.appengine.ext import vendor

lib_directory = os.path.dirname(__file__) + '/lib'
google.__path__ = [os.path.join(lib_directory, 'google')] + google.__path__
vendor.add(lib_directory)
vendor.add('lib')

import platform


def patch(module):
    def decorate(func):
        setattr(module, func.func_name, func)
        return func

    return decorate


@patch(platform)
def platform():
    return 'AppEngine'


def webapp_add_wsgi_middleware(app):
    from google.appengine.ext.appstats import recording
    app = recording.appstats_wsgi_middleware(app)
    return app