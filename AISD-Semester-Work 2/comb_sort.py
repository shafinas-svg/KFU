def comb_sort(arr):

    n = len(arr)
    gap = n
    shrink = 1.3
    swapped = True

    comparisons = 0
    swaps = 0

    while gap > 1 or swapped:
        gap = int(gap / shrink)

        if gap < 1:
            gap = 1

        swapped = False

        for i in range(0, n - gap):
            comparisons += 1

            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swaps += 1
                swapped = True

    steps = comparisons + swaps

    return arr, comparisons, swaps, steps