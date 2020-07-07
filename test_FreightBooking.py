import unittest
from pathlib import Path
import pprint
import logging

from Graph import Graph
from DSAD_FreightBooking import FreightBooking

logger = logging.getLogger("TEST")
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s[%(levelname)s]-%(name)s-%(lineno)d: %(message)s",
                    handlers=[logging.StreamHandler()])

pretty_print = pprint.PrettyPrinter()


class TestFreightBooking(unittest.TestCase):
    def test_read_file(self):
        input_file = Path(__file__).parent / 'inputPS4.txt'
        obj = FreightBooking()
        obj.read_city_train_file(input_file)
        obj.show_all()
        obj.display_transport_hub()
        obj.display_direct_train('Hyderabad', 'Kolkata')
        obj.display_direct_train('Bangalore', 'Kolkata')
        obj.find_service_available('Hyderabad', 'Kolkata')

    # def test_graphs(self):
    #     connections = [('A', {'B': ['T123']}), ('B', {'C': ['T122']}),
    #                    ('B', {'D': ['T121']}), ('C', {'D': ['T120']}),
    #                    ('E', {'F': ['T124']}), ('F', {'C': ['T125']}),
    #                    ('A', {'B': ['T111']})]
    #     g = Graph(connections, directed=False)
    #     logger.info(pretty_print.pprint(g._graph))
    #
    #     g.add('E', {'B': ['T126']})
    #     g.add('E', {'A': ['T111']})
    #     logger.info(pretty_print.pprint(g._graph))
    #     g.add('D', {'E': ['T127']})
    #     g.add('D', {'B': ['T128']})
    #     logger.info(pretty_print.pprint(g._graph))
    #
    #     g.remove('A')
    #     logger.info(pretty_print.pprint(g._graph))
    #
    #     g.add('G', {'B': 'T129'})
    #     g.add('G', {'A': 'T111'})
    #     logger.info(pretty_print.pprint(g._graph))
    #
    #     logger.info(g.find_path('B', 'F', []))
    #     logger.info(g.is_connected('B', 'F'))
    #     logger.info(g.is_connected('B', 'D'))
    #     logger.info(g.is_connected('B', 'C'))
    #     logger.info(g.find_hub())


if __name__ == '__main__':
    unittest.main()
