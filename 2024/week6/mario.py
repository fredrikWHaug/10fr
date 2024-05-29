
def get_height():
    while True:
        try:
            height = int(input('Enter an integer between 1 and 8: '))
            if 1 <= height <= 8:
                return height
        except ValueError:
            pass

def main():
    get_height()

if __name__ == '__main__':
    main()