from flask import Flask
from flask_cors import CORS
from Game.python.airport_selection_function import airportselection
from Game.python.garbage_can import garbage_can, finnair_personnel, money_from_garbage, robber, hole_in_charge

app = Flask(__name__)

@app.route('/airport/<ide>')
#Gives dictionaries within dictionary of 20 randomized airports based on location to user
def airport(ide):
    result = airportselection(ide)
    return result

@app.route('/garbage/<ide>')
#when money found works now returns dictionary money as key and value is the random amount
def garbage(ide):
    value = garbage_can(ide)
    if value == 'found_money':
        result = money_from_garbage()
        return result
    elif value == 'hole_in_charge':
        result = hole_in_charge(ide)
        return result
    elif value == 'finnair_personnel':
        #check later how it will be implemented to frontend
        result = {'value': 'Finnair_personel happened'}
        return result
    elif value == 'robber':
        result = robber(ide)
        return result


@app.route('/finnair/<ide>/<answer>')

def finnair(ide, answer):
#Javascript need to check the player input. Only true state will go through (if check)
#Returns dictionary like this {'answer': 'Ei rahaa'}
    if answer == 'true':
        result = finnair_personnel(ide, answer)
        print(type(answer))
        return result


CORS(app)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)