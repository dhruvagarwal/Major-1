import time

from .machine import Machine, get_this_machine
from .custom_mq import Producer


# no. of seconds after which machine data is updated.
DELTA = 3

# make a producer object for the queue
producer = Producer()


def dispatch_info(machine):
    machine_info = machine.get_info()

    # ensure machine_info is clean and valid data,
    # else return / raise error
    # clean_data(machine_info)

    # queue producer pushes the data
    producer.push(machine_info)


def update_data(machine):
    machine.update_info()


def main():
    """
    this function is the service function.
    It calls the update function for the machine,
    then dispatch the data into the message queue.
    """
    machine = get_this_machine()

    while True:
        # TODO: write a better method to update machine data
        update_data(machine)
        dispatch_info(machine)
        print 'Data dispatched'
        time.sleep(DELTA)
