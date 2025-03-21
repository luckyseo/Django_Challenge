from django.test import TestCase
from rest_framework.test import APITestCase
from . import models
from users import models as userModel
# Create your tests here.

#run by python manage.py test
"""
/api/v1/tweets: Test GET and POST methods
/api/v1/tweets/<int:pk>: Test GET, PUT and DELETE methods
"""
class TestTweets(APITestCase):
    #should start with test_
    
    PAYLOAD= "tweet payload"

    URL= "/api/v1/tweets/"
           

    def setUp(self):
        self.user= userModel.User.objects.create(first_name = "test_fname")
        models.Tweet.objects.create(
            user= self.user,
            payload=self.PAYLOAD,
        )

    def test_create_tweets(self):
        response = self.client.get(self.URL)
        data = response.json()
        self.assertIsInstance(data,list)
        self.assertEqual(len(data),1)
        self.assertEqual(data[0]["payload"], self.PAYLOAD,)
    
        post_user = userModel.User.objects.create(username="postuser")
        response= self.client.post(self.URL, data = {"user":post_user.id,"payload":self.PAYLOAD})
        data = response.json()

        self.assertEqual(response.status_code, 200, "error not 200")

class TestTweetsDetails(APITestCase):
    NAME = "test_fname"
    PAYLOAD  = "testDetailTest DES"
    URL= "/api/v1/tweets/1"
    def setUp(self):
        USER = userModel.User.objects.create(first_name=self.NAME)
        models.Tweet.objects.create(
            user = USER,
            payload = self.PAYLOAD
        )
    def test_get_tweet(self):
        response= self.client.get("/api/v1/tweets/1")
        self.assertEqual(response.status_code,200)

        data = response.json()
        print(data)
        self.assertEqual(data["tweets"]["id"],1)

    def test_put(self):
        response = self.client.put(
            self.URL,
            tweet = models.Tweet.objects.get(pk=1),
            data = {
                "payload":"revised"
            }, partial =True
        )
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.client.delete(self.URL)
        self.assertEqual(response.status_code, 200)