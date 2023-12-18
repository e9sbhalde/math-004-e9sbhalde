"""In this program we have to find the largest palindrome 
made from the product of two 3-digit numbers."""

def answer():
    """This function finds the largest palindrome made from
      the product of two 3-digit numbers."""
    mylist = []
    myset = ()
    for i in range(111, 1000):
        for j in range(111, 1000):
            num = i * j
            temp = num
            rev = 0
            while num > 0:
                number = num % 10
                rev = rev * 10 + number
                num = num // 10
                if temp == rev:
                    mylist.append(temp)
                    myset = set(mylist)
                    answers = max(myset)
    return answers


if __name__ == "__main__":
    print(answer())
