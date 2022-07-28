'''
print prime numbers
'''
import math
num1 = int(input('Enter Start value'))
num2 = int(input('Enter End value'))


def prime(var1, var2):
    if var1 <= 0 or var2 <= 0:
        print('Input should be +ve integers')
    if var1 == var2:
        print('Start and End values cannot be the same')
    else:
        prime_list = []
        if var1 > var2:
            temp1 = var1
            var1 = var2
            var2 = temp1
        count = var1
        while count <= var2:
            if count == 1 or count == 2:
                print(count, ' - neither prime nor composite')
            else:
                for x in range(2, math.ceil(count / 2) + 1):
                    if count % x == 0:
                        break
                    else:
                        if x == math.ceil(count / 2):
                            prime_list.append(count)
                            # print(count)
            count += 1
        # print("end")
        return prime_list


if __name__ == '__main__':
    print(prime(num1, num2))