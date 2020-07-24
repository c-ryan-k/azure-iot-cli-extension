# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_iot.product.shared import BadgeType
from azext_iot.product.providers.aics import AICSProvider
from azext_iot.common.utility import process_json_arg
from knack.util import CLIError

def list(cmd, test_id):
    ap = AICSProvider(cmd)
    return ap.show_test_cases(test_id=test_id)


def update(cmd, test_id, configuration_file):
    ap = AICSProvider(cmd)
    import os
    if not os.path.exists(configuration_file):
        raise CLIError("Specified configuration file does not exist")
    return ap.update_test_cases(test_id=test_id, patch=process_json_arg(configuration_file, 'configuration_file'))
