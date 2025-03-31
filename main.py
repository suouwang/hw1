import math_op
import math_op.advanced_op
import math_op.basic_op

func = int(input("1-加法\n2-減法\n3-乘法\n4-除法\n5-平均\n6-冪次\n7-平方根\n8-對數\n請輸入功能代碼: "))

match func:
    case 1:
        print(math_op.basic_op.add(float(input("Please enter a: ")),float(input("Please enter b: "))))
    case 2:
        print(math_op.basic_op.substract(float(input("Please enter a: ")),float(input("Please enter b: "))))
    case 3:
        print(math_op.basic_op.multiply(float(input("Please enter a: ")),float(input("Please enter b: "))))
    case 4:
        print(math_op.basic_op.devide(float(input("Please enter a: ")),float(input("Please enter b: "))))
    case 5:
        numstr = str(input("Please enter nums: "))
        numchar = numstr.split(" ")
        nums = []
        for i in numchar:
            nums.append(int(i))
        print(math_op.advanced_op.average(nums))
    case 6:
        print(math_op.advanced_op.power(float(input("Please enter a: ")),float(input("Please enter b: "))))
    case 7:
        print(math_op.advanced_op.sqrt(float(input("Please enter num: "))))
    case 8:
        print(math_op.advanced_op.log(float(input("Please enter a: ")),float(input("Please enter b: "))))
    case _:
        print("Error")