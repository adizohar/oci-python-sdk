# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeCostEstimation(object):
    """
    Cost estimation for volume
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeCostEstimation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param capacity_gb:
            The value to assign to the capacity_gb property of this VolumeCostEstimation.
        :type capacity_gb: float

        :param description:
            The value to assign to the description property of this VolumeCostEstimation.
        :type description: str

        :param total_gb_per_month:
            The value to assign to the total_gb_per_month property of this VolumeCostEstimation.
        :type total_gb_per_month: float

        :param total_gb_per_month_by_subscription:
            The value to assign to the total_gb_per_month_by_subscription property of this VolumeCostEstimation.
        :type total_gb_per_month_by_subscription: float

        """
        self.swagger_types = {
            'capacity_gb': 'float',
            'description': 'str',
            'total_gb_per_month': 'float',
            'total_gb_per_month_by_subscription': 'float'
        }

        self.attribute_map = {
            'capacity_gb': 'capacityGb',
            'description': 'description',
            'total_gb_per_month': 'totalGbPerMonth',
            'total_gb_per_month_by_subscription': 'totalGbPerMonthBySubscription'
        }

        self._capacity_gb = None
        self._description = None
        self._total_gb_per_month = None
        self._total_gb_per_month_by_subscription = None

    @property
    def capacity_gb(self):
        """
        **[Required]** Gets the capacity_gb of this VolumeCostEstimation.
        Gigabyte storage capacity


        :return: The capacity_gb of this VolumeCostEstimation.
        :rtype: float
        """
        return self._capacity_gb

    @capacity_gb.setter
    def capacity_gb(self, capacity_gb):
        """
        Sets the capacity_gb of this VolumeCostEstimation.
        Gigabyte storage capacity


        :param capacity_gb: The capacity_gb of this VolumeCostEstimation.
        :type: float
        """
        self._capacity_gb = capacity_gb

    @property
    def description(self):
        """
        Gets the description of this VolumeCostEstimation.
        Volume description


        :return: The description of this VolumeCostEstimation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this VolumeCostEstimation.
        Volume description


        :param description: The description of this VolumeCostEstimation.
        :type: str
        """
        self._description = description

    @property
    def total_gb_per_month(self):
        """
        **[Required]** Gets the total_gb_per_month of this VolumeCostEstimation.
        Gigabyte storage capacity per month.


        :return: The total_gb_per_month of this VolumeCostEstimation.
        :rtype: float
        """
        return self._total_gb_per_month

    @total_gb_per_month.setter
    def total_gb_per_month(self, total_gb_per_month):
        """
        Sets the total_gb_per_month of this VolumeCostEstimation.
        Gigabyte storage capacity per month.


        :param total_gb_per_month: The total_gb_per_month of this VolumeCostEstimation.
        :type: float
        """
        self._total_gb_per_month = total_gb_per_month

    @property
    def total_gb_per_month_by_subscription(self):
        """
        Gets the total_gb_per_month_by_subscription of this VolumeCostEstimation.
        Gigabyte storage capacity per month by subscription


        :return: The total_gb_per_month_by_subscription of this VolumeCostEstimation.
        :rtype: float
        """
        return self._total_gb_per_month_by_subscription

    @total_gb_per_month_by_subscription.setter
    def total_gb_per_month_by_subscription(self, total_gb_per_month_by_subscription):
        """
        Sets the total_gb_per_month_by_subscription of this VolumeCostEstimation.
        Gigabyte storage capacity per month by subscription


        :param total_gb_per_month_by_subscription: The total_gb_per_month_by_subscription of this VolumeCostEstimation.
        :type: float
        """
        self._total_gb_per_month_by_subscription = total_gb_per_month_by_subscription

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other