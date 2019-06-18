#import
import datetime
import math
import os

os.system('cls')
#varibles
car_num = ''

enter_time = {}

time_enter = 0
leave_time = 0
stay_length = 0
stay_second = 0
stay_index = 0
fee_index = 1 # Per 30 minutes
fee = 0

#define
#find
def find():
    car_num = input('Please input the car number here:  ')  #input car number
    if car_num in enter_time:  #car is in car park
        leave_time = datetime.datetime.now()  #when is it now
        stay_length = leave_time - enter_time[car_num]  #how long it stay
        stay_second = round(stay_length.total_seconds())  #how long it stay in second
        stay_index = stay_second/60/30  #how many period does it stay
        stay_index = round(stay_index - 0.5)
        fee = stay_index * fee_index
        print(car_num, 'has stay here for ', stay_length, 'should pay ', fee, 'pound')
        del(enter_time[car_num]) #delete car number from the dictionary that cars are in
    else: #car is not in the car park
        time_enter = datetime.datetime.now()  #get the time when it enter
        enter_time.update({car_num:time_enter})  #store the car number and time that enter in to dictionary
        print(car_num, 'has successfully enter the car park at', time_enter) #print when it enter

# run find function 
while True:
    find()
    input(' ')
    os.system('cls')