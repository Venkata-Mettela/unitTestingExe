def biggest(x,y,z):
    if(check_int_float(x) and check_int_float(y) and check_int_float(z)):
        if(y<= x >=z):
            return x
        elif(x<= y >=z):
            return y
        elif (x<= z >=y):
            return z
        else:
            return "Error"

def check_int_float(x):
    if(type(x)== int or type(x) == float):
        return True
    else:
        return False