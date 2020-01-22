import json
class ElementCalc:
    def __init__(self, path):
        self.filepath = path
        with open(path, 'r') as rawData:
            self.elements = json.loads(rawData.read())

    def save(self)
        with open(self.filepath, 'w') as savedata:
            savedata.wright(json.dumps(self.elements))


    def addElement(self, data):
        self.elements.update(data)
        # adds new data to dictionary
        self.save()
        # saves it to json file




if __name__ == '__main__':
    myEle = ElementCalc('elementdata.json')
    while True:
        userIn = input()
        if userIn == 'add element':
            newElement = {
                input('What is the symbol for the element\n'): {
                        'name': input('What is the full name of the element\n')
                        'atomic-mass': input('What is the atomic mass of the element\n')
                    }
            }
            myEle.addElement(newElement)
        else:
            print('not in system')
