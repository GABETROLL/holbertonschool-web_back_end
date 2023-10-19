#!/usr/bin/env python3
"""
Tests the 'client.py' module, found in this file.
"""
import unittest
from fixtures import TEST_PAYLOAD
import client
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests the <client.GithubOrgClient> class.
    """
    @patch("client.get_json", new=Mock(return_value=TEST_PAYLOAD))
    @parameterized.expand(
        [("google",), ("abc",)]
    )
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
        'TEST_PAYLOAD', and asserts that when accessing
        <gh_client.org> twice, 'client.get_json' was only
        called once, since it's memoized.

        And asserts that <gh_client.org> returns
        <TEST_PAYLOAD>.

        (<client.get_json> and <client.memoize>'s definitions
        are found in <utils.py>)
        """
        gh_client = client.GithubOrgClient(org)

        # print(client.get_json, gh_client.ORG_URL)

        self.assertEqual(gh_client.org, TEST_PAYLOAD)
        self.assertEqual(gh_client.org, TEST_PAYLOAD)

        client.get_json.assert_called_once_with(
            client.GithubOrgClient.ORG_URL.format(org=org)
        )

    def test_public_repos_url(self):
        """
        Makes <GH_CLIENT = client.GithubOrgClient("...")>,
        then tests that the property
        <GH_CLIENT._public_repos_url>
        returns <GH_CLIENT.org["repos_url"].

        Mocks the <GH_CLIENT.org> property to return
        <TEST_PAYLOAD>.
        """
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock(
                return_value=TEST_PAYLOAD[0][0]
            )
        ):
            GH_CLIENT = client.GithubOrgClient("...")

            # print(GH_CLIENT.org)

            self.assertEqual(
                GH_CLIENT._public_repos_url,
                TEST_PAYLOAD[0][0]["repos_url"]
            )

    @patch(
        "client.get_json",
        new=Mock(
            return_value=[
                {"name": "repo0"},
                {"name": "repo1"},
                {"name": "repo2"}
            ]
        )
    )
    def test_public_repos(self):
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
                return_value=TEST_PAYLOAD[0][0]["repos_url"]
            )
        ):
            GH_CLIENT = client.GithubOrgClient("...")

            self.assertEqual(
                GH_CLIENT.public_repos(),
                ["repo0", "repo1", "repo2"]
            )
