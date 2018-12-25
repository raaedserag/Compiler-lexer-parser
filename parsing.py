from graphviz import Digraph

if_counter = 0
assign_counter = 0
while_counter = 0
for_counter = 0

def draw(tree,parent, *edges):
    for i in range(0, len(edges)//2, 2):
        tree.edge(parent, edges[i],  label= edges[i+1])



def passing(state,start, end, main_tree, node):
    global if_counter, assign_counter, while_counter, for_counter
    i = start
    while(i <= end):
        if state[i][0] == 'if':
            if_counter+=1
            edge_name = 'if_statemnt_' + str(if_counter)
            draw(main_tree, node, edge_name, '')

            test = if_state(i,main_tree,edge_name, state)
            if test != 'error':
                i = test
            else:
                return 0
        elif state[i][1] == 'identifier':
            assign_counter+=1
            edge_name = 'assign_statemnt_' + str(assign_counter)
            draw(main_tree, node, edge_name, '')

            test = assign_state(i, main_tree, edge_name, state)
            if test != 'error':
                i = test
            else:
                return 0
        elif state[i][0] == 'while':
            while_counter +=1
            edge_name = 'while_statement_' + str(while_counter)
            draw(main_tree, node, edge_name, '')

            test = while_state(i,main_tree,edge_name, state)
            if test != 'error':
                i = test
            else:
                return 0
        elif state[i][0] == 'for':
            for_counter +=1
            edge_name = 'for_statement_' + str(for_counter)
            draw(main_tree, node, edge_name, '')

            test = for_state(i,main_tree,edge_name, state)
            if test != 'error':
                i = test
            else:
                return 0
        else:
            i+= 1
            return 0

    return 1


def assign_state(i,main_tree, node,test):
    while(i<len(test)):
        draw(main_tree,node,test[i][0], 'Identifier')          # Draw the identifier edge
        i+=1                                    # Move to the next element ==> Must be '='
        if test[i][0] != '=':
            return 'error'
        i+=1                                    # Move to the next element  ==> Start of the value to be assigned
        value_s = i
        while(test[i][0] != ';' and i < len(test)):
            if test[i][1] not in ['identifier','number','+','-','*','/'] :
                return 'error'
            i+=1
        value_e = i-1
        value_t = ''
        for j in range(value_s, value_e+1,1):
            value_t+=test[j][0]
        draw(main_tree,node,value_t, 'Value')
        i+=1
        return i

def if_state(i,main_tree,node, test):
    while(i < len(test)):

        i+=1                            # Move to the next element ==> must be '('
        if test[i][0] != '(':
            return 'error'
        i+=1                            # Move to the next element ==> start of the condition
        ############################################
        condition_s = i                 # Will hold the start index of condition
        condition_flag = 1
        while((condition_flag > 0) and (i < len(test))):          # Take all the condition
            if test[i][0] == '(':
                condition_flag+=1
            elif test[i][0] == ')':
                condition_flag-=1
            i+=1

        i-=1
        condition_e = i- 1                # Will hold the end index of condition

        t_cond = ''
        for j in range(condition_s,condition_e+1,1):
            t_cond+=test[j][0]
        draw(main_tree,node,t_cond, 'Condition')
        # ////////////Function of handling Conditions ////////////
        #############################################
        i+=1                            # Move to the next element ==> must be '{'
        if test[i][0] != '{':
            return 'error'
        i+=1                            # Move to the next element ==> start ot then-statements
        then_s = i                 # Will hold the start index of then-statement
        then_flag = 1
        while(then_flag > 0 and (i<len(test))):          # Take all then-statements
            if test[i][0] == '{':
                then_flag+=1
            elif test[i][0] == '}':
                then_flag-=1
            i+=1
        i-=1
        then_e = i-1                 # Will hold the end index of then-statement

        then_t = ''
        for j in range(then_s,then_e+1,1):
            then_t+=test[j][0]
        draw(main_tree,node,then_t, 'Then')

        passing(test, then_s, then_e, main_tree, then_t)
        i+=1                           # Move to the next element ==> maybe be else or not
        ##############################################
        if (i < len(test)) and (test[i][0] == 'else'):
            i+=1                            # Move to the next element==> must be {
            if test[i][0] != '{':
                return 'error'
            i+=1                              # Move to the next element ==> start of else_statement
            else_s = i                 # Will hold the start index of else-statement
            else_flag = 1
            while(i < len(test) and else_flag > 0):          # Take all then-statements
                if test[i][0] == '{':
                    else_flag+=1
                elif test[i][0] == '}':
                    else_flag-=1
                i+=1
            i-= 1
            else_e = i-1                 # Will hold the end index of else-statement

            else_t = ''
            for j in range(else_s,else_e+1,1):
                else_t+=test[j][0]
            draw(main_tree, node, else_t, 'Else')

            passing(test, else_s, else_e, main_tree, else_t)

            i+=1            # Move to the next element
            return i

        return i
        ################################################

def while_state(i,main_tree,node,test):
    while(i < len(test)):

        i+=1                            # Move to the next element ==> must be '('
        if test[i][0] != '(':
            return 'error'
        i+=1                            # Move to the next element ==> start of the condition
        ############################################
        condition_s = i                 # Will hold the start index of condition
        condition_flag = 1
        while(condition_flag > 0):          # Take all the condition
            if test[i][0] == '(':
                condition_flag+=1
            elif test[i][0] == ')':
                condition_flag-=1
            i+=1

        i-=1
        condition_e = i- 1                # Will hold the end index of condition

        t_cond = ''
        for j in range(condition_s,condition_e+1,1):
            t_cond+=test[j][0]
        draw(main_tree,node,t_cond, 'Condition')
        # ////////////Function of handling Conditions ////////////
        #############################################
        i+=1                            # Move to the next element ==> must be '{'
        if test[i][0] != '{':
            return 'error'
        i+=1                            # Move to the next element ==> start ot then-statements
        then_s = i                 # Will hold the start index of then-statement
        then_flag = 1
        while(then_flag > 0):          # Take all then-statements
            if test[i][0] == '{':
                then_flag+=1
            elif test[i][0] == '}':
                then_flag-=1
            i+=1
        i-=1
        then_e = i-1                 # Will hold the end index of then-statement

        then_t = ''
        for j in range(then_s,then_e+1,1):
            then_t+=test[j][0]
        draw(main_tree,node,then_t, 'Loop')

        passing(test, then_s, then_e, main_tree, then_t)
        i+=1                           # Move to the next element ==> maybe be else or not

        return i
        ################################################

def for_state(i,main_tree,node,test):
    while(i < len(test)):

        i+=1                            # Move to the next element ==> must be '('
        if test[i][0] != '(':
            return 'error'
        i+=1                            # Move to the next element ==> start of the condition
        ############################################
        condition_s = i                 # Will hold the start index of condition
        condition_flag = 1
        while(condition_flag > 0):          # Take all the condition
            if test[i] == '(':
                condition_flag+=1
            elif test[i] == ')':
                condition_flag-=1
            i+=1

        i-=1
        condition_e = i- 1                # Will hold the end index of condition

        t_cond = ''
        for j in range(condition_s,condition_e+1,1):
            t_cond+=test[j]
        draw(main_tree,node,t_cond, 'Condition')
        # ////////////Function of handling Conditions ////////////
        #############################################
        i+=1                            # Move to the next element ==> must be '{'
        if test[i][0] != '{':
            return 'error'
        i+=1                            # Move to the next element ==> start ot then-statements
        then_s = i                 # Will hold the start index of then-statement
        then_flag = 1
        while(then_flag > 0):          # Take all then-statements
            if test[i][0] == '{':
                then_flag+=1
            elif test[i][0] == '}':
                then_flag-=1
            i+=1
        i-=1
        then_e = i-1                 # Will hold the end index of then-statement

        then_t = ''
        for j in range(then_s,then_e+1,1):
            then_t+=test[j][0]
        draw(main_tree,node,then_t, 'Loop')

        passing(test, then_s, then_e, main_tree, then_t)
        i+=1                           # Move to the next element ==> maybe be else or not

        return i
        ################################################


def parser(statement):
    f = Digraph('G', filename='r.gv')
    node_name = 'start'
    f.node(node_name)
    if passing(statement,0,len(statement)-1,f,node_name):
        f.view()
        return 'Succes'
    else:
        return 'Syntax Error'


