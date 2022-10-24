def req_input(par_type):
    lv_question = "Please enter a number for " + par_type + " :"
    lv_input = str(input(lv_question))
    while not lv_input.isdigit():
        lv_input = str(input('Please enter an integer:'))
    return int(lv_input)

gv_max = req_input('the total of numbers shown')
gv_num1 = req_input('the starting number')
gv_num2 = req_input('the 2nd number')

gv_loopcount = 0
gv_list = list()
print(f"First {gv_max} Lucas numbers starting with {gv_num1} and {gv_num2}:")
while gv_loopcount < gv_max:
    if gv_loopcount == 0:
        lv_sum = gv_num1
    elif gv_loopcount == 1:
        lv_sum = gv_num2
    else:
        lv_sum = gv_num1 + gv_num2
        gv_num1 = gv_num2
        gv_num2 = lv_sum
    gv_list.append(lv_sum)
    gv_loopcount += 1
print(gv_list)
