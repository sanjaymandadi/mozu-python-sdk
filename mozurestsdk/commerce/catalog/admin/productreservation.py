
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class ProductReservation(object):
	def __init__(self, apiContext: ApiContext = None, dataViewMode="Live", mozuClient = None):
		if (apiContext.dataViewMode is None):
			apiContext.dataViewMode = dataViewMode;
		self.client = mozuClient or default_client();
		self.client.withApiContext(apiContext);
	
	def getProductReservations(self,startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		""" Retrieves a list of product reservations according to any specified filter criteria and sort options.
		
		Args:
			| startIndex (int) - 
			| pageSize (int) - The number of results to display on each page when creating paged results from a query. The maximum value is 200.
			| sortBy (string) - 
			| filter (string) - A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ProductReservationCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/productreservations/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getProductReservation(self,productReservationId, responseFields = None):
		""" Retrieves the details of a product reservation.
		
		Args:
			| productReservationId (int) - Unique identifier of the product reservation.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ProductReservation 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/productreservations/{productReservationId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("productReservationId", productReservationId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addProductReservations(self,productReservations, skipInventoryCheck = False):
		""" Creates a new product reservation for a product. This action places a hold on the product inventory for the quantity specified during the ordering process.
		
		Args:
			| productReservations(array|productReservations) - A hold placed on product inventory for a particular product so that the quantity specified is set aside and available for purchase during the ordering process.
			| skipInventoryCheck (bool) - If true, skip the process to validate inventory when creating this product reservation.
		
		Returns:
			| array of ProductReservation 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/productreservations/?skipInventoryCheck={skipInventoryCheck}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("skipInventoryCheck", skipInventoryCheck);
		self.client.withResourceUrl(url).withBody(productReservations).execute();
		return self.client.result();

	
		
	def commitReservations(self,productReservations):
		""" Commits a product reservation to decrement the product's inventory by the quantity specified then release the reservation once the order process completed successfully.
		
		Args:
			| productReservations(array|productReservations) - A hold placed on product inventory for a particular product so that the quantity specified is set aside and available for purchase during the ordering process.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/productreservations/commit", "POST", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).withBody(productReservations).execute();

	
		
	def updateProductReservations(self,productReservations, skipInventoryCheck = False):
		""" Updates an existing product reservation for a product.
		
		Args:
			| productReservations(array|productReservations) - A hold placed on product inventory for a particular product so that the quantity specified is set aside and available for purchase during the ordering process.
			| skipInventoryCheck (bool) - If true, skip the process to validate inventory when creating this product reservation.
		
		Returns:
			| array of ProductReservation 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/productreservations/?skipInventoryCheck={skipInventoryCheck}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("skipInventoryCheck", skipInventoryCheck);
		self.client.withResourceUrl(url).withBody(productReservations).execute();
		return self.client.result();

	
		
	def deleteProductReservation(self,productReservationId):
		""" Deletes a product reservation. For example, delete a reservation when an order is not processed to return the product quantity back to inventory.
		
		Args:
			| productReservationId (int) - Unique identifier of the product reservation.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/productreservations/{productReservationId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("productReservationId", productReservationId);
		self.client.withResourceUrl(url).execute();

	
	
	