# 记录所有的名片列表
card_List = []
def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用 【名片管理系统】 V1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("_" * 50)
    print("新增名片")


    # 1.提示用户输入名片信息
    name_str = input("请输入姓名： ")
    phone_str = input("请输入电话： ")
    qq_str = input("请输入QQ： ")
    email_str = input("请输入邮箱： ")

    # 2.使用用户输入的信息创建一个名片字典
    card_dict = {"name": name_str,
                  "phone": phone_str,
                  "QQ": qq_str,
                  "email": email_str}

    # 3.将名片字典添加到列表中
    card_List.append(card_dict)

    # 4.提示用户添加成功
    print("成功添加 %s 的名片" % name_str)


def show_all():
    """显示全部"""
    print("_" * 50)
    print("显示全部名片")

    # 判断是否有名片记录
    if len(card_List) == 0:
        print("当前没有任何名片记录，请使用新增功能添加名片！ ")
        return

    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)
    for card_dict in card_List:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["QQ"],
                                        card_dict["email"]))



def search_card():
    """搜索名片"""
    print("_" * 50)
    print("搜索名片")

    # 1.提示用户要搜索的姓名
    find_name = input("请输入要查找的姓名： ")

    # 2.遍历名片列表，查询要搜索的姓名，如果没有，提示用户
    for card_dict in card_List:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["QQ"],
                                            card_dict["email"]))
            # 针对找到的的名片记录进行修改和操作
            deal_card(card_dict)
            break
    else:
        print("抱歉，没有找到 %s 的名片" % find_name)


def deal_card(find_dict):
    """
    处理查找到的名片
    :param find_dict:查找到的名片字典
    :return: 结束处理函数
    """

    action_str = input("请输入要进行的操作 "
                       "[1] 修改 [2] 删除 [0] 返回上级菜单： ")

    if action_str == "1":
        find_dict["name"] = input_info(find_dict["name"], "姓名: ")
        find_dict["phone"] = input_info(find_dict["phone"], "电话: ")
        find_dict["QQ"] = input_info(find_dict["QQ"], "QQ: ")
        find_dict["email"] = input_info(find_dict["email"], "邮箱: ")
        print("成功修改名片！")

    elif action_str == "2":
        card_List.remove(find_dict)
        print("成功删除名片！")

    elif action_str == "0":
        return

def input_info(dict_value, tip_message):

    """
    输入名片信息
    :param dict_value:字典中原有的值
    :param tip_message: 提示信息
    :return:
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)

    # 2.针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str

    # 3.如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value