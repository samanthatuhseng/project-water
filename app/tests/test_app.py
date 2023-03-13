# tests/test_app.py
import unittest
import os
os. environ [ 'TESTING' ] = 'true'

from app import app
class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        # TODO Add more tests relating to the home page
          
        assert "Welcome to the MLH Fellowship program" in html
        assert '<a href="/timeline">View timeline</a>' in html
        assert '<img src="/static/images/samantha.jpg">' in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200 
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json 
        assert len( json ["timeline_posts"]) == 0
        # TODO Add more tests relating to the /api/timeline_post GET and POST apis
        # TODO Add more tests relating to the timeline page

        response = self.client.post("/api/timeline_post", json={
        "title": "My first post",
        "content": "This is my first post on the timeline"
    })
        assert response.status_code == 201 
        assert response.is_json
        json = response.get_json()
        assert "message" in json 
        assert json["message"] == "Post created successfully"

        # test POST request with invalid data
        response = self.client.post("/api/timeline_post", json={
            "title": "My second post"
        })
        assert response.status_code == 400 
        assert response.is_json
        json = response.get_json()
        assert "error" in json 
        assert json["error"] == "Missing required field: content"

        # test that the timeline page displays existing posts
        response = self.client.get("/timeline")
        assert response.status_code == 200 
        html = response.get_data(as_text=True)
        assert "My first post" in html
        assert "This is my first post on the timeline" in html

        def test_malformed_timeline_post(self):
    # POST request missing name
            response = self. client.post("/api/timeline_post", data=
            {"email": "john@example.com",
            "content": "Hello world, I'm John!"})
            assert response.status_code == 400
            html = response. get_data(as_text=True)
            assert "Invalid name" in html
            # POST request with emptv content
            response = self.client.post("/api/timeline_post", data-
            {" name":
            "John Doe", "email": "john@example.com",
            "content": ""})
            assert response.status_code == 400
            html = response. get_data(as_text=True)
            assert "Invalid content" in html
            # POST request with malformed email
            response = self.client.post("/apt/timeline_post", data=
            {"name": "John Doe","email": "not-an-email","content": "Hello world, I'm John!"})
            assert response.status_code == 400
            html = response.get_data(as_text=True)
            assert "Invalid email" in html