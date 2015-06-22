
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Location(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		client.withApiContext(apiContext);
	
	def getLocations(self,startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		"""
			Retrieves a list of all locations associated with a tenant, according to any filter and sort criteria specified in the request.
			Request Params
				string filter A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
				int pageSize The number of results to display on each page when creating paged results from a query. The maximum value is 200.
				string responseFields Use this field to include those fields which are not included by default.
				string sortBy The property by which to sort results and whether the results appear in ascending (a-z) order, represented by ASC or in descending (z-a) order, represented by DESC. The sortBy parameter follows an available property. For example: "sortBy=productCode+asc"
				int startIndex When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with a PageSize of 25, to get the 51st through the 75th items, use startIndex=3.
			Response
				LocationCollection 
		"""

		url = MozuUrl("/api/commerce/admin/locations/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getLocation(self,locationCode, responseFields = None):
		"""
			Retrieves the details of the location specified in the request by location code.
			Request Params
				string locationCode The unique, user-defined code that identifies a location. 
				string responseFields A list or array of fields returned for a call. These fields may be customized and may be used for various types of data calls in Mozu. For example, responseFields are returned for retrieving or updating attributes, carts, and messages in Mozu.
			Response
				Location 
		"""

		url = MozuUrl("/api/commerce/admin/locations/{locationCode}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("locationCode", locationCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addLocation(self,location, responseFields = None):
		"""
			Creates a new physical location for the tenant specified in the request header.
			Request Params
				string responseFields A list or array of fields returned for a call. These fields may be customized and may be used for various types of data calls in Mozu. For example, responseFields are returned for retrieving or updating attributes, carts, and messages in Mozu.
				location Properties of a physical location a tenant uses to manage inventory and fulfills orders, provide store finder functionality, or both.
			Response
				Location 
		"""

		url = MozuUrl("/api/commerce/admin/locations/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(location).execute();
		return self.client.result();

	
		
	def updateLocation(self,location, locationCode, responseFields = None):
		"""
			Updates one or more details of a the location specified in the request by location code.
			Request Params
				string locationCode The unique, user-defined code that identifies a location. 
				string responseFields Use this field to include those fields which are not included by default.
				location Properties of a physical location a tenant uses to manage inventory and fulfills orders, provide store finder functionality, or both.
			Response
				Location 
		"""

		url = MozuUrl("/api/commerce/admin/locations/{locationCode}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("locationCode", locationCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(location).execute();
		return self.client.result();

	
		
	def deleteLocation(self,locationCode):
		"""
			Deletes the location specified in the request.
			Request Params
				string locationCode The unique, user-defined code that identifies a location. 
			Response
		"""

		url = MozuUrl("/api/commerce/admin/locations/{locationCode}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("locationCode", locationCode);
		self.client.withResourceUrl(url).execute();

	
	
	