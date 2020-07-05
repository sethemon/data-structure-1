import unittest
from pathlib import Path
import pprint

from Graph import Graph
from DSAD_FreightBooking import FreightBooking

pretty_print = pprint.PrettyPrinter()


class TestFreightBooking(unittest.TestCase):
    def test_read_file(self):
        input_file = Path(__file__).parent / 'inputPS4.txt'
        obj = FreightBooking()
        obj.read_city_train_file(input_file)
        obj.show_all()

    # def test_graphs(self):
    #     connections = [('A', 'B'), ('B', 'C'),
    #                    ('B', 'D'), ('C', 'D'),
    #                    ('E', 'F'), ('F', 'C')]
    #     g = Graph(connections, directed=True)
    #     pretty_print.pprint(g._graph)
    #
    #     g.add('E', 'D')
    #     pretty_print.pprint(g._graph)
    #     g.add('D', 'E')
    #     g.add('D', 'F')
    #     pretty_print.pprint(g._graph)
    #
    #     g.remove('A')
    #     pretty_print.pprint(g._graph)
    #
    #     g.add('G', 'B')
    #     pretty_print.pprint(g._graph)
    #
    #     pretty_print.pprint(g.find_path('B', 'F', []))


if __name__ == '__main__':
    unittest.main()
