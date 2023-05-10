'''
#  1.添加图书
#  2.借书 （根据图书名字借书）要检验图书是否存在、图书是否已经借出
#  3.还书
#  4.查询书籍 （根据名字查询， 根据类别查询）
#  5.修改书籍信息（根据书籍ID修改）
#  6.本地化保存数据信息(json格式)
'''


class library_system:
    # def __init__(self, book_name, author, isborrow, bookID, category):
    #     self.book_name = book_name
    #     self.author = author
    #     self.isborrow = isborrow
    #     self.bookID = bookID
    #     self.category = category
    #     self.book_list=[]
    def __init__(self, book_name, author, isborrow, bookID, category):
        self.book_list = []
        self.book_name_list=[]
        self.book_category_list=[]

    def add_book(self, book_name, author, bookID, category):
        '''
        :param book_name: 图书名字用户输入
        :param author: 作者名字用户输入
        :param bookID: 图书ID
        :param category: 图书类型
        :return:
        '''
        dict_key_list = ['book_name', 'author', 'isborrow', 'bookID', 'category']
        book_info_list = [book_name, author, 0, bookID, category]
        book_info_dict = {}
        for i in range(len(dict_key_list)):
            # 通过for循环和字典注册书籍信息
            book_info_dict.setdefault(dict_key_list[i], book_info_list[i])
            # book_info_dict.update()
        #     将书籍添加到书籍列表
        self.book_list.append(book_info_dict)
        self.book_name_list.append(book_name)
        self.book_category_list.append(category)
        print(self.book_list)

    def isborrow_book(self, book_num):
        '''

        :param book_num: 图书在列表中的编号
        :return: 返回是否借出图书，借出返回1
        '''
        # self.book_list[book_num].update({'isborrow': '1'})
        return self.book_list[book_num].get('isborrow')

    def borrow_book(self, user_choose_book):
        '''
        :param user_choose_book: 要借的
        :return:
        '''
        for i in range(len(self.book_list)):
            if user_choose_book in list(self.book_list[i].values()) and library_system.isborrow_book(i) == '0':
                print('{} in library'.format(self.book_list[i].get('book_name')))
                self.book_list[i].update({'isborrow': '1'})
                result = library_system.isborrow_book(i)
                message = '{} for your library'.format(
                    self.book_list[i].get('book_name')) if result == '1' else 'error'
                print(message)

    def return_book(self, user_back_book):
        '''
        :param user_back_book: 要还的
        :return:
        '''
        for i in range(len(self.book_list)):
            if user_back_book in list(self.book_list[i].values()) and library_system.isborrow_book(i) == '1':
                print('{} need return'.format(self.book_list[i].get('book_name')))
                self.book_list[i].update({'isborrow': '0'})
                result = library_system.isborrow_book(i)
                message = '{} for your library'.format(
                    self.book_list[i].get('book_name')) if result == '0' else 'error'
                print(message)

    def search_book(self,need_search_book):
        '''
        :param need_search_book: 要找的书
        :return: 无
        '''
        if (need_search_book in self.book_name_list):
            book_local=self.book_name_list.index(need_search_book)
            for key,value in self.book_list[book_local].items():
                message='{}-{}'.format(key,value)
                print(message)
            pass
        for book in self.book_list:
            if need_search_book == book.get('category'):
                for key,value in book.items():
                    message='{}-{}'.format(key,value)
                    print(message)

    def change_book(self):
        pass

    def save_book_to_json(self):
        pass
