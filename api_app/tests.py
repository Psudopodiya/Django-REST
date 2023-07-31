from django.test import TestCase, Client
from rest_framework import status
from .models import Food
from .serializer import FoodSerializer

class FoodViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_food(self):
        # Create some food items in the database for testing
        Food.objects.create(name='Pizza', description='Delicious pizza')
        Food.objects.create(name='Burger', description='Tasty burger')

        # Send a GET request to the view
        response = self.client.get('/api/getFood/')  # Use the URL directly

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response data contains the expected food items
        expected_data = FoodSerializer(Food.objects.all(), many=True).data
        self.assertEqual(response.data, expected_data)

    def test_post_food(self):
        # Define the data to be sent in the POST request
        data = {
            'name': 'Sushi',
            'description': 'Delicious sushi rolls'
        }

        # Send a POST request to the view with the data and follow redirects
        response = self.client.post('/api/postFood/', data, follow=True)

        # Check if the response status code is 200 OK (after the redirect)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the food item was created in the database
        self.assertEqual(Food.objects.count(), 1)

        # Check if the created food item matches the sent data
        created_food = Food.objects.first()
        self.assertEqual(created_food.name, data['name'])
        self.assertEqual(created_food.description, data['description'])