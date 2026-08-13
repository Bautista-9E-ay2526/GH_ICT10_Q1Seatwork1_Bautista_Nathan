# Seatwork 1
from pyscript import display


name = 'Nathan Li Bautista'  #String
age = 15 #Integer
height167 = 167 #Integer
countries_visit = ['Switzerland','The Bahamas','France','England'] #List
student_type = False #Boolean 
sample_dict = {'color':'blue','car_brand':'Ferrari', 'shoe_size':'9','best_friend':'Franco'} #Dictionary
favorite_fruits = {'Mango', 'Melon','Strawberry','Banana','Apple'} #Set
days_in_week = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday") #Tuple


display(f'Hello! My name is {name} and I am {age}. My height is {height167}cm.',target = "output")
display(f'Some countries that I would like to visit are {countries_visit}.',target = "output")
display(f'It is {student_type} that I am a new student in OBMC.',target = "output")
display(f'Here are more stuff that I like {sample_dict}.',target = "output")
display(f'I am a picky eater but here are some fruits that I like {favorite_fruits}.',target = "output")
display(f'There are 7 days in a week and they are {days_in_week}.',target = "output")
