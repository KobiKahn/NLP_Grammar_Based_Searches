
'''

Tokenize by splitting with white space
First token is the key in the data base
Logical operator is the second token
Value is the third token
Connector

In order to test:
1. Test if token[0] is a vaild key name
2. Test if token[1] is a valid logical operator
3. Test if token[2] is a valid value for this operation

Use flow charts
'''




valid = True

valid_queries = ['department', 'age', 'gender', 'startdate', 'salary']

valid_dict = {'department': ['==', '='], 'age' : ['>', '<', '==', '='] , 'gender' : ['==', '='], 'startdate': ['>', '<', '==', '='] , 'salary' : ['>', '<', '==', '=']}


department_vals = ['sales', 'software', 'management']

gender_vals = ['m', 'f']



#### METHODS

def finish(valid, user_query = []):
        print(valid, user_query)



def test1(token1,valid_queries):
    global valid
    for value in valid_queries:
        if token1.lower() == value:
            valid = True
            break
        else:
            valid = False


    return valid



def test2(token1, token2, valid_dict):
    global valid
    value_c = 0

    for key, value in valid_dict.items():
        if key == token1.lower() and value_c == 0:
            for val in value:
                if val == token2:
                    valid = True
                    value_c = 1
                    break

                else:
                    valid = False

    return valid



def test3(token1, token3, department_vals, gender_vals):
    global valid

    if token1.lower() == 'age' or token1.lower() == 'salary' or token1.lower() == 'startdate':
        if token3.isdigit():
            valid = True
        else:
            valid = False

    elif token1.lower() == 'department':
        for value in department_vals:
            if value == token3.lower():
                valid = True
                break
            else:
                valid = False

    else:
        for value in gender_vals:
            if value == token3.lower():
                valid = True
                break
            else:
                valid = False

    return valid

def transition(token4):
    global valid

    if token4.lower() == 'and':
        pass

    elif token4.lower() == 'or':
        pass

    else:
        valid = False

    return token4.lower()



def main(valid_queries, valid_dict, department_vals):
    global valid
    counter_or = 0
    counter_and = 0

    query = input('Find all records with: ')


    user_query = query.split()
    size = len(user_query)


    if size == 7:

        token1 = user_query[0]
        token2 = user_query[1]
        token3 = user_query[2]

        token4 = user_query[3]

        token5 = user_query[4]
        token6 = user_query[5]
        token7 = user_query[6]

        if valid and transition(token4) == 'or':
            if test1(token1, valid_queries) or test1(token5, valid_queries):
                counter_or = 1
                if test2(token1, token2, valid_dict) or test2(token5, token6, valid_dict):
                    counter_or = 2
                    if test3(token1, token3, department_vals, gender_vals) or test3(token5, token7, department_vals,gender_vals):
                        counter_or = 3
                        finish(valid, user_query)

            if counter_or != 3:
                finish(valid)



        elif valid and transition(token4) == 'and':
            if test1(token1, valid_queries) and test1(token5, valid_queries):
                counter_and = 1
                if test2(token1, token2, valid_dict) and test2(token5, token6, valid_dict):
                    counter_and = 2
                    if test3(token1, token3, department_vals, gender_vals) and test3(token5, token7,department_vals,gender_vals):
                        counter_and = 3
                        finish(valid, user_query)

            if counter_and != 3:
                finish(valid)


    elif size == 3:
        token1 = user_query[0]
        token2 = user_query[1]
        token3 = user_query[2]

        if valid and test1(token1, valid_queries):
            pass
        if valid and test2(token1, token2, valid_dict):
            pass
        if valid and test3(token1, token3, department_vals, gender_vals):
            finish(valid, user_query)

    else:
        print('ERROR WITH THE LENGTH OF QUERY')
        valid = False
        finish(valid)



# main(valid_queries, valid_dict, department_vals)


record = {}
record['age'] = 55
token = ['age', '>', '45']
# query_str = "record["+"'" + token[0] + "'" + "]" + " " + token[1] + ' ' + token[2]
query_str = f'record[\'{token[0]}\'] {token[1]} {token[2]}'
print(query_str)

if eval(query_str):
    print(record)

