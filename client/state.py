from datetime import datetime, timedelta


class State(object):
    def __init__(self):
        # Init all the attributes with null
        self.sys_type = ""
        self.uptime = timedelta(seconds=0)
        self.tasks = 0
        self.process_count = 0
        self.cores_data = []
        self.memory = 0
        self.used_memory = 0

    def get_state(self):
        return {
                'sys_type': self.sys_type,
                'tasks': self.tasks,
                'memory': "{used}/{total}".format(used=self.used_memory,
                                                total=self.memory),
                'cores': self.cores_data,
        }

    def update(self):
        """
        Method to update the system state
        using psutil.
        """
        pass

