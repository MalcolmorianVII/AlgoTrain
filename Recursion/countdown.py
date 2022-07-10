# def count_down(num):

#     while num > 0:
#         print(num)
#         num -= 1
#     print("Take off!")
def count_down(num):
    print(num)
    if num == 0:
        return "Blast Off"
    count_down(num - 1)

count_down(5)