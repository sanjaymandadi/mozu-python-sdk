
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class ProductOption(object):
	def __init__(self, apiContext: ApiContext = None, dataViewMode="Live", mozuClient = None):
		if (apiContext.dataViewMode is None):
			apiContext.dataViewMode = dataViewMode;
		self.client = mozuClient or default_client();
		self.client.withApiContext(apiContext);
	
	def getOptions(self,productCode):
		"""
			Retrieves a list of all option attributes configured for the product specified in the request.
			Request Params
				string productCode Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
			Response
				array|ProductOption 
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Options", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("productCode", productCode);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getOption(self,productCode, attributeFQN, responseFields = None):
		"""
			Retrieves the details of an option attribute configuration for the specified product.
			Request Params
				string attributeFQN The fully qualified name of the attribute, which is a user defined attribute identifier.
				string productCode Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
				string responseFields Use this field to include those fields which are not included by default.
			Response
				ProductOption 
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Options/{attributeFQN}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addOption(self,productOption, productCode, responseFields = None):
		"""
			Configures an option attribute for the product specified in the request.
			Request Params
				string productCode Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
				string responseFields Use this field to include those fields which are not included by default.
				productOption Properties of the product option to create such as attribute detail, fully qualified name, and list of product option values.
			Response
				ProductOption 
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Options?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(productOption).execute();
		return self.client.result();

	
		
	def updateOption(self,productOption, productCode, attributeFQN, responseFields = None):
		"""
			Updates one or more properties of an option attribute configured for a product.
			Request Params
				string attributeFQN The fully qualified name of the attribute, which is a user defined attribute identifier.
				string productCode Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
				string responseFields Use this field to include those fields which are not included by default.
				productOption Properties of the product option to create such as attribute detail, fully qualified name, and list of product option values.
			Response
				ProductOption 
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Options/{attributeFQN}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(productOption).execute();
		return self.client.result();

	
		
	def deleteOption(self,productCode, attributeFQN):
		"""
			Deletes the configuration of an option attribute for the product specified in the request.
			Request Params
				string attributeFQN The fully qualified name of the attribute, which is a user defined attribute identifier.
				string productCode Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
			Response
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Options/{attributeFQN}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productCode", productCode);
		self.client.withResourceUrl(url).execute();

	
	
	