# -- Big O notations -- #

# - Time Complexity - #
# Best - O(n)
# Average - O(n^2)
# Worst - O(n^2)

# - Space Complexity - #
# Worst = O(1)


class Insertion:
    @staticmethod
    def sort(arr):
        n = len(arr)
        for i in range(n):

            cursor = arr[i]
            pos = i

            while pos > 0 and arr[pos - 1] > cursor:
                # Swap the number down the list
                arr[pos] = arr[pos - 1]
                pos = pos - 1

            arr[pos] = cursor

        return arr
