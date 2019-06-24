print(">> App Started")

numbers = [10, 20, 30, 40, 50]

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = 0
idx = int(input("Enter Index to View Data: "))

try:
    print(numbers[idx])
    c = a // b
# except IndexError as iRef:
#     print("Some Error Occurred:",iRef)
# except ZeroDivisionError as zRef:
#     print("Some Error Occurred:",zRef)
except Exception as eRef:
    print("Some Error Occurred:", eRef)
finally:
    print("This is Awesome")

print("c is:",c)

print(">> App Finished")

# Graceful/Normal Termination of Program
# Line#1 till end of line was executed :)

# AbNormal Termination of Program / Run Time Error
# Crash in Program :)

"""
    try:
        ...
    except:
        ...
    finally:
        ... 
        
    try:
        ...
    except:
        ...
    except:
        ...
    finally:
        ...   
    
    try:
        try:
            ...
        except:
            ...
        finally:
            ...   
    except:
        try:
            ...
        except:
            ...
        finally:
            ...  
    finally:
        try:
            ...
        except:
            ...
        finally:
            ...   
        
         
         
     Exception                  : Parent Class
         ZeroDivisionError      : Children to Exception 
         IndexError
         .
         ..
         .....    
                 
"""