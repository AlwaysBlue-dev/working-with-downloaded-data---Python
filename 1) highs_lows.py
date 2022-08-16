import csv
from datetime import datetime
from matplotlib import pyplot as plt


# -------------- 1) PARSING THE CSV FILE HEADERS --------------

# filename for 1 month data
# filename = "sitka_weather_07-2014.csv"

# filename for 1 year data
filename = "sitka_weather_2014.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # -------------- 2) PRINTING THE HEADERS AND THEIR POSITIONS --------------
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

  # -------------- 3) EXTRACTING AND READING DATA --------------
  # -------------- 4) PLOTTING DATES --------------
    # Get dates and high temperature from file
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%d/%m/%Y")
        dates.append(current_date)

        # highs.append(row[1])
        # Convert these strings to numbers with int() so they can be read by matplotlib
        high = int(row[1])
        highs.append(high)
        # print(highs)

    # -------------- 3) PLOTTING DATA IN A TEMPERATURE CHART --------------
    # Plot data
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red')

    # Format plot

    # For 1 month
    # plt.title("Daily High Temperature, July 2014", fontsize=24)

    # For 1 Year
    plt.title("Daily High Temperature - 2014", fontsize=24)

    plt.xlabel('', fontsize=16)

    # draw the label dates diagonally to prevent them from overlapping.
    fig.autofmt_xdate()

    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()
