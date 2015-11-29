import json

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

    def get_info(self):
        state = self.state.get_state()
        # json of all the data(state, services, process)
        return {
                'state': state,
            }

    def __str__(self):
        return self.slug

    def update_info(self):
        # completely temporary function

        self.state.update()
        # self.update_services()
        # self.update_processes()


def get_this_machine():
    config = open('config.json').read()
    config = json.loads(config)

    endpoint = config.get('endpoint', '')
    slug = config.get('slug', '')

    machine = Machine(endpoint=endpoint, slug=slug)

    return machine
