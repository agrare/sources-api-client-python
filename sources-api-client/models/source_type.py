# coding: utf-8

"""
    Sources

    Sources  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SourceType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'created_at': 'datetime',
        'id': 'str',
        'name': 'str',
        'product_name': 'str',
        'schema': 'str',
        'updated_at': 'datetime',
        'vendor': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'id': 'id',
        'name': 'name',
        'product_name': 'product_name',
        'schema': 'schema',
        'updated_at': 'updated_at',
        'vendor': 'vendor'
    }

    def __init__(self, created_at=None, id=None, name=None, product_name=None, schema=None, updated_at=None, vendor=None):  # noqa: E501
        """SourceType - a model defined in OpenAPI"""  # noqa: E501

        self._created_at = None
        self._id = None
        self._name = None
        self._product_name = None
        self._schema = None
        self._updated_at = None
        self._vendor = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if product_name is not None:
            self.product_name = product_name
        if schema is not None:
            self.schema = schema
        if updated_at is not None:
            self.updated_at = updated_at
        if vendor is not None:
            self.vendor = vendor

    @property
    def created_at(self):
        """Gets the created_at of this SourceType.  # noqa: E501


        :return: The created_at of this SourceType.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SourceType.


        :param created_at: The created_at of this SourceType.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this SourceType.  # noqa: E501

        ID of the resource  # noqa: E501

        :return: The id of this SourceType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SourceType.

        ID of the resource  # noqa: E501

        :param id: The id of this SourceType.  # noqa: E501
        :type: str
        """
        if id is not None and not re.search(r'^\\d+$', id):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/^\\d+$/`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this SourceType.  # noqa: E501


        :return: The name of this SourceType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SourceType.


        :param name: The name of this SourceType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def product_name(self):
        """Gets the product_name of this SourceType.  # noqa: E501


        :return: The product_name of this SourceType.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this SourceType.


        :param product_name: The product_name of this SourceType.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def schema(self):
        """Gets the schema of this SourceType.  # noqa: E501


        :return: The schema of this SourceType.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this SourceType.


        :param schema: The schema of this SourceType.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def updated_at(self):
        """Gets the updated_at of this SourceType.  # noqa: E501


        :return: The updated_at of this SourceType.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SourceType.


        :param updated_at: The updated_at of this SourceType.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def vendor(self):
        """Gets the vendor of this SourceType.  # noqa: E501


        :return: The vendor of this SourceType.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this SourceType.


        :param vendor: The vendor of this SourceType.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SourceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other