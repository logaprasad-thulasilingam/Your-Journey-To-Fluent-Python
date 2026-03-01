"""
To create a Rectangle like the below:

*******
*     *
*     *
*     *
*     *
*******

"""

def star_rectangle(width, length):
    for i in range(0, length):
        if i == 0 or i == length -1:
            print("*" * width)
        else:
            print("*", ' ' * (width - 4), "*")



star_rectangle(7, 6)
