# join მაგალითი
words = ['Hello', 'world', 'Python', 'is', 'awesome']
# ვაერთიანებთ სიტყვებს ერთი სტრიქონად, გამყოფად ვიყენებთ space-ს (" ")
sentence = ' '.join(words)

print(sentence)
# შედეგი: Hello world Python is awesome



def sum_two_number(a, b):
    return a + b
result = sum_two_number(5, 7)
print(result)  # შედეგი: 12




def move_zeros_to_end(lst):
       non_zeros = [x for x in lst if x != 0]
        zero_count = lst.count(0)
       return non_zeros + [0] * zero_count
original_list = [0, 5, 0, 2, 7]
result = move_zeros_to_end(original_list)
print(result)  # შედეგი: [5, 2, 7, 0, 0]




def maskify(s):
    if len(s) <= 4:
        return s
     masked_part = '#' * (len(s) - 4)
    visible_part = s[-4:]
    return masked_part + visible_part
print(maskify("4556364607935616"))
print(maskify("Skippy"))
print(maskify("1"))
print(maskify(""))
