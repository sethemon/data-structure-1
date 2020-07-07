import logging
import pprint

from Graph import Graph
logger = logging.getLogger("FreightBooking")
pretty_print = pprint.PrettyPrinter()


class FreightBooking:

    def __init__(self):
        self.freight_map = dict()
        self.train_list = []
        self.city_list = []
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
        logger.info(f"INPUT FILE : {input_file}")
        input_text_file = open(input_file, "r")
        lines = input_text_file.readlines()
        count = 1
        for line in lines:
            # Strips the newline character
            # logger.info(f"Line{count}: {line.strip()}")
            count += 1
            line_info = line.strip().split('/')
            self.freight_map.update({line_info[0]: line_info[1:]})
            for city in line_info[1:]:
                self.city_list.append(city)
        input_text_file.close()
        self.populate_graph()

    def populate_graph(self):
        """ Populates the GRAPH with Cities and Trains"""
        connections = [('Kolkata', {'Delhi': ['T12301']})]
        self.graph = Graph(connections, directed=False)
        for train, cities in self.freight_map.items():
            i = 0
            while i < len(cities) - 1:
                # print(i, cities[i], cities[i+1], train)
                self.graph.add(cities[i], {cities[i+1]: [train]})
                i += 1
        pretty_print.pprint(self.graph.show_graph)

    def show_all(self):
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
        city_set = set(self.city_list)
        logger.info(f"Total no. of freight trains: {len(self.freight_map.keys())}")
        logger.info(f"Total no. of cities: {len(city_set)}")
        logger.info(f"List of Freight trains: {self.freight_map.keys()}")
        logger.info(f"List of Cities: {city_set}")
        # logger.info(self.freight_map)

    def display_transport_hub(self):
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
        print(self.graph.find_hub())

    def display_connected_cities(self, train):
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
        :param train:
        """
        pass

    def display_direct_train(self, city_a, city_b):
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
        :param city_a:
        :param city_b:
        """
        print(self.graph.is_connected(city_a, city_b))

    def find_service_available(self, city_a, city_b):
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
        :param city_a:
        :param city_b:
        """
        path = self.graph.find_path(city_a, city_b, [])
        print(f"Shortest Path : {path}")
        i = 0
        while i < len(path) - 1:
            print(i, path[i], path[i+1])
            print(self.graph.is_connected(path[i], path[i + 1]))
            i += 1
