""" Information about a project, for use in project management.
    Estimated: 10
    Actual: 12
"""


class Project:
    """Describes information about a project"""

    def __init__(self, name: str, date: str, priority: int, cost_estimate: float, completion_percentage: float):
        """Initialize a project.

        name: Project title.
        date: Start date string in DD/MM/YYYY format.
        priority: Number indicating priority (e.g. 1 is highest priority, followed by 2, then 3...etc).
        cost_estimate: Estimated cost of the project.
        completion_percentage: Value between 0 - 100 indicating percentage completed.
        """
        self.name = name
        self.date = date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion_percentage

    def __str__(self):
        return ""  # TODO
