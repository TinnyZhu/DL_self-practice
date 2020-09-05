

def step_value(start_row,start_column,action,discount):
	vv=[]
	for action in a:
    if action=='w':
        row=start_row-1
        column=start_column
        if row<0:
            rewards=-10
            row=start_row
        else:
            rewards=0
        vv.append(rewards+discount*value[row][column])
    elif action=='s':
        row=start_row+1
        column=start_column
        if row>=8:
            rewards=-10
            row=start_row
        else:
            rewards=0
        vv.append(rewards+discount*value[row][column])
    elif action=='a':
        column=start_column-1
        row=start_row
        if column<0:
            rewards=-10
            column=start_column
        else:
            rewards=0
        vv.append(rewards+discount*value[row][column])
    elif action=='d':
        column=start_column+1
        row=start_row
        if column>=10:
            rewards=-10
            row=start_row
        else:
            rewards=0
        vv.append(rewards+discount*value[row][column])
    value[start_row][start_column]=np.max(vv)
return value, row, column