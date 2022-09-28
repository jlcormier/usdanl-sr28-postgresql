# swagger_client.FDCApi

All URIs are relative to *https://api.nal.usda.gov/fdc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_food**](FDCApi.md#get_food) | **GET** /v1/food/{fdcId} | Fetches details for one food item by FDC ID
[**get_foods**](FDCApi.md#get_foods) | **GET** /v1/foods | Fetches details for multiple food items using input FDC IDs
[**get_foods_list**](FDCApi.md#get_foods_list) | **GET** /v1/foods/list | Returns a paged list of foods, in the &#x27;abridged&#x27; format
[**get_foods_search**](FDCApi.md#get_foods_search) | **GET** /v1/foods/search | Returns a list of foods that matched search (query) keywords
[**get_json_spec**](FDCApi.md#get_json_spec) | **GET** /v1/json-spec | Returns this documentation in JSON format
[**get_yaml_spec**](FDCApi.md#get_yaml_spec) | **GET** /v1/yaml-spec | Returns this documentation in JSON format
[**post_foods**](FDCApi.md#post_foods) | **POST** /v1/foods | Fetches details for multiple food items using input FDC IDs
[**post_foods_list**](FDCApi.md#post_foods_list) | **POST** /v1/foods/list | Returns a paged list of foods, in the &#x27;abridged&#x27; format
[**post_foods_search**](FDCApi.md#post_foods_search) | **POST** /v1/foods/search | Returns a list of foods that matched search (query) keywords

# **get_food**
> InlineResponse200 get_food(fdc_id, format=format, nutrients=nutrients)

Fetches details for one food item by FDC ID

Retrieves a single food item by an FDC ID. Optional format and nutrients can be specified.

### Example
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fdc_id** | **str**| FDC id of the food to retrieve | 
 **format** | **str**| Optional. &#x27;abridged&#x27; for an abridged set of elements, &#x27;full&#x27; for all elements (default). | [optional] 
 **nutrients** | [**list[int]**](int.md)| Optional. List of up to 25 nutrient numbers. Only the nutrient information for the specified nutrients will be returned. Should be comma separated list (e.g. nutrients&#x3D;203,204) or repeating parameters (e.g. nutrients&#x3D;203&amp;nutrients&#x3D;204). If a food does not have any matching nutrients, the food will be returned with an empty foodNutrients element. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foods**
> list[object] get_foods(fdc_ids, format=format, nutrients=nutrients)

Fetches details for multiple food items using input FDC IDs

Retrieves a list of food items by a list of up to 20 FDC IDs. Optional format and nutrients can be specified. Invalid FDC ID's or ones that are not found are omitted and an empty set is returned if there are no matches.

### Example
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
fdc_ids = ['fdc_ids_example'] # list[str] | List of multiple FDC ID's. Should be comma separated list (e.g. fdcIds=534358,373052) or repeating parameters (e.g. fdcIds=534358&fdcIds=373052).
format = 'format_example' # str | Optional. 'abridged' for an abridged set of elements, 'full' for all elements (default). (optional)
nutrients = [56] # list[int] | Optional. List of up to 25 nutrient numbers. Only the nutrient information for the specified nutrients will be returned. Should be comma separated list (e.g. nutrients=203,204) or repeating parameters (e.g. nutrients=203&nutrients=204). If a food does not have any matching nutrients, the food will be returned with an empty foodNutrients element. (optional)

try:
    # Fetches details for multiple food items using input FDC IDs
    api_response = api_instance.get_foods(fdc_ids, format=format, nutrients=nutrients)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FDCApi->get_foods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fdc_ids** | [**list[str]**](str.md)| List of multiple FDC ID&#x27;s. Should be comma separated list (e.g. fdcIds&#x3D;534358,373052) or repeating parameters (e.g. fdcIds&#x3D;534358&amp;fdcIds&#x3D;373052). | 
 **format** | **str**| Optional. &#x27;abridged&#x27; for an abridged set of elements, &#x27;full&#x27; for all elements (default). | [optional] 
 **nutrients** | [**list[int]**](int.md)| Optional. List of up to 25 nutrient numbers. Only the nutrient information for the specified nutrients will be returned. Should be comma separated list (e.g. nutrients&#x3D;203,204) or repeating parameters (e.g. nutrients&#x3D;203&amp;nutrients&#x3D;204). If a food does not have any matching nutrients, the food will be returned with an empty foodNutrients element. | [optional] 

### Return type

**list[object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foods_list**
> list[AbridgedFoodItem] get_foods_list(data_type=data_type, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order)

Returns a paged list of foods, in the 'abridged' format

Retrieves a paged list of foods. Use the pageNumber parameter to page through the entire result set.

### Example
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_type** | [**list[str]**](str.md)| Optional. Filter on a specific data type; specify one or more values in an array. | [optional] 
 **page_size** | **int**| Optional. Maximum number of results to return for the current page. Default is 50. | [optional] 
 **page_number** | **int**| Optional. Page number to retrieve. The offset into the overall result set is expressed as (pageNumber * pageSize) | [optional] 
 **sort_by** | **str**| Optional. Specify one of the possible values to sort by that field. Note, dataType.keyword will be dataType and lowercaseDescription.keyword will be description in future releases. | [optional] 
 **sort_order** | **str**| Optional. The sort direction for the results. Only applicable if sortBy is specified. | [optional] 

### Return type

[**list[AbridgedFoodItem]**](AbridgedFoodItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foods_search**
> SearchResult get_foods_search(query, data_type=data_type, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, brand_owner=brand_owner)

Returns a list of foods that matched search (query) keywords

Search for foods using keywords. Results can be filtered by dataType and there are options for result page sizes or sorting.

### Example
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| One or more search terms.  The string may include [search operators](https://fdc.nal.usda.gov/help.html#bkmk-2) | 
 **data_type** | [**list[str]**](str.md)| Optional. Filter on a specific data type; specify one or more values in an array. | [optional] 
 **page_size** | **int**| Optional. Maximum number of results to return for the current page. Default is 50. | [optional] 
 **page_number** | **int**| Optional. Page number to retrieve. The offset into the overall result set is expressed as (pageNumber * pageSize) | [optional] 
 **sort_by** | **str**| Optional. Specify one of the possible values to sort by that field. Note, dataType.keyword will be dataType and lowercaseDescription.keyword will be description in future releases. | [optional] 
 **sort_order** | **str**| Optional. The sort direction for the results. Only applicable if sortBy is specified. | [optional] 
 **brand_owner** | **str**| Optional. Filter results based on the brand owner of the food. Only applies to Branded Foods | [optional] 

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_json_spec**
> get_json_spec()

Returns this documentation in JSON format

The OpenAPI 3.0 specification for the FDC API rendered as JSON (JavaScript Object Notation)

### Example
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

try:
    # Returns this documentation in JSON format
    api_instance.get_json_spec()
except ApiException as e:
    print("Exception when calling FDCApi->get_json_spec: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_yaml_spec**
> get_yaml_spec()

Returns this documentation in JSON format

The OpenAPI 3.0 specification for the FDC API rendered as YAML (YAML Ain't Markup Language)

### Example
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

try:
    # Returns this documentation in JSON format
    api_instance.get_yaml_spec()
except ApiException as e:
    print("Exception when calling FDCApi->get_yaml_spec: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_foods**
> list[object] post_foods(body)

Fetches details for multiple food items using input FDC IDs

Retrieves a list of food items by a list of up to 20 FDC IDs. Optional format and nutrients can be specified. Invalid FDC ID's or ones that are not found are omitted and an empty set is returned if there are no matches.

### Example
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
body = swagger_client.FoodsCriteria() # FoodsCriteria | 

try:
    # Fetches details for multiple food items using input FDC IDs
    api_response = api_instance.post_foods(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FDCApi->post_foods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FoodsCriteria**](FoodsCriteria.md)|  | 

### Return type

**list[object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_foods_list**
> list[AbridgedFoodItem] post_foods_list(body)

Returns a paged list of foods, in the 'abridged' format

Retrieves a paged list of foods. Use the pageNumber parameter to page through the entire result set.

### Example
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
body = swagger_client.FoodListCriteria() # FoodListCriteria | 

try:
    # Returns a paged list of foods, in the 'abridged' format
    api_response = api_instance.post_foods_list(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FDCApi->post_foods_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FoodListCriteria**](FoodListCriteria.md)|  | 

### Return type

[**list[AbridgedFoodItem]**](AbridgedFoodItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_foods_search**
> SearchResult post_foods_search(body)

Returns a list of foods that matched search (query) keywords

Search for foods using keywords. Results can be filtered by dataType and there are options for result page sizes or sorting.

### Example
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
body = swagger_client.FoodSearchCriteria() # FoodSearchCriteria | The query string may also include standard [search operators](https://fdc.nal.usda.gov/help.html#bkmk-2)

try:
    # Returns a list of foods that matched search (query) keywords
    api_response = api_instance.post_foods_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FDCApi->post_foods_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FoodSearchCriteria**](FoodSearchCriteria.md)| The query string may also include standard [search operators](https://fdc.nal.usda.gov/help.html#bkmk-2) | 

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

