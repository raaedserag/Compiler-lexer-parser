
import string

if_then = 0
if_then_else = 0
keyword = ['else', 'if', 'while', 'return', 'void', 'float', 'int', 'string', 'ch', 'include', 'double', 'for', 'do','cin','cout']
operators = ['+', '++', '--', '-', '*', '/', '=', '%', '<', '>', '<=', '>=', '==', '!=', '&&', '||']
delimiters = [',', ';', '(', ')', '{', '}', '[', ']']

single_op = ['+', '-', '*', '/', '=', '%', '<', '>', '^']
double_op = ['<=', '>=', '==', '++', '--', '!=', '&&', '||','>>','<<']
num = [0 ,1 ,2,3,4,5,6,7,8,9]
sep_list=[]
user_input = []
global output_list

def separate_op(user_input):
    for i in range (0 ,len(user_input)):
        if ((user_input[i] in single_op) and (user_input[i + 1] not in single_op )  and (user_input[i-1] not in single_op ))or user_input[i] in delimiters:
        # put spaces before and after single operators & delimiters.....

           sep_list.append(" ")
           sep_list.append(user_input[i])
           sep_list.append(" ")


        elif (user_input[i] in ['+', '-', '=', '&', '|'] and user_input[i + 1] == user_input[i]) or (
                user_input[i] in ['+', '-', '!', '<', '>'] and user_input[i + 1] == '='):

        # put spaces before and after duplicated operators.....
            sep_list.append(" ")
            sep_list.append(user_input[i])
            sep_list.append(user_input[i+1])
            sep_list.append(" ")
            i= i+1

        elif (user_input[i] in single_op) and (user_input[i-1] in single_op):
            continue


        else:
            sep_list.append(user_input[i])



    return ''.join(sep_list)  #join the list and converts into string to be splitted by split fun.
tokens = []
types = []
def kw(token):
    for i in range(0, len(keyword)):
        if keyword[i] == token:
            tokens.append(token)
            types.append("keyword")
            return 1



def idt(token):
    sp_token = list(token)
    n = len(sp_token) - 1
    if sp_token[0] in string.ascii_letters:
        for i in range(1, len(sp_token)):
            if sp_token[i] in string.ascii_letters or sp_token[i].isdigit() or sp_token[i] == '_':
                n = n - 1
        if n == 0:
            tokens.append(token)
            types.append("identifier")
            return 1


def dlm(token):
    for i in range(0, len(delimiters)):
        if delimiters[i] == token:
            tokens.append(token)
            types.append("delimiter")
            return 1


def ops(token):
    for i in range(0, len(operators)):
        if operators[i] == token:
            tokens.append(token)
            types.append("operator")
            return 1


def nums(token):
    for i in range(0,len(num)):
        tok = int(token)
        if tok %10 == num[i] :
            tokens.append(token)
            types.append("number")
            return 1

##################################################################
x = 0
input_list = []






lexer=input("please enter your code here:\n")
input_list = list(lexer)
#user_input = delete_comment(input_list)

final_separated_list = separate_op(input_list)

sp_tokens_list = final_separated_list.split()  # splited token
print(sp_tokens_list)


for i in range(0, len(sp_tokens_list)):

    r_kw = kw(sp_tokens_list[i])
    if r_kw != 1:

        r_dlm = dlm(sp_tokens_list[i])
        if r_dlm != 1:
            r_ops = ops(sp_tokens_list[i])
            if r_ops != 1:
                r_idt= idt(sp_tokens_list[i])
                if r_idt != 1:
                    nums(sp_tokens_list[i])

output_list = list(zip(tokens, types))
print(output_list)



