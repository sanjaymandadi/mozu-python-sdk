
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Channel(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		client.withApiContext(apiContext);
	
	def getChannels(self,startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		""" Retrieves a list of channels defined for a tenant according to any filter or sort criteria specified in the request.
		
		Args:
			| startIndex (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with a PageSize of 25, to get the 51st through the 75th items, use startIndex=3.
			| pageSize (int) - The number of results to display on each page when creating paged results from a query. The maximum value is 200.
			| sortBy (string) - The property by which to sort results and whether the results appear in ascending (a-z) order, represented by ASC or in descending (z-a) order, represented by DESC. The sortBy parameter follows an available property. For example: "sortBy=productCode+asc"
			| filter (string) - A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ChannelCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/channels/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getChannel(self,code, responseFields = None):
		""" Retrieves the details of the channel specified in the request.
		
		Args:
			| code (string) - User-defined code that uniqely identifies the channel group.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Channel 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/channels/{code}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("code", code);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createChannel(self,channel, responseFields = None):
		""" Creates a new channel that defines a new logical business division to use for financial reporting.
		
		Args:
			| channel(channel) - Properties of a channel used to divide a company into logical business divisions, such as "US Retail," "US Online," or "Amazon." All sites and orders are associated with a channel.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Channel 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/channels/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(channel).execute();
		return self.client.result();

	
		
	def updateChannel(self,channel, code, responseFields = None):
		""" Updates one or more details of a defined channel, including the associated sites.
		
		Args:
			| channel(channel) - Properties of a channel used to divide a company into logical business divisions, such as "US Retail," "US Online," or "Amazon." All sites and orders are associated with a channel.
			| code (string) - User-defined code that uniqely identifies the channel group.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Channel 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/channels/{code}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("code", code);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(channel).execute();
		return self.client.result();

	
		
	def deleteChannel(self,code):
		""" Deletes a defined channel for the tenant and removes the defined site associations. After deleting this channel, assign its associated sites to another channel.
		
		Args:
			| code (string) - User-defined code that uniqely identifies the channel group.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/channels/{code}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("code", code);
		self.client.withResourceUrl(url).execute();

	
	
	