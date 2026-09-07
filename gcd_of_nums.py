def gcd(n1,n2):

    #Q -> quotient
    # A -> divident
    # B -> divisor
    #R -> reminder

    gcd = None
    quotient = None
    reminder = None

    if n1 > n2:
        divident = n1
        divisor = n2
    elif n2 > n1:
        divident = n2
        divisor = n1
    elif n1 == n2:
        divident = n1
        divisor = n2
    while True:
        if divisor == 0:
            gcd = divident
            break
        else:
            reminder = divident % divisor
            quotient = divident // divisor

            divident = divisor
            divisor = reminder
    return gcd

print(gcd(12,33))