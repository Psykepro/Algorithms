# -- Big O notations -- #

# - Time Complexity - #
# Best - O(n)
# Average - O(n^2)
# Worst - O(n^2)

# - Space Complexity - #
# Worst = O(1)


class Bubble:
    @staticmethod
    def sort(arr):
        def swap(i, j):
            arr[i], arr[j] = arr[j], arr[i]

        n = len(arr)
        swapped = True
        x = -1
        while swapped:
            swapped = False
            x += 1

            for i in range(1, n-x):
                if arr[i-1] > arr[i]:
                    swap(i-1, i)
                    swapped = True

        return arr
