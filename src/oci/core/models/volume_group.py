# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeGroup(object):
    """
    Specifies a volume group which is a collection of
    volumes. For more information, see `Volume Groups`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you
    supply string values using the API.

    __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm
    """

    #: A constant which can be used with the lifecycle_state property of a VolumeGroup.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a VolumeGroup.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a VolumeGroup.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a VolumeGroup.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a VolumeGroup.
    #: This constant has a value of "FAULTY"
    LIFECYCLE_STATE_FAULTY = "FAULTY"

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeGroup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this VolumeGroup.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VolumeGroup.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this VolumeGroup.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this VolumeGroup.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VolumeGroup.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this VolumeGroup.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VolumeGroup.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param size_in_mbs:
            The value to assign to the size_in_mbs property of this VolumeGroup.
        :type size_in_mbs: int

        :param size_in_gbs:
            The value to assign to the size_in_gbs property of this VolumeGroup.
        :type size_in_gbs: int

        :param source_details:
            The value to assign to the source_details property of this VolumeGroup.
        :type source_details: oci.core.models.VolumeGroupSourceDetails

        :param time_created:
            The value to assign to the time_created property of this VolumeGroup.
        :type time_created: datetime

        :param volume_ids:
            The value to assign to the volume_ids property of this VolumeGroup.
        :type volume_ids: list[str]

        :param is_hydrated:
            The value to assign to the is_hydrated property of this VolumeGroup.
        :type is_hydrated: bool

        :param volume_group_replicas:
            The value to assign to the volume_group_replicas property of this VolumeGroup.
        :type volume_group_replicas: list[oci.core.models.VolumeGroupReplicaInfo]

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'size_in_mbs': 'int',
            'size_in_gbs': 'int',
            'source_details': 'VolumeGroupSourceDetails',
            'time_created': 'datetime',
            'volume_ids': 'list[str]',
            'is_hydrated': 'bool',
            'volume_group_replicas': 'list[VolumeGroupReplicaInfo]'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'size_in_mbs': 'sizeInMBs',
            'size_in_gbs': 'sizeInGBs',
            'source_details': 'sourceDetails',
            'time_created': 'timeCreated',
            'volume_ids': 'volumeIds',
            'is_hydrated': 'isHydrated',
            'volume_group_replicas': 'volumeGroupReplicas'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._size_in_mbs = None
        self._size_in_gbs = None
        self._source_details = None
        self._time_created = None
        self._volume_ids = None
        self._is_hydrated = None
        self._volume_group_replicas = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this VolumeGroup.
        The availability domain of the volume group.


        :return: The availability_domain of this VolumeGroup.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this VolumeGroup.
        The availability domain of the volume group.


        :param availability_domain: The availability_domain of this VolumeGroup.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this VolumeGroup.
        The OCID of the compartment that contains the volume group.


        :return: The compartment_id of this VolumeGroup.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VolumeGroup.
        The OCID of the compartment that contains the volume group.


        :param compartment_id: The compartment_id of this VolumeGroup.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this VolumeGroup.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this VolumeGroup.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this VolumeGroup.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this VolumeGroup.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this VolumeGroup.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this VolumeGroup.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VolumeGroup.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this VolumeGroup.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this VolumeGroup.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this VolumeGroup.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this VolumeGroup.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this VolumeGroup.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this VolumeGroup.
        The OCID for the volume group.


        :return: The id of this VolumeGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VolumeGroup.
        The OCID for the volume group.


        :param id: The id of this VolumeGroup.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this VolumeGroup.
        The current state of a volume group.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this VolumeGroup.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VolumeGroup.
        The current state of a volume group.


        :param lifecycle_state: The lifecycle_state of this VolumeGroup.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def size_in_mbs(self):
        """
        **[Required]** Gets the size_in_mbs of this VolumeGroup.
        The aggregate size of the volume group in MBs.


        :return: The size_in_mbs of this VolumeGroup.
        :rtype: int
        """
        return self._size_in_mbs

    @size_in_mbs.setter
    def size_in_mbs(self, size_in_mbs):
        """
        Sets the size_in_mbs of this VolumeGroup.
        The aggregate size of the volume group in MBs.


        :param size_in_mbs: The size_in_mbs of this VolumeGroup.
        :type: int
        """
        self._size_in_mbs = size_in_mbs

    @property
    def size_in_gbs(self):
        """
        Gets the size_in_gbs of this VolumeGroup.
        The aggregate size of the volume group in GBs.


        :return: The size_in_gbs of this VolumeGroup.
        :rtype: int
        """
        return self._size_in_gbs

    @size_in_gbs.setter
    def size_in_gbs(self, size_in_gbs):
        """
        Sets the size_in_gbs of this VolumeGroup.
        The aggregate size of the volume group in GBs.


        :param size_in_gbs: The size_in_gbs of this VolumeGroup.
        :type: int
        """
        self._size_in_gbs = size_in_gbs

    @property
    def source_details(self):
        """
        Gets the source_details of this VolumeGroup.

        :return: The source_details of this VolumeGroup.
        :rtype: oci.core.models.VolumeGroupSourceDetails
        """
        return self._source_details

    @source_details.setter
    def source_details(self, source_details):
        """
        Sets the source_details of this VolumeGroup.

        :param source_details: The source_details of this VolumeGroup.
        :type: oci.core.models.VolumeGroupSourceDetails
        """
        self._source_details = source_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this VolumeGroup.
        The date and time the volume group was created. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this VolumeGroup.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VolumeGroup.
        The date and time the volume group was created. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this VolumeGroup.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def volume_ids(self):
        """
        **[Required]** Gets the volume_ids of this VolumeGroup.
        OCIDs for the volumes in this volume group.


        :return: The volume_ids of this VolumeGroup.
        :rtype: list[str]
        """
        return self._volume_ids

    @volume_ids.setter
    def volume_ids(self, volume_ids):
        """
        Sets the volume_ids of this VolumeGroup.
        OCIDs for the volumes in this volume group.


        :param volume_ids: The volume_ids of this VolumeGroup.
        :type: list[str]
        """
        self._volume_ids = volume_ids

    @property
    def is_hydrated(self):
        """
        Gets the is_hydrated of this VolumeGroup.
        Specifies whether the newly created cloned volume group's data has finished copying
        from the source volume group or backup.


        :return: The is_hydrated of this VolumeGroup.
        :rtype: bool
        """
        return self._is_hydrated

    @is_hydrated.setter
    def is_hydrated(self, is_hydrated):
        """
        Sets the is_hydrated of this VolumeGroup.
        Specifies whether the newly created cloned volume group's data has finished copying
        from the source volume group or backup.


        :param is_hydrated: The is_hydrated of this VolumeGroup.
        :type: bool
        """
        self._is_hydrated = is_hydrated

    @property
    def volume_group_replicas(self):
        """
        Gets the volume_group_replicas of this VolumeGroup.
        The list of volume group replicas of this volume group.


        :return: The volume_group_replicas of this VolumeGroup.
        :rtype: list[oci.core.models.VolumeGroupReplicaInfo]
        """
        return self._volume_group_replicas

    @volume_group_replicas.setter
    def volume_group_replicas(self, volume_group_replicas):
        """
        Sets the volume_group_replicas of this VolumeGroup.
        The list of volume group replicas of this volume group.


        :param volume_group_replicas: The volume_group_replicas of this VolumeGroup.
        :type: list[oci.core.models.VolumeGroupReplicaInfo]
        """
        self._volume_group_replicas = volume_group_replicas

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
