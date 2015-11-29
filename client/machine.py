from .exceptions import NoEndpointSpecified
from .state import State


class Machine(object):
    def __init__(self, endpoint, slug=""):
        if not endpoint:
            raise NoEndpointSpecified

        self.endpoint = endpoint
        self.services = []
        self.processes = []
        self.state = State()
        self.slug = "machine-{endpoint}".format(endpoint=endpoint)

        if slug:
            self.slug = slug

    def get_state(self):
        return self.state.get_state()

    def __str__(self):
        return self.slug

    def sync_system(self):
        # completely temporary function

        self.state.update()
        # self.update_services()
        # self.update_processes()
