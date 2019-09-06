# -- Big O notations -- #

# - Time Complexity - #
# Best - O(n^2)
# Average - O(n^2)
# Worst - O(n^2)

# - Space Complexity - #
# Worst = O(1)


class Selection:
    @staticmethod
    def sort(arr):

        n = len(arr)
        for i in range(n):
            minimum = i

            for j in range(i+1, n):
                # Select the smalles value
                if arr[j] < arr[minimum]:
                    minimum = j

            # Place it at the front of the
            # sorted end of the array
            arr[i], arr[minimum] = arr[minimum], arr[i]

        return arr
