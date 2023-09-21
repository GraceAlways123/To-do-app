# Create a function that returns a calculated average of a list of temperature data
def getAverage():
    with open('files/data.txt', 'r') as file:
        temp_data = file.readlines()
    
    values = temp_data[1:]
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)
    return average_local


average = getAverage()
print(average)