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
        '1': ['add_book', '添加图书'],
        '2': ['borrow_book', '借书'],
        '3': ['return_book', '还书'],
        '4': ['search_book', '查询书籍'],
        '5': ['change_book', '修改书籍信息'],
        '6': ['save_book_to_json', '本地化保存数据信息(json格式)']
    }
    library = library_system()
    # library.add_book()
    meth_list = [library.add_book, library.borrow_book, library.return_book, library.search_book,
                 library.change_book, library.save_book_to_json]

    while True:
        for key, valus in model_dict.items():
            message = '{}-{}'.format(key, valus[1])
            print(message)

        user_choose = input('enter your choose number from the menu（q or Q is quit）')
        if user_choose.upper() == 'Q':
            break
        if not user_choose.isdecimal():
            print('error')
            continue
        # user_choose_method用户选择的操作项目
        user_choose_method = model_dict[user_choose][1]
        print(user_choose_method)
        user_choose=int(user_choose)-1
        user_method=meth_list[user_choose]()
        # library.
        # user_choose_method用户选择的操作项目
        # try:
        #     user_choose_method=model_dict[user_choose][0]
        #     print(user_choose_method)
        # except Exception as e:
        #     print('error')
