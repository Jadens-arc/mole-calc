import json
class ElementCalc:
    def __init__(self, path):
        self.filepath = path
        with open(path, 'r') as rawData:
            self.elements = json.loads(rawData.read())

    def save(self):
        with open(self.filepath, 'w') as savedata:
            savedata.wright(json.dumps(self.elements))


    def addElement(self, data):
        self.elements.update(data)
        # adds new data to dictionary
        self.save()
        # saves it to json file

    def gramToMole(self, elements, amount):
        atomicMass = 0
        for element in elements:
            if element not in self.elements:
                print('element non in system')
                return 0

            atomicMass += self.elements[element]
        return (amount / atomicMass, atomicMass)

if __name__ == '__main__':
    myEle = ElementCalc('elementdata.json')
    features = {
        'help or ?': 'for information about what you can do',
        'mtg': 'moles to grams',
        'gtm': 'grams to moles',
        'add element': 'to add an element and it\'s attributes to our data set'
    }
    while True:
        userIn = input().strip().lower()
        if userIn == 'help' or userIn == '?':
            for feature, definition in features.items():
                print(feature)
                print('-- ' + definition)

        elif userIn == 'add element':
            newElement = {
                input('What is the symbol for the element\n'): {
                        'name': input('What is the full name of the element\n'),
                        'atomic-mass': input('What is the atomic mass of the element\n')
                    }
            }
            myEle.addElement(newElement)

        elif userIn == 'gtm':
            userElements = []
            userElementIn = input('What elements are present(e.x. HHO = H2O)\nSay done when you are done\n')
            userElements.append(userElementIn)

            while userElementIn != 'done':
                userElementIn = input('What elements are present(e.x. HHO = H2O)\nSay done when you are done\n')
                userElements.append(userElementIn.upper())

            userMass = input('What is the total mass in grams\n')

            answer = myEle.gramToMole(userElements, userMass)
            print(str(answer) + 'mols')

        else:
            print('not in system')
