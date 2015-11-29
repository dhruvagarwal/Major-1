class NoEndpointSpecified(Exception):
    def __init__(self):
        message = "No Endpoints specified"
        super(NoEndpointSpecified, self).__init__(message)

