import unittest
from django.test import TestCase
from .forms import MessageForm


class TestForm(unittest.TestCase):

    def test_visitor_question_required(self):
        form = MessageForm({'question': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('question', form.errors.keys())
        self.assertEqual(form.errors['question'][0], 'This field is required.')

    def test_if_fields_in_form(self):
        form = MessageForm()
        self.assertEqual(form.Meta.fields, ('name', 'question', 'email'))

    def test_if_labels_in_form(self):
        form = MessageForm()
        self.assertEqual(form.Meta.labels, {
            'name': 'Name',
            'question': 'Question or feedback',
            'email': 'Email'
        })


if __name__ == '__main__':
    unittest.main()
