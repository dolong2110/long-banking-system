from typing import List


class Sorting:
    
    def __init__(self, arr, field: str, method: str = ""):
        self.arr = arr
        self.field = field
        self.len = len(arr)

        if self.len < 20 or method == "insertion_sort":
            self.insertion_sort()
            return

        if method == "bubble":
            self.bubble_sort()
            return

        if self.len > 10**7 or method == "counting_sort":
            self.counting_sort()
            return

        self.heap_sort()

    def selection_sort(self) -> None:
        """
        Mutates lst so that it is sorted via selecting the minimum element and
        swapping it with the corresponding index
        Time complexity: O(n^2); Space complexity: O(1)
        Naive and not stable sorting
        """
        for i in range(self.len):
            min_index = i
            for j in range(i + 1, self.len):
                # Update minimum index
                if self.arr[j][self.field] < self.arr[min_index][self.field]:
                    min_index = j

            # Swap current index with minimum element in rest of list
            self.arr[min_index], self.arr[i] = self.arr[i], self.arr[min_index]

    def bubble_sort(self) -> None:
        """
        Mutates lst so that it is sorted via swapping adjacent elements until
        the entire lst is sorted.
        Time complexity: O(n^2); Space complexity: O(1)
        Naive and stable sorting
        """
        has_swapped = True
        # if no swap occurred, lst is sorted
        while has_swapped:
            has_swapped = False
            for i in range(self.len - 1):
                if self.arr[i][self.field] > self.arr[i + 1][self.field]:
                    # Swap adjacent elements
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    has_swapped = True

    def insertion_sort(self) -> None:
        """
        Mutates elements in a lst by inserting out of place elements into appropriate
        index repeatedly until lst is sorted
        Time complexity: O(n^2); Space complexity: O(1)
        Useful for small size array or nearly sorted array
        """

        for i in range(1, self.len):
            current_index = i

            while current_index > 0 and self.arr[current_index][self.field] < self.arr[current_index - 1][self.field]:
                # Swap elements that are out of order
                self.arr[current_index], self.arr[current_index - 1] = \
                    self.arr[current_index - 1], self.arr[current_index]
                current_index -= 1

    def heap_sort(self) -> None:
        """
        Mutates elements in lst by utilizing the heap data structure
        Time complexity: O(NlogN); Space complexity: O()
        A direct optimization of selection sort
        """

        # Time Complexity: O(logN)
        def max_heapify(heap_size, index):
            left, right = 2 * index + 1, 2 * index + 2
            largest = index
            if left < heap_size and self.arr[left][self.field] > self.arr[largest][self.field]:
                largest = left
            if right < heap_size and self.arr[right][self.field] > self.arr[largest][self.field]:
                largest = right
            if largest != index:
                self.arr[index][self.field], self.arr[largest][self.field] = \
                    self.arr[largest][self.field], self.arr[index][self.field]
                max_heapify(heap_size, largest)

        # heapify original lst
        for i in range(self.len // 2 - 1, -1, -1):
            max_heapify(self.len, i)

        # Time Complexity: O(N)
        # use heap to sort elements
        for i in range(self.len - 1, 0, -1):
            # swap last element with first element
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            # note that we reduce the heap size by 1 every iteration
            max_heapify(i, 0)


    def counting_sort(self) -> None:
        """
        Sorts a list of integers where minimum value is 0 and maximum value is k
        Time complexity: O(N+k) - N is size of input, k is the maximum number in arr; Space complexity: O(N)
        better when sorting numbers - id, user_index
        """
        k = max(self.arr)
        counts = [0 for _ in range(k + 1)]
        for element in self.arr:
            counts[element] += 1

        # we now overwrite our original counts with the starting index
        # of each element in the final sorted array

        starting_index = 0
        for i, count in enumerate(counts):
            counts[i] = starting_index
            starting_index += count

        sorted_lst = [0 for _ in range(self.len)]

        for element in self.arr:
            sorted_lst[counts[element]] = element
            # since we have placed an item in index counts[element], we need to
            # increment counts[element] index by 1 so the next duplicate element
            # is placed in appropriate index
            counts[element] += 1

        # common practice to copy over sorted list into original lst
        # it's fine to just return the sorted_lst at this point as well
        for i in range(self.len):
            self.arr[i] = sorted_lst[i]

def binary_search(arr: List[dict], field: str, query: str) -> int:
    """
    A custom binary search implementation that:
    (1) Assumes the input_list to have elements of type object
       and then sorts by a common key in all those objects name
       "field"
    (2) Make the text lowercase and trims the text in the fields
       so for example "foo bar" can match "FooBar"
    """

    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid][field] > query:
            high = mid - 1
        elif arr[mid][field] < query:
            low = mid + 1
        else:
            return mid

    return -1
