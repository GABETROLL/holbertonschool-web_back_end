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
        Makes <GH_CLIENT = client.GithubOrgClient("...")>,
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
            GH_CLIENT = client.GithubOrgClient("...")

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

        this method makes <GH_CLIENT = client.GithubOrgClient()>,
        and tests that <client.GithubOrgClient().public_repos()>
        returns ["repo0", "repo1", "repo2"].

        Assuming that <<instance>.public_repos()> calls
        <<instance>.repos_payload()>"""
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock(
                return_value=self.PUBLIC_REPOS_URL_OUTPUT
            )
        ):
            GH_CLIENT = client.GithubOrgClient("...")

            self.assertEqual(
                GH_CLIENT.public_repos("other"),
                ["ios-webkit-debug-proxy", "build-debian-cloud"]
            )

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False)
        ]
    )
    def test_has_license(self,
        repo: Dict[str, Dict],
        license_key: str,
        expected: bool
    ) -> None:
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


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [
        (TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1], TEST_PAYLOAD[0][1], TEST_PAYLOAD[0][2])
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.get_patcher = patch(
            "reuqests.get",
            side_effect=Mock(
                json=Mock(return_value=TEST_PAYLOAD)
            )
        )

    def test_public_repos(self):
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.get_patcher.stop()
