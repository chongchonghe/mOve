from getdir import *

if __name__ == "__main__":
    try:
        print("'{}'".format(main(sys.argv[1])))
    except BaseException as err:
        print(err, file=sys.stderr)
        print(".")
