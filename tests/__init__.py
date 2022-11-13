import os
import unittest
from app import app, Todo,db
import random

class FlaskTests(unittest.TestCase):    
    def test_createdb(self):
        self.client = app
        db.create_all()
    
    def test_get(self):
        with app.test_client() as client:
            # GET data from endpoint
            result = client.get(
                '/', follow_redirects=True
            )
            # check result from server with expected data
            self.assertEqual(result.status_code, 200)
            self.assertIn(b'Task Master', result.data)
    
    def test_post(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            sent = {'content': 'random'}
            result = client.post(
                '/',
                data=sent, follow_redirects=True
            )
            # check result from server with expected data
            self.assertEqual(result.status_code, 200)
            self.assertIn(b'random', result.data)

    def test_index(self):
        self.client = app.test_client()
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_adding_description(self):
        self.client = app.test_client()
        random_id= random.randint(0, 1000)
        data=Todo(id =random_id, content="Mock Description", status=0)
        db.session.add(data) 
        db.session.commit() 
        response = self.client.get("/") 
        assert str(random_id) in response.data.decode('utf-8')  

    def test_deleting_descriptions(self):
        self.client = app.test_client()
        random_id= random.randint(0, 1000)
        data=Todo(id =random_id, content="Mock Description II", status=0)
        db.session.add(data) 
        db.session.commit() 
        db.session.delete(data) 
        db.session.commit()

        response = self.client.get("/") 
        assert str(random_id) not in response.data.decode('utf-8')  

if __name__ == "__main__": 
    unittest.main()