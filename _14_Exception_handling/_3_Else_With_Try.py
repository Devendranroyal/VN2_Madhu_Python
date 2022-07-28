'''
@author: madhu
'''



def get_number(x, y):
    try:
        print("-----IN TRY BLOCK--------")
        result = x / y
        print("The result for division is : ", result)
        # float_res = round(24.601 / 0.01234, 4.6)
    except Exception as err:  # Exception err = ZeroDivisionError()
        print("---Error is being handled by super class Exception-----", err)
        """  
        except ZeroDivisionError as err:
            print("Please enter value other than Zero :: ",err, " is not supported programmatically")
        except TypeError as err:
            print("Plese check the calculation :::  ",err)
        except OverflowError as err:
            print("Please enter value other than Zero :: ",err, " is not supported programmatically")
        except Exception as err:
            print("---------------")
        """
    else:
        print("--------In ELSE block---------")
    finally:
        print("------Finally block--------------")
    
get_number(20,10)

