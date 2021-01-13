import sys
from chatbot import DataTree
from chatbot.reader.Reader import ESParser
from chatbot.config.Command import Cmd
from chatbot.inference_data.Color import Color
import chatbot_conversation
import random
import getpass
import json


def resolve(fContent):
    tree = DataTree.NPIDataTree(fContent.structured_rules, fContent.facts, fContent.queries)
    results = {}

    for query in fContent.queries:
        results[query] = tree.resolve_query(query)
        if results[query]:
            print('\n' * 50)
            print(f"{Color.RED}TravelBot: {Color.END} {final_answers[query]['name']} \n\n{Color.RED}TravelBot:{Color.END} {final_answers[query]['description']}")
            print('\n' * 5)
    return results

with open('chatbot_dialogue/final_answers.json', encoding='utf-8') as f:
    final_answers = json.load(f)
    f.close()

with open('chatbot_dialogue/final_questions.json', encoding='utf-8') as f:
    questions = json.load(f)
    f.close()

answer = chatbot_conversation.answer
speechs = chatbot_conversation.travelBotSpeechs

possible_answers = chatbot_conversation.possible_answers

def printConsole(error,user_answer,question):
    if error is True:
        print( '\n' + 'Digite uma resposta válida !' + '\n')
    else:
        print('\n')

def initial_greetings():
    print('\n' * 5)
    print('TravelBot: ' + random.choice(speechs['initial']) + '\n')
    print('TravelBot: ' + random.choice(speechs['objective']) + '\n' 'Então... vamos começar !!! Primeiramente : ' + '\n')


def verify_answer(actual_state,id,user_answer):
    try:
        for pa in possible_answers[actual_state][id]:
            if(user_answer.upper() == pa.upper()):
                return True
    except:
        return False

    return False

def create_chatbot(fContent):
    last_state = ''
    error = False
    user_answer = ''
    initial_greetings()
    while(True):

        actual_state = fContent.facts[-1]

    
        if ((actual_state.islower() or actual_state==last_state)):
            break

        printConsole(error,user_answer,questions[actual_state]['question'])

        user_answer = input(Color.RED + 'TravelBot: ' + Color.END + questions[actual_state]['question'] + '\n' + Color.GREEN + 'User: ')
        

        if(user_answer == 'leave'):
            break

        if(verify_answer(actual_state, 0, user_answer) is True):
            error = False
            fContent.do_add_fact(answer[actual_state][0])
            fContent.next_fact_rule = answer[actual_state][0]
        elif(verify_answer(actual_state, 1, user_answer) is True):
            error = False
            if( len(answer[fContent.facts[-1]]) > 1):
                fContent.do_add_fact(answer[actual_state][1])
                fContent.next_fact_rule = answer[actual_state][1]
            else:
                fContent.next_fact_rule = answer[actual_state][0] + '!'
        elif(verify_answer(actual_state, 2, user_answer) is True):
            try:
                fContent.do_add_fact(answer[actual_state][2])
                fContent.next_fact_rule = answer[actual_state][2]
                error = False
            except:
                error = True
        else:
            error = True


        if(error is False):
            last_state = actual_state
            fContent.verify_facts()


if __name__ == "__main__":  
    try:
        with open('rules.txt') as f:
            lines = f.readlines()
            fContent = ESParser(lines)
            create_chatbot(fContent)
            res = resolve(fContent)
           
    except (Exception, BaseException) as e:
        print(e)
        sys.exit(1)
