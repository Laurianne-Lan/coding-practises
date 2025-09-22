import random
def find(n, lst):
    left = 0  # 左指针，初始指向数组第一个元素
    right = len(lst) - 1  # 右指针，初始指向数组最后一个元素
    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == n:
            return mid  # 找到目标，返回索引
        elif lst[mid] < n:
            left = mid + 1  # 目标在右侧，移动左指针
        else:
            right = mid - 1


#前提lst包含所有考生的成绩并从高到低排序好的
#number 为admission amount
class Admission:
    def __init__(self, number, lst):
        self.number = number
        self.lst = lst
        self.total_num = len(self.lst)
    def cal_admission_line(self):
        b = self.lst[self.number-1]
        return b
    def cal_ratio(self, grade):
        i = find(grade, self.lst)
        r = (i+1)/self.total_num
        return r




# 测试代码移到类外部（正确位置）
if __name__ == "__main__":
    # 生成测试数据
    total_students = random.randint(3000, 6000)  # 总考生数
    scores = [random.randint(450, 750) for _ in range(total_students)]  # 随机成绩
    scores_sorted = sorted(scores, reverse=True)  # 降序排列（符合前提）
    admit_number = random.randint(1, total_students)  # 合理的录取人数（1~总人数）
    sample_grade = random.choice(scores)  # 随机选一个成绩作为样本

    # 创建实例（参数匹配：录取人数、成绩列表）
    admission_obj = Admission(admit_number, scores_sorted)

    # 测试1：计算录取线
    admission_line = admission_obj.cal_admission_line()
    print(f"总考生数：{total_students}，录取人数：{admit_number}")
    print(f"录取线为：{admission_line}分（第{admit_number}名的成绩）")

    # 测试2：计算某成绩的录取率
    ratio = admission_obj.cal_ratio(sample_grade)
    print(f"成绩{sample_grade}分的录取率为：{ratio:.2%}（该成绩及以上的考生占比）")


