from Car import Car

def main():
    car1 = Car("VW", "Grey", 2012, "Jetta")
    print(car1.printCarDetails())
    print(car1.displayMPG())


if __name__ == "__main__":
    main()

# why the __pycache__ is generated
# super can be called for initializers, functions or class properties