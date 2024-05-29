# 1

def common_data(list1, list2):

    for char in list1:
        if char in list2:
            return True

    return False

print(common_data([1,2,3,4,5],[5,6,7,8,9]))
print(common_data([1,2,3,4,5],[6,7,8,9]))
print()

# 2


def test(lst,str1):
    for word in lst:
        if word in str1:
            return True

    return False


str1 = "https://www.w3resource.com/python-exercise/list/"
lst =['.com','.edu','.tv']
print(test(lst,str1))


str1 = "https://www.w3resource.net"
lst =['.com','.edu','.tv']
print(test(lst,str1))

