def update_reward(reward, raw, col, action, value):
    reward[raw][col][action] = value
    return reward
