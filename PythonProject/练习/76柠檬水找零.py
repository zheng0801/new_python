# 在柠檬水摊上，每一杯柠檬水的售价为5美元。顾客排队购买你的产品，(按账单bills支付的顺序)一次购买一杯。
# 每位顾客只买一杯柠檬水，然后向你付5美元、10 美元或 20 美元。你必须给每个顾客正确找零也就是说净交易是每位顾客向你支付5美元。
# 注意，一开始你手头没有任何零钱。如果你能给每位顾客正确找零，返回true，否则返回 false

bills = [5, 10, 10, 5, 20, 5, 10]
moneys = 0
moneys_dict = {5 : 0, 10 : 0, 20 : 0}
flag = True

# #方法一:
# # money = int(input('请输入支付的金额：'))
# for bill in bills:
#     count_moneys = 5*moneys_dict[5] +10*moneys_dict[10] +20*moneys_dict[20]
#     if bill == 10:
#         if moneys_dict[5] == 0:
#             flag =False
#             break
#         else:
#             moneys_dict[5] -= 1
#     elif bill == 20:
#         if moneys_dict[5] < 1 or count_moneys < 15:
#             flag = False
#             break
#         else:
#             moneys_dict[5] -= 1
#             moneys_dict[10] -= 1
#     moneys_dict[bill] += 1
#
# if flag:
#     print('true')
# else:
#     print('false')

#方法二：
def func(bills):
    five = 0
    ten = 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        elif bill == 20:
            if five > 0 and ten > 0:
                five -= 1
                ten -= 1
            elif five >= 3:
                five -= 3
            else:
                return False

if func(bills) == False:
    print('false')
else:
    print('true')

