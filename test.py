from pyAudioAnalysis import audioTrainTest as aT
import pickle
index, prob, emo = aT.fileClassification("amy.wav", "svmSMtemp","svm")
print index, prob, emo
weight = [1, -0.25, 2, -2, -0.5, -2, -0.5, 1]
for i, j in enumerate(prob):
    prob[i] *= weight[i]

score =  sum(prob)
if score > 0:
    pickle.dump("The person is not depressed. Their score is " + str(score), open( "disp.p", "w"))

elif score > -0.4:
    pickle.dump("The person is moderately depressed. Their score is " + str(score), open( "disp.p", "w" ))

else:
    pickle.dump("The person is severely depressed. Their score is " + str(score), open( "disp.p", "w" ))
