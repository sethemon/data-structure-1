import unittest
from pathlib import Path
import pprint
from timeit import Timer

from Graph import Graph
from DSAD_FreightBooking import FreightBooking

pretty_print = pprint.PrettyPrinter()


class TestFreightBooking(unittest.TestCase):

    def test_actual_file(self):
        input_file = Path(__file__).parent / 'inputPS4.txt'
        obj = FreightBooking()
        obj.read_city_train_file(input_file)
        obj.show_all([])
        obj.display_transport_hub([])
        obj.display_connected_cities('T12320', [])
        obj.display_connected_cities('T12325', [])
        obj.display_connected_cities('T12344', [])
        obj.display_direct_train('Hyderabad', 'Kolkata', [])
        obj.display_direct_train('Bangalore', 'Kolkata', [])
        obj.find_service_available('Hyderabad', 'Kolkata', [])

    def test_given_file(self):
        input_file = Path(__file__).parent / 'test_inputPS4.txt'
        obj = FreightBooking()
        obj.read_city_train_file(input_file)
        obj.show_all([])
        obj.display_transport_hub([])
        obj.display_connected_cities('T1235', [])
        obj.display_connected_cities('T1122', [])
        obj.display_direct_train('New Delhi', 'Calcutta', [])
        obj.display_direct_train('Calcutta', 'New Delhi', [])
        obj.find_service_available('Calcutta', 'Nagpur', [])

    def test_graphs(self):
        connections = [('A', {'B': ['T123']}), ('B', {'C': ['T122']}),
                       ('B', {'D': ['T121']}), ('C', {'D': ['T120']}),
                       ('E', {'F': ['T124']}), ('F', {'C': ['T125']}),
                       ('A', {'B': ['T111']})]
        g = Graph(connections, directed=False)
        pretty_print.pprint(g._graph)

        g.add('E', {'B': ['T126']})
        g.add('E', {'A': ['T111']})
        pretty_print.pprint(g._graph)
        g.add('D', {'E': ['T127']})
        g.add('D', {'B': ['T128']})
        pretty_print.pprint(g._graph)

        g.remove('A')
        pretty_print.pprint(g._graph)

        g.add('G', {'B': 'T129'})
        g.add('G', {'A': 'T111'})
        pretty_print.pprint(g._graph)

        print(g.find_path('B', 'F', []))
        print(g.is_connected('B', 'F'))
        print(g.is_connected('B', 'D'))
        print(g.is_connected('B', 'C'))
        print(g.find_hub())


if __name__ == '__main__':
    unittest.main()
