import json


class ElementCalc:
    def __init__(self, path):
        self.filepath = path
        with open(path, 'r') as rawData:
            self.elements = json.loads(rawData.read())

    def save(self):
        with open(self.filepath, 'w') as savedata:
            savedata.write(
                json.dumps(
                    self.elements,
                    indent=2
                )
            )

    def addElement(self, data):
        self.elements.update(data)
        # adds new data to dictionary
        self.save()
        # saves it to json file

    def gramsToMoles(self, elements, amount):
        elements = elements.upper()
        atomicMass = 0
        for element in elements:
            if element not in self.elements:
                print('element not in system')
                return 0

            atomicMass += float(self.elements[element]['atomic-mass'])
        return float(amount) / atomicMass

    def molesToGrams(self, elements, amount):
        elements = elements.upper()
        atomicMass = 0
        for element in elements:
            if element not in self.elements:
                print('element non in system')
                return 0

            atomicMass += float(self.elements[element]['atomic-mass'])
        return float(amount) * atomicMass

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

        elif 'add' in userIn:
            newElement = {
                input('What is the symbol for the element\n'): {
                        'name': input(
                            '''
                            What is the full name of the element\n
                            '''
                        ),
                        'atomic-mass': input(
                            '''
                            What is the atomic mass of the element\n
                            '''
                        )
                    }
            }
            myEle.addElement(newElement)

        elif userIn == 'gtm':
            userElements = input(
                '''
                What elements are present(e.x. HHO = H2O)\n
                Say done when you are done\n
                '''
            )
            userElements = userElements.upper()
            userMass = input('What is the total mass in grams\n')

            answer = myEle.gramsToMoles(userElements, userMass)
            print(str(answer) + 'mols')

        elif userIn == 'mtg':
            userElements = input(
                '''
                What elements are present(e.x. HHO = H2O)\n
                Say done when you are done\n
                '''
            )
            userElements = userElements.upper()
            userMass = input('What is the total mass in moles\n')

            answer = myEle.molesToGrams(userElements, userMass)
            print(str(answer) + 'grams')

        else:
            print('not in system')
