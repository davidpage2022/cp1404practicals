"""Project Management
Estimated: 70
Actual: 68 + 15
"""
import datetime
from operator import attrgetter

from prac_07.project import Project

FILENAME = "projects.txt"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


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
    # save_projects(projects, FILENAME)
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
    projects = []
    with open(filename) as in_file:
        in_file.readline()  # Ignore header row.
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            date = str_to_date(parts[1])
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            percent_completed = float(parts[4])
            projects.append(
                Project(name, date, priority, cost_estimate, percent_completed))
    return projects


def save_projects(projects: list[Project], filename):
    """Save a list of projects to a file with filename."""
    pass


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
    project_index = int(input("Project choice: "))
    return projects[project_index]  # TODO: Error check.


def get_date(prompt) -> datetime.date:
    """Ask the user for a date in the format 'DD/MM/YYYY'.
    Continues to ask until a valid date is given.
    Returns a datetime.date."""
    return str_to_date(input(prompt))  # TODO: Error check.


def get_positive_integer(prompt) -> int:
    """Ask the user for a positive integer (or zero).
    Continues to ask until a valid number is given."""
    return int(input(prompt))  # TODO: Error check.


def get_float(prompt) -> float:
    """Ask the user to enter any decimal number.
    Continues to ask until a valid number is given."""
    return float(input(prompt))  # TODO: Error check.


def get_percentage(prompt) -> float:
    """Ask the user for a number between 0 and 100.
    Continues to ask until a valid number is given."""
    return float(input(prompt))  # TODO: Error check.


def get_status_updates(project) -> (float, int):
    """Ask the user for a percentage completed and priority to update a project with.
    If blank is entered the given project values are used instead.
    Returns (percent_completed, priority) tuple."""
    percent_completed = get_percentage("New percentage: ")
    priority = get_positive_integer("New priority: ")
    if percent_completed == "":
        percent_completed = project.percent_completed
    if priority == "":
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
