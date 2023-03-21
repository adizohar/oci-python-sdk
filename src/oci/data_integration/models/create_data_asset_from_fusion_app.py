# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_data_asset_details import CreateDataAssetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataAssetFromFusionApp(CreateDataAssetDetails):
    """
    Details for the FUSION_APP data asset type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataAssetFromFusionApp object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.CreateDataAssetFromFusionApp.model_type` attribute
        of this class is ``FUSION_APP_DATA_ASSET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateDataAssetFromFusionApp.
            Allowed values for this property are: "ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET", "MYSQL_DATA_ASSET", "GENERIC_JDBC_DATA_ASSET", "FUSION_APP_DATA_ASSET", "AMAZON_S3_DATA_ASSET", "LAKE_DATA_ASSET", "REST_DATA_ASSET"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateDataAssetFromFusionApp.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateDataAssetFromFusionApp.
        :type model_version: str

        :param name:
            The value to assign to the name property of this CreateDataAssetFromFusionApp.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateDataAssetFromFusionApp.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreateDataAssetFromFusionApp.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateDataAssetFromFusionApp.
        :type identifier: str

        :param external_key:
            The value to assign to the external_key property of this CreateDataAssetFromFusionApp.
        :type external_key: str

        :param asset_properties:
            The value to assign to the asset_properties property of this CreateDataAssetFromFusionApp.
        :type asset_properties: dict(str, str)

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateDataAssetFromFusionApp.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        :param service_url:
            The value to assign to the service_url property of this CreateDataAssetFromFusionApp.
        :type service_url: str

        :param default_connection:
            The value to assign to the default_connection property of this CreateDataAssetFromFusionApp.
        :type default_connection: oci.data_integration.models.CreateConnectionDetails

        :param staging_data_asset:
            The value to assign to the staging_data_asset property of this CreateDataAssetFromFusionApp.
        :type staging_data_asset: oci.data_integration.models.DataAssetSummaryFromObjectStorage

        :param staging_connection:
            The value to assign to the staging_connection property of this CreateDataAssetFromFusionApp.
        :type staging_connection: oci.data_integration.models.ConnectionSummaryFromObjectStorage

        :param bucket_schema:
            The value to assign to the bucket_schema property of this CreateDataAssetFromFusionApp.
        :type bucket_schema: oci.data_integration.models.Schema

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'external_key': 'str',
            'asset_properties': 'dict(str, str)',
            'registry_metadata': 'RegistryMetadata',
            'service_url': 'str',
            'default_connection': 'CreateConnectionDetails',
            'staging_data_asset': 'DataAssetSummaryFromObjectStorage',
            'staging_connection': 'ConnectionSummaryFromObjectStorage',
            'bucket_schema': 'Schema'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'external_key': 'externalKey',
            'asset_properties': 'assetProperties',
            'registry_metadata': 'registryMetadata',
            'service_url': 'serviceUrl',
            'default_connection': 'defaultConnection',
            'staging_data_asset': 'stagingDataAsset',
            'staging_connection': 'stagingConnection',
            'bucket_schema': 'bucketSchema'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._name = None
        self._description = None
        self._object_status = None
        self._identifier = None
        self._external_key = None
        self._asset_properties = None
        self._registry_metadata = None
        self._service_url = None
        self._default_connection = None
        self._staging_data_asset = None
        self._staging_connection = None
        self._bucket_schema = None
        self._model_type = 'FUSION_APP_DATA_ASSET'

    @property
    def service_url(self):
        """
        Gets the service_url of this CreateDataAssetFromFusionApp.
        The generic JDBC host name.


        :return: The service_url of this CreateDataAssetFromFusionApp.
        :rtype: str
        """
        return self._service_url

    @service_url.setter
    def service_url(self, service_url):
        """
        Sets the service_url of this CreateDataAssetFromFusionApp.
        The generic JDBC host name.


        :param service_url: The service_url of this CreateDataAssetFromFusionApp.
        :type: str
        """
        self._service_url = service_url

    @property
    def default_connection(self):
        """
        Gets the default_connection of this CreateDataAssetFromFusionApp.

        :return: The default_connection of this CreateDataAssetFromFusionApp.
        :rtype: oci.data_integration.models.CreateConnectionDetails
        """
        return self._default_connection

    @default_connection.setter
    def default_connection(self, default_connection):
        """
        Sets the default_connection of this CreateDataAssetFromFusionApp.

        :param default_connection: The default_connection of this CreateDataAssetFromFusionApp.
        :type: oci.data_integration.models.CreateConnectionDetails
        """
        self._default_connection = default_connection

    @property
    def staging_data_asset(self):
        """
        Gets the staging_data_asset of this CreateDataAssetFromFusionApp.

        :return: The staging_data_asset of this CreateDataAssetFromFusionApp.
        :rtype: oci.data_integration.models.DataAssetSummaryFromObjectStorage
        """
        return self._staging_data_asset

    @staging_data_asset.setter
    def staging_data_asset(self, staging_data_asset):
        """
        Sets the staging_data_asset of this CreateDataAssetFromFusionApp.

        :param staging_data_asset: The staging_data_asset of this CreateDataAssetFromFusionApp.
        :type: oci.data_integration.models.DataAssetSummaryFromObjectStorage
        """
        self._staging_data_asset = staging_data_asset

    @property
    def staging_connection(self):
        """
        Gets the staging_connection of this CreateDataAssetFromFusionApp.

        :return: The staging_connection of this CreateDataAssetFromFusionApp.
        :rtype: oci.data_integration.models.ConnectionSummaryFromObjectStorage
        """
        return self._staging_connection

    @staging_connection.setter
    def staging_connection(self, staging_connection):
        """
        Sets the staging_connection of this CreateDataAssetFromFusionApp.

        :param staging_connection: The staging_connection of this CreateDataAssetFromFusionApp.
        :type: oci.data_integration.models.ConnectionSummaryFromObjectStorage
        """
        self._staging_connection = staging_connection

    @property
    def bucket_schema(self):
        """
        Gets the bucket_schema of this CreateDataAssetFromFusionApp.

        :return: The bucket_schema of this CreateDataAssetFromFusionApp.
        :rtype: oci.data_integration.models.Schema
        """
        return self._bucket_schema

    @bucket_schema.setter
    def bucket_schema(self, bucket_schema):
        """
        Sets the bucket_schema of this CreateDataAssetFromFusionApp.

        :param bucket_schema: The bucket_schema of this CreateDataAssetFromFusionApp.
        :type: oci.data_integration.models.Schema
        """
        self._bucket_schema = bucket_schema

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
