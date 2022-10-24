import datetime

gv_input = str(input('Please enter your age: '))
while not gv_input.isdigit():
    gv_input = input('Please enter an integer for your age:')

gv_age = int(gv_input)
gv_datetime = datetime.datetime.now()
gv_age100 = gv_datetime.year - gv_age + 100

print(f"You can look forward to your 100th anniversary in  {gv_age100}.")