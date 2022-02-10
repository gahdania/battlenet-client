from tests.test_base import *


class TestRetailCredentialClient(TestBaseClass):
    def test_credential_client_retail(self):
        self.assertEqual(self.client.static, "static-us")
        self.assertEqual(self.client.dynamic, "dynamic-us")
        self.assertEqual(self.client.profile, "profile-us")

    def test_credential_client_vanilla(self):
        self.assertNotEqual(self.client.static, "static-classic1x-us")
        self.assertNotEqual(self.client.dynamic, "dynamic-classic1x-us")
        self.assertNotEqual(self.client.profile, "profile-classic1x-us")

    def test_credential_client_tbc(self):
        self.assertNotEqual(self.client.static, "static-classic-us")
        self.assertNotEqual(self.client.dynamic, "dynamic-classic-us")
        self.assertNotEqual(self.client.profile, "profile-classic-us")
