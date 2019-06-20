def gd(data, label, iters, eta, w):
	'''
	Outputs a (d, 1) np.array with the result of the GD over <iter> iterations.
	:param data:	type=np.array, shape=(n_samples, n_features)
	:param label: 	type=np.array, shape=(n_samples, 1)
	:param iters:	type=int
	:param eta: 	type=uint
	:param w: 		type=np.array, shape=(n_features + 1, 1)
	:return: 		type=np.array, shape=(n_features, 1)
	'''
	pass

def sgd(data, label, iters, eta, w, batch):
	'''
	:param data:	type=np.array, shape=(n_samples, n_features)
	:param label: 	type=np.array, shape?=(n_samples, 1)
	:param iters:	type=int
	:param eta: 	type=uint
	:param w: 		type=np.array, shape=(n_features + 1, 1)
	:return: 		type=np.array, shape=(n_features, 1)
	:param batch:	type=uint
	:return: 		type=np.array, shape=(n_features, 1)
	'''
	pass

def test_error(w, test_data, test_labels, threshold):
	'''
	:param w: 			type=np.array, shape=(n_features + 1, 1)
	:param test_data: 	type=np.array, shape=(n_samples, n_features)
	:param test_labels:	type=np.array, shape=(n_samples, 1)
	:return: 			type=scalar
	'''
	pass
