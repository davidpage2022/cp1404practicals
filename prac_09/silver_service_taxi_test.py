"""Silver service taxi class test"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [SilverServiceTaxi(name="Premium Taxi", fuel=100, fanciness=2),
             SilverServiceTaxi(name="Express Taxi", fuel=100, fanciness=1.5)]

    print(f"Base taxis price per km: ${Taxi.price_per_km:0.2f}")
    for taxi in taxis:
        print(taxi)
    print(f"Base taxis price per km: ${Taxi.price_per_km:0.2f}")


if __name__ == '__main__':
    main()
