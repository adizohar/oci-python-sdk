# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SpanFilterReference(object):
    """
    Describes an item that references the span filter.
    """

    #: A constant which can be used with the config_type property of a SpanFilterReference.
    #: This constant has a value of "SPAN_FILTER"
    CONFIG_TYPE_SPAN_FILTER = "SPAN_FILTER"

    #: A constant which can be used with the config_type property of a SpanFilterReference.
    #: This constant has a value of "METRIC_GROUP"
    CONFIG_TYPE_METRIC_GROUP = "METRIC_GROUP"

    #: A constant which can be used with the config_type property of a SpanFilterReference.
    #: This constant has a value of "APDEX"
    CONFIG_TYPE_APDEX = "APDEX"

    #: A constant which can be used with the config_type property of a SpanFilterReference.
    #: This constant has a value of "OPTIONS"
    CONFIG_TYPE_OPTIONS = "OPTIONS"

    def __init__(self, **kwargs):
        """
        Initializes a new SpanFilterReference object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SpanFilterReference.
        :type id: str

        :param config_type:
            The value to assign to the config_type property of this SpanFilterReference.
            Allowed values for this property are: "SPAN_FILTER", "METRIC_GROUP", "APDEX", "OPTIONS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type config_type: str

        :param options_group:
            The value to assign to the options_group property of this SpanFilterReference.
        :type options_group: str

        :param display_name:
            The value to assign to the display_name property of this SpanFilterReference.
        :type display_name: str

        """
        self.swagger_types = {
            'id': 'str',
            'config_type': 'str',
            'options_group': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'config_type': 'configType',
            'options_group': 'optionsGroup',
            'display_name': 'displayName'
        }

        self._id = None
        self._config_type = None
        self._options_group = None
        self._display_name = None

    @property
    def id(self):
        """
        Gets the id of this SpanFilterReference.
        The `OCID`__ of the configuration item. An OCID is generated
        when the item is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this SpanFilterReference.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SpanFilterReference.
        The `OCID`__ of the configuration item. An OCID is generated
        when the item is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this SpanFilterReference.
        :type: str
        """
        self._id = id

    @property
    def config_type(self):
        """
        Gets the config_type of this SpanFilterReference.
        The type of configuration item.

        Allowed values for this property are: "SPAN_FILTER", "METRIC_GROUP", "APDEX", "OPTIONS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The config_type of this SpanFilterReference.
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """
        Sets the config_type of this SpanFilterReference.
        The type of configuration item.


        :param config_type: The config_type of this SpanFilterReference.
        :type: str
        """
        allowed_values = ["SPAN_FILTER", "METRIC_GROUP", "APDEX", "OPTIONS"]
        if not value_allowed_none_or_none_sentinel(config_type, allowed_values):
            config_type = 'UNKNOWN_ENUM_VALUE'
        self._config_type = config_type

    @property
    def options_group(self):
        """
        Gets the options_group of this SpanFilterReference.
        A string that specifies the group that an OPTIONS item belongs to.


        :return: The options_group of this SpanFilterReference.
        :rtype: str
        """
        return self._options_group

    @options_group.setter
    def options_group(self, options_group):
        """
        Sets the options_group of this SpanFilterReference.
        A string that specifies the group that an OPTIONS item belongs to.


        :param options_group: The options_group of this SpanFilterReference.
        :type: str
        """
        self._options_group = options_group

    @property
    def display_name(self):
        """
        Gets the display_name of this SpanFilterReference.
        The name by which a configuration entity is displayed to the end user.


        :return: The display_name of this SpanFilterReference.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SpanFilterReference.
        The name by which a configuration entity is displayed to the end user.


        :param display_name: The display_name of this SpanFilterReference.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other