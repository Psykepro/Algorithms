# -- Big O notations -- #

# - Time Complexity - #
# Best - O(n * log(n))
# Average - O(n * log(n))
# Worst - O(n^2)

# - Space Complexity - #
# Worst = O(log(n))


class Quick:

    @staticmethod
    def partition(array, begin, end):
        pivot_idx = begin
        for i in range(begin + 1, end + 1):
            if array[i] <= array[begin]:
                pivot_idx += 1
                array[i], array[pivot_idx] = array[pivot_idx], array[i]
        array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
        return pivot_idx

    @staticmethod
    def sort_recursion(array, begin, end):
        if begin >= end:
            return

        pivot_idx = Quick.partition(array, begin, end)
        Quick.sort_recursion(array, begin, pivot_idx-1)
        Quick.sort_recursion(array, pivot_idx+1, end)

    @staticmethod
    def sort(array, begin=0, end=None):
        if end is None:
            end = len(array) - 1

        Quick.sort_recursion(array, begin, end)


arr = [3, 1, 4, 9, 2, 1]
Quick.sort(arr)
print(arr)
