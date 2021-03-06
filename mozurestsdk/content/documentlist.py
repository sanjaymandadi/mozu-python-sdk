
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class DocumentList(object):
	def __init__(self, apiContext: ApiContext = None, dataViewMode="Live", mozuClient = None):
		if (apiContext is not None and apiContext.dataViewMode is None):
			apiContext.dataViewMode = dataViewMode;
		else:
			apiContext = ApiContext(dataViewMode = dataViewMode);
		self.client = mozuClient or default_client();
		self.client.withApiContext(apiContext);
	
	def getDocumentLists(self,pageSize = None, startIndex = None, responseFields = None):
		""" Retrieves a collection of document lists.
		
		Args:
			| pageSize (int) - The number of results to display on each page when creating paged results from a query. The maximum value is 200.
			| startIndex (int) - 
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| DocumentListCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentlists/?pageSize={pageSize}&startIndex={startIndex}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getDocumentList(self,documentListName, responseFields = None):
		""" Retrieve the details of a document list by providing the list name.
		
		Args:
			| documentListName (string) - Name of content documentListName to delete
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| DocumentList 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("documentListName", documentListName);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createDocumentList(self,list, responseFields = None):
		""" Creates a new documentList
		
		Args:
			| list(list) - The list of document types and related properties that define content used by the content management system (CMS).
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| DocumentList 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentlists/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(list).execute();
		return self.client.result();

	
		
	def updateDocumentList(self,list, documentListName, responseFields = None):
		""" Updates a  DocumentListName .
		
		Args:
			| list(list) - The list of document types and related properties that define content used by the content management system (CMS).
			| documentListName (string) - Name of content documentListName to delete
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| DocumentList 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("documentListName", documentListName);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(list).execute();
		return self.client.result();

	
		
	def deleteDocumentList(self,documentListName):
		""" Deletes the specified  DocumentListName .
		
		Args:
			| documentListName (string) - Name of content documentListName to delete
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("documentListName", documentListName);
		self.client.withResourceUrl(url).execute();

	
	
	