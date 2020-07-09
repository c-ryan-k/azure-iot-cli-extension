# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import pytest
import random
import json
import os

from io import open
from os.path import exists
from . import PNPLiveScenarioTest
from azext_iot.common.utility import read_file_content
from azext_iot.common.embedded_cli import EmbeddedCLI
from azext_iot.pnp.common import RoleIdentifier

_interface_payload = "test_pnp_create_payload_interface.json"
_capability_model_payload = "test_pnp_create_payload_model.json"


@pytest.mark.usefixtures("set_cwd")
class TestPnPModelLifecycle(PNPLiveScenarioTest):
    def __init__(self, _):
        super(TestPnPModelLifecycle, self).__init__(_)
        account_settings = EmbeddedCLI().invoke("account show").as_json()["user"]
        repo_id = EmbeddedCLI().invoke("iot pnp repo list").as_json()[0]["tenantId"]
        self.kwargs.update(
            {
                "model": "test_model_definition.json",
                "user_id": account_settings["name"],
                "user_type": account_settings["type"],
                "repo_id": repo_id,
            }
        )

    def setUp(self):
        if self._testMethodName == "test_model_lifecycle":
            # RBAC for model integration tests (create, show, publish models in tenant)

            EmbeddedCLI().invoke(
                "iot pnp role-assignment create --resource-id {} --resource-type Tenant --subject-id {} --subject-type {} --role ModelsCreator".format(
                    self.kwargs["repo_id"],
                    self.kwargs["user_id"],
                    self.kwargs["user_type"],
                )
            )

            EmbeddedCLI().invoke(
                "iot pnp role-assignment create --resource-id {} --resource-type Tenant --subject-id {} --subject-type {} --role ModelsPublisher".format(
                    self.kwargs["repo_id"],
                    self.kwargs["user_id"],
                    self.kwargs["user_type"],
                )
            )

            model = str(read_file_content(_capability_model_payload))
            _model_id = self._generate_model_id(json.loads(model)["@id"])
            self.kwargs.update({"model_id": _model_id})
            model_newContent = model.replace(
                json.loads(model)["@id"], self.kwargs["model_id"]
            )
            model_newContent = model_newContent.replace("\n", "")

            fo = open(self.kwargs["model"], "w+", encoding="utf-8")
            fo.write(model_newContent)
            fo.close()

    def tearDown(self):
        if exists(self.kwargs["model"]):
            os.remove(self.kwargs["model"])

        if self._testMethodName == "test_model_lifecycle":
            # RBAC for model integration tests (create, show, publish models in tenant)

            EmbeddedCLI().invoke(
                "iot pnp role-assignment delete --resource-id {} --resource-type Tenant --subject-id {} --role ModelsCreator".format(
                    self.kwargs["repo_id"], self.kwargs["user_id"],
                )
            )

            EmbeddedCLI().invoke(
                "iot pnp role-assignment delete --resource-id {} --resource-type Tenant --subject-id {} --role ModelsPublisher".format(
                    self.kwargs["repo_id"], self.kwargs["user_id"],
                )
            )

    def _generate_model_id(self, model_id):
        from datetime import datetime

        now = datetime.now()
        date_str = now.strftime("test%m%d%H")
        time_str = now.strftime("%M").strip("0")
        return "{}:{};{}".format(model_id, date_str, time_str)

    def test_model_lifecycle(self):

        # # Error: Invalid model definition file
        self.cmd(
            "iot pnp model create --model ''", expect_failure=True,
        )

        # Error: wrong path of model definition
        self.cmd(
            "iot pnp model create --model model.json", expect_failure=True,
        )

        # Success: Create new model
        created = self.cmd("iot pnp model create --model {model}",).get_output_in_json()
        assert created["@id"] == self.kwargs["model_id"]

        # Checking the model list
        self.cmd(
            "iot pnp model list",
            checks=[
                self.greater_than("length([*])", 0),
                self.exists("[?modelId==`{}`]".format(self.kwargs["model_id"])),
            ],
        )

        # Get model
        model = self.cmd("iot pnp model show -m {model_id}").get_output_in_json()
        assert json.dumps(model)
        assert model["@id"] == self.kwargs["model_id"]

        # Publish model
        published = self.cmd(
            "iot pnp model publish -m {model_id} --yes"
        ).get_output_in_json()
        assert json.dumps(published)
        assert published["@id"] == self.kwargs["model_id"]

        # Checking the model list for published model
        self.cmd(
            "iot pnp model list -q {} --state {}".format(
                self.kwargs["model_id"], "Listed"
            ),
            checks=[
                self.greater_than("length([*])", 0),
                self.exists("[?modelId==`{}`]".format(self.kwargs["model_id"])),
            ],
        )


class TestPNPRepo(PNPLiveScenarioTest):
    def __init__(self, test_case):
        account = EmbeddedCLI().invoke("account show").as_json()
        self.user_id = account["user"]["name"]
        self.user_type = account["user"]["type"]
        super(TestPNPRepo, self).__init__(test_case)

    @pytest.mark.skipif(True, reason="Create not functional at the moment")
    def test_repo_create(self):

        # create repo

        repo = self.cmd("iot pnp repo create").get_output_in_json()

        repo_id = repo["tenantId"]

        # list repos

        repos = self.cmd("az iot pnp repo list").get_output_in_json()

        assert len(repos) == 1
        assert repos[0]["tenantId"] == repo_id

        # get role assignments for repo, should only be one (tenant admin)

        role_assignments = self.cmd(
            "az iot pnp role-assignment list --resource-id {0} --resource-type Tenant".format(
                repo_id
            )
        ).get_output_in_json()

        assert len(role_assignments) == 1
        assert role_assignments[0]["subjectMetadata"]["subjectId"] == self.user_id
        assert (
            role_assignments[0]["subject"]["role"] == RoleIdentifier.tenantAdmin.value
        )

    def test_repo_rbac(self):

        # get repo

        repos = self.cmd("az iot pnp repo list").get_output_in_json()

        repo_id = repos[0]["tenantId"]

        # add role assignment for repo (tenant)
        new_role = RoleIdentifier.modelsCreator.value
        self.cmd(
            "az iot pnp role-assignment create --resource-id {0} --resource-type Tenant "
            "--subject-id {1} --subject-type {2} --role {3}".format(
                repo_id, self.user_id, self.user_type, new_role
            )
        )

        # get newest role assignments for user

        role_assignments = self.cmd(
            "az iot pnp role-assignment list --resource-id {0} --resource-type Tenant --subject-id {1}".format(
                repo_id, self.user_id
            )
        ).get_output_in_json()

        # ensure our new role exists

        assert (
            len(
                [
                    role
                    for role in role_assignments
                    if role["subjectMetadata"]["subjectId"] == self.user_id
                    and role["subject"]["role"] == new_role
                ]
            )
            == 1
        )

        # delete role assignment

        self.cmd(
            "az iot pnp role-assignment delete --resource-id {0} --resource-type Tenant --role {1} --subject {2}".format(
                repo_id, new_role, self.user_id
            )
        )

        # get assignments again

        role_assignments = self.cmd(
            "az iot pnp role-assignment list --resource-id {0} --resource-type Tenant --subject-id {1}".format(
                repo_id, self.user_id
            )
        ).get_output_in_json()

        # ensure our new role does not exist
        assert (
            len(
                [
                    role
                    for role in role_assignments
                    if role["subjectMetadata"]["subjectId"] == self.user_id
                    and role["subject"]["role"] == new_role
                ]
            )
            == 0
        )
