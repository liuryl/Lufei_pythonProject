import random

# 代码示例：（请补充实现）
total_poke_list = []
card = []
result = {}
user_list = ["alex","武沛齐","李路飞"]
color_list = ["红桃", "黑桃", "方片", "梅花"]
big_king = ('大王', 15*0.5)
small_king = ('小王', 14*0.5)

for color in color_list:
    for i in range(1,14):
        card.append(color)
        if i>10:
            i = i*0.5
        card.append(i)
        card_tuple = tuple(card)
        # print(card_tuple)
        total_poke_list.append(card_tuple)
        card.clear()
# 补充代码
total_poke_list.append(big_king)
total_poke_list.append(small_king)
print(total_poke_list)
for name in user_list:
    first_num = random.randint(0,len(total_poke_list)+1)
    first_card = total_poke_list[first_num]
    result.setdefault(name,first_card[1])
    total_poke_list.pop(first_num)
print(result)
while True:
    # alex choose
    alex_choose = input("please alex enter y or n")
    if alex_choose == 'n':
        print("alex choose skip")
        pass
    elif alex_choose == 'y':
        alex_new_num = random.randint(0,len(total_poke_list)-1)
        alex_new_card = total_poke_list[alex_new_num][1]
        # print(alex_new_card)
        new_num = int(alex_new_card) + int(result['alex'])
        # print(new_num)
        if new_num > 11:
            print("alex boom")
            new_num = 0
        result.update({'alex': new_num})
        # print(alex_new_card)
        print(result['alex'])
        total_poke_list.pop(alex_new_num)
    # wupeiq_choose = input("please enter y or n")
    # if wupeiq_choose == 'n':
    #     print("wupeiqi choose skip")
    #     pass
    # wupeiqi choose
    wu_choose = input("please wu_choose enter y or n")
    if wu_choose == 'n':
        print("wu_choose choose skip")
        pass
    elif wu_choose == 'y':
        wu_new_num = random.randint(0,len(total_poke_list)-1)
        wu_new_card = total_poke_list[wu_new_num][1]
        # print(wu_new_card)
        new_num = int(wu_new_card) + int(result['武沛齐'])
        # print("wu"+str(new_num))
        if new_num > 11:
            print("wu boom")
            new_num = 0
        result.update({'武沛齐': new_num})
        # print(wu_new_card)
        print(result['武沛齐'])
    total_poke_list.pop(wu_new_num)


    # li choose
    li_choose = input("please wu_choose enter y or n")
    if li_choose == 'n':
        print("li_choose choose skip")
        pass
    elif li_choose == 'y':
        li_new_num = random.randint(0, len(total_poke_list)-1)
        li_new_card = total_poke_list[li_new_num][1]
        # print(li_new_card)
        new_num = int(li_new_card) + int(result['李路飞'])
        # print("li" + str(new_num))
        if new_num > 11:
            print("li boom")
            new_num = 0
        result.update({'李路飞': new_num})
        # print(li_new_card)
        print(result['李路飞'])
    total_poke_list.pop(li_new_num)

    if len(total_poke_list) == 0:
        print("end")
        break
    print("len : "+str(len(total_poke_list)))