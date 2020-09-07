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
		self.keys=['a','s','d','w']
		self.rewards=dict.fromkeys(self.keys,0)
		
	def up_value(self,):
		self.row-=1
		if self.row<0:
			self.rewards['w']=-10
			self.row=self.start_row
		self.upvalue=self.rewards['w']+self.discount*self.value[self.row][self.column]
		self.start_row=self.row
		self.start_column=self.column
		self.new_input={'row':self.start_row,'column':self.start_column}
		return self.upvalue,self.new_input

	def down_value(self,):
		self.row+=1
		if self.row>=self.max_row:
			self.rewards['s']=-10
			self.row=self.start_row
		self.downvalue=self.rewards['s']+self.discount*self.value[self.row][self.column]
		self.start_row=self.row
		self.start_column=self.column
		self.new_input={'row':self.start_row,'column':self.start_column}
		return self.downvalue,self.new_input

	def left_value(self,):
		self.column-=1
		if self.column<0:
			self.rewards['a']=-10
			self.column=self.start_column
		self.leftvalue=self.rewards['a']+self.discount*self.value[self.row][self.column]
		self.start_row=self.row
		self.start_column=self.column
		self.new_input={'row':self.start_row,'column':self.start_column}
		return self.leftvalue,self.new_input

	def right_value(self,):
		self.column+=1
		if self.column>=self.max_column:
			self.rewards['d']=-10
			self.column=self.start_column
		self.rightvalue=self.rewards['d']+self.discount*self.value[self.row][self.column]
		self.start_row=self.row
		self.start_column=self.column
		self.new_input={'row':self.start_row,'column':self.start_column}
		return self.rightvalue,self.new_input


def value_map(start_row,start_column,initial_value,discount,dp,iteration):
    k=0
    while k<iteration:
        step_value,step_policy=step_optimization(start_row,start_column,initial_value,discount,dp)
        max_value=max(step_value.values())
        initial_value[start_row][start_column]=max_value
        opt_action={}
        for key in step_value.keys():
            if step_value.get(key)==max_value:
                start=step_policy.get(key)
                break
        start_row=start['row']
        start_column=start['column']
        k+=1
    value=initial_value
    return value


def step_optimization(start_row,start_column,value_map,discount,dp):
    
    udp=(1-dp)/3
    
    Step_motion=Motion(start_row,start_column,value_map,discount)
    upvalue=Step_motion.up_value()
    Step_motion=Motion(start_row,start_column,value_map,discount)
    downvalue=Step_motion.down_value()
    Step_motion=Motion(start_row,start_column,value_map,discount)
    leftvalue=Step_motion.left_value()
    Step_motion=Motion(start_row,start_column,value_map,discount)
    rightvalue=Step_motion.right_value()
    
    policy_value={'up':upvalue,'down':downvalue,'left':leftvalue,'right':rightvalue}
    action_value={}
    
    for a in policy_value.keys():
        d_value=0
        for b in policy_value.keys():
            if b==a:
                d_value=d_value+dp*policy_value[b]
            else:
                d_value=d_value+udp*policy_value[b]
        action_value.update({a:d_value})
    
    opt_action=max(action_value)
    return action_value