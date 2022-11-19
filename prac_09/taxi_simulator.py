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
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            try:
                taxi_index = int(input("Choose taxi: "))
                if 0 <= taxi_index < len(taxis):
                    current_taxi = taxis[taxi_index]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi is not None:
                try:
                    distance = float(input("Drive how far? "))
                    if distance > 0:
                        current_taxi.start_fare()
                        current_taxi.drive(distance)
                        fare = current_taxi.get_fare()
                        current_bill += fare
                        print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                    else:
                        print("Invalid distance")
                except ValueError:
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
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()
