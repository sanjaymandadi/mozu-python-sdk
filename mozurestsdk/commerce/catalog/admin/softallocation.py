
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class SoftAllocation(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		client.withApiContext(apiContext);
	
	def getSoftAllocations(self,startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		"""
			Retrieves a list of sof allocations according to any specified filter criteria and sort options.
			Request Params
				string filter A set of filter expressions representing the search parameters for a query: eq=equals, ne=not equals, gt=greater than, lt = less than or equals, gt = greater than or equals, lt = less than or equals, sw = starts with, or cont = contains. Optional.
				int pageSize The number of results to display on each page when creating paged results from a query. The amount is divided and displayed on the `pageCount `amount of pages. The default is 20 and maximum value is 200 per page.
				string responseFields A list or array of fields returned for a call. These fields may be customized and may be used for various types of data calls in Mozu. For example, responseFields are returned for retrieving or updating attributes, carts, and messages in Mozu.
				string sortBy The element to sort the results by and the channel in which the results appear. Either ascending (a-z) or descending (z-a) channel. Optional.
				int startIndex When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with a `pageSize `of 25, to get the 51st through the 75th items, use `startIndex=3`.
			Response
				SoftAllocationCollection 
		"""

		url = MozuUrl("/api/commerce/catalog/admin/softallocations/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getSoftAllocation(self,softAllocationId, responseFields = None):
		"""
			Retrieves the details of a soft allocation.
			Request Params
				string responseFields A list or array of fields returned for a call. These fields may be customized and may be used for various types of data calls in Mozu. For example, responseFields are returned for retrieving or updating attributes, carts, and messages in Mozu.
				int softAllocationId 
			Response
				SoftAllocation 
		"""

		url = MozuUrl("/api/commerce/catalog/admin/softallocations/{softAllocationId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("softAllocationId", softAllocationId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addSoftAllocations(self,softAllocationsIn):
		"""
			Creates a new product reservation for a product. This places a hold on the product inventory for the quantity specified during the ordering process.
			Request Params
				array|softAllocationsIn Mozu.ProductAdmin.Contracts.SoftAllocation ApiType DOCUMENT_HERE 
			Response
				array|SoftAllocation 
		"""

		url = MozuUrl("/api/commerce/catalog/admin/softallocations/", "POST", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).withBody(softAllocationsIn).execute();
		return self.client.result();

	
		
	def convertToProductReservation(self,softAllocations):
		"""
			Converts a set of existing softAllocations into productReservations
			Request Params
				array|softAllocations Mozu.ProductAdmin.Contracts.SoftAllocation ApiType DOCUMENT_HERE 
			Response
				array|ProductReservation 
		"""

		url = MozuUrl("/api/commerce/catalog/admin/softallocations/convert", "POST", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).withBody(softAllocations).execute();
		return self.client.result();

	
		
	def renewSoftAllocations(self,softAllocationRenew):
		"""
			Updates a set of softAllocations expiration time in a non trassactional batch
			Request Params
				softAllocationRenew Mozu.ProductAdmin.Contracts.SoftAllocationRenew ApiType DOCUMENT_HERE 
			Response
				array|SoftAllocation 
		"""

		url = MozuUrl("/api/commerce/catalog/admin/softallocations/renew", "POST", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).withBody(softAllocationRenew).execute();
		return self.client.result();

	
		
	def updateSoftAllocations(self,softAllocations):
		"""
			Updates a soft allocationt. This updates a hold on the product inventory for the quantity specified during the ordering process.
			Request Params
				array|softAllocations Mozu.ProductAdmin.Contracts.SoftAllocation ApiType DOCUMENT_HERE 
			Response
				array|SoftAllocation 
		"""

		url = MozuUrl("/api/commerce/catalog/admin/softallocations/", "PUT", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).withBody(softAllocations).execute();
		return self.client.result();

	
		
	def deleteSoftAllocation(self,softAllocationId):
		"""
			Deletes a soft allocation. You might delete a allocation when an order or cart is not processed to return the product quantity back to inventory.
			Request Params
				int softAllocationId 
			Response
		"""

		url = MozuUrl("/api/commerce/catalog/admin/softallocations/{softAllocationId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("softAllocationId", softAllocationId);
		self.client.withResourceUrl(url).execute();

	
	
	