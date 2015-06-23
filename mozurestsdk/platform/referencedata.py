
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation

class ReferenceData(object):
	def __init__(self, mozuClient = None):
		self.client = mozuClient or default_client();
	
	def getAddressSchema(self,countryCode = None, responseFields = None):
		""" Retrieves a specific address schema based on the country code provided. This operation allows the creation of custom shipping and billing address fields.
		
		Args:
			| countryCode (string) - The 2-letter geographic code representing the country for the physical or mailing address. Currently limited to the US.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| AddressSchema 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/reference/addressschema/{countryCode}?responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("countryCode", countryCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getAddressSchemas(self,responseFields = None):
		""" Retrieves the entire list of address schemas that the system supports.
		
		Args:
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| AddressSchemaCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/reference/addressschemas?responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getBehavior(self,behaviorId, responseFields = None):
		""" Retrieves the details of a behavior based on the behavior ID specified in the request.
		
		Args:
			| behaviorId (int) - Unique identifier of the behavior.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Behavior 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/reference/behaviors/{behaviorId}?responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("behaviorId", behaviorId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getBehaviorCategory(self,categoryId, responseFields = None):
		""" Retrieves the details of the behavior category specified in the request.
		
		Args:
			| categoryId (int) - Unique identifier of the category to modify.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| BehaviorCategory 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/reference/behaviors/categories/{categoryId}?responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("categoryId", categoryId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getBehaviorCategories(self,responseFields = None):
		""" Retrieves the list of behavior categories.
		
		Args:
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| BehaviorCategoryCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/reference/behaviors/categories?responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getBehaviors(self,userType = None, responseFields = None):
		""" Retrieves a list of application behaviors.
		
		Args:
			| userType (string) - The user type associated with the behaviors to retrieve.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| BehaviorCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/reference/behaviors?userType={userType}&responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("userType", userType);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getContentLocales(self,responseFields = None):
		""" Retrieves the list of content locales the system supports. Content locales indicate the language used and the country where the language is used.
		
		Args:
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ContentLocaleCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/reference/contentLocales?responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getCountries(self,responseFields = None):
		""" Retrieves the entire list of countries that the system supports.
		
		Args:
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| CountryCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/reference/countries?responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getCountriesWithStates(self,responseFields = None):
		""" Retrieves the entire list of countries that the system supports.
		
		Args:
			| responseFields (string) - A list or array of fields returned for a call. These fields may be customized and may be used for various types of data calls in Mozu. For example, responseFields are returned for retrieving or updating attributes, carts, and messages in Mozu.
		
		Returns:
			| CountryWithStatesCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/reference/countrieswithstates?responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getCurrencies(self,responseFields = None):
		""" Retrieves the entire list of currencies that the system supports.
		
		Args:
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| CurrencyCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/reference/currencies?responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getTimeZones(self,responseFields = None):
		""" Retrieves the entire list of time zones that the system supports.
		
		Args:
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| TimeZoneCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/reference/timezones?responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getTopLevelDomains(self,responseFields = None):
		""" Retrieves the entire list of top-level internet domains that the system supports.
		
		Args:
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| TopLevelDomainCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/reference/topleveldomains?responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getUnitsOfMeasure(self,filter = None, responseFields = None):
		""" Retrieves an array list of all units of measure the system supports.
		
		Args:
			| filter (string) - A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| UnitOfMeasureCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/reference/unitsofmeasure?filter={filter}&responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
	
	