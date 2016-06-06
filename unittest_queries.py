from unittest import TestCase, main
from queries import *
from server import app
from model import *
from flask import Flask, request, session


class FlaskTests(TestCase):
    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = "JMD"
        connect_to_db(app, "postgresql:///testdb")
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_generic(self):
        """General Test to make sure server & database are connect & working."""

        self.assertEqual(1, 1)

    def test_checkin_user(self):
        """Tests checkin_user function."""

        db_user = checkin_user({"user_id": "bla|123"})
        self.assertIsNotNone(db_user)
        self.assertEqual(db_user.name, "jane")
        self.assertIsNotNone(db_user.getaways)
        self.assertEqual(len(db_user.getaways), 1)

        db_user2 = checkin_user({"user_id": "bla|0000"})
        self.assertIsNone(db_user2)

    def test_get_or_create_song(self):
        """Tests get_or_create_song function."""

        db_song = get_or_create_song(3326, "happy")
        self.assertIsNotNone(db_song.track_id)
        self.assertIsNotNone(db_song.song_name)
        self.assertIs(db_song.track_id, 1)
        self.assertIsNot(db_song.song_name, "yellow")
        db_song = get_or_create_song(1253, "sunshine")
        self.assertIs(db_song.track_id, 2)
        self.assertIsNotNone(db_song.song_name)

    def test_get_or_create_location(self):
        """Tests get_or_create_location function."""

        db_location = get_or_create_location("San Francisco", "http://www.picture.com/puppy")
        self.assertIsNotNone(db_location.pict_URL)
        self.assertIsNotNone(db_location.loc_name)
        self.assertEqual(db_location.loc_name, "San Francisco")
        self.assertIs(db_location.location_id, 1)
        db_location = get_or_create_location("San Diego", "http://www.signonsandiego.com")
        self.assertIs(db_location.location_id, 2)
        self.assertIsNotNone(db_location.pict_URL)
        self.assertEqual(db_location.loc_name, "San Diego")

    # def test_save_current_getaway(self):
    #     """Tests save_current_getaway function."""

    #     with app.test_request_context():
    #         with self.client as c:
    #             with c.session_transaction() as sess:
    #                 sess['user'] = "{u'user_id': u'auth0|123', u'name': u'jane'}"
    #                 sess['lurl'] = "http://www.picture.com/puppy"
    #                 sess['locname'] = "San Francisco"
    #                 sess['track_id'] = 3326
    #                 sess['song_name'] = "happy"
    #                 sess['name'] = "jane"
    #                 self.assertEqual(sess["locname"], "San Francisco")
    #                 db_getaway = save_current_getaway({"user_id": "bla|123"})
    #     #             #db_getaway = save_current_getaway(flask.sess['user']) - doesn't work either

    #     # with app.test_client() as c:
    #     #     rv = c.get('/')
    #     #     assert flask.session['user'] == "{u'user_id': u'auth0|123', u'name': u'jane'}"

    def test_homepage_status(self):
        """Tests that server is running for index page."""

        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)

    def test_homepage_contents(self):
        """Tests that home.html is rendering at index location."""

        result = self.client.get('/')
        self.assertIn('<title>One Minute Getaway</title>', result.data)

    # def test_no_song_found_contents(self):
    #     """Tests that no_song_found is rendering when applicable."""

    #     result = self.client.post('/song_process', data={'sname': 'paieut'})
    #     print result.data
    #     # self.assertIn('<title>Song Not Found</title>', result.data)

    # def test_song_problem_contents(self):



if __name__ == "__main__":
    main()
