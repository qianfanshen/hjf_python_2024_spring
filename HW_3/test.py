# 迭代器的构建与使用，以及使用类建立数据结构
class MinHeap:
    def __init__(self, compare=lambda x, y: x[1] < y[1]):
        # 初始化
        self.heap_list = [("", 0)]
        self.current_size = 0
        self.compare = compare

    def append(self, k):
        # 将k放入最小堆中，同时维护最小堆
        self.heap_list.append(k)
        self.current_size += 1
        self.sift_up(self.current_size)

    def sift_up(self, i):
        # 向上移动二叉树中的值，维护最小堆
        while i // 2 > 0:
            if self.compare(self.heap_list[i], self.heap_list[i // 2]):
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

    def sift_down(self, i):
        # 向下移动二叉树中的值，维护最小堆
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.compare(self.heap_list[mc], self.heap_list[i]):
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        if (i * 2) + 1 > self.current_size:
            return i * 2
        else:
            if self.compare(self.heap_list[i * 2], self.heap_list[(i * 2) + 1]):
                return i * 2
            else:
                return (i * 2) + 1

    def delete_min(self):
        # 删除最小值
        if len(self.heap_list) == 1:
            return 'Empty heap'

        root = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        *self.heap_list, _ = self.heap_list
        self.current_size -= 1

        # TODO 这里应该做什么？ (1')
        self.sift_down(1)

        return root

    def __iter__(self):
        # TODO (1')
        return self

    def __next__(self):
        # TODO (1')
        if self.current_size == 0:  # 如果堆为空，抛出StopIteration异常
            raise StopIteration
        return self.delete_min()


minheap = MinHeap()
minheap.append(('a', 10))
minheap.append(('b', 20))
minheap.append(('c', 5))
print(list(minheap))