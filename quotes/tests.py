from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Quote


class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='test_user', password='pass')
        test_user.save()

        test_quote = Quote.objects.create(author=test_user, theme="Inspirational", the_quote="You Got This!")
        test_quote.save()

    def test_quotes_model(self):
        quote = Quote.objects.get(id=1)
        actual_author = str(quote.author)
        actual_theme = str(quote.theme)
        actual_the_quote = str(quote.the_quote)
        self.assertEqual(actual_author, "test_user")
        self.assertEqual(actual_theme, "Inspirational")
        self.assertEqual(actual_the_quote, "You Got This!")
