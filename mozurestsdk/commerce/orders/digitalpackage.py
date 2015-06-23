
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class DigitalPackage(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		client.withApiContext(apiContext);
	
	def getAvailableDigitalPackageFulfillmentActions(self,orderId, digitalPackageId):
		""" Retrieves a collection of fulfillment options for digital packages. Options may include emailed files/links or provided links. 
		
		Args:
			| orderId (string) - Unique identifier of the order.
			| digitalPackageId (string) - This parameter supplies package ID to get fulfillment actions for the digital package.
		
		Returns:
			| array of string 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/digitalpackages/{digitalPackageId}/actions", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("digitalPackageId", digitalPackageId);
		url.formatUrl("orderId", orderId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getDigitalPackage(self,orderId, digitalPackageId, responseFields = None):
		""" This operation retreives a digital package within an order and it requires two parameters: orderId and digitalPackageId.
		
		Args:
			| orderId (string) - Unique identifier of the order.
			| digitalPackageId (string) - This parameter supplies package ID to get fulfillment actions for the digital package.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| DigitalPackage 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/digitalpackages/{digitalPackageId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("digitalPackageId", digitalPackageId);
		url.formatUrl("orderId", orderId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createDigitalPackage(self,digitalPackage, orderId, responseFields = None):
		""" Lets you apply a digital package to the order using the orderId and digitalPackage parameters.
		
		Args:
			| digitalPackage(digitalPackage) - Lets you manage an order's digital packages, by applying a digital package to the order.
			| orderId (string) - Unique identifier of the order.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| DigitalPackage 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/digitalpackages?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(digitalPackage).execute();
		return self.client.result();

	
		
	def updateDigitalPackage(self,digitalPackage, orderId, digitalPackageId, responseFields = None):
		""" This method operates on one digital package, specified by the id given. This method ensures that the digital package ID provided is in the order with the id given, and then updates the properties of that package with the properties of the one passed in using the ‘digitalpackage’ parameter.
		
		Args:
			| digitalPackage(digitalPackage) - Lets you manage an order's digital packages, by applying a digital package to the order.
			| orderId (string) - Unique identifier of the order.
			| digitalPackageId (string) - This parameter supplies package ID to get fulfillment actions for the digital package.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| DigitalPackage 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/digitalpackages/{digitalPackageId}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("digitalPackageId", digitalPackageId);
		url.formatUrl("orderId", orderId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(digitalPackage).execute();
		return self.client.result();

	
		
	def deleteDigitalPackage(self,orderId, digitalPackageId):
		""" This operation deletes a digital package from an order. This operation requires three parameters: orderId, digitalPackageId, and digitalPackage.
		
		Args:
			| orderId (string) - Unique identifier of the order.
			| digitalPackageId (string) - This parameter supplies package ID to get fulfillment actions for the digital package.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/digitalpackages/{digitalPackageId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("digitalPackageId", digitalPackageId);
		url.formatUrl("orderId", orderId);
		self.client.withResourceUrl(url).execute();

	
	
	