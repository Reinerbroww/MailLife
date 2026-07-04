import time


class Observer:

    def __init__(self):

        self.agents = []

        self.total_start = None

        self.total_end = None

    def start_session(self):

        self.total_start = time.perf_counter()

    def end_session(self):

        self.total_end = time.perf_counter()

    def add_agent(self, name, execution_time):

        self.agents.append({

            "name": name,

            "time": execution_time
        })

    @property
    def total_time(self):

        if self.total_start is None or self.total_end is None:
            return 0

        return round(
            self.total_end - self.total_start,
            3
        )

    @property
    def average_time(self):

        if len(self.agents) == 0:
            return 0

        return round(

            sum(a["time"] for a in self.agents)

            / len(self.agents),

            3
        )

    @property
    def ai_calls(self):

        return len(self.agents)