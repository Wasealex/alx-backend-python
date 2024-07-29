#!/usr/bin/env python3
"""unittests using nested maps.
"""

from typing import Dict
import unittest
from unittest.mock import MagicMock, PropertyMock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class
    """
    @parameterized.expand([
        ("google",  {'login': "google"}),
        ("abc",  {'login': "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self,
                 org_name: str,
                 response: Dict,
                 mock_function: MagicMock) -> None:
        """Test org method of GithubOrgClient
        Args:
            org_name (str): org name
            response (Dict): response
            mock_function (MagicMock): mock function
        """
        client = GithubOrgClient(org_name)
        client.org()
        mock_function.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
            )

    def test_public_repos_url(self) -> None:
        """method to unit-test GithubOrgClient._public_repos_url"""
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_function: MagicMock) -> None:
        """Test public_repos method of GithubOrgClient
        Args:
            mock_function (MagicMock): mock function
        """
        mock_function.return_value = [
            {"name": "google"},
            {"name": "abc"},
        ]
        url_test = "https://api.github.com/users/google/repos"
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = url_test
            client = GithubOrgClient("google")
            response = client.public_repos()
            self.assertEqual(response, ["google", "abc"])
            mock_function.assert_called_once_with(url_test)

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Tests the `has_license` method."""
        gh_org_client = GithubOrgClient("google")
        client_has_licence = gh_org_client.has_license(repo, key)
        self.assertEqual(client_has_licence, expected)


if __name__ == '__main__':
    unittest.main()
