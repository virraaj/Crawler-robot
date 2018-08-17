import GoToHome
import generate_rewardmatrix
## 0 = up / 1 = down / 2 = left / 3= right
def action_select(raw,col,n):
    # action selection according to selction of state
    if raw == 0 and col == 0:
        return [1, 3]
    elif raw == 0 and (col == -1 or col == n-1):
        return [1, 2]
    elif raw == 0:
        return [1, 2, 3]

    elif raw == n-1 and col == 0:
        return [0, 3]
    elif raw == n-1 and (col == -1 or col == n-1):
        return [0, 2]
    elif raw == n-1:
        return [0, 2, 3]

    elif col == 0:
        return [0, 1, 3]
    elif (col == -1 or col == n-1):
        return [0, 1, 2]

    else:
        return [0,1,2,3]  # cells where all four actions are possible
# def rewardseg(action,row,col):
#     ENC= encoder.getData()
#     action_20.playAction(a,row,col,n,p,p1)
#     time.sleep(0.25)
#     ENClast = encoder.getData()
#     generate_rewardmatrix[row][col][action] = ENClast - ENC

def rewardsegregation(n,p,p1,encoder,ENClast):
    reward = generate_rewardmatrix.generate_rewardmatrix(n)
    for row in range(0,n-1):
        for col in range(0,n-1):
            for action in action_select(row,col,n):
                gotopos(row,col,p,p1)
                ENClast= encoder.setData(0)
                action_20.playAction(action,row,col,n,p,p1)
                time.sleep(0.25)
                ENC = encoder.getData()
                reward[row][col][action] = ENC - ENClast
    return reward
    # generate_rewardmatrix(n)
    # GoToHome(p,p1)
    # #rewardseg(0,0,1)
    # row=0
    # col=0
    # action = 1
    # encoder.setData(0)
    # ENC= encoder.getData()
    # action_20.playAction(a,raw ,col,n,p,p1)
    # time.sleep(0.25)
    # ENClast = encoder.getData()
    # generate_rewardmatrix[row][col][action] = ENClast - ENC
    # rewardseg(0,1,0)#action that you want to do and the current row and col positions
    # rewardseg(3,0,0)
    # rewardseg(2,0,1)
    # rewardseg(3,0,0)
    # rewardseg(3,0,1)
    # rewardseg(2,0,2)
