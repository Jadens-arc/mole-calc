import clipboard
import dialogs
from calc import ElementCalc

options = [
    'Add Element', 'Moles to Grams', 'Moles to Atoms', 'Grams to Moles',
    'Grams to Atoms', 'Atoms to Grams', 'Atoms to Moles'
]

userSelect = dialogs.list_dialog(title='mole calc', items=options)

myCalc = ElementCalc('elementdata.json')

if userSelect == options[0]:
    formula = dialogs.input_alert(title='Formula')

    amount = int(dialogs.input_alert(title='Amount (in moles)'))
    answer = str(float(myCalc.molesToGrams(formula, amount)))
    isCopy = dialogs.alert(
        answer, hide_cancel_button=True, button1='copy', button2='done')
    if isCopy == 1:
        clipboard.set(answer)

elif userSelect == options[1]:
    formula = dialogs.input_alert(title='Formula')

    amount = int(dialogs.input_alert(title='Amount (in grams)'))
    answer = str(float(myCalc.gramsToMoles(formula, amount)))
    isCopy = dialogs.alert(
        answer, hide_cancel_button=True, button1='copy', button2='done')
    if isCopy == 1:
        clipboard.set(answer)

elif userSelect == options[2]:
    try:
        newElement = {
            dialogs.input_alert(title='What is the symbol').lower(): {
                'name':
                dialogs.input_alert(
                    title='What is the element\'s name').capitalize(),
                'atomic-mass':
                float(
                    dialogs.input_alert(title='What is the the atomic mass'))
            }
        }
        myCalc.addElement(newElement)
    except:
        dialogs.hud_alert('not a number')

