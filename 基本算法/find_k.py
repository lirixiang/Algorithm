def find_k(test_list, k):
    flag = test_list[0]
    test_list.pop(0)
    l_list = [i for i in test_list if i < flag]
    r_list = [i for i in test_list if i >= flag]

    # 结果递归的基线条件
    if len(r_list) == k - 1:
        return flag
    elif len(r_list) > k - 1:
        return find_k(r_list, k)
    else:
        # 因为test_list.pop(0)让test_list少了一个元素，所以下面需要+1
        print(len(test_list))
        print(len(l_list))
        gap = len(test_list) - len(l_list) + 1
        k = k - gap
        return find_k(l_list, k)


if __name__ == '__main__':
    test_list = [6,5, 4, 3, 2, 1]
    res = find_k(test_list, 3)
    print(res)

