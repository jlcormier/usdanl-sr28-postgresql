# coding: utf-8

"""
    Food Data Central API

    The FoodData Central API provides REST access to FoodData Central (FDC). It is intended primarily to assist application developers wishing to incorporate nutrient data into their applications or websites.   To take full advantage of the API, developers should familiarize themselves with the database by reading the database documentation available via links on [Data Type Documentation](https://fdc.nal.usda.gov/data-documentation.html). This documentation provides the detailed definitions and descriptions needed to understand the data elements referenced in the API documentation.      Additional details about the API including rate limits, access, and licensing are available on the [FDC website](https://fdc.nal.usda.gov/api-guide.html)  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SurveyFoodItem(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'fdc_id': 'int',
        'datatype': 'str',
        'description': 'str',
        'end_date': 'str',
        'food_class': 'str',
        'food_code': 'str',
        'publication_date': 'str',
        'start_date': 'str',
        'food_attributes': 'list[FoodAttribute]',
        'food_portions': 'list[FoodPortion]',
        'input_foods': 'list[InputFoodSurvey]',
        'wweia_food_category': 'WweiaFoodCategory'
    }

    attribute_map = {
        'fdc_id': 'fdcId',
        'datatype': 'datatype',
        'description': 'description',
        'end_date': 'endDate',
        'food_class': 'foodClass',
        'food_code': 'foodCode',
        'publication_date': 'publicationDate',
        'start_date': 'startDate',
        'food_attributes': 'foodAttributes',
        'food_portions': 'foodPortions',
        'input_foods': 'inputFoods',
        'wweia_food_category': 'wweiaFoodCategory'
    }

    def __init__(self, fdc_id=None, datatype=None, description=None, end_date=None, food_class=None, food_code=None, publication_date=None, start_date=None, food_attributes=None, food_portions=None, input_foods=None, wweia_food_category=None):  # noqa: E501
        """SurveyFoodItem - a model defined in Swagger"""  # noqa: E501
        self._fdc_id = None
        self._datatype = None
        self._description = None
        self._end_date = None
        self._food_class = None
        self._food_code = None
        self._publication_date = None
        self._start_date = None
        self._food_attributes = None
        self._food_portions = None
        self._input_foods = None
        self._wweia_food_category = None
        self.discriminator = None
        self.fdc_id = fdc_id
        if datatype is not None:
            self.datatype = datatype
        self.description = description
        if end_date is not None:
            self.end_date = end_date
        if food_class is not None:
            self.food_class = food_class
        if food_code is not None:
            self.food_code = food_code
        if publication_date is not None:
            self.publication_date = publication_date
        if start_date is not None:
            self.start_date = start_date
        if food_attributes is not None:
            self.food_attributes = food_attributes
        if food_portions is not None:
            self.food_portions = food_portions
        if input_foods is not None:
            self.input_foods = input_foods
        if wweia_food_category is not None:
            self.wweia_food_category = wweia_food_category

    @property
    def fdc_id(self):
        """Gets the fdc_id of this SurveyFoodItem.  # noqa: E501


        :return: The fdc_id of this SurveyFoodItem.  # noqa: E501
        :rtype: int
        """
        return self._fdc_id

    @fdc_id.setter
    def fdc_id(self, fdc_id):
        """Sets the fdc_id of this SurveyFoodItem.


        :param fdc_id: The fdc_id of this SurveyFoodItem.  # noqa: E501
        :type: int
        """
        if fdc_id is None:
            raise ValueError("Invalid value for `fdc_id`, must not be `None`")  # noqa: E501

        self._fdc_id = fdc_id

    @property
    def datatype(self):
        """Gets the datatype of this SurveyFoodItem.  # noqa: E501


        :return: The datatype of this SurveyFoodItem.  # noqa: E501
        :rtype: str
        """
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        """Sets the datatype of this SurveyFoodItem.


        :param datatype: The datatype of this SurveyFoodItem.  # noqa: E501
        :type: str
        """

        self._datatype = datatype

    @property
    def description(self):
        """Gets the description of this SurveyFoodItem.  # noqa: E501


        :return: The description of this SurveyFoodItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SurveyFoodItem.


        :param description: The description of this SurveyFoodItem.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def end_date(self):
        """Gets the end_date of this SurveyFoodItem.  # noqa: E501


        :return: The end_date of this SurveyFoodItem.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SurveyFoodItem.


        :param end_date: The end_date of this SurveyFoodItem.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def food_class(self):
        """Gets the food_class of this SurveyFoodItem.  # noqa: E501


        :return: The food_class of this SurveyFoodItem.  # noqa: E501
        :rtype: str
        """
        return self._food_class

    @food_class.setter
    def food_class(self, food_class):
        """Sets the food_class of this SurveyFoodItem.


        :param food_class: The food_class of this SurveyFoodItem.  # noqa: E501
        :type: str
        """

        self._food_class = food_class

    @property
    def food_code(self):
        """Gets the food_code of this SurveyFoodItem.  # noqa: E501


        :return: The food_code of this SurveyFoodItem.  # noqa: E501
        :rtype: str
        """
        return self._food_code

    @food_code.setter
    def food_code(self, food_code):
        """Sets the food_code of this SurveyFoodItem.


        :param food_code: The food_code of this SurveyFoodItem.  # noqa: E501
        :type: str
        """

        self._food_code = food_code

    @property
    def publication_date(self):
        """Gets the publication_date of this SurveyFoodItem.  # noqa: E501


        :return: The publication_date of this SurveyFoodItem.  # noqa: E501
        :rtype: str
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this SurveyFoodItem.


        :param publication_date: The publication_date of this SurveyFoodItem.  # noqa: E501
        :type: str
        """

        self._publication_date = publication_date

    @property
    def start_date(self):
        """Gets the start_date of this SurveyFoodItem.  # noqa: E501


        :return: The start_date of this SurveyFoodItem.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SurveyFoodItem.


        :param start_date: The start_date of this SurveyFoodItem.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def food_attributes(self):
        """Gets the food_attributes of this SurveyFoodItem.  # noqa: E501


        :return: The food_attributes of this SurveyFoodItem.  # noqa: E501
        :rtype: list[FoodAttribute]
        """
        return self._food_attributes

    @food_attributes.setter
    def food_attributes(self, food_attributes):
        """Sets the food_attributes of this SurveyFoodItem.


        :param food_attributes: The food_attributes of this SurveyFoodItem.  # noqa: E501
        :type: list[FoodAttribute]
        """

        self._food_attributes = food_attributes

    @property
    def food_portions(self):
        """Gets the food_portions of this SurveyFoodItem.  # noqa: E501


        :return: The food_portions of this SurveyFoodItem.  # noqa: E501
        :rtype: list[FoodPortion]
        """
        return self._food_portions

    @food_portions.setter
    def food_portions(self, food_portions):
        """Sets the food_portions of this SurveyFoodItem.


        :param food_portions: The food_portions of this SurveyFoodItem.  # noqa: E501
        :type: list[FoodPortion]
        """

        self._food_portions = food_portions

    @property
    def input_foods(self):
        """Gets the input_foods of this SurveyFoodItem.  # noqa: E501


        :return: The input_foods of this SurveyFoodItem.  # noqa: E501
        :rtype: list[InputFoodSurvey]
        """
        return self._input_foods

    @input_foods.setter
    def input_foods(self, input_foods):
        """Sets the input_foods of this SurveyFoodItem.


        :param input_foods: The input_foods of this SurveyFoodItem.  # noqa: E501
        :type: list[InputFoodSurvey]
        """

        self._input_foods = input_foods

    @property
    def wweia_food_category(self):
        """Gets the wweia_food_category of this SurveyFoodItem.  # noqa: E501


        :return: The wweia_food_category of this SurveyFoodItem.  # noqa: E501
        :rtype: WweiaFoodCategory
        """
        return self._wweia_food_category

    @wweia_food_category.setter
    def wweia_food_category(self, wweia_food_category):
        """Sets the wweia_food_category of this SurveyFoodItem.


        :param wweia_food_category: The wweia_food_category of this SurveyFoodItem.  # noqa: E501
        :type: WweiaFoodCategory
        """

        self._wweia_food_category = wweia_food_category

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(SurveyFoodItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SurveyFoodItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
