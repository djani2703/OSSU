# Iterative solution:
def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

# Recursive solution:
def mult_recurs(a, b):
    if b == 1:
        return a
    else:
        return a + mult_recurs(a, b-1)

# Iterative version of factorial:
def factorial_iter(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod

# Recursive version of factorial:
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Recursion solution of Tower of Hanoi:
def print_move(fr, to):
    print('move from ', str(fr) + 'to' + str(to))

def towers(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)
    else:
        towers(n-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)

# Recursion solution of Fibonacci:
def fib(n):
    if n in [0, 1]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Palindrome example:
def is_palindrome(s):
    def to_chars(s):
        s = s.lower()
        answer = ''
        for char in s:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                answer += char
            return answer
    
    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])
    return is_pal(to_chars(s))

# Creating a dictionary:
def lyrics_to_frequencies(lyrics):
    my_dict = {}
    for word in lyrics:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict

# Using the dictionary:
def most_commot_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)
 
# Leveraging dictionary properties:
def words_often(freqs, min_times):
    result = []
    done = False    
    while not done:
        temp = most_commot_words(freqs)
        if temp[1] >= min_times:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

# Fibonacci with a dictionary:
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans


if __name__ == '__main__':
    # Iterative solution:
    print(mult_iter(2, 5))

    # Recursive solution:
    print(mult_recurs(2, 5))

    # Iterative and recursive versions of factorial:
    print(factorial_iter(5))
    print(factorial(5))

    # Recursion solution of Fibonacci:
    print(fib(5))

    # Palindrome example:
    print(is_palindrome('smallams'))

    # A Python dictionaries:
    my_dict = {}
    
    grades = {'Ana': 'B', 'John': 'A+', 'Denise': 'A', 'Katy': 'A'}
    grades['Sylvan'] = 'A'
    del(grades['Ana'])

    keys = grades.keys()
    values = grades.values()
    
    # Creating a dictionary:

    limp_bizkit_angels_text = [
        'Lookin', 'back', 'the', 'day', 'you', 'left',
        'Where', 'you', 'went', 'I', 'can', 'only', 'guess',
        'Where', 'I', 'will', 'be', 'some', 'other', 'day',
        'A', 'memory', 'with', 'all', 'I', 'had', 'to', 'say']

    lyrics = lyrics_to_frequencies(limp_bizkit_angels_text)

    # Using the dictionary:
    (words, best) = most_commot_words(lyrics)

    # Leveraging dictionary properties:
    print(words_often(lyrics, 2))

    # Fibonacci with a dictionary:
    d = {1: 1, 2: 2}
    print(fib_efficient(6, d))