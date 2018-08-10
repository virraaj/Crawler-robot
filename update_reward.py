def update_reward(reward, raw, col, action, diff):
    reward[raw][col][action] = diff
    return reward
