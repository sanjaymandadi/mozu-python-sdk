
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation

class Application(object):
	def __init__(self, mozuClient = None):
		self.client = mozuClient or default_client();
	
	def getAppPackageNames(self,applicationKey, responseFields = None):
		""" platform-developer Get GetAppPackageNames description DOCUMENT_HERE 
		
		Args:
			| applicationKey (string) - 
			| responseFields (string) - A list or array of fields returned for a call. These fields may be customized and may be used for various types of data calls in Mozu. For example, responseFields are returned for retrieving or updating attributes, carts, and messages in Mozu.
		
		Returns:
			| PackageNamesCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/developer/applications/{applicationKey}/packagenames?responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("applicationKey", applicationKey);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getAppVersions(self,nsAndAppId, responseFields = None):
		""" platform-developer Get GetAppVersions description DOCUMENT_HERE 
		
		Args:
			| nsAndAppId (string) - 
			| responseFields (string) - A list or array of fields returned for a call. These fields may be customized and may be used for various types of data calls in Mozu. For example, responseFields are returned for retrieving or updating attributes, carts, and messages in Mozu.
		
		Returns:
			| ApplicationVersionsCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/developer/applications/versions/{nsAndAppId}?responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("nsAndAppId", nsAndAppId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getPackageFileMetadata(self,applicationKey, filepath, responseFields = None):
		""" platform-developer Get GetPackageFileMetadata description DOCUMENT_HERE 
		
		Args:
			| applicationKey (string) - 
			| filepath (string) - 
			| responseFields (string) - A list or array of fields returned for a call. These fields may be customized and may be used for various types of data calls in Mozu. For example, responseFields are returned for retrieving or updating attributes, carts, and messages in Mozu.
		
		Returns:
			| FileMetadata 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/developer/packages/{applicationKey}/filemetadata/{filepath}?responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("applicationKey", applicationKey);
		url.formatUrl("filepath", filepath);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getPackageMetadata(self,applicationKey, responseFields = None):
		""" platform-developer Get GetPackageMetadata description DOCUMENT_HERE 
		
		Args:
			| applicationKey (string) - 
			| responseFields (string) - A list or array of fields returned for a call. These fields may be customized and may be used for various types of data calls in Mozu. For example, responseFields are returned for retrieving or updating attributes, carts, and messages in Mozu.
		
		Returns:
			| FolderMetadata 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/developer/packages/{applicationKey}/metadata?responseFields={responseFields}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("applicationKey", applicationKey);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def upsertPackageFile(self,stream, applicationKey, filepath, lastModifiedTime = None, responseFields = None, contentType = None):
		""" platform-developer Post UpsertPackageFile description DOCUMENT_HERE 
		
		Args:
			| stream(stream) - Data stream that delivers information. Used to input and output data.
			| applicationKey (string) - 
			| filepath (string) - 
			| lastModifiedTime (string) - 
			| responseFields (string) - A list or array of fields returned for a call. These fields may be customized and may be used for various types of data calls in Mozu. For example, responseFields are returned for retrieving or updating attributes, carts, and messages in Mozu.
			| contentType (string) - set content type of the data uploaded|
		
		Returns:
			| FileMetadata 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/developer/packages/{applicationKey}/files/{filepath}?lastModifiedTime={lastModifiedTime}&responseFields={responseFields}", "POST", UrlLocation.HomePod, False);
		url.formatUrl("applicationKey", applicationKey);
		url.formatUrl("filepath", filepath);
		url.formatUrl("lastModifiedTime", lastModifiedTime);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(stream).withContentType(contentType).execute();
		return self.client.result();

	
		
	def renamePackageFile(self,renameInfo, applicationKey, responseFields = None):
		""" platform-developer Post RenamePackageFile description DOCUMENT_HERE 
		
		Args:
			| renameInfo(renameInfo) - Information required to update the name of a file in a package, which consists of the original name and the new name.
			| applicationKey (string) - 
			| responseFields (string) - A list or array of fields returned for a call. These fields may be customized and may be used for various types of data calls in Mozu. For example, responseFields are returned for retrieving or updating attributes, carts, and messages in Mozu.
		
		Returns:
			| FileMetadata 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/developer/packages/{applicationKey}/files_rename?responseFields={responseFields}", "POST", UrlLocation.HomePod, False);
		url.formatUrl("applicationKey", applicationKey);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(renameInfo).execute();
		return self.client.result();

	
		
	def deletePackageFile(self,applicationKey, filepath):
		""" platform-developer Delete DeletePackageFile description DOCUMENT_HERE 
		
		Args:
			| applicationKey (string) - 
			| filepath (string) - 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/developer/packages/{applicationKey}/files/{filepath}", "DELETE", UrlLocation.HomePod, False);
		url.formatUrl("applicationKey", applicationKey);
		url.formatUrl("filepath", filepath);
		self.client.withResourceUrl(url).execute();

	
	
	