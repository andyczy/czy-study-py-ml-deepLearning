import pymysql
pymysql.install_as_MySQLdb()
from flask import _app_ctx_stack, current_app


class MySQLDB(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('MYSQL_HOST', 'localhost')
        app.config.setdefault('MYSQL_USER', 'root')
        app.config.setdefault('MYSQL_PASSWORD', 'root')
        app.config.setdefault('MYSQL_DB', 'py_czy_test')
        app.config.setdefault('MYSQL_PORT', 3306)
        app.config.setdefault('MYSQL_UNIX_SOCKET', None)
        app.config.setdefault('MYSQL_CONNECT_TIMEOUT', 10)
        app.config.setdefault('MYSQL_READ_DEFAULT_FILE', None)
        app.config.setdefault('MYSQL_USE_UNICODE', True)
        app.config.setdefault('MYSQL_CHARSET', 'utf8')
        app.config.setdefault('MYSQL_SQL_MODE', None)
        app.config.setdefault('MYSQL_CURSORCLASS', None)
        app.config.setdefault('USERNAME','root')
        app.config.setdefault('PASSWORD','root')
        app.config['SECRET_KEY'] = 'nihao'

        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)

    @property
    def connect(self):
        kwargs = {}

        if current_app.config['MYSQL_HOST']:
            kwargs['host'] = current_app.config['MYSQL_HOST']

        if current_app.config['MYSQL_USER']:
            kwargs['user'] = current_app.config['MYSQL_USER']

        if current_app.config['MYSQL_PASSWORD']:
            kwargs['passwd'] = current_app.config['MYSQL_PASSWORD']

        if current_app.config['MYSQL_DB']:
            kwargs['db'] = current_app.config['MYSQL_DB']

        if current_app.config['MYSQL_PORT']:
            kwargs['port'] = current_app.config['MYSQL_PORT']

        if current_app.config['MYSQL_UNIX_SOCKET']:
            kwargs['unix_socket'] = current_app.config['MYSQL_UNIX_SOCKET']

        if current_app.config['MYSQL_CONNECT_TIMEOUT']:
            kwargs['connect_timeout'] = \
                current_app.config['MYSQL_CONNECT_TIMEOUT']

        if current_app.config['MYSQL_READ_DEFAULT_FILE']:
            kwargs['read_default_file'] = \
                current_app.config['MYSQL_READ_DEFAULT_FILE']

        if current_app.config['MYSQL_USE_UNICODE']:
            kwargs['use_unicode'] = current_app.config['MYSQL_USE_UNICODE']

        if current_app.config['MYSQL_CHARSET']:
            kwargs['charset'] = current_app.config['MYSQL_CHARSET']

        if current_app.config['MYSQL_SQL_MODE']:
            kwargs['sql_mode'] = current_app.config['MYSQL_SQL_MODE']

        if current_app.config['MYSQL_CURSORCLASS']:
            kwargs['cursorclass'] = getattr(pymysql.cursors.DictCursor, current_app.config['MYSQL_CURSORCLASS'])

        return pymysql.connect(**kwargs)

    @property
    def connection(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'mysql_db'):
                ctx.mysql_db = self.connect
            return ctx.mysql_db

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'mysql_db'):
            ctx.mysql_db.close()
 