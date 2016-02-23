# wrapper around skikit ML library
# exposes wrappers for MLP and SAE
from sknn.mlp import Classifier, Layer

class ClassificationTools():
	def __init__(self, inputVector, outputVector):
		pass

	def MultilayerPerceptron(self):
		pass

	def StackedAutoEncoder(self):
		pass

if __name__ == "__main__":
	# test
	X_train = [[0, 0], [0, 1], [1, 0], [1, 1]]
	y_train = [0, 1, 1, 0]
	nn = Classifier(
  	  layers=[
        Layer("Maxout", units=100, pieces=2),
        Layer("Softmax")],
   	 learning_rate=0.001,
    	n_iter=25)
	nn.fit(X_train, y_train)