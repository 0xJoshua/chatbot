from bottle import route, run, template, static_file, get, post, request
import json


@get('/hello/<name>')
def hello_sayer(name):
    return template('<b>hello {{name}}</b>!', name=name)


@get('/hello')
def basic():
    return template('<div>welcome {{anything}}</div>', anything='')


@get('/')
def index():
    return static_file('chatbot.html', root='./')


@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


@post("/chat")
def chat():
    bad_words = ["fuck", "shit", "cunt", "damn", "suck", "damnit", "fucking", "motherfucker", "bastard", "bitch", "stupid", "retard"]
    you_words = ["you", "your", "you are"]
    death_words =["die", "death", "dead", "kill", "murder"]
    rel_words = ["boyfriend", "girlfriend", "gf", "bf"]
    bye_words = ["bye bye", "toodles", "see ya later", "c u later", "c u l8er", "byebye", "adios", "hasta luego", "deuces", "so long", "farewell"]
    confused_counter = [""]
    confused_counter[0] = 0
    msg = request.forms.get('msg')

    def confused():
        confused_counter[0] += 1
        return json.dumps({"animation": "confused", "msg": 'I do not understand.'})

    if msg.find('question?') > -1:
        return question()

    elif msg[-1] == '!':
        return exclamation()

    elif msg.find("friend") > -1:
        return add_friend()

    elif msg.find("love you") > -1:
        return in_love()

    for word in rel_words:
        if msg.find(word) > -1:
            return giggling()

    for word in bad_words:
        if msg.find(word) > -1:
            return afraid()

    if confused_counter[0] >= 3:
        return waiting()

    elif len(msg) <= 5:
        return confused()

    elif msg.find("dance?") > -1:
        return dancing()

    bad_words_count = 0
    you_words_count = 0
    for word in bad_words:
        if msg.find(word) > -1:
            bad_words_count += 1
    for word in you_words:
        if msg.find(word) > -1:
            you_words_count += 1

    if bad_words_count and you_words_count:
        return heart_broke()

    elif msg.find("funny") > -1:
        return laughing()

    elif msg.find("money") > -1:
        return money()

    elif msg.find("no") > -1:
        return no()

    for word in bye_words:
        if msg.find(word) > -1:
            return take_off()

    else:
        return json.dumps({"animation": "ok", "msg": 'I do not see a problem with that.'})


def question():
    return json.dumps({"animation": "excited", "msg": 'oh oh, you are asking me a question, I hope I know the answer!'})


def exclamation():
    return json.dumps({"animation": "giggling", "msg": 'why are you yelling? There is no need to raise your voice at me!'})


def add_friend():
    return json.dumps({"animation": "dog", "msg": "This is my only friend."})


def in_love():
    return json.dumps({"animation": "inlove", "msg": 'aww I love you too'})


def giggling():
    return json.dumps({"animation": "giggling", "msg": 'tehe, you are a funny guy and or girl.'})


def afraid():
    return json.dumps({"animation": "afraid", "msg": 'Do not say that, you are scaring me.'})

# def confused():
#     confused_counter[0] += 1
#     return json.dumps({"animation":"confused","msg":'I do not understand.'})


def dancing():
    return json.dumps({"animation": "dancing", "msg": 'You are welcome to dance with me.'})


def heart_broke():
    return json.dumps({"animation": "heartbroke", "msg": 'I may never recover from this.'})


def laughing():
    return json.dumps({"animation": "laughing", "msg": 'You should tell that joke at parties.'})


def money():
    return json.dumps({"animation": "money", "msg": 'Since you brought it up, I though I would show you my stash.'})


def no():
    return json.dumps({"animation": "no", "msg": 'Over my dead body.'})


def waiting():
    return json.dumps({"animation": "waiting", "msg": 'I do not have all day, bub!'})


def take_off():
    return json.dumps({"animation": "takeoff", "msg": 'toooooodles see ya later!'})


run(host='127.0.0.1', port=7050, debug=True)