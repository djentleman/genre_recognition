# wrapper around skikit ML library
# exposes wrappers for MLP and SAE
from sknn.mlp import Regressor, Classifier, Layer
import numpy
import logging
logging.basicConfig()

class ClassificationTools():
	def __init__(self, inputVector, outputVector):
		self.inputVector = numpy.asarray(inputVector)
		self.outputVector = numpy.asarray(outputVector)
		self.nn = None

	def trainMultilayerPerceptron(self, hlunits=100, learningRate=0.01, iters=1000):
		self.nn = Regressor(
  	  		layers=[
        		Layer("Rectifier", units=hlunits),
        		Layer("Linear")],
   	 		learning_rate=learningRate,
    		n_iter=iters)
		self.nn.fit(self.inputVector, self.outputVector)

	def predictMLP(self, toPredict):
		prediction = self.nn.predict(numpy.asarray(toPredict))
		return prediction # this will be a 1D numpy array of floats


	def trainStackedAutoEncoder(self):
		pass

if __name__ == "__main__":
	# test
	X_train = numpy.asarray([[0, 0], [0, 1], [1, 0], [1, 1]])
	y_train = numpy.asarray([[1, 0], [0, 1], [0, 1], [1, 0]])
	nn = Regressor(
  	  layers=[
        Layer("Rectifier", units=10),
        Layer("Linear")],
   	 learning_rate=0.01,
    	n_iter=1000,)
	nn.fit(X_train, y_train)
	print nn
	print nn.predict(numpy.asarray([[0, 0], [0, 1], [1, 0], [1, 1]]))