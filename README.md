# data-structures-1
First Install Anaconda onto your system:
https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86_64.exe

After successsful installation of Anaconda, then install PyCharm: (or VS Code)
https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC

When installed, create a new project with Conda environment (set Python==3.7), and download the files (to your project folder) to run the code. 

References: https://www.python.org/doc/essays/graphs/


DSAD for Freight Booking 
======================================

Problem Statement
------------------------------------------------------------
A startup company is venturing into the space of online railway freight booking and wants your help in developing a system which can record all railway freight routes that are available between cities in India. The data is captured such that each freight train and its associated cities are captured as vertices and the association as edges.
As a first phase, they want to identify the following information.
1. List of unique freight trains and list of unique cities that have freight service.
2. Find out which city is the main transport hub. (City which is visited by the greatest number of trains)
3. Find out which cities are connected by a single train.
4. If a package needs to be sent directly from city a to city b, which train should they book?
5. Can a package be sent from city a to city b even if it must be transferred (change trains) at an intermediary city c (any number of transfers).

Operations
------------------------------------------------------------
1. def readCityTrainfile(self, inputfile): 
------------------------------------------------------------
This function reads the input file inputPS4.txt containing the name of the cities and the freight trains between them in one line separated by a slash. A sample input file entry is shown below. The Train number is the first entry in each row followed by the different cities it services separated by a slash ‘/’

T1235 / Chennai / New Delhi

The function should create relevant vertices for both the freight train and its associated cities and relevant edges to indicate the association of a train and its connecting cities. Ensure that the vertices are unique and there are no duplicates.

2. def showAll(self): 
------------------------------------------------------------
This function displays the count of unique freight trains and cities entered through the input file. It should also list out the unique freight trains and cities that have freight service stored. This function is called after all input data has been captured. The output of this function should be pushed into outputPS4.txt file. The output format should be as mentioned below.

--------Function showAll --------

Total no. of freight trains: 5

Total no. of cities: 8

List of Freight trains:

T1235

T2342

T1122

T2341

T5623

List of cities:

Chennai

New Delhi

Ahmedabad

Mumbai

Nagpur

Hyderabad

Calcutta

Vishakhapatnam

---------------------------------------

3. def displayTransportHub(self): 
------------------------------------------------------------
This function displays the name of the city which is visited by the greatest number of trains. The function also displays the names of the incoming freight trains to the outputPS4 file. The function is triggered when the ‘searchTransportHub’ tag is found in the file promptsPS4.txt file.

searchTransportHub:
The output of this function should be appended into outputPS4.txt file. The output format should be as mentioned below.

--------Function displayTransportHub --------

Main transport hub: New Delhi

Number of trains visited: 3

List of Freight trains:

T1235

T2342

T2341

-----------------------------------------

4. def displayConnectedCities(self, train): 
------------------------------------------------------------
This function displays all the cities are connected by a single train. The function reads the input freight train number from the file promptsPS4.txt with the tag as shown below.

searchTrain: T1122

searchTrain: T1235

The output of this function should be appended into outputPS4.txt file. If a train is not found, an appropriate message should be output to file. The output format should be as mentioned below.

--------Function displayConnectedCities --------

Freight train number: T1122

Number of cities connected: 3

List of cities connected directly by T1122:

Ahmedabad

Mumbai

Nagpur

-----------------------------------------

5. def displayDirectTrain(self, city a, city b): 
------------------------------------------------------------
This function displays the freight train name which can be booked to send a package directly from city a to city b. The function reads the input cities from the file promptsPS4.txt with the tag as shown below.

searchCities: Calcutta: New Delhi

searchCities: Chennai: Hyderabad

The output of this function should be appended into outputPS4.txt file. If there is no direct train or a city is not found, an appropriate message should be output to the file. The output format should be as mentioned below. If there is more than one train that can be booked, the train number you encounter first can be output.

--------Function displayDirectTrain --------

City A: Calcutta

City B: New Delhi

Package can be sent directly: Yes, T2342 (if no, display appropriate message)

-----------------------------------------

6. def findServiceAvailable(self, city a, city b): 
------------------------------------------------------------
This function finds whether a package can be sent from city a to city b with any number of stops/transfers (ie to deliver the package from city a to city b it might even get transferred on another train at an intermediary city c). The function reads the input cities from the file promptsPS4.txt with the tag as shown below.

ServiceAvailability: Calcutta: Mumbai

ServiceAvailability: Nagpur: Vishakhapatnam

Also display the entire route to transfer the package from city a to city b. The output of this function should be appended into outputPS4.txt file. If the package can’t be transferred or a city is not found, an appropriate message should be output to the file. The output format should be as mentioned below.

--------Function findServiceAvailable --------

City A: Calcutta

City B: Nagpur

Can the package be sent: Yes, Calcutta > T2342 > New Delhi > T2341 > Ahmedabad > T1122 > Nagpur (if no, display appropriate message)

-----------------------------------------

Sample Input file format
------------------------------------------------------------
The input file inputPS4.txt contains names of the trains and the connected cities in one line separated by a slash (/).

Sample inputPS4.txt
------------------------------------------------------------

T1235 / Chennai / New Delhi

T2342 / Calcutta / New Delhi

T1122 / Ahmedabad / Nagpur / Mumbai

T2341 / Ahmedabad / New Delhi

T5623 / Vishakhapatnam / Hyderabad

Sample promptsPS4.txt
------------------------------------------------------------

searchTransportHub

searchTrain: T1122

searchTrain: T1235

searchCities: Calcutta: New Delhi

searchCities: Chennai: Hyderabad

ServiceAvailability: Calcutta: Mumbai

ServiceAvailability: Nagpur: Vishakhapatnam

Sample outputPS4.txt
------------------------------------------------------------

--------Function showAll --------

Total no. of freight trains: 5

Total no. of cities: 8

List of Freight trains:

T1235

T2342

T1122

T2341

T5623


List of cities:

Chennai

New Delhi

Ahmedabad

Mumbai

Nagpur

Hyderabad

Calcutta

Vishakhapatnam

---------------------------------------

--------Function displayTransportHub --------

Main transport hub: New Delhi

Number of trains visited: 3

List of Freight trains:

T1235

T2342

T2341

-----------------------------------------

--------Function displayConnectedCities --------

Freight train name: T1122

Number of cities connected: 3

List of cities connected directly by T1122:

Ahmedabad

Mumbai

Nagpur

-----------------------------------------

--------Function displayDirectTrain --------

City A: Calcutta

City B: New Delhi

Package can be sent directly: Yes, T2342 (if no, display appropriate message)

-----------------------------------------

--------Function findServiceAvailable --------

City A: Calcutta

City B: Nagpur

Can the package be sent: Yes, Can the package be sent: Yes, Calcutta > T2342 > New Delhi > T2341 > Ahmedabad > T1122 > Nagpur (if no, display appropriate message)

-----------------------------------------
