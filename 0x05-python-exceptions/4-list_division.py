#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res_list = []

    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            result = my_list_1[i] / my_list_2[i]
            res_list.append(result)
        except ZeroDivisionError:
            res_list.append(0)
            print("division by 0")
        except TypeError:
            res_list.append(0)
            print("wrong type")
        except IndexError:
            res_list.append(0)
            print("out of range")
        finally:
            pass

    return res_list
