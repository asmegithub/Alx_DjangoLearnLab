from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.authtoken.models import Token

from .models import Book, Author
from django.contrib.auth.models import User


class TestBookViews(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        # Create a token for the user
        self.token, _ = Token.objects.get_or_create(user=self.user)
        # Authenticate the user for the test client
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.list_url = reverse('book_list')
        self.create_url = reverse('book_create')

        self.author = Author.objects.create(name='test author')
        self.book = Book.objects.create(
            title='test book',
            publication_year=2021,
            author=self.author
        )
        self.detail_url = reverse('book_detail', args=[self.book.id])
        self.update_url = reverse('book_update', args=[self.book.id])
        self.delete_url = reverse('book_delete', args=[self.book.id])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        data = {
            "title": "test book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Verify that the book was created
        # count=2 because we already have one book created in the setUp method
        self.assertEqual(Book.objects.count(), 2)
        # Verify the response data is correct
        self.assertEqual(data['title'], response.data['title'])
        self.assertEqual(data['publication_year'],
                         response.data['publication_year'])
        self.assertEqual(data['author'], response.data['author'])

    def test_retrieve_book(self):
        respoonse = self.client.get(self.detail_url)
        self.assertEqual(respoonse.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        response = self.client.patch(self.update_url, {
            'title': 'test book updated',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_ordering_books(self):
        response = self.client.get(self.list_url, {'ordering': 'title'})
        # ordering by publication year
        response2 = self.client.get(
            self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

    def test_search_books(self):
        # verify that the search functionality works
        response1 = self.client.get(self.list_url, {'search': 'test'})
        # verify by giving the publication year
        response2 = self.client.get(self.list_url, {'search': '2021'})
        # verify by giving a non-existing search term
        response3 = self.client.get(self.list_url, {'search': 'non-existing'})
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(response3.status_code, status.HTTP_200_OK)
