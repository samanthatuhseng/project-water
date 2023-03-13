# test_db.py
import unittest
from peewee import *
from app import TimelinePost

MODELS = [TimelinePost]

# use an in-memory SQLite for tests.
test_db = SqliteDatabase(':memory:')

class TimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection...but a good practice all the same.
        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()

        # If we wanted, we could re-bind the models to their original
        # database here. But for tests this is probably not necessary.

    
    
    def test_timeline_post(self):
        #create 2 timeline posts
        first_post = TimelinePost.create(name='Nora Chamseddin',
email='nchamseddin@gmail.com', content='Hello world, I\'m John!')

        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe',
email='jame@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2
#TODO: Get timeline posts and assert that they are correct 
# Get timeline posts
        posts = TimelinePost.select()
        post_list = list(posts)

    # Assert that the posts are correct
        self.assertEqual(len(post_list), 2)
        self.assertEqual(post_list[0].name, 'Nora Chamseddin')
        self.assertEqual(post_list[0].email, 'nchamseddin@gmail.com')
        self.assertEqual(post_list[0].content, 'Hello world, I\'m John!')
        self.assertEqual(post_list[1].name, 'Jane Doe')
        self.assertEqual(post_list[1].email, 'jame@example.com')
        self.assertEqual(post_list[1].content, 'Hello world, I\'m Jane!')





