
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class GeneralSettings(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		client.withApiContext(apiContext);
	
	def getGeneralSettings(self,responseFields = None):
		"""
			Retrieve a site's general global settings.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
			Response
				GeneralSettings 
		"""

		url = MozuUrl("/api/commerce/settings/general/?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def updateGeneralSettings(self,generalSettings, responseFields = None):
		"""
			Updates a site's general global settings.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
				generalSettings General settings used on the storefront site.
			Response
				GeneralSettings 
		"""

		url = MozuUrl("/api/commerce/settings/general/?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(generalSettings).execute();
		return self.client.result();

	
	
	