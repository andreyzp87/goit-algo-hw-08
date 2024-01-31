import heapq

if __name__ == "__main__":
    cables = [1, 5, 4, 18, 6, 3, 4, 10]

    heap = []
    for cable in cables:
        heapq.heappush(heap, cable)

    print("Витрати будуть мінімальними якщо завжди вибирати кабелі з найменшою довжиною:")
    result = 0
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        print(f"{first} + {second}")
        result += first + second
        heapq.heappush(heap, first + second)

    print(f"Витрати: {result}")
    print(f"Загальна довжина: {heap[0]}")

    print("\nВитрати будуть максимальними якщо завжди вибирати кабелі з наибільшою довжиною:")

    heap = []
    for cable in cables:
        heapq.heappush(heap, -1*cable)

    result = 0
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        print(f"{-1*first} + {-1*second}")
        result += -1*(first + second)
        heapq.heappush(heap, first + second)

    print(f"Витрати: {result}")
    print(f"Загальна довжина: {-1*heap[0]}")