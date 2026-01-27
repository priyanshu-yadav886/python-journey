def box_print(s, w, h):
    if len(s) != 1:
        raise Exception('Symbol must be a single character string.')
    if w <= 2:
        raise Exception('Width must be greater than 2.')
    if h <=2 :
        raise Exception('Height must be greater than 2.')
    
    print(s * w)
    for i in range(h - 2):
        print(s + (' ' * (w - 2)) + s)

    print(s * w)

try:
    box_print('*', 10 , 10)
    box_print('zz', 10 , 10)

except Exception as err:
    print('An Exception happened: ' + str(err))