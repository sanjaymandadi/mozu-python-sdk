
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class EntityList(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		client.withApiContext(apiContext);
	
	def getEntityLists(self,pageSize = None, startIndex = None, filter = None, sortBy = None, responseFields = None):
		"""
			Get a filtered list of EntityLists for a specific tenant.
			Request Params
				string filter A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
				int pageSize The number of results to display on each page when creating paged results from a query. The amount is divided and displayed on the `pageCount `amount of pages. The default is 20 and maximum value is 200 per page.
				string responseFields Use this field to include those fields which are not included by default.
				string sortBy The element to sort the results by and the channel in which the results appear. Either ascending (a-z) or descending (z-a) channel. Optional.
				int startIndex When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with a `pageSize `of 25, to get the 51st through the 75th items, use `startIndex=3`.
			Response
				EntityListCollection 
		"""

		url = MozuUrl("/api/platform/entitylists/?pageSize={pageSize}&startIndex={startIndex}&filter={filter}&sortBy={sortBy}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getEntityList(self,entityListFullName, responseFields = None):
		"""
			Get an existing EntityList definition for a specific tenant
			Request Params
				string entityListFullName The full name of the EntityList including namespace in name@nameSpace format
				string responseFields Use this field to include those fields which are not included by default.
			Response
				EntityList 
		"""

		url = MozuUrl("/api/platform/entitylists/{entityListFullName}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("entityListFullName", entityListFullName);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createEntityList(self,entityList, responseFields = None):
		"""
			Create a new EntityList for a specific tenant.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
				entityList The definition of an MZDB EntityList which describes the characteristics of the EntityList on a per tenant basis. EntityLists are created at the tenant level, but instances of the EntityLists are implicitly created at the appropriate context level as entities are added or removed from the EntityList.
			Response
				EntityList 
		"""

		url = MozuUrl("/api/platform/entitylists/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(entityList).execute();
		return self.client.result();

	
		
	def updateEntityList(self,entityList, entityListFullName, responseFields = None):
		"""
			Update an existing Entitylist for a specific tenant.
			Request Params
				string entityListFullName The full name of the EntityList including namespace in name@nameSpace format
				string responseFields Use this field to include those fields which are not included by default.
				entityList The definition of an MZDB EntityList which describes the characteristics of the EntityList on a per tenant basis. EntityLists are created at the tenant level, but instances of the EntityLists are implicitly created at the appropriate context level as entities are added or removed from the EntityList.
			Response
				EntityList 
		"""

		url = MozuUrl("/api/platform/entitylists/{entityListFullName}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("entityListFullName", entityListFullName);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(entityList).execute();
		return self.client.result();

	
		
	def deleteEntityList(self,entityListFullName):
		"""
			Delete an existing EntityList for a specific tenant. This will also delete all Entities in all instances of this EntityList for the tenant.
			Request Params
				string entityListFullName The full name of the EntityList including namespace in name@nameSpace format
			Response
		"""

		url = MozuUrl("/api/platform/entitylists/{entityListFullName}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("entityListFullName", entityListFullName);
		self.client.withResourceUrl(url).execute();

	
	
	