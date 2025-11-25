import unittest
from app import app

class TestAppSmoke(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()
    
    # Complete the function below to test a success in running the application
    def test_prediction_route_success(self):
        response = self.client.get('/')
        # App should respond OK
        self.assertEqual(response.status_code, 200)

    # Complete the function below to test a form is rendered
    def test_get_form(self):
        response = self.client.get('/')
        html = response.data.decode('utf-8').lower()
        # Page should contain an HTML form and one of the input fields
        self.assertIn('<form', html)
        self.assertIn('temperature', html)
 
if __name__ == '__main__':
    unittest.main()

