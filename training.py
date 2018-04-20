from pyAudioAnalysis import audioTrainTest as aT
aT.featureAndTrain(["./pyAudioAnalysis/Neutral", "./pyAudioAnalysis/Calm", "./pyAudioAnalysis/Happy", "./pyAudioAnalysis/Angry", "./pyAudioAnalysis/Disgust", "./pyAudioAnalysis/Sad", "./pyAudioAnalysis/Fearful", "./pyAudioAnalysis/Surprise"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)
