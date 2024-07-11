import datetime
from mean_var_std import calculate


def main():
    print("Programmer: Mamoudou T. Bah")
    time = datetime.datetime.now()
    print("Mean, Variance, Standard Deviation Calculator")
    print("Date and Time:", time.strftime("%B %d, %Y @ %H:%M:%S"))

    input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    result = calculate(input_list)

    # Print each calculation on its own line with proper formatting
    print("\nFormatted Results:\n")

    for key in result:
        print(f"{key.capitalize()}:")
        print(f"  Axis 1: {result[key][0]}")
        print(f"  Axis 2: {result[key][1]}")
        print(f"  Flattened: {result[key][2]}\n")


if __name__ == "__main__":
    main()
