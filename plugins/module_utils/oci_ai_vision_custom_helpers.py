# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils


class AiVisionDocumentJobHelperCustom:
    def list_resources(self):
        # as this resource doesn't have a model for list of document jobs
        # this is required for create. So overriding it
        return []

    def get_module_resource_id_param(self):
        # this is required other fetch_fun() fails. So overriding it
        return "document_job_id"


class AiVisionImageJobHelperCustom:
    def list_resources(self):
        # as this resource doesn't have a model for list of image jobs
        # this is required for create. So overriding it
        return []

    def get_module_resource_id_param(self):
        # this is required other fetch_fun() fails. So overriding it
        return "image_job_id"


class AiVisionAnalyzeImageResultActionsHelperCustom:
    def get_resource(self):
        # Resource doesn't have get_resource method and perform_action calls get_resource.
        # So, overriding get_resource to return default response.
        return oci_common_utils.get_default_response_from_resource(resource=None)
