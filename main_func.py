from pathlib import Path

from DSAD_FreightBooking import FreightBooking
outputList = []

input_file = Path(__file__).parent / 'test_inputPS4.txt'
input_trigger_file = Path(__file__).parent / 'promptsPS4.txt'
print(f"INPUT TRIGGER FILE : {input_trigger_file}")
input_text_file = open(input_trigger_file, "r")
outputFile = open("outputPS4.txt", "w+")

obj = FreightBooking()
obj.read_city_train_file(input_file)
outputList = obj.show_all(outputList)
lines = input_text_file.readlines()
for prompt in lines:
        prompt = prompt.strip();
        if prompt == "searchTransportHub":
                obj.display_transport_hub(outputList)
        elif prompt.startswith("searchTrain"):
                train_no = prompt.split(':')[1].strip()
                obj.display_connected_cities(train_no,outputList)
        elif prompt.startswith("searchCities"):
                city_a = prompt.split(':')[1].strip()
                city_b = prompt.split(':')[2].strip()
                obj.display_direct_train(city_a, city_b,outputList)
        elif prompt.strip("ServiceAvailability"):
                city_a = prompt.split(':')[1].strip()
                city_b = prompt.split(':')[2].strip()
                obj.find_service_available(city_a, city_b,outputList)

for item in outputList:
        outputFile.write("%s\n" % item)
outputFile.close()
"""obj = FreightBooking()
obj.read_city_train_file(input_file)
obj.show_all()
if lines = "searchTransportHub" :
        print"Calling searchTransportHub"
        obj.display_transport_hub()
'obj.display_transport_hub()'
obj.display_connected_cities('T1235')
obj.display_connected_cities('T1122')
obj.display_direct_train('New Delhi', 'Calcutta')
obj.display_direct_train('Calcutta', 'New Delhi')
obj.find_service_available('Calcutta', 'Nagpur')"""