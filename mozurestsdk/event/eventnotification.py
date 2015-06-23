
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation

class EventNotification(object):
	def __init__(self, mozuClient = None):
		self.client = mozuClient or default_client();
	
	def getEvents(self,startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		""" Retrieves a list of events.
		
		Args:
			| startIndex (int) - 
			| pageSize (int) - The number of results to display on each page when creating paged results from a query. The maximum value is 200.
			| sortBy (string) - 
			| filter (string) - A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| EventCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/event/pull/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getEvent(self,eventId, responseFields = None):
		""" Retrieves an event by providing the event ID.
		
		Args:
			| eventId (string) - The unique identifier of the event being retrieved. An event is a notification about a create, read, update, or delete on an order, product, discount or category.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Event 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/event/pull/{eventId}?responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("eventId", eventId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
	
	