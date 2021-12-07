# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBuildRunDetails(object):
    """
    Information about the new build run.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBuildRunDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateBuildRunDetails.
        :type display_name: str

        :param build_pipeline_id:
            The value to assign to the build_pipeline_id property of this CreateBuildRunDetails.
        :type build_pipeline_id: str

        :param commit_info:
            The value to assign to the commit_info property of this CreateBuildRunDetails.
        :type commit_info: oci.devops.models.CommitInfo

        :param build_run_arguments:
            The value to assign to the build_run_arguments property of this CreateBuildRunDetails.
        :type build_run_arguments: oci.devops.models.BuildRunArgumentCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateBuildRunDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateBuildRunDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'build_pipeline_id': 'str',
            'commit_info': 'CommitInfo',
            'build_run_arguments': 'BuildRunArgumentCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'build_pipeline_id': 'buildPipelineId',
            'commit_info': 'commitInfo',
            'build_run_arguments': 'buildRunArguments',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._build_pipeline_id = None
        self._commit_info = None
        self._build_run_arguments = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateBuildRunDetails.
        Build run display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :return: The display_name of this CreateBuildRunDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateBuildRunDetails.
        Build run display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :param display_name: The display_name of this CreateBuildRunDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def build_pipeline_id(self):
        """
        **[Required]** Gets the build_pipeline_id of this CreateBuildRunDetails.
        The OCID of the build pipeline.


        :return: The build_pipeline_id of this CreateBuildRunDetails.
        :rtype: str
        """
        return self._build_pipeline_id

    @build_pipeline_id.setter
    def build_pipeline_id(self, build_pipeline_id):
        """
        Sets the build_pipeline_id of this CreateBuildRunDetails.
        The OCID of the build pipeline.


        :param build_pipeline_id: The build_pipeline_id of this CreateBuildRunDetails.
        :type: str
        """
        self._build_pipeline_id = build_pipeline_id

    @property
    def commit_info(self):
        """
        Gets the commit_info of this CreateBuildRunDetails.

        :return: The commit_info of this CreateBuildRunDetails.
        :rtype: oci.devops.models.CommitInfo
        """
        return self._commit_info

    @commit_info.setter
    def commit_info(self, commit_info):
        """
        Sets the commit_info of this CreateBuildRunDetails.

        :param commit_info: The commit_info of this CreateBuildRunDetails.
        :type: oci.devops.models.CommitInfo
        """
        self._commit_info = commit_info

    @property
    def build_run_arguments(self):
        """
        Gets the build_run_arguments of this CreateBuildRunDetails.

        :return: The build_run_arguments of this CreateBuildRunDetails.
        :rtype: oci.devops.models.BuildRunArgumentCollection
        """
        return self._build_run_arguments

    @build_run_arguments.setter
    def build_run_arguments(self, build_run_arguments):
        """
        Sets the build_run_arguments of this CreateBuildRunDetails.

        :param build_run_arguments: The build_run_arguments of this CreateBuildRunDetails.
        :type: oci.devops.models.BuildRunArgumentCollection
        """
        self._build_run_arguments = build_run_arguments

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateBuildRunDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateBuildRunDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateBuildRunDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateBuildRunDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateBuildRunDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateBuildRunDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateBuildRunDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateBuildRunDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other