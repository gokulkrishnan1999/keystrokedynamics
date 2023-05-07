from sklearn import tree
import numpy as np
import demjson
import math
class Model(object):
	"""docstring for Model"""
	def __init__(self,i,j):

		super(Model, self).__init__()
		self.row = i
		self.col = j
		self.model = tree.DecisionTreeClassifier()
		self.user_one = None
		self.user_two = None
		self.user_two_op = None
		self.user_one_op = None

	def train(self,X_train_1,X_train_2,Y_train_1,Y_train_2):
		# self.model.fit(X_train_1,X_train_2,Y_train_1,Y_train_2)
		self.user_one = X_train_1
		self.user_two = X_train_2
		self.user_one_op =Y_train_1
		self.user_two_op =Y_train_2
		print(self.user_one_op)
		print(self.user_two_op)
		print("USER 1 FEATURE")
		print(self.user_one)
		print("USER 2 FEATURE")
		print(self.user_two)


	def predict(self,X):

		# res = self.model.predict(X)
		

		features1 =self.user_one 
		features2 = self.user_two


		def get_avg(features):
			total = 0 
			for feature in features:
				sum = 0 
				for val in feature:
					sum = sum  + float(val)
				t = sum / len(feature)
				total = total + t
			total = total / len(features)
			return total

		bool = [-1]
		thresh = 100
		avg_feat_1 = get_avg(features1)

		avg_feat_2 = get_avg(features2)

		search = get_avg(X)

			
		error = math.sqrt( abs((avg_feat_1 ** 2) - (search ** 2)))  
		print(error)

		if error < thresh:
			bool =self.user_one_op

		error = math.sqrt( abs((avg_feat_2 ** 2) - (search ** 2)  ))
		print(error)

		if error < thresh:
			bool =self.user_one_op

		if bool[0] > -1:
			return np.bincount(bool).argmax()
		else:
			return -1

			
