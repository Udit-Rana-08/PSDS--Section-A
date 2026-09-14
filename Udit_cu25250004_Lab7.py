#Question 1:
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        # Bubble up
        while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
            p = (i - 1) // 2
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()

        # Sink down
        i = 0
        n = len(self.heap)
        while 2 * i + 1 < n:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = left

            if right < n and self.heap[right] < self.heap[left]:
                smallest = right

            if self.heap[i] <= self.heap[smallest]:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

        return root


class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()

    def enqueue(self, item):
        self.heap.insert(item)

    def dequeue(self):
        return self.heap.extract_min()


def heap_sort(arr):
    h = MinHeap()
    for item in arr:
        h.insert(item)
    return [h.extract_min() for _ in range(len(arr))]


# --- Execution / Testing ---
if __name__ == "__main__":
    # 1 & 2. Min-Heap / Priority Queue Test
    pq = PriorityQueue()
    pq.enqueue(15)
    pq.enqueue(5)
    pq.enqueue(20)
    pq.enqueue(1)

    print("Priority Queue Dequeue:", [pq.dequeue() for _ in range(4)])

    # 3. Heap Sort Test
    data = [12, 11, 13, 5, 6, 7]
    print("Original Array:        ", data)
    print("Heap Sorted Array:     ", heap_sort(data))

#Question2:

def maximize_adjacent_difference(arr):
    # Step 1: Sort the array
    arr.sort()
    
    n = len(arr)
    rearranged = [0] * n
    
    # Step 2: Use two pointers (smallest at start, largest at end)
    left = 0
    right = n - 1
    
    # Step 3: Alternate placing smallest and largest elements
    idx = 0
    while left <= right:
        if idx % 2 == 0:
            rearranged[idx] = arr[left]
            left += 1
        else:
            rearranged[idx] = arr[right]
            right -= 1
        idx += 1
        
    # Step 4: Calculate the total absolute difference sum
    total_sum = sum(abs(rearranged[i] - rearranged[i + 1]) for i in range(n - 1))
    
    return rearranged, total_sum

# --- Execution / Testing ---
if __name__ == "__main__":
    input_array = [4, 2, 7, 1]
    
    result_array, max_sum = maximize_adjacent_difference(input_array)
    
    print("Rearranged Array:", result_array)
    print("Maximum Sum:     ", max_sum)

#Question3:

def min_subarray_len(target, arr):
    n = len(arr)
    left = 0
    current_sum = 0
    min_length = float('inf')

    # Expand the right side of the window
    for right in range(n):
        current_sum += arr[right]

        # Shrink the window from the left while sum is strictly greater than target
        while current_sum > target:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1

    # Return -1 if no valid subarray is found
    return min_length if min_length != float('inf') else -1


# --- Execution / Testing ---
if __name__ == "__main__":
    arr = [2, 1, 5, 2, 3, 2]
    target = 7

    result = min_subarray_len(target, arr)
    print("Smallest Subarray Length:", result)

