# coding: utf-8

"""
    Ours

    The Ours Server-Side REST API

    The version of the OpenAPI document: 1.0.0
    Contact: support@oursprivacy.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from oursprivacy_client.api.ours_privacy_api import OursPrivacyApi


class TestOursPrivacyApi(unittest.TestCase):
    """OursPrivacyApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OursPrivacyApi()

    def tearDown(self) -> None:
        pass

    def test_identify(self) -> None:
        """Test case for identify

        Identify Users
        """
        pass

    def test_track(self) -> None:
        """Test case for track

        Track Events
        """
        pass


if __name__ == '__main__':
    unittest.main()
