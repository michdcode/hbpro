from unittest import TestCase, main
#from queries import *
from server import app


class FlaskTests(TestCase):

    def setup(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def teardown(self):
        pass

    def test1(self):
        pass

    def test2(self):
        pass


if __name__ == "__main__":
    main()
