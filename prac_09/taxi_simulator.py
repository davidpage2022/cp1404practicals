"""Taxi Simulator exercise:
Simulates various taxi services."""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Allow user to select taxis, drive them and then display the fare cost."""
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi(name="Limo", fuel=100, fanciness=2),
             SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]
    current_taxi = None
    current_bill = 0.0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_index = get_taxi_index(taxis)
            if taxi_index is not None:
                current_taxi = taxis[taxi_index]
            else:
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi is not None:
                distance = get_drive_distance()
                if distance is not None:
                    current_taxi.start_fare()
                    current_taxi.drive(distance)
                    fare = current_taxi.get_fare()
                    current_bill += fare
                    print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                else:
                    print("Invalid distance")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${current_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${current_bill}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display taxis in a numbered list, showing their details."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_taxi_index(taxis):
    """Asks the user for a taxi index.

    :return: If the taxi index is valid returns the index.
    Otherwise, returns None."""
    try:
        taxi_index = int(input("Choose taxi: "))
        if 0 <= taxi_index < len(taxis):
            return taxi_index
        else:
            return None
    except ValueError:
        return None


def get_drive_distance():
    """Asks the user for a distance to drive.

    :return: If the distance is valid (i.e. a positive number), returns the distance.
    Otherwise, returns None."""
    try:
        distance = float(input("Drive how far? "))
        if distance > 0:
            return distance
        else:
            return None
    except ValueError:
        return None


if __name__ == '__main__':
    main()
