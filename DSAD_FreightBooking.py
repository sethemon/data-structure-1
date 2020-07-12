import pprint
import itertools

from Graph import Graph

pretty_print = pprint.PrettyPrinter()
end_of_func = "---------------------------------------------------"


class FreightBooking:

    def __init__(self):
        self.freight_map = dict()
        self.train_list = []
        self.city_list = []
        self.analyze_list = []
        self.graph = None

    def read_city_train_file(self, input_file):
        """
        This function reads the input file inputPS4.txt containing the name of the cities and the freight trains
        between them in one line separated by a slash. A sample input file entry is shown below. The Train number
        is the first entry in each row followed by the different cities it services separated by a slash ‘/’
        T1235 / Chennai / New Delhi
        The function should create relevant vertices for both the freight train and its associated cities and relevant
        edges to indicate the association of a train and its connecting cities. Ensure that the vertices are unique
        and there are no duplicates.
        :param input_file:
        """
        print(f"INPUT FILE : {input_file}")
        input_text_file = open(input_file, "r")
        lines = input_text_file.readlines()
        count = 1
        for line in lines:
            # Strips the newline character
            # print(f"Line{count}: {line.strip()}")
            count += 1
            line_info = line.strip().split('/')
            self.freight_map.update({line_info[0].strip(): [cities.strip() for cities in line_info[1:]]})
            for city in line_info[1:]:
                self.city_list.append(city.strip())
        input_text_file.close()
        self.populate_graph()

    def populate_graph(self):
        """ Populates the GRAPH with Cities and Trains"""
        connections = []
        self.graph = Graph(connections, directed=False)
        pretty_print.pprint(self.freight_map)
        for train, cities in self.freight_map.items():
            i = 0
            while i < len(cities) - 1:
                # print(i, cities[i], cities[i+1], train)
                self.graph.add(cities[i], {cities[i+1]: [train]})
                i += 1
        print("GRAPH as ADJACENCY LIST : ")
        pretty_print.pprint(self.graph.get_graph)

    def show_all(self, output_list):
        """
        This function displays the count of unique freight trains and cities entered through the input file.
        It should also list out the unique freight trains and cities that have freight service stored. This function
        is called after all input data has been captured. The output of this function should be pushed into
        outputPS4.txt file. The output format should be as mentioned below.
        --------Function showAll --------
        Total no. of freight trains: 5
        Total no. of cities: 8
        -----------------------------------------
        List of Freight trains:
        -----------------------------------------
        List of Cities:
        -----------------------------------------
        """
        cities, trains, counter = self.graph.show_all()
        # city_set = set(self.city_list)
        # output_list.append(f"Total no. of freight trains: {len(self.freight_map.keys())}")
        output_list.append(f"Total no. of freight trains: {len(trains)}")
        output_list.append(f"Total no. of cities: {len(cities)}")
        output_list.append(end_of_func)
        output_list.append(f"List of Freight trains: ")
        # for train in self.freight_map.keys():
        for train in trains:
            output_list.append(train)
        output_list.append(end_of_func)
        output_list.append(f"List of Cities: ")
        for city in cities:
            output_list.append(city)
        output_list.append(end_of_func)
        self.analyze_list.append(f"cities  ->  Vertices of the Graph")
        self.analyze_list.append(f"trains  ->  Edges of the Graph")
        self.analyze_list.append(end_of_func)
        self.analyze_list.append(f"-----------------Function showAll -----------------")
        self.analyze_list.append(f"Time Complexity for Average case scenario -> "
                                 f"Big-Theta({counter})")
        self.analyze_list.append(f"Time Complexity for Worst case scenario -> Big-O(vertices+edges) -> "
                                 f"Big-O(all cities + all trains)")
        # print(f"Total no. of freight trains: {len(self.freight_map.keys())}")
        # print(f"Total no. of cities: {len(city_set)}")
        # print(f"List of Freight trains: {self.freight_map.keys()}")
        # print(f"List of Cities: {city_set}")

    def display_transport_hub(self, output_list):
        """
        This function displays the name of the city which is visited by the greatest number of trains. The function
        also displays the names of the incoming freight trains to the outputPS4 file. The function is triggered when
        the ‘searchTransportHub’ tag is found in the file promptsPS4.txt file.
        searchTransportHub:
        The output of this function should be appended into outputPS4.txt file.
        The output format should be as mentioned below.
        --------Function displayTransportHub --------
        Main transport hub: New Delhi
        Number of trains visited: 3
        List of Freight trains:
        -----------------------------------------
        """
        hub = self.graph.find_hub()
        output_list.append(f"Main transport hub: {hub['hub']}")
        output_list.append(f"Number of trains visited: {hub['size']}")
        output_list.append(f"List of Freight trains: {hub['trains']}")
        output_list.append(end_of_func)
        self.analyze_list.append(end_of_func)
        self.analyze_list.append(f"-----------Function displayTransportHub -----------")
        self.analyze_list.append(f"Time Complexity for Average case scenario -> Big-Theta({hub['counter']})")
        self.analyze_list.append(
            f"Time Complexity for Worst case scenario -> Big-O(all cities + trains connecting them)")
        # print(f"Main transport hub: {hub['hub']}")
        # print(f"Number of trains visited: {hub['size']}")
        # print(f"List of Freight trains: {hub['trains']}")

    def display_connected_cities(self, train, output_list):
        """
        This function displays all the cities are connected by a single train. The function reads the input freight
        train number from the file promptsPS4.txt with the tag as shown below.
        searchTrain: T1122
        searchTrain: T1235
        The output of this function should be appended into outputPS4.txt file. If a train is not found, an
        appropriate message should be output to file. The output format should be as mentioned below.
        --------Function displayConnectedCities --------
        Freight train number: T1122
        Number of cities connected: 3
        List of cities connected directly by T1122:
        Ahmedabad
        Mumbai
        Nagpur
        -----------------------------------------
        :param output_list:
        :param train:
        """
        train_map, counter = self.graph.get_train(str(train).strip())
        # print(train_map)
        if bool(train_map):
            output_list.append(f"Freight train number: {train_map['train']}")
            output_list.append(f"Number of cities connected: {train_map['count']}")
            output_list.append(f"List of cities connected directly by {train_map['train']}: {train_map['cities']}")
            # print(f"Freight train number: {train_map['train']}")
            # print(f"Number of cities connected: {train_map['count']}")
            # print(f"List of cities connected directly by {train_map['train']}: {train_map['cities']}")
        else:
            output_list.append(f"Train no: {str(train).strip()} does not exist in our Freight Booking system.")
            # print(f"Train no: {str(train).strip()} is INVALID")
        output_list.append(end_of_func)
        self.analyze_list.append(end_of_func)
        self.analyze_list.append(f"----------Function displayConnectedCities ---------")
        self.analyze_list.append(f"Time Complexity for Average case scenario -> Big-Theta({counter})")
        self.analyze_list.append(
            f"Time Complexity for Worst case scenario -> Big-O(all trains + cities connected by these trains)")

    def display_direct_train(self, city_a, city_b, output_list):
        """
        This function displays the freight train name which can be booked to send a package directly from city a to
        city b. The function reads the input cities from the file promptsPS4.txt with the tag as shown below.
        searchCities: Calcutta: New Delhi
        searchCities: Chennai: Hyderabad
        The output of this function should be appended into outputPS4.txt file. If there is no direct train or a
        city is not found, an appropriate message should be output to the file. The output format should be as
        mentioned below. If there is more than one train that can be booked, the train number you encounter first
        can be output.
        --------Function displayDirectTrain --------
        City A: Calcutta
        City B: New Delhi
        Package can be sent directly: Yes, T2342 (if no, display appropriate message)
        -----------------------------------------
        :param output_list:
        :param city_a:
        :param city_b:
        """
        output_list.append(f"City A: {city_a}")
        output_list.append(f"City B: {city_b}")
        # print(f"City A: {city_a}")
        # print(f"City B: {city_b}")
        if city_a in self.graph.get_graph and city_b in self.graph.get_graph:
            # print(self.graph.is_connected(str(city_a).strip(), str(city_b).strip()))
            connected_train, counter = self.graph.is_connected(str(city_a).strip(), str(city_b).strip())
            output_list.append(connected_train)
            self.analyze_list.append(end_of_func)
            self.analyze_list.append(f"------------Function displayDirectTrain -----------")
            self.analyze_list.append(f"Time Complexity for Average case scenario -> Big-Theta({counter})")
            self.analyze_list.append(
                f"Time Complexity for Worst case scenario -> Big-O(city + cities directly connected with it)")
        else:
            # print(f"INVALID city name, does not exist in our Freight Booking system")
            output_list.append(f"INVALID city name, does not exist in our Freight Booking system.")
        output_list.append(end_of_func)

    def find_service_available(self, city_a, city_b, output_list):
        """
        This function finds whether a package can be sent from city a to city b with any number of stops/transfers
        (ie to deliver the package from city a to city b it might even get transferred on another train at an
        intermediary city c). The function reads the input cities from the file promptsPS4.txt with the tag as
        shown below.
        ServiceAvailability: Calcutta: Mumbai
        ServiceAvailability: Nagpur: Vishakhapatnam
        Also display the entire route to transfer the package from city a to city b. The output of this function
        should be appended into outputPS4.txt file. If the package can’t be transferred or a city is not found,
        an appropriate message should be output to the file. The output format should be as mentioned below.
        --------Function findServiceAvailable --------
        City A: Calcutta
        City B: Nagpur
        Can the package be sent: Yes, Calcutta > T2342 > New Delhi > T2341 > Ahmedabad > T1122 > Nagpur
        (if no, display appropriate message)
        -----------------------------------------
        :param output_list:
        :param city_a:
        :param city_b:
        """
        # print(f"City A: {city_a}")
        # print(f"City B: {city_b}")
        output_list.append(f"City A: {city_a}")
        output_list.append(f"City B: {city_b}")
        trains = []
        if city_a in self.graph.get_graph and city_b in self.graph.get_graph:
            path = self.graph.find_path(str(city_a).strip(), str(city_b).strip(), [])
            count = self.graph.counter
            if path:
                # print("Can the package be sent: Yes")
                output_list.append("Can the package be sent: Yes")
                i = 0
                while i < len(path) - 1:
                    # print(self.graph.is_connected(path[i], path[i + 1]))
                    temp, counter = self.graph.is_connected(path[i], path[i + 1])
                    count = count + counter
                    trains.append(temp.split(',')[-1:][0].strip())
                    i += 1
                # print(f"Shortest Path : {path}")
                temp_print = ''
                for train, city in itertools.zip_longest(trains, path, fillvalue='END'):
                    temp_print = temp_print + f"{city} > {train} > "
                temp_print = "".join(temp_print.rsplit(" >", 1)).strip()
                output_list.append(f"Shortest Path : {temp_print}")
                self.analyze_list.append(end_of_func)
                self.analyze_list.append(f"----------Function findServiceAvailable -----------")
                self.analyze_list.append(f"Time Complexity for Average case scenario -> Big-Theta({count})")
                self.analyze_list.append(f"Time Complexity for Worst case scenario -> "
                                         f"Big-O(city + all cities connected directly or indirectly with it)")
            else:
                # print("Can the package be sent: No")
                output_list.append("Can the package be sent: No")
                # print(f"Path does not exist between {city_a} and {city_b}")
                output_list.append(f"Feasible Path does not exist between {city_a} and {city_b}")
                # print(f"Shortest Path : {path}")
                self.analyze_list.append(end_of_func)
                self.analyze_list.append(f"----------Function findServiceAvailable -----------")
                self.analyze_list.append(f"Time Complexity for Worst case scenario -> "
                                         f"Big-O(city + all cities connected directly or indirectly with it)")
        else:
            # print(f"INVALID city name, does not exist in our Freight Booking system")
            output_list.append(f"INVALID city name, does not exist in our Freight Booking system")
        output_list.append(end_of_func)

    def get_analysis_list(self):
        return self.analyze_list
