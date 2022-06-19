import unittest
from fastapi.testclient import TestClient
import sys
sys.path.append("..")
from main import app


client = TestClient(app)

class TestAPIMethods(unittest.TestCase):
    def test_ner_extract(self):
        global client
        sentence = "I am Hamza".replace(" ","%20")
        response = client.get(f"/ner_extract/{sentence}")

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),{"Hamza": "PERSON"})
    
if __name__ == '__main__':
    unittest.main()
