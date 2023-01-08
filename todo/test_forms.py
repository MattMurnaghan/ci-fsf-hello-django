from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        # test for valid form
        self.assertFalse(form.is_valid())
        # test to make sure name is in the list of keys
        self.assertIn('name', form.errors.keys())
        # test to make sure that the first string in the list of errors
        #  is confirming that the name field is required
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    # test that the only field displayed are the name and the done fields
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
