import dialogs
import console
import clipboard
from calc import ElementCalc

options = [
    'Moles to Grams', 
    'Grams to Moles',
    'Add Element'
]
  
userSelect = console.alert(
        title='mole calc', 
        button1=options[0],
        button2=options[1],
        button3=options[2]
    )
    
myCalc = ElementCalc('elementdata.json')
    
if userSelect == 1:
    formula = console.input_alert(
        title='Formula'
    )
    
    amount = int(console.input_alert(
        title='Amount (in moles)'
    ))
    answer = str(float(myCalc.molesToGrams(
            formula, amount
        )))
    isCopy = console.alert(
        answer,
        hide_cancel_button=True,
        button1='copy',
        button2='done'
    )
    if isCopy == 1:
        clipboard.set(answer)
    
elif userSelect == 2:
    formula = console.input_alert(
        title='Formula'
    )
    
    amount = int(console.input_alert(
        title='Amount (in grams)'
    ))
    answer = str(float(myCalc.gramsToMoles(
            formula, amount
        )))
    isCopy = console.alert(
        answer,
        hide_cancel_button=True,
        button1='copy',
        button2='done'
    )
    if isCopy == 1:
        clipboard.set(answer)
    
    
elif userSelect == 3:
    try:
        newElement = {
            console.input_alert(
                title = 'What is the symbol'
            ).upper(): {
                'name': console.input_alert(
                    title = 'What is the element\'s name'
                ).capitalize(),
                'atomic-mass': 
                    float(
                        console.input_alert(
                            title = 'What is the the atomic mass'
                        )
                    )
            }
            
        }
        myCalc.addElement(newElement)
    except:
        console.hud_alert('not a number')
    

