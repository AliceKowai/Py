def power1(n):
    if n <= 0:
        return 1
    else: 
        return 2*power1(n-1)

def sun_intergers(n):
    if n <=1:
        return 1
    else: 
        return n + sun_intergers(n-1)

def sun_array(array):
    if len(array) ==1:
        return[0]
    return array[0] + sun_array(array[1:])
