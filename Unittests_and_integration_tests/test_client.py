#!/usr/bin/env python3
"""
Tests the 'client.py' module, found in this file.
"""
import unittest
from fixtures import TEST_PAYLOAD
import client
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from typing import Dict

TEST_ORG_NAME = "google"
ORG_GET_JSON_OUTPUT = TEST_PAYLOAD[0][0]
ORG_OUTPUT = ORG_GET_JSON_OUTPUT
PUBLIC_REPOS_URL_OUTPUT = ORG_OUTPUT["repos_url"]
REPOS_PAYLOAD_GET_JSON_OUTPUT = TEST_PAYLOAD[0][1]
PUBLIC_REPOS_OUTPUT = TEST_PAYLOAD[0][-2]
APACHE2_LICENSE = "apache-2.0"
PUBLIC_REPOS_APACHE2_OUTPUT = TEST_PAYLOAD[0][-1]


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests the <client.GithubOrgClient> class.
    """
    ORG_GET_JSON_OUTPUT = TEST_PAYLOAD[0][1][0]["owner"]
    ORG_OUTPUT = ORG_GET_JSON_OUTPUT
    PUBLIC_REPOS_URL_OUTPUT = ORG_OUTPUT["repos_url"]
    REPOS_PAYLOAD_GET_JSON_OUTPUT = TEST_PAYLOAD[0][1]

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json", new=Mock(return_value=ORG_GET_JSON_OUTPUT))
    def test_org(self, org: str) -> None:
        """
        Using 'google' and 'abc' as the 'org' argument,
        this method creates a new <gh_client = GutHubOrgClient(<org>)>
        instance, and accesses its 'org' property twice.

        <gh_client.org> should return
        <client.get_json(client.GithubOrgClient.ORG_URL.format(org=org))>,
        and should also be memoized, using
        @<client.memoize>.

        So, this method mocks 'client.get_json' to just return the
        'self.ORG_OUTPUT', and asserts that when accessing
        <gh_client.org> twice, 'client.get_json' was only
        called once, since it's memoized.

        And asserts that <gh_client.org> returns
        <self.ORG_OUTPUT>.

        (<client.get_json> and <client.memoize>'s definitions
        are found in <utils.py>)
        """
        gh_client = client.GithubOrgClient(org)

        # print(client.get_json, gh_client._org_name, type(gh_client.org))

        self.assertEqual(gh_client.org, self.ORG_GET_JSON_OUTPUT)

        client.get_json.assert_called_once_with(
            client.GithubOrgClient.ORG_URL.format(org=org)
        )

        self.assertEqual(gh_client.org, self.ORG_GET_JSON_OUTPUT)

        client.get_json.assert_called_once_with(
            client.GithubOrgClient.ORG_URL.format(org=org)
        )

    def test_public_repos_url(self) -> None:
        """
        Makes <GH_CLIENT = client.GithubOrgClient(TEST_ORG_NAME)>,
        then tests that the property
        <GH_CLIENT._public_repos_url>
        returns <GH_CLIENT.org["repos_url"].

        Mocks the <GH_CLIENT.org> property to return
        <ORG_OUTPUT>.
        """
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock(
                return_value=self.ORG_OUTPUT
            )
        ):
            GH_CLIENT = client.GithubOrgClient(TEST_ORG_NAME)

            self.assertEqual(
                GH_CLIENT._public_repos_url,
                self.PUBLIC_REPOS_URL_OUTPUT
            )

    @patch(
        "client.get_json",
        new=Mock(
            return_value=REPOS_PAYLOAD_GET_JSON_OUTPUT
        )
    )
    def test_public_repos(self) -> None:
        """
        While mocking
        client.get_json(...) -> [
            {"name": "repo0"}, {"name": "repo1"}, {"name": "repo2"}
        ],

        this method makes <GH_CLIENT = client.GithubOrgClient(TEST_ORG_NAME)>,
        and tests that <GH_CLIENT.public_repos(APACHE2_LICENSE)>
        returns ["repo0", "repo1", "repo2"].

        Assuming that <<instance>.public_repos(APACHE2_LICENSE)> calls
        <<instance>.repos_payload()>.

        <instance>.repos_payload uses <instance>._public_repos_url,
        which has been mocked, so it doesn't call <client.get_json>.

        This means that <client.get_json> should only be called once.
        """
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock(
                return_value=self.PUBLIC_REPOS_URL_OUTPUT
            )
        ):
            GH_CLIENT = client.GithubOrgClient(TEST_ORG_NAME)

            self.assertEqual(
                GH_CLIENT.public_repos(APACHE2_LICENSE),
                PUBLIC_REPOS_APACHE2_OUTPUT
            )

            client.get_json.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False)
        ]
    )
    def test_has_license(self,
                         repo: Dict[str, Dict],
                         license_key: str,
                         expected: bool) -> None:
        """
        Tests that:

        client.GithubOrgClient.has_license(
            {"license": {"key": "my_license"}},
            "my_license"
        ) -> True
        client.GithubOrgClient.has_license(
            {"license": {"key": "other_license"}},
            "my_license"
        ) -> False
        """
        self.assertEqual(
            client.GithubOrgClient.has_license(repo, license_key),
            expected
        )

    def test_public_repos(self):
        """
        Tests that <client.GithubOrgClient("google").public_repos()>
        is a superset of
        <PUBLIC_REPOS_OUTPUT>.
        """
        GH_CLIENT = client.GithubOrgClient("google")

        self.assertTrue(
            set(GH_CLIENT.public_repos()).issuperset(
                PUBLIC_REPOS_OUTPUT
            )
        )

    def test_public_repos_with_license(self):
        """
        Tests that <client.GithubOrgClient("google").public_repos(
            APACHE2_LICENSE
        )>
        is a superset of
        <PUBLIC_REPOS_APACHE2_OUTPUT>.
        """
        GH_CLIENT = client.GithubOrgClient("google")

        self.assertTrue(
            set(GH_CLIENT.public_repos(APACHE2_LICENSE)).issuperset(
                PUBLIC_REPOS_APACHE2_OUTPUT
            )
        )


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [(
        ORG_GET_JSON_OUTPUT,
        PUBLIC_REPOS_URL_OUTPUT,
        REPOS_PAYLOAD_GET_JSON_OUTPUT,
        PUBLIC_REPOS_APACHE2_OUTPUT
    )]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Tests the <client.GithubOrgClient.public_repos> method,
    in integration, by only mocking external requests.

    All requests are done with <utils.requests.get>.
    """
    @classmethod
    def setUpClass(cls) -> None:
        ORG_REQUEST_URL = client.GithubOrgClient.ORG_URL.format(
            org=TEST_ORG_NAME
        )
        """
        What the request URL produced by the
        <GithubOrgClient.org>, to <utils.requests.get>,
        should be
        """
        REPOS_PAYLOAD_REQUEST_URL = PUBLIC_REPOS_URL_OUTPUT

        def mocked_requests_get(url: str):
            json_output = None

            if url == ORG_REQUEST_URL:
                json_output = ORG_GET_JSON_OUTPUT
            elif url == REPOS_PAYLOAD_REQUEST_URL:
                json_output = REPOS_PAYLOAD_GET_JSON_OUTPUT
            else:
                raise ValueError(f"Unexpected url: {url}")

            return Mock(json=Mock(return_value=json_output))

        cls.get_patcher = patch(
            "requests.get",
            new=Mock(side_effect=mocked_requests_get)
        )
        cls.get_patcher.start()

    def test_public_repos(self):
        """
        Tests that <GH_CLIENT.public_repos(APACHE2_LICENSE)>
        returns the expected output, which should be
        <PUBLIC_REPOS_APACHE2_OUTPUT>,

        while only mocking <client.get_json> calls.
        """
        GH_CLIENT = client.GithubOrgClient(TEST_ORG_NAME)

        # Test the 'org' method first.
        GH_CLIENT_ORG = GH_CLIENT.org
        self.assertIn("repos_url", GH_CLIENT_ORG)

        self.assertEqual(
            GH_CLIENT.public_repos(APACHE2_LICENSE),
            PUBLIC_REPOS_APACHE2_OUTPUT
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.get_patcher.stop()
