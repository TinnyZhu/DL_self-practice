import numpy as np

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




class Get_value:
	def __init__(self,initial_value,initial_policy,discount,dp):
		self.initial_value=initial_value
		self.initial_policy=initial_policy
		self.discount=discount
		self.dp=dp
		self.udp=(1-self.dp)/3
		self.value_shape=self.initial_value.shape
		self.max_row=self.value_shape[0]
		self.max_column=self.value_shape[1]
		self.start_row=np.random.random_integers(0,self.max_row-1)
		self.start_column=np.random.random_integers(0,self.max_column-1)

		if self.start_row>self.max_row-1:
			raise ValueError('Not so many rows')

		if self.start_column>self.max_column-1:
			raise ValueError('Not so many columns')




	def Final_map(self,):
		for f_row in range(self.max_row):
			for f_column in range(self.max_column):
				potential_action_value={}
				if f_row==0:
					if f_column==0:
						up={'up':self.value[f_row][f_column]}
						down={'down':self.value[f_row+1][f_column]}
						left={'left':self.value[f_row][f_column]}
						right={'right':self.value[f_row][f_column+1]}
					elif f_column==self.max_column-1:
						up={'up':self.value[f_row][f_column]}
						down={'down':self.value[f_row+1][f_column]}
						left={'left':self.value[f_row][f_column-1]}
						right={'right':self.value[f_row][f_column]}
					else:
						up={'up':self.value[f_row][f_column]}
						down={'down':self.value[f_row+1][f_column]}
						left={'left':self.value[f_row][f_column-1]}
						right={'right':self.value[f_row][f_column+1]}
				elif f_row==self.max_row-1:
					if f_column<=0:
						up={'up':self.value[f_row-1][f_column]}
						down={'down':self.value[f_row][f_column]}
						left={'left':self.value[f_row][f_column]}
						right={'right':self.value[f_row][f_column+1]}
					elif f_column>=self.max_column-1:
						up={'up':self.value[f_row-1][f_column]}
						down={'down':self.value[f_row][f_column]}
						left={'left':self.value[f_row][f_column-1]}
						right={'right':self.value[f_row][f_column]}
					else:
						up={'up':self.value[f_row-1][f_column]}
						down={'down':self.value[f_row][f_column]}
						left={'left':self.value[f_row][f_column-1]}
						right={'right':self.value[f_row][f_column+1]}
				else:
					if f_column==0:
						up={'up':self.value[f_row-1][f_column]}
						down={'down':self.value[f_row+1][f_column]}
						left={'left':self.value[f_row][f_column]}
						right={'right':self.value[f_row][f_column+1]}
					elif f_column>=self.max_column-1:
						up={'up':self.value[f_row-1][f_column]}
						down={'down':self.value[f_row+1][f_column]}
						left={'left':self.value[f_row][f_column-1]}
						right={'right':self.value[f_row][f_column]}
					else:
						up={'up':self.value[f_row-1][f_column]}
						down={'down':self.value[f_row+1][f_column]}
						left={'left':self.value[f_row][f_column-1]}
						right={'right':self.value[f_row][f_column+1]}
				potential_action_value.update(up)
				potential_action_value.update(down)
				potential_action_value.update(left)
				potential_action_value.update(right)
				mmax=max(potential_action_value.values())
				for key in potential_action_value.keys():
					if potential_action_value.get(key)==mmax:
						self.policy[f_row][f_column]=key
		return self.policy




	def value_map(self,iteration):
		k=0
		while k<iteration:
			step_value,step_policy=self.step_optimization()
			max_value=max(step_value.values())
			self.initial_value[self.start_row][self.start_column]=max_value
			for key in step_value.keys():
				if step_value.get(key)==max_value:
					start=step_policy.get(key)
					self.initial_policy[self.start_row][self.start_column]=key
					break
			self.start_row=start['row']
			self.start_column=start['column']
			k+=1
		self.value=self.initial_value
		self.policy=self.initial_policy

		self.final_policy=self.Final_map()

		return self.value,self.final_policy


	def step_optimization(self,):

		Step_motion=Motion(self.start_row,self.start_column,self.initial_value,self.discount)
		upvalue,upnew=Step_motion.up_value()

		Step_motion=Motion(self.start_row,self.start_column,self.initial_value,self.discount)
		downvalue,downnew=Step_motion.down_value()

		Step_motion=Motion(self.start_row,self.start_column,self.initial_value,self.discount)
		leftvalue,leftnew=Step_motion.left_value()

		Step_motion=Motion(self.start_row,self.start_column,self.initial_value,self.discount)
		rightvalue,rightnew=Step_motion.right_value()

		policy_value={'up':upvalue,'down':downvalue,'left':leftvalue,'right':rightvalue}
		self.policy_new_input={'up':upnew,'down':downnew,'left':leftnew,'right':rightnew}
		self.action_value={}

		for a in policy_value.keys():
			d_value=0
			for b in policy_value.keys():
				if b==a:
					d_value=d_value+self.dp*policy_value[b]
				else:
					d_value=d_value+self.udp*policy_value[b]
			self.action_value.update({a:d_value})

		return self.action_value,self.policy_new_input