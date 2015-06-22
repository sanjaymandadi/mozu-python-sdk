
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Document(object):
	def __init__(self, apiContext: ApiContext = None, dataViewMode="Live", mozuClient = None):
		if (apiContext.dataViewMode is None):
			apiContext.dataViewMode = dataViewMode;
		self.client = mozuClient or default_client();
		self.client.withApiContext(apiContext);
	
	def getDocumentContent(self,documentListName, documentId):
		"""
			Retrieve the content associated with a document, such as a product image or PDF specifications file, by supplying the document ID.
			Request Params
				string documentId Unique identifier for a document, used by content and document calls. Document IDs are associated with document types, document type lists, sites, and tenants.
				string documentListName Name of content documentListName to delete
			Response
				Stream 
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}/documents/{documentId}/content", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("documentId", documentId);
		url.formatUrl("documentListName", documentListName);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getDocument(self,documentListName, documentId, responseFields = None):
		"""
			Retrieves a document within the specified document list.
			Request Params
				string documentId Unique identifier for a document, used by content and document calls. Document IDs are associated with document types, document type lists, sites, and tenants.
				string documentListName Name of content documentListName to delete
				string responseFields Use this field to include those fields which are not included by default.
			Response
				Document 
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}/documents/{documentId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("documentId", documentId);
		url.formatUrl("documentListName", documentListName);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getDocuments(self,documentListName, filter = None, sortBy = None, pageSize = None, startIndex = None, responseFields = None):
		"""
			Retrieves a collection of documents according to any filter and sort criteria.
			Request Params
				string documentListName Name of content documentListName to delete
				string filter A set of filter expressions representing the search parameters for a query: eq=equals, ne=not equals, gt=greater than, lt = less than or equals, gt = greater than or equals, lt = less than or equals, sw = starts with, or cont = contains. Optional.
				int pageSize The number of results to display on each page when creating paged results from a query. The maximum value is 200.
				string responseFields Use this field to include those fields which are not included by default.
				string sortBy The property by which to sort results and whether the results appear in ascending (a-z) order, represented by ASC or in descending (z-a) order, represented by DESC. The sortBy parameter follows an available property. For example: "sortBy=productCode+asc"
				int startIndex When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with a PageSize of 25, to get the 51st through the 75th items, use startIndex=3.
			Response
				DocumentCollection 
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}/documents?filter={filter}&sortBy={sortBy}&pageSize={pageSize}&startIndex={startIndex}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("documentListName", documentListName);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createDocument(self,document, documentListName, responseFields = None):
		"""
			Creates a new document in an defined document list.
			Request Params
				string documentListName Name of content documentListName to delete
				string responseFields Use this field to include those fields which are not included by default.
				document The document properties that define the content used by the content management system (CMS).
			Response
				Document 
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}/documents?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("documentListName", documentListName);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(document).execute();
		return self.client.result();

	
		
	def updateDocumentContent(self,stream, documentListName, documentId, contentType):
		"""
			Updates the content associated with a document, such as a product image or PDF specifications file, by supplying the document ID.
			Request Params
				string documentId Unique identifier for a document, used by content and document calls. Document IDs are associated with document types, document type lists, sites, and tenants.
				string documentListName Name of content documentListName to delete
				stream Data stream that delivers information. Used to input and output data.
			Response
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}/documents/{documentId}/content", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("documentId", documentId);
		url.formatUrl("documentListName", documentListName);
		self.client.withResourceUrl(url).withBody(stream).withContentType(contentType).execute();

	
		
	def updateDocument(self,document, documentListName, documentId, responseFields = None):
		"""
			Updates a document in a document list.
			Request Params
				string documentId Unique identifier for a document, used by content and document calls. Document IDs are associated with document types, document type lists, sites, and tenants.
				string documentListName Name of content documentListName to delete
				string responseFields Use this field to include those fields which are not included by default.
				document The document properties that define the content used by the content management system (CMS).
			Response
				Document 
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}/documents/{documentId}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("documentId", documentId);
		url.formatUrl("documentListName", documentListName);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(document).execute();
		return self.client.result();

	
		
	def deleteDocument(self,documentListName, documentId):
		"""
			Deletes a specific document based on the specified document ID.
			Request Params
				string documentId Unique identifier for a document, used by content and document calls. Document IDs are associated with document types, document type lists, sites, and tenants.
				string documentListName Name of content documentListName to delete
			Response
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}/documents/{documentId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("documentId", documentId);
		url.formatUrl("documentListName", documentListName);
		self.client.withResourceUrl(url).execute();

	
		
	def deleteDocumentContent(self,documentListName, documentId):
		"""
			Deletes the content associated with a document, such as a product image or PDF specification, by supplying the document ID.
			Request Params
				string documentId Unique identifier for a document, used by content and document calls. Document IDs are associated with document types, document type lists, sites, and tenants.
				string documentListName Name of content documentListName to delete
			Response
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}/documents/{documentId}/content", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("documentId", documentId);
		url.formatUrl("documentListName", documentListName);
		self.client.withResourceUrl(url).execute();

	
	
	