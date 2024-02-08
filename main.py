from source.add import add
from source.sub import sub


def main():
    add_number = add(1, 2, 3, 4, 5)
    sub_number = sub(1, 2, 3, 4, 5)

    return (add_number, sub_number)


print(main())