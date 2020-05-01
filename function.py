def square(n):
    return n * n

def main():
    for i in range(1, 21):
        print("{} squared is {}".format(i, square(i)))

if __name__ == "__main__":
    main()