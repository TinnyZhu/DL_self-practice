class Motion:
	def __init__(self,start_row,start_column,value,discount):
		self.start_row=start_row
		self.start_column=start_column
		self.row=self.start_row
		self.column=self.start_column
		self.value=value
		self.max_row=self.value.shape[0]
		self.max_column=self.value.shape[1]
		self.discount=discount
		keys=['a','s','d','w']
		self.rewards=dict.fromkeys(keys,0)
		
	def up_value(self,):
		self.row-=1
		if self.row<0:
			self.rewards['w']=-10
			self.row=self.start_row
		self.upvalue=self.rewards['w']+self.discount*self.value[self.row][self.column]
		return self.upvalue

	def down_value(self,):
		self.row+=1
		if self.row>=self.max_row:
			self.rewards['s']=-10
			self.row=self.start_row
		self.downvalue=self.rewards['s']+self.discount*self.value[self.row][self.column]
		return self.downvalue

	def left_value(self,):
		self.column-=1
		if self.column<0:
			self.rewards['a']=-10
			self.column=self.start_column
		self.leftvalue=self.rewards['a']+self.discount*self.value[self.row][self.column]
		return self.leftvalue

	def right_value(self,):
		self.column+=1
		if self.column>=self.max_column:
			self.rewards['d']=-10
			self.column=self.start_column
		self.rightvalue=self.rewards['d']+self.discount*self.value[self.row][self.column]
		return self.rightvalue






def step_value(start_row,start_column,action,discount):
	vv=[]
	for action in a:
    if action=='w':
        row=start_row-1
        column=start_column
        if row<0:
            rewards=-10
            row=start_row
        elif row==4 and column==5:
        	rewards=100
        else:
            rewards=0
        vv.append(rewards+discount*value[row][column])
    elif action=='s':
        row=start_row+1
        column=start_column
        if row>=8:
            rewards=-10
            row=start_row
        elif row==4 and column==5:
        	rewards=100
        else:
            rewards=0
        vv.append(rewards+discount*value[row][column])
    elif action=='a':
        column=start_column-1
        row=start_row
        if column<0:
            rewards=-10
            column=start_column
        elif row==4 and column==5:
        	rewards=100
        else:
            rewards=0
        vv.append(rewards+discount*value[row][column])
    elif action=='d':
        column=start_column+1
        row=start_row
        if column>=10:
            rewards=-10
            row=start_row
        elif row==4 and column==5:
        	rewards=100
        else:
            rewards=0
        vv.append(rewards+discount*value[row][column])
    value[start_row][start_column]=np.max(vv)
return value, row, column