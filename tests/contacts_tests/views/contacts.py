from django.test import TestCase, Client
from django.urls import reverse

from audi_our_love_shop_project.contacts.models import ContactsModel


class ContactsTests(TestCase):
    VALID_CONTACT_FORM = {
        'first_name': 'Gosho',
        'last_name': 'Goshov',
        'email': 'goshov@example.com',
        'content': 'Test',
        'reason': 'Other',
    }

    def test_about_correct_url(self):
        client = Client()
        response = client.get(reverse('contacts'))
        self.assertEqual(response.status_code, 200)

    def test_about_correct_template(self):
        client = Client()
        response = client.get(reverse('contacts'))
        self.assertTemplateUsed(response, 'contacts/contacts.html')

    def test_filling_the_contacts_form_with_proper_data_expect_success(self):
        client = Client()
        response = client.post(reverse('contacts'), self.VALID_CONTACT_FORM)
        contact = ContactsModel.objects.get(id=1)
        self.assertEqual(ContactsModel.objects.count(), 1)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        # asserts for the contact
        self.assertEqual(contact.first_name, self.VALID_CONTACT_FORM['first_name'])
        self.assertEqual(contact.last_name, self.VALID_CONTACT_FORM['last_name'])
        self.assertEqual(contact.email, self.VALID_CONTACT_FORM['email'])
        self.assertEqual(contact.content, self.VALID_CONTACT_FORM['content'])
        self.assertEqual(contact.reason, self.VALID_CONTACT_FORM['reason'])

    def test_filling_the_contacts_form_with_invalid_data_expect_failure(self):
        INVALID_DATA = {
            'first_name': 'Gosho',
            'last_name': 'Goshov',
            'email': 'wrong email',
            'content': 'Test',
            'reason': 'Other',
        }
        client = Client()
        client.post(reverse('contacts'), INVALID_DATA)
        self.assertEqual(ContactsModel.objects.count(), 0)


