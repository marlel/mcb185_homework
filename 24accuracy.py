# 24accuracy.py by marle_lamountry

def accuracy(tp, fp, tn, fn):
	x = (tp + tn)/(tp + tn + fp + fn)
	precision = tp/(tp + fp)
	recall = tp/(tp + fn)
	f1 = (2 * precision * recall)/ precision + recall
	return accuracy, f1
	
print(accuracy(1, 1, 1, 1))
print(accuracy(23, 59, 36, 90))
print(accuracy(81, 16, 47, 33))