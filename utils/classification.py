# wrapper around skikit ML library
# exposes wrappers for MLP and SAE
from sknn.mlp import Regressor, Classifier, Layer
import numpy
import pickle
import logging
logging.basicConfig()

class ClassificationTools():
	def __init__(self, inputVector=[], outputVector=[], filepath=''):
		if filepath == '':
			self.inputVector = numpy.asarray(inputVector)
			self.outputVector = numpy.asarray(outputVector)
			self.model = None
		else:
			self.model = pickle.load(file(filepath, 'r'))

	def setVectors(self, inputVector, outputVector):
		self.inputVector = numpy.asarray(inputVector)
		self.outputVector = numpy.asarray(outputVector)


	def trainMultilayerPerceptron(self, hlunits=10000, learningRate=0.01, iters=1000):
		# trains a simple MLP with a single hidden layer
		self.model = Regressor(
			layers=[
				Layer("Rectifier", units=hlunits),
				Layer("Linear")],
			learning_rate=learningRate,
			n_iter=iters)
		self.model.fit(self.inputVector, self.outputVector)

	def predict(self, toPredict):
		prediction = self.model.predict(numpy.asarray(toPredict))
		return prediction # this will be a 1D numpy array of floats

	def trainDeepNetwork(self):
		# trains a deep network based a multi layer autoencoder
		# which is then fine tuned using an MLP
		pass

	def serializeModel(self, filepath):
		pickle.dump(self.model, file(filepath, 'w'))

if __name__ == "__main__":
	# test / basic usage
	X_train = [[0, 0], [0, 1], [1, 0], [1, 1]]
	y_train = [[1, 0], [0, 1], [0, 1], [1, 0]]
	# train a classifier (technically multiclass regressor)
	x = ClassificationTools(X_train, y_train)
	x.trainMultilayerPerceptron()
	# make some predictions based on this (XOR) dataset
	y = x.predict([[0, 0], [0, 1], [1, 0], [1, 1]])
	# looking good :^)
	print y
	# save the model
	x.serializeModel('tmp.dat')

