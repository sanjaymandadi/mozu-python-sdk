
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class View(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getViewDocuments(self,documentListName, viewName, filter = None, sortBy = None, pageSize = None, startIndex = None, includeInactive = False, responseFields = None):
		""" Retrieves a collection of documents associated with a view.
		
		Args:
			| documentListName (string) - Name of content documentListName to delete
			| viewName (string) - The name for a view. Views are used to render data in Mozu, such as document and entity lists. Each view includes a schema, format, name, ID, and associated data types to render.
			| filter (string) - A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
			| sortBy (string) - The element to sort the results by and the channel in which the results appear. Either ascending (a-z) or descending (z-a) channel. Optional.
			| pageSize (int) - The number of results to display on each page when creating paged results from a query. The amount is divided and displayed on the  pageCount  amount of pages. The default is 20 and maximum value is 200 per page.
			| startIndex (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with a  pageSize  of 25, to get the 51st through the 75th items, use  startIndex=3 .
			| includeInactive (bool) - 
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| DocumentCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}/views/{viewName}/documents?filter={filter}&sortBy={sortBy}&pageSize={pageSize}&startIndex={startIndex}&includeInactive={includeInactive}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("documentListName", documentListName);
		url.formatUrl("filter", filter);
		url.formatUrl("includeInactive", includeInactive);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		url.formatUrl("viewName", viewName);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
	
	