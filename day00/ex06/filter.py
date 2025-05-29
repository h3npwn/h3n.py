import sys

def ft_filter(func, it):
    if not func:
        return (item for item in it if item)
    else:
        return (item for item in it if func(item))

def main():
    if len(sys.argv) > 3:
        print("AssertionError: more than two argument are provided")
        exit(2)
    elif len(sys.argv) < 3:
        print("AssertionError: less than two argument are provided")
        exit(2)
    if not sys.argv[2].isdigit():
        print("AssertionError: argument is not an integer")
        exit(2)
    w = sys.argv[1].split(' ')
    s = int(sys.argv[2])
    print(list(ft_filter((lambda x: len(x) > s), w)))

if __name__ == "__main__":
    main()
