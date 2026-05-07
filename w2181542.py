"""
****************************************************************************
Additional info
 1. I declare that my work contains no examples of misconduct, such as
 plagiarism, or collusion.
 2. Any code taken from other sources is referenced within my code solution.
 3. Student ID: 20250404
 4. Date: 23/11/2025
****************************************************************************

"""
from graphics import *
import csv
import math

data_list = []   # data_list An empty list to load and hold data from csv file

def load_csv(CSV_chosen):
    """
    This function loads any csv file by name (set by the variable 'selected_data_file') into the list "data_list"
    YOU DO NOT NEED TO CHANGE THIS BLOCK OF CODE
    """
    try:
        with open(CSV_chosen, 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                data_list.append(row)
        return True
    
    except FileNotFoundError:
        return False

#************************************************************************************************************

valid_airport = {'LHR' : 'London Heathrow',
                 'MAD' : 'Madrid Adolfo Suárez-Barajas',
                 'CDG' : 'Charles De Gaulle International',
                 'IST' : 'Istanbul Airport International',
                 'AMS' : 'Amsterdam Schiphol',
                 'LIS' : 'Lisbon Portela',
                 'FRA' : 'Frankfurt Main',
                 'FCO' : 'Rome Fiumicino',
                 'MUC' : 'Munich International',
                 'BCN' : 'Barcelona International'
                 }

run_program = True

while run_program:
    
    data_list.clear()
    
    
    def validate_citycode():
        print("please enter a three-letter city code: ", end='')
        while True:
            citycode = input().upper()
            if(len(citycode) != 3):
                print("Wrong code length - please enter a three-letter city code: ", end='')
            elif(citycode not in valid_airport):
                print("Unavailable city code - please enter a valid city code: ", end='')
            else:
                return citycode

    def validate_year():
        print("Please enter the year required in the format YYYY: ", end='')
        while True:
            try:
                year = int(input())

                if not (2000 <= year <= 2025):
                    print("Out of range - please enter a value from 2000 to 2025: ",end='')
                else:
                    return year
            
            except ValueError:
                print("Wrong datatype - please enter a four-digit year value: ", end='')

    citycode = validate_citycode()
    year = validate_year()
    

    selected_data_file = (f'{citycode}{year}.csv') #hard coded csv name to be replaced with your dynamically created filename
    print()
    print('**********************************************************************')
    print(f'{selected_data_file} selected - Planes departing {valid_airport[citycode]} {year}')
    print('**********************************************************************')
    print()

    if not load_csv(selected_data_file): #calls the function "load_csv" sending the variable 'selected_data_file" as a parameter
        print(f"file {selected_data_file} is not found.")
        print()
        continue
    else:
        print()
        
    validate_airline = {'BA' : 'British Airways',
                        'AF' : 'Air France',
                        'AY' : 'Finnair',
                        'KL' : 'KLM',
                        'SK' : 'Scandinavian Airlines',
                        'TP' : 'TAP Air Portugal',
                        'TK' : 'Turkish Airlines',
                        'W6' : 'Wizz Air',
                        'U2' : 'easyJet',
                        'FR' : 'Ryanair',
                        'A3' : 'Aegean Airlines',
                        'SN' : 'Brussels Airlines',
                        'EK' : 'Emirates',
                        'QR' : 'Qatar Airways',
                        'IB' : 'Iberia',
                        'LH' : 'Lufthansa'
                        }

    airport = 0
    terminal = 0
    miles = 0
    air_france = 0
    temperature = 0
    b_airway = 0
    average = 0
    percentage_1 = 0
    percentage_2 = 0
    total_dep = 0
    delay = 0
    w_conditions = 0
    hour = 0
    count_hours = 0


    rain_hour = []
    destination = {}

    for row in data_list:
        airport += 1
        
        if(row[8] == '2'):
            terminal += 1
        
        if int(row[5]) < 600:
            miles += 1
        
        flight_1 = row[1][0:2]
        if (flight_1 == 'AF'):
            air_france += 1
        
        Weather = row[10]
        Weather_new = Weather.replace('Â','') 
        temp_value = Weather_new.split('°')[0]
        
        if (float(temp_value) < 15):
            temperature += 1
        
        flight_2 = row[1][0:2]
        if (flight_2 == 'BA'):
            b_airway += 1
            
            average = round(b_airway/12,2)
        
        total_dep = airport
        percentage_1 = round((b_airway/total_dep)*100,2)
        
        if flight_1 == row[1][0:2]:
            if (flight_1 == 'AF'):
                if row[2] < row[3]:
                    delay += 1
                    
        if air_france > 0:
            percentage_2 = round((delay/air_france)*100,2)
        else:
            percentage_2 = 0
                    
        w_conditions = row[10].lower()   
        hour = row[2].split(':')[0]
        if 'rain' in w_conditions and (0 <= int(hour) < 12):
            if hour not in rain_hour:  
                rain_hour.append(hour)
        count_hours = len(rain_hour) 
        
        #least common destination
        destination_code = row[4]
         
        if destination_code in destination: 
             destination[destination_code] = destination[destination_code] + 1 
        else:
             destination[destination_code] = 1 
             
        min_value = None
        min_code = [] 
         
        for destination_code in destination:
            if min_value is None:
                min_value = destination[destination_code]
                
            elif destination[destination_code] < min_value: 
                min_value = destination[destination_code]
                 
        for destination_code in destination:
            if destination[destination_code] == min_value:
                min_code.append(destination_code) 
                
        least_names = []
        for x in min_code:
            least_names.append(valid_airport[x])
         
         
    print("The total number of flights from this airport was", airport)
    print("The total number of  flights departing Terminal Two was", terminal )
    print("The total number of departures of flights that are under 600 miles was", miles)
    print("There were", air_france, "Air France flights from this airport")
    print("There were", temperature, "flights departing in temperatures below 15 degrees")
    print("There was an average of", average, "British Airways flights per hour from this airport")
    print("British Airways planes made up", percentage_1, "%", "of all departures")
    print(percentage_2 ,"%", "of Air France departures were delayed")
    print("There were", count_hours, "hours", "in which rain fell")

    if len(least_names) > 1:
        print("The least common destinations are", least_names)
    else:
        print("The least common destination is", least_names)


    #save outcomes as a text file
    with open("results.txt", 'a') as file: 
        print('**********************************************************************', file=file)
        print(f'{selected_data_file} selected - Planes departing {valid_airport[citycode]} {year}', file=file)
        print('**********************************************************************', file=file)
        print("The total number of flights from this airport was", airport, file=file)
        print("The total number of  flights departing Terminal Two was", terminal, file=file)
        print("The total number of departures of flights that are under 600 miles was", miles, file=file)
        print("There were", air_france, "Air France flights from this airport", file=file)
        print("There were", temperature, "flights departing in temperatures below 15 degrees", file=file)
        print("There was an average of", average, "British Airways flights per hour from this airport", file=file)
        print("British Airways planes made up", percentage_1, "%", "of all departures", file=file)
        print(percentage_2 ,"%", "of Air France departures were delayed", file=file)
        print("There were", count_hours, "hours", "in which rain fell", file=file)
        
        if len(least_names) > 1:
            print("The least common destinations are", least_names, file=file)
        else:
            print("The least common destination is", least_names, file=file)
        print('', file=file)


    def airline_code():
        print('')
        print("Enter a two-character Airline code to plot a histogram: ", end='')
        while True:
            aircode = input().upper()
            if aircode not in validate_airline:
                print("Unavailable Airline code please try again. ")
                print("Enter the two-character Airline code to plot a histogram: ", end='')
            else:
                return aircode
            
    def count_of_flights(data_list, aircode):
        flight_hour = {
            '00' : 0,
            '01' : 0,
            '02' : 0,
            '03' : 0,
            '04' : 0,
            '05' : 0,
            '06' : 0,
            '07' : 0,
            '08' : 0,
            '09' : 0,
            '10' : 0,
            '11' : 0
            }

        for row in data_list:
            if row[1][:2] == aircode:
                hour = row[2].split(':')[0]
                if 0 <= int(hour) < 12:
                    flight_hour[hour] += 1
                    
        return flight_hour
    
    aircode = airline_code()
    flight_hour = count_of_flights(data_list, aircode)

    #Count of maximum hours
    max_value = max(flight_hour.values())

    win = GraphWin(f"Departures by hour for {validate_airline[aircode]} from {valid_airport[citycode]} {year}", 850, 650)
    win.setBackground("lightblue")

    graph_title = (f"Departures by hour for {validate_airline[aircode]} from {valid_airport[citycode]} {year}")
    title = Text(Point(400, 30), graph_title)
    title.setSize(14)
    title.setStyle("bold")
    title.draw(win)

    #bar scales
    height = 20
    max_width = 600
    start_point_x = 120
    start_point_y = 100
    gap = 40

    index = 0

    for hour in flight_hour:
        count = flight_hour[hour]
        y_axis = 100 + (index*40)
        
        #labelling y axis
        hour_count = Text(Point(100, y_axis + 10), f'{hour}')
        hour_count.setSize(10)
        hour_count.draw(win)

        if max_value > 0:
            width = (count/max_value) * max_width
        else:
            width = 0
            
        if count > 0:
            bar = Rectangle(Point(start_point_x, y_axis), Point(start_point_x + width, y_axis + height))
            bar.setFill("darkblue")
            bar.draw(win)
            
            bar_count = Text(Point(start_point_x + width + 20, y_axis + height/2), str(count))
            bar_count.setSize(10)
            bar_count.draw(win)
            
        index += 1

    #naming y axis
    axis_name = ['Hour', '', '00:00', 'to', '12:00']
    for i in range(5):
        y_name = Text(Point(50, (270 + 20*i)), axis_name[i])
        y_name.setSize(11)
        y_name.setStyle("bold")
        y_name.draw(win)
        
    try:
        win.getMouse()
        win.close()
    except GraphicsError:
        pass

    #To continue
    re_code = input("Do you want to select a new data file? Y/N: ").upper()
    if re_code != 'Y':
        run_program = False
        print("Thank you. End of run")
        
