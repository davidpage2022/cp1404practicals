"""Information about a project, for use in project management."""

class Project:
    """Describes information about a project"""

    def __init__(self, name: str, date: str, priority: int, cost_estimate: float, percent_completed: float):
        """Initialize a project.

        name: Project title.
        date: Start date string in DD/MM/YYYY format.  TODO: Use built-in date format.
        priority: Number indicating priority (e.g. 1 is highest priority, followed by 2, then 3...etc).
        cost_estimate: Estimated cost of the project.
        percent_completed: Value between 0 - 100 indicating percentage completed.
        """
        self.name = name
        self.date = date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_completed = percent_completed

    def __str__(self):
        return ""  # TODO

    def is_complete(self) -> bool:
        """ If the project is 100% completed. """
        return False
