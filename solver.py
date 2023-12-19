"""In this program we have to find function that returns the largest palindrome from the product of
 two n-digit numbers where both numbers are inside a range."""


def solver(n, p=None, q=None):
    """this is the function that returns the largest palindrome from the product of
    two n-digit numbers where both numbers are inside a range."""
    mylist = []
    if p is None:
        p = 10 ** (n - 1)
    if q is None:
        q = 10**n

    for i in range(p, q + 1):
        for j in range(i, q + 1):
            num = i * j
            temp = num
            rev = 0

            while num > 0:
                number = num % 10
                rev = rev * 10 + number
                num = num // 10

            if temp == rev:
                mylist.append(temp)

    return max(mylist, default=None)


if __name__ == "__main__":
    print(solver(3))
