from DataStructures import primerange2d


def check_prime_anagram(lst):
    ret_lst = []  # List to return 2D Array
    anagram_list = []  # List to contain all anagrams
    non_ana_list = []  # List to contain non anagram primes
    while len(lst) != 0:
        temp = lst.pop(0)  # temp contains rows of primes from 2D array in check_prime_range()
        for i in range(len(temp)):
            for j in range(len(temp)):
                if i != j and sorted(str(temp[i])) == sorted(str(temp[j])):  # Check for Anagram
                    anagram_list.append(temp[i])
        for ana in anagram_list:
            if ana in temp:  # Removing anagram primes
                temp.remove(ana)
        for ele in temp:
            non_ana_list.append(ele)  # Adding elements into list of non anagram primes
    ret_lst.append(anagram_list)  # Creating 2-D return array
    ret_lst.append(non_ana_list)
    return ret_lst


if __name__ == "__main__":
    x = primerange2d.check_prime_range()
    y = check_prime_anagram(x)
    print(y)