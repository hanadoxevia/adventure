from scenes import *
from introduction import introduction
import session

# Moved everything into main function
def main():
    session.init_session()
    introduction()
    scene = 0
    while True:
        if scene==0:
            scene = beach()
        elif scene == 1:
            scene = leftside()
        elif scene == 2:
            scene = rightside()
        else:
            print("other scene")
            break
    return

# Using if __name__ to detect when the file is being run directly as opposed to being imported
if __name__ == '__main__':
    # Run main function
    main()
