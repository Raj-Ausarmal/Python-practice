def myfunc():
    print("Hello world")


if __name__ == "__main__":
    # If this code is directly executed by running the file in its own
    # context the code below this line is executed
    myfunc()
    print(__name__)
