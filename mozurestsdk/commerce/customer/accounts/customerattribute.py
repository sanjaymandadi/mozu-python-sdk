
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class CustomerAttribute(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		client.withApiContext(apiContext);
	
	def getAccountAttribute(self,accountId, attributeFQN, responseFields = None):
		"""
			Retrieves the contents of an attribute associated with the specified customer account.
			Request Params
				int accountId Unique identifier of the customer account.
				string attributeFQN The fully qualified name of the attribute, which is a user defined attribute identifier.
				string responseFields Use this field to include those fields which are not included by default.
			Response
				CustomerAttribute 
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/attributes/{attributeFQN}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getAccountAttributes(self,accountId, startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		"""
			Retrieves the list of customer account attributes.
			Request Params
				int accountId Unique identifier of the customer account.
				string filter 
				int pageSize 
				string responseFields Use this field to include those fields which are not included by default.
				string sortBy 
				int startIndex 
			Response
				CustomerAttributeCollection 
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/attributes?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addAccountAttribute(self,attribute, accountId, responseFields = None):
		"""
			Applies a defined attribute to the customer account specified in the request and assigns a value to the customer attribute.
			Request Params
				int accountId Unique identifier of the customer account.
				string responseFields Use this field to include those fields which are not included by default.
				attribute Properties of an attribute associated with a customer account.
			Response
				CustomerAttribute 
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/attributes?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(attribute).execute();
		return self.client.result();

	
		
	def updateAccountAttribute(self,attribute, accountId, attributeFQN, responseFields = None):
		"""
			Updates one or more details of a customer account attribute.
			Request Params
				int accountId Unique identifier of the customer account.
				string attributeFQN The fully qualified name of the attribute, which is a user defined attribute identifier.
				string responseFields Use this field to include those fields which are not included by default.
				attribute Properties of an attribute associated with a customer account.
			Response
				CustomerAttribute 
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/attributes/{attributeFQN}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(attribute).execute();
		return self.client.result();

	
		
	def deleteAccountAttribute(self,accountId, attributeFQN):
		"""
			Removes the attribute specified in the request from the customer account.
			Request Params
				int accountId Unique identifier of the customer account.
				string attributeFQN The fully qualified name of the attribute, which is a user defined attribute identifier.
			Response
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/attributes/{attributeFQN}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("attributeFQN", attributeFQN);
		self.client.withResourceUrl(url).execute();

	
	
	