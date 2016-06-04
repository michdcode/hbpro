from unittest import TestCase, main
from queries import *
from server import app
from model import *


class FlaskTests(TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'JMD'
#        with app as c:
#            with c.session_transaction() as sess:
#                sess['user_id'] = "123"
        print "hello"
        print connect_to_db
        connect_to_db(app, "postgresql:///testdb")
        db.create_all()
        example_data()



    def tearDown(self):
        db.session.close()
        db.drop_all()

    def test1(self):
        self.assertEqual(1, 1)

    def testusercheckin(self):
        db_user = checkin_user({"user_id": "bla|123"})
        self.assertIsNotNone(db_user)
        self.assertEqual(db_user.name, "jane")
        self.assertIsNotNone(db_user.getaways)
        self.assertEqual(len(db_user.getaways), 1)

        db_user2 = checkin_user({"user_id": "bla|0000"})
        self.assertIsNone(db_user2)

if __name__ == "__main__":
    main()
