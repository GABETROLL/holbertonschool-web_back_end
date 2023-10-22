from test_client import *


class TestReal(unittest.TestCase):
    """
    Tests <client.GithubOrgClient> without mocking external requests.
    """
    @classmethod
    def setUpClass(cls):
        cls.gh_client = client.GithubOrgClient("google")

    def test_fields(self):
        """The fields of the <gh_client> should be
        ORG_URL = "https://api.github.com/orgs/{org}"
        and
        _org_name = "google".
        """
        self.assertEqual(
            self.gh_client.ORG_URL,
            "https://api.github.com/orgs/{org}"
        )
        self.assertEqual(
            self.gh_client._org_name,
            "google"
        )

    def test_org(self):
        """
        The output of <self.gh_client.org>
        should be a superset of <ORG_OUTPUT>.
        """
        self.assertDictContainsSubset(
            ORG_OUTPUT,
            self.gh_client.org
        )

    def test_public_repos_url(self):
        """
        The output of <self.gh_client._public_repos_url>
        should be <PUBLIC_REPOS_URL_OUTPUT>.
        """
        self.assertEqual(
            self.gh_client._public_repos_url,
            PUBLIC_REPOS_URL_OUTPUT
        )

    """def test_repos_payload(self):
        self.assertTrue(
            set(self.gh_client.repos_payload).issuperset(
                REPOS_PAYLOAD_GET_JSON_OUTPUT
            )
        )"""

    def test_public_repos(self):
        """
        The output of <self.gh_client.public_repos(APACHE2_LICENSE)>
        should be a superset of <PUBLIC_REPOS_APACHE2_OUTPUT>.
        """
        self.assertTrue(
            set(self.gh_client.public_repos(APACHE2_LICENSE)).issuperset(
                PUBLIC_REPOS_APACHE2_OUTPUT
            )
        )
