import psycopg2
from psycopg2.extras import DictCursor


class Database:
    def __init__(self, db_url):
        self.connection = psycopg2.connect(db_url, sslmode='require')
        self.cursor = self.connection.cursor(cursor_factory=DictCursor)

    def get_news(self, url):
        with self.connection:
            self.cursor.execute('SELECT url FROM news WHERE url=%s', (url, ))
            result = self.cursor.fetchone()
            return bool(result)

    def add_news(self, title, url):
        with self.connection:
            return self.cursor.execute('INSERT INTO news(title, url) VALUES(%s, %s)', (title, url))

    def close(self):
        self.connection.close()
