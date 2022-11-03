"""Project Management
Estimated: 70
Actual: 68
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
            display_projects()

        elif choice == "F":  # Filter.
            date = get_date("Show projects that start after date (dd/mm/yy): ")
            filtered_projects = filter_projects_by_date(projects, date)
            for project in filtered_projects:
                print(project)

        elif choice == "A":  # Add.
            project = get_new_project()
            projects.append(project)

        elif choice == "U":  # Update.
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            project = get_project(projects)
            print(project)
            percent_completed, priority = get_status_updates(project)
            project.percent_completed = percent_completed
            project.priority = priority

        print(MENU)
        choice = input(">>> ").upper()
    save_projects(projects, FILENAME)
    print("Thank you for using custom-built project management software.")


def load_projects(filename) -> list[Project]:
    """"""
    return []


def save_projects(projects, filename):
    """"""
    pass


def get_new_project() -> Project:
    """"""
    pass


def get_project(projects) -> Project:
    """"""
    pass


def get_date(param) -> datetime.date:
    """"""
    pass


def get_status_updates(project) -> (float, int):
    """"""
    percent_completed = input("New percentage: ")
    priority = input("New priority: ")

    if percent_completed == "":
        percent_completed = project.percent_completed
    if priority == "":
        priority = project.priority

    return percent_completed, priority


def filter_projects_by_date(projects, date) -> list[Project]:
    """"""
    filtered_projects = [project for project in projects if project.date > date]
    return sorted(filtered_projects, key=attrgetter(date))


def display_projects():
    """"""
    pass


def update_project(project):
    """"""
    pass


if __name__ == '__main__':
    main()
