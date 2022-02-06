from shapes.Rectangle import Rectangle
from shapes.Circle import Circle

def main():

    # handle the polymorphism
    shapes = [Rectangle(5, 10), Circle(10)]

    print(str(shapes[0].getArea()))
    print(str(shapes[0].getPerimeter()))
    
    print(str(shapes[1].getArea()))
    print(str(shapes[1].getPerimeter()))

if __name__ == '__main__':
    main()
