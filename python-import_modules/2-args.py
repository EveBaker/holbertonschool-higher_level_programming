import sys

def print_arguments():
    num_args = len(sys.argv) - 1 # Subtracting 1 because the script name itself is considered an argument

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
        print("1: " + sys.argv[1])
    else:
        print(f"{num_args} arguments:")
        for i in range(1, num_args + 1):
            print(f"{i}: {sys.argv[i]}")

if __name__ == "__main__":
    print_arguments()
