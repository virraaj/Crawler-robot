def valueiteratingpolicy(n):
    import ValueIteration
    import pinSetup
    import action_20
    import gotopos
    import initvalact
    import rewardsegregation_20 as rewardsegregation
    pinVar = pinSetup.pinSetup()
    p = pinVar[0]
    p1 = pinVar[1]
    encoder = pinVar[2]
    ENClast = pinVar[3]
    p.start(10.0)
    p1.start(10.0)
    v = initvalact.initvalact(n)
    value = v[0]
    action = v[1]
    reward = rewardsegregation.rewardsegregation(n, p, p1, encoder, ENClast)
    test = ValueIteration.valueiteration(value, reward, action)
    policy = test[1]
    raw = 0
    col = 0
    gotopos.gotopos(raw, col, p, p1, n)
    # 0 = up / 1 = down / 2 = left / 3= right
    while True:
        if action[raw][col] == 0:
            action_20.playAction(0, raw, col, n, p, p1)
            raw = raw - 1

        elif action[raw][col] == 1:
            action_20.playAction(1, raw, col, n, p, p1)
            raw = raw + 1

        elif action[raw][col] == 2:
            action_20.playAction(2, raw, col, n, p, p1)
            col = col - 1

        elif action[raw][col] == 3:
            action_20.playAction(3, raw, col, n, p, p1)
            col = col + 1


valueiteratingpolicy(4)
