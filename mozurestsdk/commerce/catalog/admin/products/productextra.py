
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class ProductExtra(object):
	def __init__(self, apiContext: ApiContext = None, dataViewMode="Live", mozuClient = None):
		if (apiContext.dataViewMode is None):
			apiContext.dataViewMode = dataViewMode;
		self.client = mozuClient or default_client();
		self.client.withApiContext(apiContext);
	
	def getExtras(self,productCode):
		""" Retrieves a list of extras configured for the product according to any defined filter and sort criteria.
		
		Args:
			| productCode (string) - Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
		
		Returns:
			| array of ProductExtra 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Extras", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("productCode", productCode);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getExtraValueLocalizedDeltaPrices(self,productCode, attributeFQN, value):
		""" Retrieves a collection of all localized delta price values for a product extra. Localized delta prices are deltas between two differing monetary conversion amounts between countries, such as US Dollar vs Euro.
		
		Args:
			| productCode (string) - The unique, user-defined product code of a product, used throughout Mozu to reference and associate to a product.
			| attributeFQN (string) - Fully qualified name for an attribute.
			| value (string) - The value string to create.
		
		Returns:
			| array of ProductExtraValueDeltaPrice 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Extras/{attributeFQN}/Values/{value}/localizedDeltaPrice", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productCode", productCode);
		url.formatUrl("value", value);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getExtraValueLocalizedDeltaPrice(self,productCode, attributeFQN, value, currencyCode, responseFields = None):
		""" Retrieves the localized delta price value for a product extra. Localized delta prices are deltas between two differing monetary conversion amounts between countries, such as US Dollar vs Euro.
		
		Args:
			| productCode (string) - The unique, user-defined product code of a product, used throughout Mozu to reference and associate to a product.
			| attributeFQN (string) - Fully qualified name for an attribute.
			| value (string) - The value string to create.
			| currencyCode (string) - The three character ISO currency code, such as USD for US Dollars.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ProductExtraValueDeltaPrice 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Extras/{attributeFQN}/Values/{value}/localizedDeltaPrice/{currencyCode}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("currencyCode", currencyCode);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("value", value);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getExtra(self,productCode, attributeFQN, responseFields = None):
		""" Retrieves the details of an extra attribute configuration for the product specified in the request.
		
		Args:
			| productCode (string) - Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
			| attributeFQN (string) - The fully qualified name of the attribute, which is a user defined attribute identifier.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ProductExtra 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Extras/{attributeFQN}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addExtraValueLocalizedDeltaPrice(self,localizedDeltaPrice, productCode, attributeFQN, value, responseFields = None):
		""" Adds a localized delta price value for a product extra. Localized delta prices are deltas between two differing monetary conversion amounts between countries, such as US Dollar vs Euro.
		
		Args:
			| localizedDeltaPrice(localizedDeltaPrice) - The properties of the price difference between the product extra and the base product.
			| productCode (string) - The unique, user-defined product code of a product, used throughout Mozu to reference and associate to a product.
			| attributeFQN (string) - Fully qualified name for an attribute.
			| value (string) - The value string to create.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ProductExtraValueDeltaPrice 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Extras/{attributeFQN}/Values/{value}/localizedDeltaPrice?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("value", value);
		self.client.withResourceUrl(url).withBody(localizedDeltaPrice).execute();
		return self.client.result();

	
		
	def addExtra(self,productExtra, productCode, responseFields = None):
		""" Configure an extra attribute for the product specified in the request.
		
		Args:
			| productExtra(productExtra) - Properties of an extra attribute to defined for a product that is associated with a product type that uses the extra. Setting up extras for a product enables shopper-entered information, such as initials for a monogram.
			| productCode (string) - Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ProductExtra 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Extras?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(productExtra).execute();
		return self.client.result();

	
		
	def updateExtraValueLocalizedDeltaPrices(self,localizedDeltaPrice, productCode, attributeFQN, value):
		""" Updates all localized delta price values for a product extra. Localized delta prices are deltas between two differing monetary conversion amounts between countries, such as US Dollar vs Euro.
		
		Args:
			| localizedDeltaPrice(array|localizedDeltaPrice) - The properties of the price difference between the product extra and the base product.
			| productCode (string) - The unique, user-defined product code of a product, used throughout Mozu to reference and associate to a product.
			| attributeFQN (string) - Fully qualified name for an attribute.
			| value (string) - The value string to create.
		
		Returns:
			| array of ProductExtraValueDeltaPrice 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Extras/{attributeFQN}/Values/{value}/localizedDeltaPrice", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productCode", productCode);
		url.formatUrl("value", value);
		self.client.withResourceUrl(url).withBody(localizedDeltaPrice).execute();
		return self.client.result();

	
		
	def updateExtraValueLocalizedDeltaPrice(self,localizedDeltaPrice, productCode, attributeFQN, value, currencyCode, responseFields = None):
		""" Updates the localized delta price value for a product extra. Localized delta prices are deltas between two differing monetary conversion amounts between countries, such as US Dollar vs Euro.
		
		Args:
			| localizedDeltaPrice(localizedDeltaPrice) - The properties of the price difference between the product extra and the base product.
			| productCode (string) - The unique, user-defined product code of a product, used throughout Mozu to reference and associate to a product.
			| attributeFQN (string) - Fully qualified name for an attribute.
			| value (string) - The value string to create.
			| currencyCode (string) - The three character ISO currency code, such as USD for US Dollars.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ProductExtraValueDeltaPrice 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Extras/{attributeFQN}/Values/{value}/localizedDeltaPrice/{currencyCode}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("currencyCode", currencyCode);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("value", value);
		self.client.withResourceUrl(url).withBody(localizedDeltaPrice).execute();
		return self.client.result();

	
		
	def updateExtra(self,productExtra, productCode, attributeFQN, responseFields = None):
		""" Updates the configuration of an extra attribute for the product specified in the request.
		
		Args:
			| productExtra(productExtra) - Properties of an extra attribute to defined for a product that is associated with a product type that uses the extra. Setting up extras for a product enables shopper-entered information, such as initials for a monogram.
			| productCode (string) - Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
			| attributeFQN (string) - The fully qualified name of the attribute, which is a user defined attribute identifier.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ProductExtra 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Extras/{attributeFQN}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(productExtra).execute();
		return self.client.result();

	
		
	def deleteExtra(self,productCode, attributeFQN):
		""" Delete a product extra configuration for the product specified in the request.
		
		Args:
			| productCode (string) - Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
			| attributeFQN (string) - The fully qualified name of the attribute, which is a user defined attribute identifier.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Extras/{attributeFQN}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productCode", productCode);
		self.client.withResourceUrl(url).execute();

	
		
	def deleteExtraValueLocalizedDeltaPrice(self,productCode, attributeFQN, value, currencyCode):
		""" Deletes the localized delta price value for a product extra. Localized delta prices are deltas between two differing monetary conversion amounts between countries, such as US Dollar vs Euro.
		
		Args:
			| productCode (string) - The unique, user-defined product code of a product, used throughout Mozu to reference and associate to a product.
			| attributeFQN (string) - Fully qualified name for an attribute.
			| value (string) - Use this field to include those fields which are not included by default.
			| currencyCode (string) - The three character ISO currency code, such as USD for US Dollars.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Extras/{attributeFQN}/Values/{value}/localizedDeltaPrice/{currencyCode}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("currencyCode", currencyCode);
		url.formatUrl("productCode", productCode);
		url.formatUrl("value", value);
		self.client.withResourceUrl(url).execute();

	
	
	