from pathlib import Path

from DSAD_FreightBooking import FreightBooking
eol = '\n'
outputList = []
analyze_list = []

input_file = Path(__file__).parent / 'inputPS4.txt'
input_trigger_file = Path(__file__).parent / 'promptsPS4.txt'
outputList.append(f"INPUT TRIGGER FILE : {input_trigger_file} \n")
input_text_file = open(input_trigger_file, "r")
outputFile = open("outputPS4.txt", "w+")
analysisFile = open("analysisPS4.txt", "w+")

obj = FreightBooking()
obj.read_city_train_file(input_file)
outputList.append("-----------------Function showAll -----------------")
obj.show_all(outputList)
outputList.append(eol)
prompt_lines = input_text_file.readlines()
for prompt in prompt_lines:
    prompt = prompt.strip()
    if prompt == "searchTransportHub":
        outputList.append("-----------Function displayTransportHub -----------")
        obj.display_transport_hub(outputList)
        outputList.append(eol)
    elif prompt.startswith("searchTrain"):
        train_no = prompt.split(':')[1].strip()
        outputList.append("----------Function displayConnectedCities ---------")
        obj.display_connected_cities(train_no, outputList)
        outputList.append(eol)
    elif prompt.startswith("searchCities"):
        city_a = prompt.split(':')[1].strip()
        city_b = prompt.split(':')[2].strip()
        outputList.append("------------Function displayDirectTrain -----------")
        obj.display_direct_train(city_a, city_b, outputList)
        outputList.append(eol)
    elif prompt.strip("ServiceAvailability"):
        city_a = prompt.split(':')[1].strip()
        city_b = prompt.split(':')[2].strip()
        outputList.append("----------Function findServiceAvailable -----------")
        obj.find_service_available(city_a, city_b, outputList)
        outputList.append(eol)

analyze_list = obj.get_analysis_list()
for item in outputList:
    outputFile.write("%s\n" % item)
outputFile.close()
for analysis in analyze_list:
    analysisFile.write("%s\n" % analysis)
analysisFile.close()
