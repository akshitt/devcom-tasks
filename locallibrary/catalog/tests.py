from django.test import TestCase
from models import Book

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Book.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')


    def test_first_name_max_length(self):
        author = Book.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)


# Create your tests here.
