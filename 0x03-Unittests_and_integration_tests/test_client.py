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


if __name__ == '__main__':
    unittest.main()
