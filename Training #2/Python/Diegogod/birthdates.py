from sys import stdin

def solve(names, days, months, years) -> tuple:

    youngest_index = max(range(len(names)), key=lambda i: (years[i], months[i], days[i]))
    oldest_index = min(range(len(names)), key=lambda i: (years[i], months[i], days[i]))

    return names[youngest_index], names[oldest_index]

def main():
    TC = int(stdin.readline().strip())  # Number of people in the class
    names, days, months, years = [], [], [], []

    for _ in range(TC):
        line = stdin.readline().strip().split()
        name = line[0]
        day, month, year = int(line[1]), int(line[2]), int(line[3])

        names.append(name)
        days.append(day)
        months.append(month)
        years.append(year)

    youngest, oldest = solve(names, days, months, years)

    # Print the youngest and oldest person
    print(youngest)
    print(oldest)

if __name__ == "__main__":
    main()
