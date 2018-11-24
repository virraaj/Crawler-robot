import Q_learning_V3_1 as qLearning
import qLamda_V1_2 as qLamda
import valueiteratingpolicy
import pinSetup
import GoToHome
pinVar = pinSetup.pinSetup()
p = pinVar[0]
p1 = pinVar[1]
encoder = pinVar[2]
ENClast = pinVar[3]
p.start(3.0)
p1.start(3.0)
GoToHome.GoToHome(p, p1)

val1 = pinSetup.valueRead_ON()
val2 = pinSetup.valueRead_alg()

while True:
    if val1 == 0:
        if val2 == "Value iteration":
            valueiteratingpolicy.valueiteratingpolicy(3)
        elif val2 == "Q Learning":
            trial = qLearning.qLearning(3, p, p1, encoder, ENClast)
            print(trial[0])
            print("\n")
            print(trial[1])
            print("\n")
            print(trial[2])
        else:  # qLamda learning
            trial = qLamda.qLamda(3, p, p1, encoder, ENClast)
            print(trial[0])
            print("\n")
            print(trial[1])
            print("\n")
            print(trial[2])
    else:
        print "stopped"
