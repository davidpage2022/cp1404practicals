"""Information about a project, for use in project management."""
from datetime import datetime


class Project:
    """Describes information about a project"""

    def __init__(self, name: str, date: datetime.date, priority: int,
                 cost_estimate: float, percent_completed: int):
        """Initialize a project.

        name: Project title.
        date: Start date.
        priority: Number indicating priority (e.g. 1 is highest priority, followed by 2, then 3...etc).
        cost_estimate: Estimated cost of the project.
        percent_completed: Number between 0 - 100 indicating percentage completed.
        """
        self.name = name
        self.date = date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_completed = percent_completed

    def __str__(self):
        date_string = self.date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {date_string}, priority: {self.priority}, "
                f"estimate: {self.cost_estimate}, completion: {self.percent_completed}%")

    def __repr__(self):
        return (f"Project({self.name}, {repr(self.date)}, {self.priority}, "
                f"{self.cost_estimate}, {self.percent_completed})")

    def __lt__(self, other: "Project"):
        return self.priority < other.priority

    def is_complete(self) -> bool:
        """ If the project is 100% completed. """
        return self.percent_completed == 100
