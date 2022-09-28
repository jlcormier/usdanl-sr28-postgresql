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

class SearchResult(object):
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
        'food_search_criteria': 'FoodSearchCriteria',
        'total_hits': 'int',
        'current_page': 'int',
        'total_pages': 'int',
        'foods': 'list[SearchResultFood]'
    }

    attribute_map = {
        'food_search_criteria': 'foodSearchCriteria',
        'total_hits': 'totalHits',
        'current_page': 'currentPage',
        'total_pages': 'totalPages',
        'foods': 'foods'
    }

    def __init__(self, food_search_criteria=None, total_hits=None, current_page=None, total_pages=None, foods=None):  # noqa: E501
        """SearchResult - a model defined in Swagger"""  # noqa: E501
        self._food_search_criteria = None
        self._total_hits = None
        self._current_page = None
        self._total_pages = None
        self._foods = None
        self.discriminator = None
        if food_search_criteria is not None:
            self.food_search_criteria = food_search_criteria
        if total_hits is not None:
            self.total_hits = total_hits
        if current_page is not None:
            self.current_page = current_page
        if total_pages is not None:
            self.total_pages = total_pages
        if foods is not None:
            self.foods = foods

    @property
    def food_search_criteria(self):
        """Gets the food_search_criteria of this SearchResult.  # noqa: E501


        :return: The food_search_criteria of this SearchResult.  # noqa: E501
        :rtype: FoodSearchCriteria
        """
        return self._food_search_criteria

    @food_search_criteria.setter
    def food_search_criteria(self, food_search_criteria):
        """Sets the food_search_criteria of this SearchResult.


        :param food_search_criteria: The food_search_criteria of this SearchResult.  # noqa: E501
        :type: FoodSearchCriteria
        """

        self._food_search_criteria = food_search_criteria

    @property
    def total_hits(self):
        """Gets the total_hits of this SearchResult.  # noqa: E501

        The total number of foods found matching the search criteria.  # noqa: E501

        :return: The total_hits of this SearchResult.  # noqa: E501
        :rtype: int
        """
        return self._total_hits

    @total_hits.setter
    def total_hits(self, total_hits):
        """Sets the total_hits of this SearchResult.

        The total number of foods found matching the search criteria.  # noqa: E501

        :param total_hits: The total_hits of this SearchResult.  # noqa: E501
        :type: int
        """

        self._total_hits = total_hits

    @property
    def current_page(self):
        """Gets the current_page of this SearchResult.  # noqa: E501

        The current page of results being returned.  # noqa: E501

        :return: The current_page of this SearchResult.  # noqa: E501
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this SearchResult.

        The current page of results being returned.  # noqa: E501

        :param current_page: The current_page of this SearchResult.  # noqa: E501
        :type: int
        """

        self._current_page = current_page

    @property
    def total_pages(self):
        """Gets the total_pages of this SearchResult.  # noqa: E501

        The total number of pages found matching the search criteria.  # noqa: E501

        :return: The total_pages of this SearchResult.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this SearchResult.

        The total number of pages found matching the search criteria.  # noqa: E501

        :param total_pages: The total_pages of this SearchResult.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

    @property
    def foods(self):
        """Gets the foods of this SearchResult.  # noqa: E501

        The list of foods found matching the search criteria. See Food Fields below.  # noqa: E501

        :return: The foods of this SearchResult.  # noqa: E501
        :rtype: list[SearchResultFood]
        """
        return self._foods

    @foods.setter
    def foods(self, foods):
        """Sets the foods of this SearchResult.

        The list of foods found matching the search criteria. See Food Fields below.  # noqa: E501

        :param foods: The foods of this SearchResult.  # noqa: E501
        :type: list[SearchResultFood]
        """

        self._foods = foods

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
        if issubclass(SearchResult, dict):
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
        if not isinstance(other, SearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other