# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExtensionPosixGroup(object):
    """
    POSIX Group extension
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExtensionPosixGroup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param gid_number:
            The value to assign to the gid_number property of this ExtensionPosixGroup.
        :type gid_number: int

        """
        self.swagger_types = {
            'gid_number': 'int'
        }

        self.attribute_map = {
            'gid_number': 'gidNumber'
        }

        self._gid_number = None

    @property
    def gid_number(self):
        """
        Gets the gid_number of this ExtensionPosixGroup.
        Integer uniquely identifying a group in a POSIX administrative domain

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: integer
         - uniqueness: server


        :return: The gid_number of this ExtensionPosixGroup.
        :rtype: int
        """
        return self._gid_number

    @gid_number.setter
    def gid_number(self, gid_number):
        """
        Sets the gid_number of this ExtensionPosixGroup.
        Integer uniquely identifying a group in a POSIX administrative domain

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: request
         - type: integer
         - uniqueness: server


        :param gid_number: The gid_number of this ExtensionPosixGroup.
        :type: int
        """
        self._gid_number = gid_number

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other