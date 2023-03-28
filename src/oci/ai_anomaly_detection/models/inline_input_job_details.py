# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .input_job_details import InputJobDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InlineInputJobDetails(InputJobDetails):
    """
    This is the specialized JSON format with an additional field for 'locationType'. This is a required field
    used for deciding if it is an inline location or contains object-storage location.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InlineInputJobDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_anomaly_detection.models.InlineInputJobDetails.input_type` attribute
        of this class is ``INLINE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param input_type:
            The value to assign to the input_type property of this InlineInputJobDetails.
            Allowed values for this property are: "INLINE", "OBJECT_LIST"
        :type input_type: str

        :param message:
            The value to assign to the message property of this InlineInputJobDetails.
        :type message: str

        """
        self.swagger_types = {
            'input_type': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'input_type': 'inputType',
            'message': 'message'
        }

        self._input_type = None
        self._message = None
        self._input_type = 'INLINE'

    @property
    def message(self):
        """
        **[Required]** Gets the message of this InlineInputJobDetails.
        Inline input details.


        :return: The message of this InlineInputJobDetails.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this InlineInputJobDetails.
        Inline input details.


        :param message: The message of this InlineInputJobDetails.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other