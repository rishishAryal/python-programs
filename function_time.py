# hello guys today we are going to code  "how to calculate the execution time of a function using python"


# first step
# import time module
import time


# now lets create a decorator
def timer(func):
    def wrapper(*args,**kwargs):
        # we are using *args and **kwargs so we can take any number of paramneters or key value 
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        total_time=end_time-start_time  # since end time is greater than start time
        print("Time taken to execute a given function: ",total_time)
        return result
    return wrapper


# now lets create a function whose time we need to calculate
# for this examle we will use for loop for 10000 iterations
@timer
def loop():
    for _ in range(10000):
        return "run"
    
# now lets call the loop function
a=loop()

print(a)
# lets run and check if we have any error in the code
#so our code works yay!!!!

        
        
        
        
