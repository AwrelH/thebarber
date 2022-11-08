import unittest
from django.test import TestCase
from .forms import CommentForm


class TestForm(unittest.TestCase):

    def test_if_field_in_form(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))


if __name__ == '__main__':
    unittest.main()
