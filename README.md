# swagger-client
The FoodData Central API provides REST access to FoodData Central (FDC). It is intended primarily to assist application developers wishing to incorporate nutrient data into their applications or websites.   To take full advantage of the API, developers should familiarize themselves with the database by reading the database documentation available via links on [Data Type Documentation](https://fdc.nal.usda.gov/data-documentation.html). This documentation provides the detailed definitions and descriptions needed to understand the data elements referenced in the API documentation.      Additional details about the API including rate limits, access, and licensing are available on the [FDC website](https://fdc.nal.usda.gov/api-guide.html)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://nal.altarama.com/reft100.aspx?key=FoodData](https://nal.altarama.com/reft100.aspx?key=FoodData)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FDCApi(swagger_client.ApiClient(configuration))
fdc_id = 'fdc_id_example' # str | FDC id of the food to retrieve
format = 'format_example' # str | Optional. 'abridged' for an abridged set of elements, 'full' for all elements (default). (optional)
nutrients = [56] # list[int] | Optional. List of up to 25 nutrient numbers. Only the nutrient information for the specified nutrients will be returned. Should be comma separated list (e.g. nutrients=203,204) or repeating parameters (e.g. nutrients=203&nutrients=204). If a food does not have any matching nutrients, the food will be returned with an empty foodNutrients element. (optional)

try:
    # Fetches details for one food item by FDC ID
    api_response = api_instance.get_food(fdc_id, format=format, nutrients=nutrients)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FDCApi->get_food: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FDCApi(swagger_client.ApiClient(configuration))
fdc_ids = ['fdc_ids_example'] # list[str] | List of multiple FDC ID's. Should be comma separated list (e.g. fdcIds=534358,373052) or repeating parameters (e.g. fdcIds=534358&fdcIds=373052).
format = 'format_example' # str | Optional. 'abridged' for an abridged set of elements, 'full' for all elements (default). (optional)
nutrients = [56] # list[int] | Optional. List of up to 25 nutrient numbers. Only the nutrient information for the specified nutrients will be returned. Should be comma separated list (e.g. nutrients=203,204) or repeating parameters (e.g. nutrients=203&nutrients=204). If a food does not have any matching nutrients, the food will be returned with an empty foodNutrients element. (optional)

try:
    # Fetches details for multiple food items using input FDC IDs
    api_response = api_instance.get_foods(fdc_ids, format=format, nutrients=nutrients)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FDCApi->get_foods: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FDCApi(swagger_client.ApiClient(configuration))
data_type = ['data_type_example'] # list[str] | Optional. Filter on a specific data type; specify one or more values in an array. (optional)
page_size = 56 # int | Optional. Maximum number of results to return for the current page. Default is 50. (optional)
page_number = 56 # int | Optional. Page number to retrieve. The offset into the overall result set is expressed as (pageNumber * pageSize) (optional)
sort_by = 'sort_by_example' # str | Optional. Specify one of the possible values to sort by that field. Note, dataType.keyword will be dataType and lowercaseDescription.keyword will be description in future releases. (optional)
sort_order = 'sort_order_example' # str | Optional. The sort direction for the results. Only applicable if sortBy is specified. (optional)

try:
    # Returns a paged list of foods, in the 'abridged' format
    api_response = api_instance.get_foods_list(data_type=data_type, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FDCApi->get_foods_list: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FDCApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | One or more search terms.  The string may include [search operators](https://fdc.nal.usda.gov/help.html#bkmk-2)
data_type = ['data_type_example'] # list[str] | Optional. Filter on a specific data type; specify one or more values in an array. (optional)
page_size = 56 # int | Optional. Maximum number of results to return for the current page. Default is 50. (optional)
page_number = 56 # int | Optional. Page number to retrieve. The offset into the overall result set is expressed as (pageNumber * pageSize) (optional)
sort_by = 'sort_by_example' # str | Optional. Specify one of the possible values to sort by that field. Note, dataType.keyword will be dataType and lowercaseDescription.keyword will be description in future releases. (optional)
sort_order = 'sort_order_example' # str | Optional. The sort direction for the results. Only applicable if sortBy is specified. (optional)
brand_owner = 'brand_owner_example' # str | Optional. Filter results based on the brand owner of the food. Only applies to Branded Foods (optional)

try:
    # Returns a list of foods that matched search (query) keywords
    api_response = api_instance.get_foods_search(query, data_type=data_type, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, brand_owner=brand_owner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FDCApi->get_foods_search: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FDCApi(swagger_client.ApiClient(configuration))

try:
    # Returns this documentation in JSON format
    api_instance.get_json_spec()
except ApiException as e:
    print("Exception when calling FDCApi->get_json_spec: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FDCApi(swagger_client.ApiClient(configuration))

try:
    # Returns this documentation in JSON format
    api_instance.get_yaml_spec()
except ApiException as e:
    print("Exception when calling FDCApi->get_yaml_spec: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FDCApi(swagger_client.ApiClient(configuration))
body = swagger_client.FoodsCriteria() # FoodsCriteria | 

try:
    # Fetches details for multiple food items using input FDC IDs
    api_response = api_instance.post_foods(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FDCApi->post_foods: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FDCApi(swagger_client.ApiClient(configuration))
body = swagger_client.FoodListCriteria() # FoodListCriteria | 

try:
    # Returns a paged list of foods, in the 'abridged' format
    api_response = api_instance.post_foods_list(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FDCApi->post_foods_list: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FDCApi(swagger_client.ApiClient(configuration))
body = swagger_client.FoodSearchCriteria() # FoodSearchCriteria | The query string may also include standard [search operators](https://fdc.nal.usda.gov/help.html#bkmk-2)

try:
    # Returns a list of foods that matched search (query) keywords
    api_response = api_instance.post_foods_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FDCApi->post_foods_search: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.nal.usda.gov/fdc*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FDCApi* | [**get_food**](docs/FDCApi.md#get_food) | **GET** /v1/food/{fdcId} | Fetches details for one food item by FDC ID
*FDCApi* | [**get_foods**](docs/FDCApi.md#get_foods) | **GET** /v1/foods | Fetches details for multiple food items using input FDC IDs
*FDCApi* | [**get_foods_list**](docs/FDCApi.md#get_foods_list) | **GET** /v1/foods/list | Returns a paged list of foods, in the &#x27;abridged&#x27; format
*FDCApi* | [**get_foods_search**](docs/FDCApi.md#get_foods_search) | **GET** /v1/foods/search | Returns a list of foods that matched search (query) keywords
*FDCApi* | [**get_json_spec**](docs/FDCApi.md#get_json_spec) | **GET** /v1/json-spec | Returns this documentation in JSON format
*FDCApi* | [**get_yaml_spec**](docs/FDCApi.md#get_yaml_spec) | **GET** /v1/yaml-spec | Returns this documentation in JSON format
*FDCApi* | [**post_foods**](docs/FDCApi.md#post_foods) | **POST** /v1/foods | Fetches details for multiple food items using input FDC IDs
*FDCApi* | [**post_foods_list**](docs/FDCApi.md#post_foods_list) | **POST** /v1/foods/list | Returns a paged list of foods, in the &#x27;abridged&#x27; format
*FDCApi* | [**post_foods_search**](docs/FDCApi.md#post_foods_search) | **POST** /v1/foods/search | Returns a list of foods that matched search (query) keywords

## Documentation For Models

 - [AbridgedFoodItem](docs/AbridgedFoodItem.md)
 - [AbridgedFoodNutrient](docs/AbridgedFoodNutrient.md)
 - [BrandedFoodItem](docs/BrandedFoodItem.md)
 - [BrandedFoodItemLabelNutrients](docs/BrandedFoodItemLabelNutrients.md)
 - [BrandedFoodItemLabelNutrientsCalcium](docs/BrandedFoodItemLabelNutrientsCalcium.md)
 - [BrandedFoodItemLabelNutrientsCalories](docs/BrandedFoodItemLabelNutrientsCalories.md)
 - [BrandedFoodItemLabelNutrientsCarbohydrates](docs/BrandedFoodItemLabelNutrientsCarbohydrates.md)
 - [BrandedFoodItemLabelNutrientsFat](docs/BrandedFoodItemLabelNutrientsFat.md)
 - [BrandedFoodItemLabelNutrientsFiber](docs/BrandedFoodItemLabelNutrientsFiber.md)
 - [BrandedFoodItemLabelNutrientsIron](docs/BrandedFoodItemLabelNutrientsIron.md)
 - [BrandedFoodItemLabelNutrientsPotassium](docs/BrandedFoodItemLabelNutrientsPotassium.md)
 - [BrandedFoodItemLabelNutrientsProtein](docs/BrandedFoodItemLabelNutrientsProtein.md)
 - [BrandedFoodItemLabelNutrientsSaturatedFat](docs/BrandedFoodItemLabelNutrientsSaturatedFat.md)
 - [BrandedFoodItemLabelNutrientsSugars](docs/BrandedFoodItemLabelNutrientsSugars.md)
 - [BrandedFoodItemLabelNutrientsTransFat](docs/BrandedFoodItemLabelNutrientsTransFat.md)
 - [FoodAttribute](docs/FoodAttribute.md)
 - [FoodAttributeFoodAttributeType](docs/FoodAttributeFoodAttributeType.md)
 - [FoodCategory](docs/FoodCategory.md)
 - [FoodComponent](docs/FoodComponent.md)
 - [FoodListCriteria](docs/FoodListCriteria.md)
 - [FoodNutrient](docs/FoodNutrient.md)
 - [FoodNutrientDerivation](docs/FoodNutrientDerivation.md)
 - [FoodNutrientSource](docs/FoodNutrientSource.md)
 - [FoodPortion](docs/FoodPortion.md)
 - [FoodSearchCriteria](docs/FoodSearchCriteria.md)
 - [FoodUpdateLog](docs/FoodUpdateLog.md)
 - [FoodsCriteria](docs/FoodsCriteria.md)
 - [FoundationFoodItem](docs/FoundationFoodItem.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InputFoodFoundation](docs/InputFoodFoundation.md)
 - [InputFoodSurvey](docs/InputFoodSurvey.md)
 - [MeasureUnit](docs/MeasureUnit.md)
 - [Nutrient](docs/Nutrient.md)
 - [NutrientAcquisitionDetails](docs/NutrientAcquisitionDetails.md)
 - [NutrientAnalysisDetails](docs/NutrientAnalysisDetails.md)
 - [NutrientConversionFactors](docs/NutrientConversionFactors.md)
 - [OneOfinlineResponse200](docs/OneOfinlineResponse200.md)
 - [RetentionFactor](docs/RetentionFactor.md)
 - [SRLegacyFoodItem](docs/SRLegacyFoodItem.md)
 - [SampleFoodItem](docs/SampleFoodItem.md)
 - [SearchResult](docs/SearchResult.md)
 - [SearchResultFood](docs/SearchResultFood.md)
 - [SurveyFoodItem](docs/SurveyFoodItem.md)
 - [WweiaFoodCategory](docs/WweiaFoodCategory.md)

## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: URL query string


## Author


