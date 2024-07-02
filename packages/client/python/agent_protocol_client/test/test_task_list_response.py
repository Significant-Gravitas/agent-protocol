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

from agent_protocol_client.models.task_list_response import TaskListResponse


class TestTaskListResponse(unittest.TestCase):
    """TaskListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaskListResponse:
        """Test TaskListResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TaskListResponse`
        """
        model = TaskListResponse()
        if include_optional:
            return TaskListResponse(
                tasks = [
                    null
                    ],
                pagination = agent_protocol_client.models.pagination.Pagination(
                    total_items = 42, 
                    total_pages = 97, 
                    current_page = 1, 
                    page_size = 25, )
            )
        else:
            return TaskListResponse(
                tasks = [
                    null
                    ],
                pagination = agent_protocol_client.models.pagination.Pagination(
                    total_items = 42, 
                    total_pages = 97, 
                    current_page = 1, 
                    page_size = 25, ),
        )
        """

    def testTaskListResponse(self):
        """Test TaskListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
