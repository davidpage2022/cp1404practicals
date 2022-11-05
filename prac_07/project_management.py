"""Project Management
Estimated: 70
Actual: 118
"""
import datetime
import json
import pickle
from operator import attrgetter

from prac_07.project import Project

FILENAME = "projects.txt"
HEADER = "Name	Start Date	Priority	Cost Estimate	Completion Percentage"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


class ExitRequested(Exception):
    """Used to handle user wishing to exit out of entering input."""
    pass


def main():
    """Allow user to load, save and manage a list of projects."""
    projects = load_projects(FILENAME)

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":  # Quit.

        if choice == "L":  # Load.
            filename = input("Filename: ")
            projects = load_projects(filename)

        elif choice == "S":  # Save.
            filename = input("Filename: ")
            save_projects(projects, filename)

        elif choice == "D":  # Display.
            display_projects(projects)

        elif choice == "F":  # Filter.
            date = get_date("Show projects that start after date (DD/MM/YYYY): ")
            filtered_projects = filter_projects_by_date(projects, date)
            for project in filtered_projects:
                print(project)

        elif choice == "A":  # Add.
            project = get_new_project()
            projects.append(project)

        elif choice == "U":  # Update.
            project = get_project(projects)
            print(project)
            percent_completed, priority = get_status_updates(project)
            project.percent_completed = percent_completed
            project.priority = priority

        print(MENU)
        choice = input(">>> ").upper()
    save_projects(projects, FILENAME)
    print("Thank you for using custom-built project management software.")


def str_to_date(date_string) -> datetime.date:
    """Convert a string in format DD/MM/YYYY to a datetime.date."""
    return datetime.datetime.strptime(date_string, "%d/%m/%Y").date()


def date_to_str(date) -> str:
    """Convert a datetime.date to a string in format DD/MM/YYYY."""
    return date.strftime("%d/%m/%Y")


def load_projects(filename) -> list[Project]:
    """Load projects from filename.
    Returns a list of loaded projects."""

    # Load JSON data.
    with open(filename, "r") as in_file:
        projects = json.load(in_file)

    # Recreate Project objects from JSON data.
    for i, project in enumerate(projects):
        project["date"] = str_to_date(project["date"])  # Recreate date object.
        projects[i] = Project(*project.values())
    return projects

    # PICKLE METHOD:
    # ----------------------------------------------
    # with open(filename, "rb") as in_file:
    #     data = pickle.load(in_file)
    # return data


def save_projects(projects: list[Project], filename):
    """Save a list of projects to a file with filename."""

    # Save data as JSON.
    with open(filename, "w") as out_file:

        # Project contains a datetime.date field which cannot be JSON serialized,
        # so we call str_to_date when JSON does not know how to serialize a field.
        json_string = json.dumps([vars(project) for project in projects], default=date_to_str)
        print(json_string, file=out_file)

    # PICKLE METHOD:
    # ----------------------------------------------
    # with open(filename, "wb") as out_file:
    #     pickle.dump(projects, out_file)


def get_new_project() -> Project:
    """Ask the user for information needed to create a new project.
    Returns the newly created project."""
    print("Let's add a new project")
    name = input("Name: ")
    date = get_date("Start date (DD/MM/YYYY): ")
    priority = int(input("Priority: "))
    cost_estimate = get_float("Cost estimate: ")
    percentage_complete = get_percentage("Percentage complete: ")
    return Project(name, date, priority, cost_estimate, percentage_complete)


def get_project(projects) -> Project:
    """Asks the user to select a project from projects.
    Continues to ask until a valid project is selected.
    Returns the project selected."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_number = get_positive_integer("Project choice: ")
    while project_number < 0 or project_number >= len(projects):
        print("Not a valid project number")
        project_number = get_positive_integer("Project choice: ")
    return projects[project_number]


def get_date(prompt) -> datetime.date:
    """Ask the user for a date in the format 'DD/MM/YYYY'.
    Continues to ask until a valid date is given.
    Returns a datetime.date."""
    while True:
        try:
            return str_to_date(input(prompt))
        except ValueError:
            print("Date entered does not match DD/MM/YYYY format")


def get_positive_integer(prompt, raise_exception_on_blank=False) -> int:
    """Ask the user for a positive integer (or zero).
    Continues to ask until a valid number is given.

    If raise_exception_on_blank is enabled we throw a ExitRequested exception
    when the user enters a blank line.
    """
    is_valid = False
    string = ""  # Prevents warnings.
    number = 0   # Prevents warnings.
    while not is_valid:
        try:
            string = input(prompt)
            number = int(string)
            if number >= 0:
                is_valid = True
            else:
                print("Number cannot be less than 0")
        except ValueError:
            if raise_exception_on_blank and string == "":
                raise ExitRequested()
            else:
                print("Not a valid number")
    return number


def get_float(prompt) -> float:
    """Ask the user to enter any decimal number.
    Continues to ask until a valid number is given."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Not a valid whole number")


def get_percentage(prompt, raise_exception_on_blank=False) -> int:
    """Ask the user for an integer between 0 and 100.
    Continues to ask until a valid number is given.

    If raise_exception_on_blank is enabled we throw a ExitRequested exception
    when the user enters a blank line.
    """
    percentage = get_positive_integer(prompt, raise_exception_on_blank)
    while percentage > 100:
        print("Must be between 0 and 100")
        percentage = get_positive_integer(prompt, raise_exception_on_blank)
    return percentage


def get_status_updates(project) -> (int, int):
    """Ask the user for a percentage completed and priority to update a project with.
    If blank is entered the given project values are used instead.
    Returns (percent_completed, priority) tuple."""
    try:
        percent_completed = get_percentage("New percentage: ", raise_exception_on_blank=True)
    except ExitRequested:
        percent_completed = project.percent_completed
    try:
        priority = get_positive_integer("New priority: ", raise_exception_on_blank=True)
    except ExitRequested:
        priority = project.priority
    return percent_completed, priority


def filter_projects_by_date(projects, date) -> list[Project]:
    """Make a list of projects filtered so that only those later than date
    are included, and sort these by date.
    Return the list created."""
    filtered_projects = [project for project in projects if project.date > date]
    return sorted(filtered_projects, key=attrgetter("date"))


def display_projects(projects):
    """Prints a list of incomplete projects and a list of complete projects,
    both sorted by priority."""
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]

    print("Incomplete projects")
    for project in sorted(incomplete):
        print(f"\t{project}")

    print("Complete projects")
    for project in sorted(complete):
        print(f"\t{project}")


if __name__ == '__main__':
    main()
