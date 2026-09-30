#Global scope
customer_age = 25
print("Gobal Variable: ", customer_age)

#Local Variable
def add():
    print("Global Variable In Local Scop: ", customer_age)
    local_variable_1 = 100
    local_variable_2 = 200
    sum = local_variable_1 + local_variable_2
    print("Local Variables Sum: ", sum)


add()
#Not supported
#print("Local Variable 1: ", local_variable_1)