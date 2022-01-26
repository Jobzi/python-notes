try: 
    print(5/9)
except ZeroDivisionError:
    print("You can't divide by zero!")
    flash_msg="perro"
finally:
    print("This is the 'finally' block.")
print("->",flash_msg)