import random

RAND_KEY = 123456

# matrix 1000 x 1000, max 999999 combinations 
random.seed(RAND_KEY)
a = random.sample(range(1000), 1000)

random.seed(RAND_KEY + 555)
b = random.sample(range(1000), 1000)

def encode(id):
    row_y = int(id/1000)
    if row_y > 0:
        row_x = id - 1000*row_y
    else: 
        row_x = id
    return "%03.0f" % (a[row_x]) + "%03.0f" % (b[row_y])
    
def decode(val):
    def s(data):
        return data.lstrip('0')
    row_x = a.index(int(s(val[0:3])))
    row_y = b.index(int(s(val[3:6])))
    if row_y == 0:
        return row_x
    else:
        return 1000*row_y + row_x
    
def test():
    data = []
    for i in xrange(999999):        
        data.append(encode(i))
    return len(set(data))

print encode(93442)
print decode(encode(93442))
print test()


    