def is_if(list,i):
    global if_then, if_then_else
    initial_flag=0
    if_then=0
    if_then_else=0

    if list[i][0] =='if' and list[i][1] =='keyword':
        initial_flag=1
        i+=1
    else:
        initial_flag=0
    if list[i][0]=='(' and list[i][1]=='delimiter' and initial_flag==1:
        initial_flag=1
        i += 1
    else:
        initial_flag=0
    # if list[i+2][0] == 'if' and initial_flag==1:
    #     is_if(list[i+2:],i+2)
    if list[i][1] == 'number' or 'identifier' and initial_flag==1:
        initial_flag=1
        i += 1
    else:
        initial_flag=0
    if list[i][1] == 'operator':
        initial_flag=1
        i += 1
    else:
        initial_flag=0
    if list[i][1] == 'number' or 'identifier' and initial_flag==1:
        initial_flag=1
        i += 1
    else:
        initial_flag=0
    if list[i][0]==')' and list[i][1]=='delimiter' and initial_flag==1:
        initial_flag=1
        i += 1
    else:
        initial_flag=0
    if list[i][0]=='{' and list[i][1]=='delimiter' and initial_flag==1:
        initial_flag=1
        i += 1
    else:
        initial_flag=0
    if list[i][0] == 'if' and initial_flag == 1:
        is_if(list[i:], i )

    if list[i][1] == 'identifier' and initial_flag==1:
        initial_flag=1
        i += 1
    else:
        initial_flag=0
    if list[i][1]=='operator' and initial_flag==1:
        initial_flag=1
        i += 1
    else:
        initial_flag=0
    if list[i][1]== 'number' or 'identifier' and initial_flag==1:
        initial_flag=1
        i += 1
    else:
        initial_flag=0
    if list[i][0]=='}' and list[i][1]=='delimiter' and initial_flag==1:
        initial_flag=1
        i += 1
        if_then=1
    else:
        initial_flag=0
    if list[i][0]=='else' and list[i][1]=='keyword' and initial_flag==1:
        initial_flag=1
        i += 1
    else:
        initial_flag=0
    if list[i][0]=='{' and list[i][1]=='delimiter' and initial_flag==1:
        initial_flag=1
        i += 1
    else:
        initial_flag=0
    if list[i][1]=='identifier' and initial_flag==1:
        initial_flag=1
        i += 1
    else:
        initial_flag=0
    if list[i][1]=='operator' and initial_flag==1:
        initial_flag=1
        i += 1
    else:
        initial_flag=0
    if list[i][1]=='number' or 'identifier' and initial_flag==1:
        initial_flag=1
        i += 1
    else:
        initial_flag=0
    if list[i][0]=='}' and list[i][1]=='delimiter' and initial_flag==1:
        initial_flag=1
        if_then_else=1
        i += 1
    else:
        initial_flag=0
    return (if_then,if_then_else)

def is_While(list,i):
    while_flag=0
    initial_flag = 0
    if list[i][0] =='while' and list[i][1] =='keyword':
        initial_flag=1
    else:
        initial_flag=0
    if list[i+1][0]=='(' and list[i+1][1]=='delimiter' and initial_flag==1:
        initial_flag=1
    else:
        initial_flag=0
    if list[i+2][1] == 'number' or 'identifier' and initial_flag==1:
        initial_flag=1
    else:
        initial_flag=0
    if list[i+3][1] == 'operator':
        initial_flag=1
    else:
        initial_flag=0
    if list[i+4][1] == 'number' or 'identifier' and initial_flag==1:
        initial_flag=1
    else:
        initial_flag=0
    if list[i+5][0]==')' and list[i+5][1]=='delimiter' and initial_flag==1:
        initial_flag=1
    else:
        initial_flag=0
    if list[i+6][0]=='{' and list[i+6][1]=='delimiter' and initial_flag==1:
        initial_flag=1
    else:
        initial_flag=0
    if list[i+7][1] == 'identifier' and initial_flag==1:
        initial_flag=1
    else:
        initial_flag=0
    if list[i+8][1]=='operator' and initial_flag==1:
        initial_flag=1
    else:
        initial_flag=0
    if list[i+9][1]== 'number' or 'identifier' and initial_flag==1:
        initial_flag=1
    else:
        initial_flag=0
    if list[i+10][0]=='}' and list[i+10][1]=='delimiter' and initial_flag==1:
        initial_flag=1
        while_flag=1
    else:
        initial_flag=0
    return(while_flag)


def Lexer():
    global if_then_else, if_then
    return output_list












