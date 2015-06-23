
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Adjustment(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		client.withApiContext(apiContext);
	
	def applyShippingAdjustment(self,adjustment, orderId, updateMode = None, version = None, responseFields = None):
		""" Applies a shipping adjustment to the specified order.
		
		Args:
			| adjustment(adjustment) - Properties of an ad-hoc price adjustment for an order.
			| orderId (string) - Unique identifier of the order.
			| updateMode (string) - Specifies whether to update the original order, update the order in draft mode, or update the order in draft mode and then commit the changes to the original. Draft mode enables users to make incremental order changes before committing the changes to the original order. Valid values are "ApplyToOriginal," "ApplyToDraft," or "ApplyAndCommit."
			| version (string) - System-supplied integer that represents the current version of the order, which prevents users from unintentionally overriding changes to the order. When a user performs an operation for a defined order, the system validates that the version of the updated order matches the version of the order on the server. After the operation completes successfully, the system increments the version number by one.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Order 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/adjustment/shipping?updatemode={updateMode}&version={version}&responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("updateMode", updateMode);
		url.formatUrl("version", version);
		self.client.withResourceUrl(url).withBody(adjustment).execute();
		return self.client.result();

	
		
	def applyAdjustment(self,adjustment, orderId, updateMode = None, version = None, responseFields = None):
		""" Applies a price adjustment to the specified order.
		
		Args:
			| adjustment(adjustment) - Properties of an ad-hoc price adjustment for an order.
			| orderId (string) - Unique identifier of the order.
			| updateMode (string) - Specifies whether to update the original order, update the order in draft mode, or update the order in draft mode and then commit the changes to the original. Draft mode enables users to make incremental order changes before committing the changes to the original order. Valid values are "ApplyToOriginal," "ApplyToDraft," or "ApplyAndCommit."
			| version (string) - System-supplied integer that represents the current version of the order, which prevents users from unintentionally overriding changes to the order. When a user performs an operation for a defined order, the system validates that the version of the updated order matches the version of the order on the server. After the operation completes successfully, the system increments the version number by one.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Order 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/adjustment?updatemode={updateMode}&version={version}&responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("updateMode", updateMode);
		url.formatUrl("version", version);
		self.client.withResourceUrl(url).withBody(adjustment).execute();
		return self.client.result();

	
		
	def removeShippingAdjustment(self,orderId, updateMode = None, version = None):
		""" Removes a shipping adjustment previously applied to an order or draft.
		
		Args:
			| orderId (string) - Unique identifier of the order.
			| updateMode (string) - Specifies whether to update the original order, update the order in draft mode, or update the order in draft mode and then commit the changes to the original. Draft mode enables users to make incremental order changes before committing the changes to the original order. Valid values are "ApplyToOriginal," "ApplyToDraft," or "ApplyAndCommit."
			| version (string) - System-supplied integer that represents the current version of the order, which prevents users from unintentionally overriding changes to the order. When a user performs an operation for a defined order, the system validates that the version of the updated order matches the version of the order on the server. After the operation completes successfully, the system increments the version number by one.
		
		Returns:
			| Order 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/adjustment/shipping?updatemode={updateMode}&version={version}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("updateMode", updateMode);
		url.formatUrl("version", version);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def removeAdjustment(self,orderId, updateMode = None, version = None):
		""" Removes a price adjustment from the specified order.
		
		Args:
			| orderId (string) - Unique identifier of the order.
			| updateMode (string) - Specifies whether to update the original order, update the order in draft mode, or update the order in draft mode and then commit the changes to the original. Draft mode enables users to make incremental order changes before committing the changes to the original order. Valid values are "ApplyToOriginal," "ApplyToDraft," or "ApplyAndCommit."
			| version (string) - System-supplied integer that represents the current version of the order, which prevents users from unintentionally overriding changes to the order. When a user performs an operation for a defined order, the system validates that the version of the updated order matches the version of the order on the server. After the operation completes successfully, the system increments the version number by one.
		
		Returns:
			| Order 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/adjustment?updatemode={updateMode}&version={version}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("updateMode", updateMode);
		url.formatUrl("version", version);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
	
	