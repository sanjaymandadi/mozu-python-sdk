
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class CustomerNote(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getAccountNote(self,accountId, noteId, responseFields = None):
		""" Retrieves the contents of a particular note attached to a specified customer account.
		
		Args:
			| accountId (int) - Unique identifier of the customer account.
			| noteId (int) - Unique identifier of a particular note to retrieve.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| CustomerNote 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/notes/{noteId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("noteId", noteId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getAccountNotes(self,accountId, startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		""" Retrieves a list of notes added to a customer account according to any specified filter criteria and sort options.
		
		Args:
			| accountId (int) - Unique identifier of the customer account.
			| startIndex (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with a PageSize of 25, to get the 51st through the 75th items, use startIndex=3.
			| pageSize (int) - The number of results to display on each page when creating paged results from a query. The maximum value is 200.
			| sortBy (string) - The property by which to sort results and whether the results appear in ascending (a-z) order, represented by ASC or in descending (z-a) order, represented by DESC. The sortBy parameter follows an available property. For example: "sortBy=productCode+asc"
			| filter (string) - A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| CustomerNoteCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/notes?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addAccountNote(self,note, accountId, responseFields = None):
		""" Adds a new note to the specified customer account.
		
		Args:
			| note(note) - Properties of a note configured for a customer account.
			| accountId (int) - Unique identifier of the customer account.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| CustomerNote 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/notes?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(note).execute();
		return self.client.result();

	
		
	def updateAccountNote(self,note, accountId, noteId, responseFields = None):
		""" Modifies an existing note for a customer account.
		
		Args:
			| note(note) - Properties of a note configured for a customer account.
			| accountId (int) - Unique identifier of the customer account.
			| noteId (int) - Unique identifier of a particular note to retrieve.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| CustomerNote 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/notes/{noteId}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("noteId", noteId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(note).execute();
		return self.client.result();

	
		
	def deleteAccountNote(self,accountId, noteId):
		""" Removes a note from the specified customer account.
		
		Args:
			| accountId (int) - Unique identifier of the customer account.
			| noteId (int) - Unique identifier of a particular note to retrieve.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/notes/{noteId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("noteId", noteId);
		self.client.withResourceUrl(url).execute();

	
	
	