from django.test import TestCase


class TestSite(TestCase):
    def test_index_page(self):
        self.assertEquals(self.client.get('').status_code, 200)
    def test_admin_page(self):
            self.assertEquals(self.client.get('admin/').status_code, 200)
