def move_square(size):
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")

def move_rect(length, width):
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")

def move_circle():
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")

def dancing_square():
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        size = 20
        length = 20
        print("* Move Forward "+str(length))
        # print("Moving in a square of size 10")
        move_square(size)

def crop_circle(length):
    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward "+str(length))
        # print("Moving in a circle")
        move_circle()

# TODO: Decompose into functions
def move():
    size = 10
    length = 20
    width = 10 

    move_square(size)
    move_rect(length, width)
    move_circle()
    dancing_square()
    crop_circle(length)

def robot_start():
    move()

if __name__ == "__main__":
    robot_start()
