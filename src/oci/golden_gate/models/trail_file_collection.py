# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TrailFileCollection(object):
    """
    A list of TrailFiles.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TrailFileCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_last_fetched:
            The value to assign to the time_last_fetched property of this TrailFileCollection.
        :type time_last_fetched: datetime

        :param items:
            The value to assign to the items property of this TrailFileCollection.
        :type items: list[oci.golden_gate.models.TrailFileSummary]

        """
        self.swagger_types = {
            'time_last_fetched': 'datetime',
            'items': 'list[TrailFileSummary]'
        }

        self.attribute_map = {
            'time_last_fetched': 'timeLastFetched',
            'items': 'items'
        }

        self._time_last_fetched = None
        self._items = None

    @property
    def time_last_fetched(self):
        """
        **[Required]** Gets the time_last_fetched of this TrailFileCollection.
        The time the data was last fetched from the deployment. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_last_fetched of this TrailFileCollection.
        :rtype: datetime
        """
        return self._time_last_fetched

    @time_last_fetched.setter
    def time_last_fetched(self, time_last_fetched):
        """
        Sets the time_last_fetched of this TrailFileCollection.
        The time the data was last fetched from the deployment. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_last_fetched: The time_last_fetched of this TrailFileCollection.
        :type: datetime
        """
        self._time_last_fetched = time_last_fetched

    @property
    def items(self):
        """
        **[Required]** Gets the items of this TrailFileCollection.
        An array of TrailFiles.


        :return: The items of this TrailFileCollection.
        :rtype: list[oci.golden_gate.models.TrailFileSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this TrailFileCollection.
        An array of TrailFiles.


        :param items: The items of this TrailFileCollection.
        :type: list[oci.golden_gate.models.TrailFileSummary]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
