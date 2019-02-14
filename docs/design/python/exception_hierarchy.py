# Logical exception hierarchy:
#
# AzureError
#     |- AzureLibraryError
#         |- AzureLibraryRequestError
#         |- AzureLibraryResponseError
#     |- ServiceRequestError
#         |- ConnectionTimeoutError
#         |- ServiceHttpRequestError
#             |- ClientRequestError
#             |- ClientAuthenticationError
#             |- ConflictError
#             |- PreconditionFailedError
#                 |- ResourceExistsError
#                 |- ResourceModifiedError
#             |- ServerError
#             |- TooManyRedirectsError
#         |- TooManyRetriesError

class AzureError(Error):
  pass

class AzureLibraryError(AzureError):
  """ An error has occured in the azure library.
  """
  pass

class AzureLibraryRequestError(AzureLibraryError):
  """ An error has occured in the azure library while trying to make a request.
  
  No request was made. 
  """
  pass

class AzureLibraryResponseError(AzureLibraryError):
  """ An error has occured while handling a response.
  
  The request was performed, but the response was not understood. 
  """
  pass

class ServiceRequestError(AzureError):
  """ A request to a service has failed. This may or may not be an HTTP service
  """
  pass

class ConnectionTimeout(ServiceRequestError):
  pass

class ServiceHttpRequestError(ServiceRequestError):
  """ A service request to a HTTP based service failed (returned a non-2xx status code)
  """
  def __init__(self, response):
    self.response = response
    self.status_code = resonse.status_code

class ClientRequestError(ServiceHttpRequestError):
  """ A service request failed (returned a 4xx status code)

  See below for more specific exception types. 
  """
  pass

class ClientAuthenticationError(ClientRequestError):
  """ A service request failed with a 403 response.
  """
  pass

class ConflictError(ServiceHttpRequestError):
  """ A service request failed with a 409 error.

  This request is not retryable. The client must make some modifications to
  the request before the call will succeed. 
  """
  pass

class PreconditionFailedError(ServiceHttpRequestError):
  """ A service request failed with a 412 error.

  This request is not retryable. The client must make some modifications to
  the request before the call will succeed.

  See more specific derived classes.
  """
  pass

class ResourceExistsError(PreconditionFailedError):
  """ A service request failed with a 412 error due to a resource already existing.

  The client sent an if-none-match: '*' precondition in the request, and the precondition failed.
  This request is not retryable. The client must make some modifications to
  the request before the call will succeed. 
  """
  pass

class ResourceModifiedError(PreconditionFailedError):
  """ A service request failed with a 412 error due to a resource having been modified existing.

  The client sent an if-match: <etag> precondition in the request, and the precondition failed.
  This request is not retryable. The client must make some modifications to
  the request before the call will succeed. 
  """
  pass

class ResourceNotFoundError(PreconditionFailedError):
  """ A service request failed with a 412 error due to not finding a matching resource.

  The client sent an if-match: * precondition in the request, and the precondition failed.
  This request is not retryable.
  """
  pass

class TooManyRequestsError(ServiceHttpRequestError):
  """ A service request failed with a 429 response

  The request is usually retryable.
  """
  pass

class ServerError(ServiceHttpRequestError):
  """ A service request failed (returned a 5xx status code)
  """
  pass

class TooManyRetriesError(ServiceRequestError):
  """ Composite exception indicating that the library has run out of retries.

  The request is not retryable. 
  """
  pass

class TooManyRedirectsError(ServiceRequestHttpError):
  """ We hit the upper limits for the number of retries to follow.
  """
  pass
