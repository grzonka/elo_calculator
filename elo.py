import sys



def print_name(name):
    print(name)

if __name__ == '__main__':
    #print("Number of arguments:" + str(len(sys.argv))) + " arguments."
    #print("Arguments are: " + str(sys.argv))
    print_name(sys.argv[1])