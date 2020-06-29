
class ListHelper:

    @staticmethod
    def find_all(list_target,condition):
        """
        生成器，按条件寻找所有符合条件的元素
        :param list_target:
        :param condition:
        :return:
        """
        for item in list_target:
            if condition(item):
                yield item

    @staticmethod
    def select(list_target, func_handle):
        """
            通用的筛选方法,与内置高阶函数map作用一致
        :param list_target: 需要筛选的列表
        :param func_handle: 需要筛选的处理逻辑,函数类型
                函数名(参数) --> int／str/元组/其他类型的对象
        :return: 生成器
         """
        for item in list_target:
            yield func_handle(item)
    @staticmethod
    def find_count(list_target,condition):
        """
                生成器，对所有符合条件的元素计数
                :param list_target:
                :param condition:
                :return:
                """
        i=0
        for item in list_target:
            if condition(item):
                i+=1
                yield i
    @staticmethod
    def judge_person_consist(list_target,condition):
        """
                生成器，判断列表中是否存在满足人名条件的元素
                :param list_target:
                :param condition:
                :return:
                """
        state=0
        for item in list_target:
            if condition(item):
                state=1
                yield True
                break
        if state==0:
            yield False

    @staticmethod
    def judge_atk_range(list_target,condition):
        """
                生成器，判断是否有元素的攻击力在condition条件里的
                :param list_target:
                :param condition:
                :return:
                """
        state = 0
        for item in list_target:
            if condition(item):
                state = 1
                yield True
                break
        if state == 0:
            yield False

    @staticmethod
    def find_singele(list_target, condition):
        """
                不是生成器，按条件寻找单一符合条件的元素
                :param list_target:
                :param condition:
                :return:
                """
        for item in list_target:
            if condition(item):
                return item
    @staticmethod
    def sum_mine(list_target, condition):
        """
                不是生成器，按条件对所有元素做和
                :param list_target:
                :param condition:
                :return:
                """
        i=0
        for item in list_target:
            i+=condition(item)
        return i


    @staticmethod
    def find_all_data(list_target, condition):
        """
                    不是生成器，按条件对所有满足条件的元素做成列表并返回列表
                    :param list_target:
                    :param condition:
                    :return:
        """
        list01=[]
        for item in list_target:
            list01.append(condition(item))
        return list01

    @staticmethod
    def find_max_data(list_target, func_handle):
        """
                    不是生成器，寻找最大值
                    :param list_target:
                    :param condition:
                    :return:
        """
        max_value=list_target[0]
        for i in range(1,len(list_target)):
            if func_handle(max_value)<func_handle(list_target[i]):
                max_value=list_target[i]
        return max_value

    @staticmethod
    def find_min_data(list_target, func_handle):
        """
                    不是生成器，寻找最小值
                    :param list_target:
                    :param condition:
                    :return:
        """
        min_value = list_target[0]
        for i in range(1, len(list_target)):
            if func_handle(min_value) > func_handle(list_target[i]):
                min_value = list_target[i]
        return min_value

    @staticmethod
    def down_range(list_target, func_handle,term):
        """
                    不是生成器，升序（小在前，大在后）排序，如果term=True对原列表操作，没有返回值，
                    如果term=Flase则不对原列表操作，返回新列表
                    排序变量由func_handle给出
                    :param list_target:
                    :param condition:
                    :return:
        """
        if type(term)!=bool:
            raise ValueError("term应该赋bool类型变量")
        if term==True:
            for r in range(len(list_target) - 1):
                for c in range(r + 1, len(list_target)):
                    if func_handle(list_target[r]) < func_handle(list_target[c]):
                        list_target[r], list_target[c] = list_target[c], list_target[r]
        else:
            list00=[]
            for item in list_target:
                list00.append(item)
            list01=[]
            for r in range(len(list00) ):
                max=list00[r]
                for c in range(r + 1, len(list00)):
                    if func_handle(list00[r]) < func_handle(list00[c]):
                        max = list00[c]
                        list00[r], list00[c] =list00[c], list00[r]
                list01.append(max)
            return list01

    @staticmethod
    def up_range(list_target, func_handle, term):
        """
                    不是生成器，降序（大在前，小在后）排序，如果term=True对原列表操作，没有返回值，
                    如果term=Flase则不对原列表操作，返回新列表
                    排序变量由func_handle给出
                    :param list_target:
                    :param condition:
                    :return:
        """
        if type(term) != bool:
            raise ValueError("term应该赋bool类型变量")
        if term == True:
            for r in range(len(list_target) - 1):
                for c in range(r + 1, len(list_target)):
                    if func_handle(list_target[r]) > func_handle(list_target[c]):
                        list_target[r], list_target[c] = list_target[c], list_target[r]
        else:
            list00 = []
            for item in list_target:
                list00.append(item)
            list01 = []
            for r in range(len(list00)):
                max = list00[r]
                for c in range(r + 1, len(list00)):
                    if func_handle(list00[r]) > func_handle(list00[c]):
                        max = list00[c]
                        list00[r], list00[c] = list00[c], list00[r]
                list01.append(max)
            return list01

    @staticmethod
    def delete_element(list_target,condition):
        for i in range(len(list_target)-1,-1,-1):
            if condition(list_target[i]):
                del list_target[i]