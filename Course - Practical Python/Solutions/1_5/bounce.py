"""
THis program will print the height of a ball

"""


def main():
    """Entry point if called as an executable"""
    height = 100
    bounce = 1
    while bounce <= 10:
        height = height * (3 / 5)
        print(bounce, round(height, 4))
        bounce += 1


if __name__ == "__main__":
    main()
