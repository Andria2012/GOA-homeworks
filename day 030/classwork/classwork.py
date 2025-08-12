def count_to_100():
    for i in range(1, 101):
        print(i)

count_to_100()



def my_function():
  print("hello ixvis tolma")


def print_reversed_list(lst):
    index = len(lst) - 1
    while index >= 0:
        print(lst[index])
        index -= 1

def filter_greater_than_10(numbers):
    result = []
    for num in numbers:
        if num > 10:
            result.append(num)
    return result

def remove_first_and_last(chars):
    return chars[1:-1]


def გამოითვალე_ჯამების_ნამრავლი(სია1, სია2):
    ჯამი1 = 0
    ჯამი2 = 0

    for ელემენტი in სია1:
        ჯამი1 += ელემენტი

    for ელემენტი in სია2:
        ჯამი2 += ელემენტი

    შედეგი = ჯამი1 * ჯამი2
    return შედეგი


def გააორმაგე_რიცხვები(სია):
    ახალი_სია = []
    ინდექსი = 0

    while ინდექსი < len(სია):
        გაორმაგებული = სია[ინდექსი] * 2
        ახალი_სია.append(გაორმაგებული)
        ინდექსი += 1

    return ახალი_სია


def ამოარჩიე_ლუწები(რიცხვების_სია):
    ლუწები = []
    for რიცხვი in რიცხვების_სია:
        if რიცხვი % 2 == 0:
            ლუწები.append(რიცხვი)
    return ლუწები