
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Shipment(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		client.withApiContext(apiContext);
	
	def getShipment(self,orderId, shipmentId, responseFields = None):
		""" Retrieves the details of the order shipment specified in the request.
		
		Args:
			| orderId (string) - Unique identifier of the order.
			| shipmentId (string) - Unique identifier of the shipment to retrieve.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Shipment 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/shipments/{shipmentId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("shipmentId", shipmentId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getAvailableShipmentMethods(self,orderId, draft = False):
		""" Retrieves the available shipping methods applicable to the order. Typically used to display available shipping method options on the checkout page.
		
		Args:
			| orderId (string) - Unique identifier of the order.
			| draft (bool) - If true, retrieve the draft version of the order, which might include uncommitted changes to the order or its components.
		
		Returns:
			| array of ShippingRate 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/shipments/methods?draft={draft}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("draft", draft);
		url.formatUrl("orderId", orderId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createPackageShipments(self,packageIds, orderId):
		""" Creates a shipment from one or more package associated with an order and assign a label and tracking number to an order shipment.
		
		Args:
			| packageIds(array|packageIds) - List of unique identifiers for each package associated with this shipment. Not all packages must belong to the same shipment.
			| orderId (string) - Unique identifier of the order.
		
		Returns:
			| array of Package 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/shipments", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		self.client.withResourceUrl(url).withBody(packageIds).execute();
		return self.client.result();

	
		
	def deleteShipment(self,orderId, shipmentId):
		""" Deletes the shipment specified in the request.
		
		Args:
			| orderId (string) - Unique identifier of the order.
			| shipmentId (string) - Unique identifier of the shipment to retrieve.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/shipments/{shipmentId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("shipmentId", shipmentId);
		self.client.withResourceUrl(url).execute();

	
	
	