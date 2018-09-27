class ApiException(Exception):
    """
    This exception is raised when Currency Layer API response is not
    a success.
    """
    def __init__(self, message):
        self.message = message
