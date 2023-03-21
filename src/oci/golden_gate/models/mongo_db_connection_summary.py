# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .connection_summary import ConnectionSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MongoDbConnectionSummary(ConnectionSummary):
    """
    Summary of the MongoDB Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MongoDbConnectionSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.MongoDbConnectionSummary.connection_type` attribute
        of this class is ``MONGODB`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this MongoDbConnectionSummary.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB"
        :type connection_type: str

        :param id:
            The value to assign to the id property of this MongoDbConnectionSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this MongoDbConnectionSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this MongoDbConnectionSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MongoDbConnectionSummary.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MongoDbConnectionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MongoDbConnectionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MongoDbConnectionSummary.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MongoDbConnectionSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MongoDbConnectionSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this MongoDbConnectionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MongoDbConnectionSummary.
        :type time_updated: datetime

        :param vault_id:
            The value to assign to the vault_id property of this MongoDbConnectionSummary.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this MongoDbConnectionSummary.
        :type key_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this MongoDbConnectionSummary.
        :type subnet_id: str

        :param ingress_ips:
            The value to assign to the ingress_ips property of this MongoDbConnectionSummary.
        :type ingress_ips: list[oci.golden_gate.models.IngressIpDetails]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this MongoDbConnectionSummary.
        :type nsg_ids: list[str]

        :param technology_type:
            The value to assign to the technology_type property of this MongoDbConnectionSummary.
        :type technology_type: str

        :param connection_string:
            The value to assign to the connection_string property of this MongoDbConnectionSummary.
        :type connection_string: str

        :param username:
            The value to assign to the username property of this MongoDbConnectionSummary.
        :type username: str

        :param database_id:
            The value to assign to the database_id property of this MongoDbConnectionSummary.
        :type database_id: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'vault_id': 'str',
            'key_id': 'str',
            'subnet_id': 'str',
            'ingress_ips': 'list[IngressIpDetails]',
            'nsg_ids': 'list[str]',
            'technology_type': 'str',
            'connection_string': 'str',
            'username': 'str',
            'database_id': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'subnet_id': 'subnetId',
            'ingress_ips': 'ingressIps',
            'nsg_ids': 'nsgIds',
            'technology_type': 'technologyType',
            'connection_string': 'connectionString',
            'username': 'username',
            'database_id': 'databaseId'
        }

        self._connection_type = None
        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._vault_id = None
        self._key_id = None
        self._subnet_id = None
        self._ingress_ips = None
        self._nsg_ids = None
        self._technology_type = None
        self._connection_string = None
        self._username = None
        self._database_id = None
        self._connection_type = 'MONGODB'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this MongoDbConnectionSummary.
        The MongoDB technology type.


        :return: The technology_type of this MongoDbConnectionSummary.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this MongoDbConnectionSummary.
        The MongoDB technology type.


        :param technology_type: The technology_type of this MongoDbConnectionSummary.
        :type: str
        """
        self._technology_type = technology_type

    @property
    def connection_string(self):
        """
        Gets the connection_string of this MongoDbConnectionSummary.
        MongoDB connection string.
        e.g.: 'mongodb://mongodb0.example.com:27017/recordsrecords'


        :return: The connection_string of this MongoDbConnectionSummary.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this MongoDbConnectionSummary.
        MongoDB connection string.
        e.g.: 'mongodb://mongodb0.example.com:27017/recordsrecords'


        :param connection_string: The connection_string of this MongoDbConnectionSummary.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def username(self):
        """
        Gets the username of this MongoDbConnectionSummary.
        The username Oracle GoldenGate uses to connect to the database.
        This username must already exist and be available by the database to be connected to.


        :return: The username of this MongoDbConnectionSummary.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this MongoDbConnectionSummary.
        The username Oracle GoldenGate uses to connect to the database.
        This username must already exist and be available by the database to be connected to.


        :param username: The username of this MongoDbConnectionSummary.
        :type: str
        """
        self._username = username

    @property
    def database_id(self):
        """
        Gets the database_id of this MongoDbConnectionSummary.
        The `OCID`__ of the Oracle Autonomous Json Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_id of this MongoDbConnectionSummary.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this MongoDbConnectionSummary.
        The `OCID`__ of the Oracle Autonomous Json Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this MongoDbConnectionSummary.
        :type: str
        """
        self._database_id = database_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
