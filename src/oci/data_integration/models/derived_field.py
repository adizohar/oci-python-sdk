# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .typed_object import TypedObject
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DerivedField(TypedObject):
    """
    The type representing the derived field concept. Derived fields have an expression to define how to derive the field.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DerivedField object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.DerivedField.model_type` attribute
        of this class is ``DERIVED_FIELD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DerivedField.
            Allowed values for this property are: "SHAPE", "INPUT_PORT", "SHAPE_FIELD", "INPUT_FIELD", "DERIVED_FIELD", "MACRO_FIELD", "OUTPUT_FIELD", "DYNAMIC_PROXY_FIELD", "OUTPUT_PORT", "DYNAMIC_INPUT_FIELD", "PROXY_FIELD", "PARAMETER", "PIVOT_FIELD", "MACRO_PIVOT_FIELD", "CONDITIONAL_OUTPUT_PORT", "INPUT_PROXY_FIELD", "MATERIALIZED_DYNAMIC_FIELD", "DECISION_OUTPUT_PORT"
        :type model_type: str

        :param key:
            The value to assign to the key property of this DerivedField.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DerivedField.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this DerivedField.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param config_values:
            The value to assign to the config_values property of this DerivedField.
        :type config_values: oci.data_integration.models.ConfigValues

        :param object_status:
            The value to assign to the object_status property of this DerivedField.
        :type object_status: int

        :param name:
            The value to assign to the name property of this DerivedField.
        :type name: str

        :param description:
            The value to assign to the description property of this DerivedField.
        :type description: str

        :param expr:
            The value to assign to the expr property of this DerivedField.
        :type expr: oci.data_integration.models.Expression

        :param type:
            The value to assign to the type property of this DerivedField.
        :type type: str

        :param is_use_inferred_type:
            The value to assign to the is_use_inferred_type property of this DerivedField.
        :type is_use_inferred_type: bool

        :param labels:
            The value to assign to the labels property of this DerivedField.
        :type labels: list[str]

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'config_values': 'ConfigValues',
            'object_status': 'int',
            'name': 'str',
            'description': 'str',
            'expr': 'Expression',
            'type': 'str',
            'is_use_inferred_type': 'bool',
            'labels': 'list[str]'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'config_values': 'configValues',
            'object_status': 'objectStatus',
            'name': 'name',
            'description': 'description',
            'expr': 'expr',
            'type': 'type',
            'is_use_inferred_type': 'isUseInferredType',
            'labels': 'labels'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._config_values = None
        self._object_status = None
        self._name = None
        self._description = None
        self._expr = None
        self._type = None
        self._is_use_inferred_type = None
        self._labels = None
        self._model_type = 'DERIVED_FIELD'

    @property
    def expr(self):
        """
        Gets the expr of this DerivedField.

        :return: The expr of this DerivedField.
        :rtype: oci.data_integration.models.Expression
        """
        return self._expr

    @expr.setter
    def expr(self, expr):
        """
        Sets the expr of this DerivedField.

        :param expr: The expr of this DerivedField.
        :type: oci.data_integration.models.Expression
        """
        self._expr = expr

    @property
    def type(self):
        """
        Gets the type of this DerivedField.
        The type of the field.


        :return: The type of this DerivedField.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DerivedField.
        The type of the field.


        :param type: The type of this DerivedField.
        :type: str
        """
        self._type = type

    @property
    def is_use_inferred_type(self):
        """
        Gets the is_use_inferred_type of this DerivedField.
        Specifies whether to use inferred expression output type as output type of the derived field. Default value of this flag is false.


        :return: The is_use_inferred_type of this DerivedField.
        :rtype: bool
        """
        return self._is_use_inferred_type

    @is_use_inferred_type.setter
    def is_use_inferred_type(self, is_use_inferred_type):
        """
        Sets the is_use_inferred_type of this DerivedField.
        Specifies whether to use inferred expression output type as output type of the derived field. Default value of this flag is false.


        :param is_use_inferred_type: The is_use_inferred_type of this DerivedField.
        :type: bool
        """
        self._is_use_inferred_type = is_use_inferred_type

    @property
    def labels(self):
        """
        Gets the labels of this DerivedField.
        Labels are keywords or labels that you can add to data assets, dataflows and so on. You can define your own labels and use them to categorize content.


        :return: The labels of this DerivedField.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this DerivedField.
        Labels are keywords or labels that you can add to data assets, dataflows and so on. You can define your own labels and use them to categorize content.


        :param labels: The labels of this DerivedField.
        :type: list[str]
        """
        self._labels = labels

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
