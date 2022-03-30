# https://www.codechef.com/MARCH222D/problems/INCRIQ


def checkIQ(iq):
    eiq = 170

    if ((iq +7) > eiq):
        return 'Yes'
    else:
        return 'No'

iq = int(input())
print(checkIQ(iq))
