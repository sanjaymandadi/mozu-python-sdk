
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class InStockNotificationSubscription(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		client.withApiContext(apiContext);
	
	def getInStockNotificationSubscriptions(self,startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		""" Retrieves a list of in-stock notification subscriptions.
		
		Args:
			| startIndex (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with a PageSize of 25, to get the 51st through the 75th items, use startIndex=3.
			| pageSize (int) - The number of results to display on each page when creating paged results from a query. The maximum value is 200.
			| sortBy (string) - The property by which to sort results and whether the results appear in ascending (a-z) order, represented by ASC or in descending (z-a) order, represented by DESC. The sortBy parameter follows an available property. For example: "sortBy=productCode+asc"
			| filter (string) - A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| InStockNotificationSubscriptionCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/instocknotifications/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getInStockNotificationSubscription(self,id, responseFields = None):
		""" Retrieves the details of a subscription that sends a push notification when a product is available in a site's active stock.
		
		Args:
			| id (int) - Unique identifier of the customer segment to retrieve.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| InStockNotificationSubscription 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/instocknotifications/{id}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("id", id);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addInStockNotificationSubscription(self,inStockNotificationSubscription, responseFields = None):
		""" Creates a new subscription that notifies the customer when the product specified in the request is available in the active inventory of the defined location.
		
		Args:
			| inStockNotificationSubscription(inStockNotificationSubscription) - Properties of a push notification to which the shopper subscribes. This notification sends the shopper an alert when a new product or a product previously out of stock becomes available in the specified location's active product inventory.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| InStockNotificationSubscription 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/instocknotifications/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(inStockNotificationSubscription).execute();
		return self.client.result();

	
		
	def deleteInStockNotificationSubscription(self,id):
		""" Deletes a subscription for a customer in-stock notification.
		
		Args:
			| id (int) - Unique identifier of the customer segment to retrieve.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/instocknotifications/{id}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("id", id);
		self.client.withResourceUrl(url).execute();

	
	
	