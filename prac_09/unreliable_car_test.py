"""Unreliable car class test"""
from prac_09.unreliable_car import UnreliableCar


def main():
    car = UnreliableCar(name="Lemon", fuel=100, reliability=50)
    for i in range(15):
        print(f"{car.name} drove {car.drive(2)}")


if __name__ == '__main__':
    main()
