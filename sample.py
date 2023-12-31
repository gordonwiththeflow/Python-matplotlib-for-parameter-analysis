import matplotlib.pyplot as plt
import win32com.client

# Function to create and display a chart for a given worksheet
def create_and_display_chart(workbook_path, worksheet_name, title, fig_number):
    excel = win32com.client.Dispatch("Excel.Application")

    # Open the workbook
    workbook = excel.Workbooks.Open(workbook_path)
    worksheet = workbook.Sheets(worksheet_name)

    start_value = 10
    end_value = 990
    step = 5

    data_combined = []

    while start_value <= end_value:
        # Update the value of cell I4
        worksheet.Cells(4, 9).Value = start_value
        # Force recalculation of all formulas
        worksheet.Calculate()
        # Get the calculation result of cell M4
        totalQ1 = worksheet.Cells(4, 13).Value

        # Add data to the dataset
        data_combined.append((start_value, totalQ1))

        # Increase by 5
        start_value += step

    # Close the workbook and the Excel application
    workbook.Close(SaveChanges=False)
    excel.Quit()

    # Extract X and Y coordinates from the dataset
    x = [point[0] for point in data_combined]
    y1 = [point[1] for point in data_combined]

    # Create a new figure with the specified number
    plt.figure(fig_number)

    # Create the chart for the current worksheet
    plt.plot(x, y1, marker='o', linestyle='-', label=worksheet_name, color='blue')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title(title)
    plt.legend()

# List of worksheets and their corresponding titles
worksheets = [
    ("Parameter1", " Parameter1_ sample "),
    ("Parameter2", " Parameter2_ sample "),
    ("Parameter3", " Parameter3_ sample "),
    ("Parameter4", " Parameter4_ sample "),
    ("Parameter5", " Parameter5_ sample "),
    ("Parameter6", " Parameter6_ sample ")
]

# Create and display charts for each worksheet with separate figures
for index, (worksheet_name, title) in enumerate(worksheets):
    create_and_display_chart(
        r'C:\Users\Administrator\PycharmProjects\optionreport\venv\sample.xlsx',
        worksheet_name,
        title,
        fig_number=index + 1
    )

plt.show()

