def my_decorator(function):
    def my_squeak(*arg):
        print ("SQUEAK")
        result = function(*arg)
        return result
    return my_squeak

@my_decorator
def add_ingot(purse):
    result = {}
    result.update(purse)
    result.update( {"gold_ingots": result.get("gold_ingots", 0) + 1} )
    return result

@my_decorator
def get_ingot(purse):
    result = {}
    result.update(purse)
    if result.get("gold_ingots", 0) != 0:
        result.update( {"gold_ingots": result.get("gold_ingots", 1) - 1} )
    return result

@my_decorator
def empty(purse):
    return {}

def split_booty(*args):
    pur_1 = {}
    pur_2 = {}
    pur_3 = {}
    sum = 0
    for i in args:
        sum += i.get("gold_ingots", 0)
    while (sum != 0):
        pur_1 = add_ingot(pur_1)
        sum -= 1
        if (sum != 0):
            pur_2 = add_ingot(pur_2)
            sum -= 1
            if (sum != 0):
                pur_3 = add_ingot(pur_3)
                sum -= 1
    return (pur_1, pur_2, pur_3)


if __name__ == "__main__":
    purse = {"gold_ingots": 2, "apple": 3}
    print (add_ingot(purse))
    print (get_ingot(purse))

    print (add_ingot({}))
    print (get_ingot({}))
    print (add_ingot(get_ingot(add_ingot(empty(purse)))))
    purse = {"apple": 3}
    print (get_ingot(purse))
    print (add_ingot(purse))

    print ()
    print ("split_ test")
    purse1 = {"gold_ingots": 2, "apple": 3}
    purse2 = {"gold_ingots": 5, "app": 2}
    purse3 = {}
    print (split_booty(purse1, purse2, purse3))
