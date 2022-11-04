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
            load_projects(filename)

        elif choice == "S":  # Save.
            filename = input("Filename: ")
            save_projects(projects, filename)

        elif choice == "D":  # Display.
            display_projects(projects)

        elif choice == "F":  # Filter.
            date = get_date("Show projects that start after date (dd/mm/yy): ")
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


def load_projects(filename) -> list[Project]:
    """Load projects from filename.
    Returns a list of loaded projects."""
    projects = []
    with open(filename) as in_file:
        in_file.readline()  # Ignore header row.
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
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
    pass


def get_project(projects) -> Project:
    """Asks the user to select a project from projects.
    Returns the project selected."""
    # for i, project in enumerate(projects):
    #     print(f"{i} {project}")
    pass


def get_date(prompt) -> datetime.date:
    """Ask the user for a date in the format 'dd/mm/yy'.
    Returns a datetime.date."""
    pass


def get_status_updates(project) -> (float, int):
    """Ask the user for a percentage completed and priority to update a project with.
    If blank is entered the given project values are used instead.
    Returns (percent_completed, priority) tuple."""
    percent_completed = input("New percentage: ")
    priority = input("New priority: ")

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
    return sorted(filtered_projects, key=attrgetter(date))


def display_projects(projects):
    """Prints a list of incomplete projects and a list of complete projects,
    both sorted by priority."""
    for project in projects:
        print(project)   # TODO: Separate into incomplete and complete lists, then sort each by priority.


if __name__ == '__main__':
    main()
