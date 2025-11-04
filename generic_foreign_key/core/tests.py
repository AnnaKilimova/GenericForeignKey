from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import ActionLog
from users.models import Profile
from blog.models import Post, Comment

User = get_user_model()


class ActionLogTests(TestCase):
    '''Test suite for the ActionLog model.

    This class verifies the core functionality of ActionLog:
    - correct creation of log entries with GenericForeignKey links;
    - integrity of relations between users, posts, comments, and profiles;
    - reverse GenericRelation behavior for connected models.

    Django's built-in TestCase automatically creates an isolated
    in-memory database for each test, ensuring test independence.
    '''

    def setUp(self):
        '''Create initial test data.'''
        self.user_1 = User.objects.create_user(username='user_1', password='1234')
        self.user_2 = User.objects.create_user(username='user_2', password='1234')
        self.profile_1 = Profile.objects.create(user=self.user_1, biography="Hi, I'm User_1!", city='Manchester',  birth_date='1995-01-12')
        self.profile_2 = Profile.objects.create(user=self.user_2, city='Liverpool')
        self.post_1 = Post.objects.create(title='First post', content="This is a test post", author=self.user_1)
        self.post_2 = Post.objects.create(title='Second post', content='Hello world',  author=self.user_2)
        self.comment_1 = Comment.objects.create( post=self.post_1, author=self.user_2, content="Nice post, User_1!")
        self.comment_2 = Comment.objects.create( post=self.post_2, author=self.user_1, content="Thanks, User_2!")


    def test_create_log(self):
        '''Test that a delete action log is created correctly and associated with the right user and object.'''
        log_post_1 = ActionLog.objects.create(action_type='create', user=self.user_1, content_object=self.post_1)
        self.assertEqual(log_post_1.content_object, self.post_1)
        self.assertEqual(log_post_1.user, self.user_1)
        self.assertEqual(log_post_1.action_type, 'create')
        
        log_comment_1 = ActionLog.objects.create(action_type='create', user=self.user_2, content_object=self.comment_1)
        self.assertEqual(log_comment_1.content_object, self.comment_1)
        self.assertEqual(log_comment_1.user, self.user_2)
        self.assertEqual(log_comment_1.action_type, 'create')
        
        log_profile_1 = ActionLog.objects.create(action_type='create', user=self.user_2, content_object=self.profile_2)
        self.assertEqual(log_profile_1.content_object, self.profile_2)
        self.assertEqual(log_profile_1.user.username, 'user_2')
        self.assertEqual(log_profile_1.action_type, 'create')

    def test_generic_relation(self):
        '''Ensure that objects can access their logs via reverse GenericRelation.'''
        log_post_1 = ActionLog.objects.create(action_type='update', user=self.user_1, content_object=self.post_1)
        self.assertIn(log_post_1, self.post_1.logs.all())
        
        log_post_2 = ActionLog.objects.create(action_type='update', user=self.user_2, content_object=self.post_2)
        self.assertIn(log_post_2, self.post_2.logs.all())
        
        log_profile_1 = ActionLog.objects.create(action_type='update', user=self.user_1, content_object=self.profile_1)
        self.assertIn(log_profile_1, self.profile_1.logs.all())

        
    def test_delete_log(self):
        log = ActionLog.objects.create(action_type='delete', user=self.user_1, content_object=self.comment_2)
        self.assertEqual(log.action_type, 'delete')
        self.assertEqual(log.user, self.user_1)
        self.assertEqual(log.content_object, self.comment_2)

    # def test_create_log_for_profile(self):
    #     '''Test creating a log linked to a profile.'''
    #     log = ActionLog.objects.create(action_type='update', user=self.user_2, content_object=self.profile)
    #     self.assertEqual(log.content_object, self.profile)
    #     self.assertEqual(log.user.username, 'user_2')
    #     self.assertEqual(log.action_type, 'update')
