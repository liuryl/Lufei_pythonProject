# 图书管理系统的编写:
# 图书类Book：
#     属性：书名name 作者author 是否借出isborrow 书籍ID bookID 书籍类型category
#     注意：书籍ID不能重复
# 图书管理系统BookManager类
#  存放图书的工具使用列表
#  方法：
#  1.添加图书
#  2.借书 （根据图书名字借书）要检验图书是否存在、图书是否已经借出
#  3.还书
#  4.查询书籍 （根据名字查询， 根据类别查询）
#  5.修改书籍信息（根据书籍ID修改）
#  6.本地化保存数据信息(json格式)

from library_system import library_system
# import
if __name__ == '__main__':
    # book_dict =
    model_dict = {
        '1': [library_system.add_book, '添加图书'],
        '2': [library_system.borrow_book, '借书'],
        '3': [library_system.return_book, '还书'],
        '4': [library_system.search_book, '查询书籍'],
        '5': [library_system.change_book, '修改书籍信息'],
        '6': [library_system.save_book_to_json, '本地化保存数据信息(json格式)']
    }

    a=library_system(1,1,1,1,1)
    a.add_book(1,1,1,1)
    while True:
        for key,valus in model_dict.items():
            message='{}-{}'.format(key,valus[1])
            print(message)

        user_choose=input('enter your choose number from the menu（q or Q is quit）')
        if user_choose.upper()=='Q':
            break
        if not user_choose.isdecimal():
            print('error')
            continue

        # user_choose_method用户选择的操作项目
        user_choose_method = model_dict[user_choose][1]
        print(user_choose_method)
        # user_choose_method用户选择的操作项目
        # try:
        #     user_choose_method=model_dict[user_choose][0]
        #     print(user_choose_method)
        # except Exception as e:
        #     print('error')