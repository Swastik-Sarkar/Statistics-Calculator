import pyfiglet
from collections import Counter

logo = pyfiglet.figlet_format("STATISTICS CALCULATOR")
print(f"{logo}\n(github.com/Swastik-Sarkar/Statistics-Calculator)")

fi = []
xi = []

try:
    fin = input("Enter frequency values (space-separated): ").strip()
    fi = list(map(int, fin.split()))
    xin = input("Enter class values (space-separated): ").strip()
    xi = list(map(int, xin.split()))

    if len(fi) != len(xi):
        raise ValueError("Number of frequency values must match class values.")

except ValueError as e:
    print(f"ERROR: {e}")
else:
    def querry(fi, xi):
        print("\nGiven fi:", fi)
        print("Given xi:", xi)
        while True:
            print("\nPress:\n[1] Mean\n[2] Median\n[3] Mode\n[4] Exit")
            try:
                q = int(input("> "))
                if q == 1:
                    mean(fi, xi)
                elif q == 2:
                    median(fi, xi)
                elif q == 3:
                    mode(fi, xi)
                elif q == 4:
                    break
                else:
                    print("Expected a number from the range...")
            except ValueError:
                print("Expected a number...")

    def mean(fi, xi):
        total_weighted_sum = sum(fi[i] * xi[i] for i in range(len(fi)))
        total_frequency = sum(fi)
        m = total_weighted_sum / total_frequency
        print(f"Mean: {m:.2f}")

    def median(fi, xi):
        sorted_xi = sorted(xi)
        sorted_fi = sorted(fi)

        def find_median(lst):
            n = len(lst)
            if n % 2 == 0:
                return (lst[n // 2 - 1] + lst[n // 2]) / 2
            else:
                return lst[n // 2]

        print(f"Median of fi: {find_median(sorted_fi)}")
        print(f"Median of xi: {find_median(sorted_xi)}")

    def mode(fi, xi):
        def find_mode(lst):
            counter = Counter(lst)
            max_freq = max(counter.values())
            modes = [k for k, v in counter.items() if v == max_freq]
            return modes

        print("Mode(s) of fi:", find_mode(fi))
        print("Mode(s) of xi:", find_mode(xi))

    querry(fi, xi)
