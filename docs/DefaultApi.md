# sources-api-client.DefaultApi

All URIs are relative to *https://cloud.redhat.com//api/sources/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application**](DefaultApi.md#create_application) | **POST** /applications | Create a new Application
[**create_authentication**](DefaultApi.md#create_authentication) | **POST** /authentications | Create a new Authentication
[**create_endpoint**](DefaultApi.md#create_endpoint) | **POST** /endpoints | Create a new Endpoint
[**create_source**](DefaultApi.md#create_source) | **POST** /sources | Create a new Source
[**create_source_type**](DefaultApi.md#create_source_type) | **POST** /source_types | Create a new SourceType
[**delete_application**](DefaultApi.md#delete_application) | **DELETE** /applications/{id} | Delete an existing Application
[**delete_authentication**](DefaultApi.md#delete_authentication) | **DELETE** /authentications/{id} | Delete an existing Authentication
[**delete_endpoint**](DefaultApi.md#delete_endpoint) | **DELETE** /endpoints/{id} | Delete an existing Endpoint
[**delete_source**](DefaultApi.md#delete_source) | **DELETE** /sources/{id} | Delete an existing Source
[**get_documentation**](DefaultApi.md#get_documentation) | **GET** /openapi.json | Return this API document in JSON format
[**list_application_types**](DefaultApi.md#list_application_types) | **GET** /application_types | List ApplicationTypes
[**list_applications**](DefaultApi.md#list_applications) | **GET** /applications | List Applications
[**list_authentications**](DefaultApi.md#list_authentications) | **GET** /authentications | List Authentications
[**list_endpoint_authentications**](DefaultApi.md#list_endpoint_authentications) | **GET** /endpoints/{id}/authentications | List Authentications for Endpoint
[**list_endpoints**](DefaultApi.md#list_endpoints) | **GET** /endpoints | List Endpoints
[**list_source_applications**](DefaultApi.md#list_source_applications) | **GET** /sources/{id}/applications | List Applications for Source
[**list_source_endpoints**](DefaultApi.md#list_source_endpoints) | **GET** /sources/{id}/endpoints | List Endpoints for Source
[**list_source_type_sources**](DefaultApi.md#list_source_type_sources) | **GET** /source_types/{id}/sources | List Sources for SourceType
[**list_source_types**](DefaultApi.md#list_source_types) | **GET** /source_types | List SourceTypes
[**list_sources**](DefaultApi.md#list_sources) | **GET** /sources | List Sources
[**show_application**](DefaultApi.md#show_application) | **GET** /applications/{id} | Show an existing Application
[**show_application_type**](DefaultApi.md#show_application_type) | **GET** /application_types/{id} | Show an existing ApplicationType
[**show_authentication**](DefaultApi.md#show_authentication) | **GET** /authentications/{id} | Show an existing Authentication
[**show_endpoint**](DefaultApi.md#show_endpoint) | **GET** /endpoints/{id} | Show an existing Endpoint
[**show_source**](DefaultApi.md#show_source) | **GET** /sources/{id} | Show an existing Source
[**show_source_type**](DefaultApi.md#show_source_type) | **GET** /source_types/{id} | Show an existing SourceType
[**update_authentication**](DefaultApi.md#update_authentication) | **PATCH** /authentications/{id} | Update an existing Authentication
[**update_endpoint**](DefaultApi.md#update_endpoint) | **PATCH** /endpoints/{id} | Update an existing Endpoint
[**update_source**](DefaultApi.md#update_source) | **PATCH** /sources/{id} | Update an existing Source


# **create_application**
> Application create_application(application)

Create a new Application

Creates a Application object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
application = sources-api-client.Application() # Application | Application attributes to create

try:
    # Create a new Application
    api_response = api_instance.create_application(application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | [**Application**](Application.md)| Application attributes to create | 

### Return type

[**Application**](Application.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_authentication**
> Authentication create_authentication(authentication)

Create a new Authentication

Creates a Authentication object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
authentication = sources-api-client.Authentication() # Authentication | Authentication attributes to create

try:
    # Create a new Authentication
    api_response = api_instance.create_authentication(authentication)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_authentication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentication** | [**Authentication**](Authentication.md)| Authentication attributes to create | 

### Return type

[**Authentication**](Authentication.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_endpoint**
> Endpoint create_endpoint(endpoint)

Create a new Endpoint

Creates a Endpoint object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
endpoint = sources-api-client.Endpoint() # Endpoint | Endpoint attributes to create

try:
    # Create a new Endpoint
    api_response = api_instance.create_endpoint(endpoint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | [**Endpoint**](Endpoint.md)| Endpoint attributes to create | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_source**
> Source create_source(source)

Create a new Source

Creates a Source object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
source = sources-api-client.Source() # Source | Source attributes to create

try:
    # Create a new Source
    api_response = api_instance.create_source(source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | [**Source**](Source.md)| Source attributes to create | 

### Return type

[**Source**](Source.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_source_type**
> SourceType create_source_type(source_type)

Create a new SourceType

Creates a SourceType object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
source_type = sources-api-client.SourceType() # SourceType | SourceType attributes to create

try:
    # Create a new SourceType
    api_response = api_instance.create_source_type(source_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_source_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_type** | [**SourceType**](SourceType.md)| SourceType attributes to create | 

### Return type

[**SourceType**](SourceType.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application**
> delete_application(id)

Delete an existing Application

Deletes a Application object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    # Delete an existing Application
    api_instance.delete_application(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

void (empty response body)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authentication**
> delete_authentication(id)

Delete an existing Authentication

Deletes a Authentication object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    # Delete an existing Authentication
    api_instance.delete_authentication(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_authentication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

void (empty response body)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_endpoint**
> delete_endpoint(id)

Delete an existing Endpoint

Deletes a Endpoint object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    # Delete an existing Endpoint
    api_instance.delete_endpoint(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

void (empty response body)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_source**
> delete_source(id)

Delete an existing Source

Deletes a Source object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    # Delete an existing Source
    api_instance.delete_source(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

void (empty response body)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documentation**
> get_documentation()

Return this API document in JSON format

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))

try:
    # Return this API document in JSON format
    api_instance.get_documentation()
except ApiException as e:
    print("Exception when calling DefaultApi->get_documentation: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_types**
> ApplicationTypesCollection list_application_types(limit=limit, offset=offset, filter=filter)

List ApplicationTypes

Returns an array of ApplicationType objects

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
limit = 100 # int | The numbers of items to return per page. (optional) (default to 100)
offset = 0 # int | The number of items to skip before starting to collect the result set. (optional) (default to 0)
filter = NULL # object | Filter for querying collections. (optional)

try:
    # List ApplicationTypes
    api_response = api_instance.list_application_types(limit=limit, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_application_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return per page. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **filter** | [**object**](.md)| Filter for querying collections. | [optional] 

### Return type

[**ApplicationTypesCollection**](ApplicationTypesCollection.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_applications**
> ApplicationsCollection list_applications(limit=limit, offset=offset, filter=filter)

List Applications

Returns an array of Application objects

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
limit = 100 # int | The numbers of items to return per page. (optional) (default to 100)
offset = 0 # int | The number of items to skip before starting to collect the result set. (optional) (default to 0)
filter = NULL # object | Filter for querying collections. (optional)

try:
    # List Applications
    api_response = api_instance.list_applications(limit=limit, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return per page. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **filter** | [**object**](.md)| Filter for querying collections. | [optional] 

### Return type

[**ApplicationsCollection**](ApplicationsCollection.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_authentications**
> AuthenticationsCollection list_authentications(limit=limit, offset=offset, filter=filter)

List Authentications

Returns an array of Authentication objects

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
limit = 100 # int | The numbers of items to return per page. (optional) (default to 100)
offset = 0 # int | The number of items to skip before starting to collect the result set. (optional) (default to 0)
filter = NULL # object | Filter for querying collections. (optional)

try:
    # List Authentications
    api_response = api_instance.list_authentications(limit=limit, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_authentications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return per page. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **filter** | [**object**](.md)| Filter for querying collections. | [optional] 

### Return type

[**AuthenticationsCollection**](AuthenticationsCollection.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_endpoint_authentications**
> AuthenticationsCollection list_endpoint_authentications(id, limit=limit, offset=offset, filter=filter)

List Authentications for Endpoint

Returns an array of Authentication objects

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource
limit = 100 # int | The numbers of items to return per page. (optional) (default to 100)
offset = 0 # int | The number of items to skip before starting to collect the result set. (optional) (default to 0)
filter = NULL # object | Filter for querying collections. (optional)

try:
    # List Authentications for Endpoint
    api_response = api_instance.list_endpoint_authentications(id, limit=limit, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_endpoint_authentications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **limit** | **int**| The numbers of items to return per page. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **filter** | [**object**](.md)| Filter for querying collections. | [optional] 

### Return type

[**AuthenticationsCollection**](AuthenticationsCollection.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_endpoints**
> EndpointsCollection list_endpoints(limit=limit, offset=offset, filter=filter)

List Endpoints

Returns an array of Endpoint objects

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
limit = 100 # int | The numbers of items to return per page. (optional) (default to 100)
offset = 0 # int | The number of items to skip before starting to collect the result set. (optional) (default to 0)
filter = NULL # object | Filter for querying collections. (optional)

try:
    # List Endpoints
    api_response = api_instance.list_endpoints(limit=limit, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_endpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return per page. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **filter** | [**object**](.md)| Filter for querying collections. | [optional] 

### Return type

[**EndpointsCollection**](EndpointsCollection.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_source_applications**
> ApplicationsCollection list_source_applications(id, limit=limit, offset=offset, filter=filter)

List Applications for Source

Returns an array of Application objects

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource
limit = 100 # int | The numbers of items to return per page. (optional) (default to 100)
offset = 0 # int | The number of items to skip before starting to collect the result set. (optional) (default to 0)
filter = NULL # object | Filter for querying collections. (optional)

try:
    # List Applications for Source
    api_response = api_instance.list_source_applications(id, limit=limit, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_source_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **limit** | **int**| The numbers of items to return per page. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **filter** | [**object**](.md)| Filter for querying collections. | [optional] 

### Return type

[**ApplicationsCollection**](ApplicationsCollection.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_source_endpoints**
> EndpointsCollection list_source_endpoints(id, limit=limit, offset=offset, filter=filter)

List Endpoints for Source

Returns an array of Endpoint objects

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource
limit = 100 # int | The numbers of items to return per page. (optional) (default to 100)
offset = 0 # int | The number of items to skip before starting to collect the result set. (optional) (default to 0)
filter = NULL # object | Filter for querying collections. (optional)

try:
    # List Endpoints for Source
    api_response = api_instance.list_source_endpoints(id, limit=limit, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_source_endpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **limit** | **int**| The numbers of items to return per page. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **filter** | [**object**](.md)| Filter for querying collections. | [optional] 

### Return type

[**EndpointsCollection**](EndpointsCollection.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_source_type_sources**
> SourcesCollection list_source_type_sources(id, limit=limit, offset=offset, filter=filter)

List Sources for SourceType

Returns an array of Source objects

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource
limit = 100 # int | The numbers of items to return per page. (optional) (default to 100)
offset = 0 # int | The number of items to skip before starting to collect the result set. (optional) (default to 0)
filter = NULL # object | Filter for querying collections. (optional)

try:
    # List Sources for SourceType
    api_response = api_instance.list_source_type_sources(id, limit=limit, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_source_type_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **limit** | **int**| The numbers of items to return per page. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **filter** | [**object**](.md)| Filter for querying collections. | [optional] 

### Return type

[**SourcesCollection**](SourcesCollection.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_source_types**
> SourceTypesCollection list_source_types(limit=limit, offset=offset, filter=filter)

List SourceTypes

Returns an array of SourceType objects

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
limit = 100 # int | The numbers of items to return per page. (optional) (default to 100)
offset = 0 # int | The number of items to skip before starting to collect the result set. (optional) (default to 0)
filter = NULL # object | Filter for querying collections. (optional)

try:
    # List SourceTypes
    api_response = api_instance.list_source_types(limit=limit, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_source_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return per page. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **filter** | [**object**](.md)| Filter for querying collections. | [optional] 

### Return type

[**SourceTypesCollection**](SourceTypesCollection.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sources**
> SourcesCollection list_sources(limit=limit, offset=offset, filter=filter)

List Sources

Returns an array of Source objects

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
limit = 100 # int | The numbers of items to return per page. (optional) (default to 100)
offset = 0 # int | The number of items to skip before starting to collect the result set. (optional) (default to 0)
filter = NULL # object | Filter for querying collections. (optional)

try:
    # List Sources
    api_response = api_instance.list_sources(limit=limit, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return per page. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional] [default to 0]
 **filter** | [**object**](.md)| Filter for querying collections. | [optional] 

### Return type

[**SourcesCollection**](SourcesCollection.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_application**
> Application show_application(id)

Show an existing Application

Returns a Application object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    # Show an existing Application
    api_response = api_instance.show_application(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->show_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**Application**](Application.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_application_type**
> ApplicationType show_application_type(id)

Show an existing ApplicationType

Returns a ApplicationType object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    # Show an existing ApplicationType
    api_response = api_instance.show_application_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->show_application_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**ApplicationType**](ApplicationType.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_authentication**
> Authentication show_authentication(id)

Show an existing Authentication

Returns a Authentication object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    # Show an existing Authentication
    api_response = api_instance.show_authentication(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->show_authentication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**Authentication**](Authentication.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_endpoint**
> Endpoint show_endpoint(id)

Show an existing Endpoint

Returns a Endpoint object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    # Show an existing Endpoint
    api_response = api_instance.show_endpoint(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->show_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_source**
> Source show_source(id)

Show an existing Source

Returns a Source object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    # Show an existing Source
    api_response = api_instance.show_source(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->show_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**Source**](Source.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_source_type**
> SourceType show_source_type(id)

Show an existing SourceType

Returns a SourceType object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource

try:
    # Show an existing SourceType
    api_response = api_instance.show_source_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->show_source_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 

### Return type

[**SourceType**](SourceType.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_authentication**
> update_authentication(id, authentication)

Update an existing Authentication

Updates a Authentication object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource
authentication = sources-api-client.Authentication() # Authentication | Authentication attributes to update

try:
    # Update an existing Authentication
    api_instance.update_authentication(id, authentication)
except ApiException as e:
    print("Exception when calling DefaultApi->update_authentication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **authentication** | [**Authentication**](Authentication.md)| Authentication attributes to update | 

### Return type

void (empty response body)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_endpoint**
> update_endpoint(id, endpoint)

Update an existing Endpoint

Updates a Endpoint object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource
endpoint = sources-api-client.Endpoint() # Endpoint | Endpoint attributes to update

try:
    # Update an existing Endpoint
    api_instance.update_endpoint(id, endpoint)
except ApiException as e:
    print("Exception when calling DefaultApi->update_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **endpoint** | [**Endpoint**](Endpoint.md)| Endpoint attributes to update | 

### Return type

void (empty response body)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_source**
> update_source(id, source)

Update an existing Source

Updates a Source object

### Example

* Basic Authentication (UserSecurity): 
```python
from __future__ import print_function
import time
import sources-api-client
from sources-api-client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: UserSecurity
configuration = sources-api-client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = sources-api-client.DefaultApi(sources-api-client.ApiClient(configuration))
id = 'id_example' # str | ID of the resource
source = sources-api-client.Source() # Source | Source attributes to update

try:
    # Update an existing Source
    api_instance.update_source(id, source)
except ApiException as e:
    print("Exception when calling DefaultApi->update_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **source** | [**Source**](Source.md)| Source attributes to update | 

### Return type

void (empty response body)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

