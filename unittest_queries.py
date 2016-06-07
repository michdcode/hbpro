from unittest import TestCase, main
from queries import *
from server import app
from model import *
from flask import Flask, request, session
# to test:
# python unittest_queries.py
# coverage
# coverage run --source=. --omit=env/* unittest_queries.py
# coverage report -m > testresults.txt
# subl testresults.txt
# coverage html
# cd htmlcov/
# open index.html


class DatabaseTests(TestCase):
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
        """General Test to make sure server & database are connected & working."""

        self.assertEqual(1, 1)

    def test_checkin_user(self):
        """Tests checkin_user function."""

        db_user = checkin_user("123")
        self.assertIsNotNone(db_user)
        self.assertEqual(db_user.name, "jane")
        self.assertIsNotNone(db_user.getaways)
        self.assertEqual(len(db_user.getaways), 1)
        db_user2 = checkin_user("456")
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

    def test_save_current_getaway(self):
        """Tests save_current_getaway function."""

        db_save_current_getaway = save_current_getaway("123", 3326, "http://www.picture.com/puppy",
                                                       "San Francisco", "happy")
        self.assertIsNotNone(db_save_current_getaway.getaway_id)
        self.assertIsNotNone(db_save_current_getaway.created)
        self.assertEqual(db_save_current_getaway.location.loc_name, "San Francisco")
        self.assertIs(db_save_current_getaway.getaway_id, 2)

    def test_check_new_user(self):
        """Tests check_new_user function."""

        db_check_new_user = check_new_user("123", "jane")
        self.assertFalse(db_check_new_user)
        db_check_new_user = check_new_user("456", "mary")
        self.assertIsNotNone(db_check_new_user.user_id)

    def test_prior_getaways(self):
        """Tests prior_getaways function."""

        db_prior_getaways = prior_getaways("123")
        self.assertIsNotNone(db_prior_getaways)

    def test_get_getaway(self):
        """Tests get_getaway function"""

        db_getaway = get_getaway(1)
        self.assertIsNotNone(db_getaway)


class ServerTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = "JMD"
        self.client = app.test_client()

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1
                sess['user'] = "{u'user_id': u'auth0|123', u'name': u'jane'}"
                sess['lurl'] = "http://www.picture.com/puppy"
                sess['locname'] = "San Francisco"
                sess['track_id'] = 3326
                sess['song_name'] = "happy"
                sess['name'] = "jane"
                sess['profile'] = "{u'user_id': u'auth0|123', u'name': u'jane',}"

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_generic(self):
        """General Test to make sure server is connected & working."""

        self.assertEqual(1, 1)

    def test_homepage_status(self):
        """Tests that server is running for index page."""

        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)

    def test_homepage_contents(self):
        """Tests that home.html is rendering at index location."""

        result = self.client.get('/')
        self.assertIn('<title>One Minute Getaway</title>', result.data)

    def test_play_route(self):
        """Tests play route."""

        result = self.client.get('/play')
        self.assertEqual(result.status_code, 200)
        self.assertIn('input type="hidden" name="track_id" id="track_id" value="3326"', result.data)

    def test_select_location_route(self):

        result = self.client.get('/select_loc')
        self.assertEqual(result.status_code, 200)
        self.assertIn('<p id="locwelcome">Now it\'s time to pick a location! </p>', result.data)


if __name__ == "__main__":
    main()
