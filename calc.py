import json  # for parsing elements json file


class ElementCalc:
    def __init__(self, path):
        self.filepath = path
        with open(path, 'r') as rawData:
            try:
                self.elements = json.loads(rawData.read())
            except:
                raise KeyboardInterrupt('Not valid json')
                # throws error if json not valid
        # loads path into public dictionary and saves path in public filepath

    # writes elements dictonary(as json) to filepath
    def save(self):
        with open(self.filepath, 'w') as savedata:
            savedata.write(
                json.dumps(
                    self.elements,
                    indent=2
                )
                # converts python dictionary to json
            )
            # write return json to filepath

    def addElement(self, data):
        self.elements.update(data)
        # adds new data to dictionary
        self.save()
        # saves it to json file
        
    def parseElement(self, elements):
        atomicMass = 0  #total mass
        
        elements = elements.split(' ')
        # splits string into list
        
        # loops through elements list
        for element in elements:
            element = element.lower()
            
            # if element is trailing white space it is skipped
            if element == '':
                continue
            
            # if element is not in database raises error  
            if element not in self.elements:
                raise KeyError('Element not in Database')
            # adds elemets individual atomic mass to total
            atomicMass += float(self.elements[element]['atomic-mass'])
            
        return atomicMass

    def gramsToMoles(self, elements, amount):
        atomicMass = self.parseElement(elements)
        return float(amount) / atomicMass

    def molesToGrams(self, elements, amount):
        atomicMass = self.parseElement(elements)
        return float(amount) * atomicMass

if __name__ == '__main__':
    print('Element Calulator ')
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
