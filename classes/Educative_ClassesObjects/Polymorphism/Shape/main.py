from shapes.Rectangle import Rectangle
from shapes.Circle import Circle

def main():

    # handle the polymorphism
    shapes = [Rectangle(5, 10), Circle(10)]

    print(str(shapes[0].getArea()))
    print(str(shapes[0].getPerimeter()))
    print(shapes[0].__dict__)
    
    print(str(shapes[1].getArea()))
    print(str(shapes[1].getPerimeter()))
    print(shapes[1].__dict__)

if __name__ == '__main__':
    main()
