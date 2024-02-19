from source.add import add
from source.sub import sub
from ZOO.bird import Bird

def main():
    add_number = add(1, 2, 3, 4, 5)
    sub_number = sub(1, 2, 3, 4, 5)

    type_animal_dict = {
        1: 'khazandeh',
        2: 'parandeh'
    }

    print(type_animal_dict)
    type_animal = input("enter type animal: ")
    name = input("enter name animal: ")


    bird = Bird(type=type_animal, name=name)
    print(bird.fly())


    return (add_number, sub_number)





print(main())