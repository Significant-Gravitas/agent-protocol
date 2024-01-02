# coding: utf-8

"""
    Agent Protocol

    Specification of the API protocol for communication with an agent.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from agent_protocol_client.models.artifact import Artifact


class TestArtifact(unittest.TestCase):
    """Artifact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Artifact:
        """Test Artifact
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Artifact`
        """
        model = Artifact()
        if include_optional:
            return Artifact(
                artifact_id = 'b225e278-8b4c-4f99-a696-8facf19f0e56',
                agent_created = False,
                file_name = 'main.py',
                relative_path = 'python/code/'
            )
        else:
            return Artifact(
                artifact_id = 'b225e278-8b4c-4f99-a696-8facf19f0e56',
                agent_created = False,
                file_name = 'main.py',
        )
        """

    def testArtifact(self):
        """Test Artifact"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()