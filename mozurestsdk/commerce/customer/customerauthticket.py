
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class CustomerAuthTicket(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		client.withApiContext(apiContext);
	
	def createAnonymousShopperAuthTicket(self,):
		""" Creates an authentication ticket for an anonymous shopper user.
		
		Returns:
			| Stream 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/authtickets/anonymousshopper", "GET", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createUserAuthTicket(self,userAuthInfo, responseFields = None):
		""" Generates a new authentication ticket for a customer account.
		
		Args:
			| userAuthInfo(userAuthInfo) - The authentication information required to generate an authentication ticket for a customer account.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| CustomerAuthTicket 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/authtickets/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(userAuthInfo).execute();
		return self.client.result();

	
		
	def refreshUserAuthTicket(self,refreshToken, responseFields = None):
		""" Refreshes an existing authentication ticket for a customer account by providing the refresh token string.
		
		Args:
			| refreshToken (string) - Alphanumeric string used for access tokens. This token refreshes access for accounts by generating a new developer or application account authentication ticket after an access token expires.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| CustomerAuthTicket 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/authtickets/refresh?refreshToken={refreshToken}&responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("refreshToken", refreshToken);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
	
	