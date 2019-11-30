from com.bridgelabz.utility import utility

def checkPrimeRange(lower_lim,upper_lim):
    primes_list = []
    for i in range(lower_lim,upper_lim):
        x = utility.isPrime(i)
        if x == True:
            primes_list.append(i)
    return primes_list

def check_prime_anagram():
    l_lim = int(input("Enter Lower Limit:\n"))
    u_lim = int(input("Enter Upper Limit:\n"))
    prime_anagrams = {}
    x = checkPrimeRange(l_lim,u_lim)
    for i in range(0,len(x)-1):
        for j in range(i+1,len(x)):
            if sorted(str(x[i])) == sorted(str(x[j])):
                prime_anagrams[x[i]] = x[j]
    return prime_anagrams

def check_prime_palindrome():
    l_lim = int(input("Enter Lower Limit:\n"))
    u_lim = int(input("Enter Upper Limit:\n"))
    prime_palindrome = {}
    x = checkPrimeRange(l_lim,u_lim)
    for i in range(0,len(x)-1):
        for j in range(i+1,len(x)):
            if str(x[i])[::] == str(x[j])[::-1]:
                prime_palindrome[x[i]] = x[j]
    return prime_palindrome

print(check_prime_anagram())
print(check_prime_palindrome())
