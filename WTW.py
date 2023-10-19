# Objects

class picklist:
    def __init__(self, box_location, barcode, fulfillment_area):
        self.box_location = box_location
        self.barcode = barcode
        self.fulfillment_area = fulfillment_area
    def format_list(self):
        some_list = []
        some_list.append(self.box_location)
        some_list.append(self.barcode)
        some_list.append(self.fulfillment_area)
        return some_list
def give_box_location(picklist_file):
    with open(picklist_file,'r') as InFile:
        data = InFile.readlines()
        stripped_data = [line.strip() for line in data]
        return stripped_data[0]
def give_barcode(picklist_file):
    with open(picklist_file,'r') as InFile:
        data = InFile.readlines()
        stripped_data = [line.strip() for line in data]
        return stripped_data[1]
def give_fulfillment_area(picklist_file):
    with open(picklist_file,'r') as InFile:
        data = InFile.readlines()
        stripped_data = [line.strip() for line in data]
        return stripped_data[2]

# Program to open and read a WTW file

text_file = 'picklist.txt'
box_location = give_box_location(text_file)
barcode = give_barcode(text_file)
fulfillment_area = give_fulfillment_area(text_file)

meow = picklist(box_location, barcode, fulfillment_area)
boy = meow.format_list()
print(boy)