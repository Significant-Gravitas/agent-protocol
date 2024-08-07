# coding: utf-8

"""
Agent Protocol

Specification of the API protocol for communication with an agent.

The version of the OpenAPI document: v1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import datetime
import unittest

from agent_protocol_client.models.task_artifacts_list_response import (
    TaskArtifactsListResponse,
)


class TestTaskArtifactsListResponse(unittest.TestCase):
    """TaskArtifactsListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaskArtifactsListResponse:
        """Test TaskArtifactsListResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TaskArtifactsListResponse`
        """
        model = TaskArtifactsListResponse()
        if include_optional:
            return TaskArtifactsListResponse(
                artifacts = [
                    agent_protocol_client.models.artifact.Artifact(
                        artifact_id = 'b225e278-8b4c-4f99-a696-8facf19f0e56', 
                        agent_created = False, 
                        file_name = 'main.py', 
                        relative_path = 'python/code/', )
                    ],
                pagination = agent_protocol_client.models.pagination.Pagination(
                    total_items = 42, 
                    total_pages = 97, 
                    current_page = 1, 
                    page_size = 25, )
            )
        else:
            return TaskArtifactsListResponse(
                artifacts = [
                    agent_protocol_client.models.artifact.Artifact(
                        artifact_id = 'b225e278-8b4c-4f99-a696-8facf19f0e56', 
                        agent_created = False, 
                        file_name = 'main.py', 
                        relative_path = 'python/code/', )
                    ],
                pagination = agent_protocol_client.models.pagination.Pagination(
                    total_items = 42, 
                    total_pages = 97, 
                    current_page = 1, 
                    page_size = 25, ),
        )
        """

    def testTaskArtifactsListResponse(self):
        """Test TaskArtifactsListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
