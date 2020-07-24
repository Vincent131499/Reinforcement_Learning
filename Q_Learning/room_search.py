#-*- coding:utf-8 -*-
"""
    desc:走5号房间问题
    author:MeteorMan
    datetime:2020/7/24
"""
import numpy as np
import random

# 建立 Q 表
q = np.zeros((6, 6))
q = np.matrix(q)

# 建立 R 表

r = np.array([[-1, -1, -1, -1, 0, -1], [-1, -1, -1, 0, -1, 100], [-1, -1, -1, 0, -1, -1], [-1, 0, 0, -1, 0, -1],
              [0, -1, -1, 0, -1, 100], [-1, 0, -1, -1, 0, 100]])
r = np.matrix(r)

# 贪婪指数
gamma = 0.8

# 训练

for i in range(1000):
    # 对每一个训练,随机选择一种状态
    state = random.randint(0, 5)
    while state != 5:
        # 选择r表中非负的值的动作
        r_pos_action = []
        for action in range(6):
            if r[state, action] >= 0:
                r_pos_action.append(action)
        next_state = r_pos_action[random.randint(0, len(r_pos_action) - 1)]
        q[state, next_state] = r[state, next_state] + gamma * q[next_state].max()
        state = next_state
    # 输出训练过程
    if i % 10 == 0:
        print("------------------------------------------------")
        print("训练的次数为: %d" % i)
        print(q)
print('最终训练得到的Q:')
print(q)

print('==================================================\n\n\n')


# 验证
for i in range(10):
    print("第{}次验证".format(i + 1))

    state = random.randint(0, 5)
    print('机器人处于{}'.format(state))
    count = 0
    while state != 5:
        if count > 20:
            print('fail')
            break
        # 选择最大的q_max
        q_max = q[state].max()

        q_max_action = []
        for action in range(6):
            if q[state, action] == q_max:
                q_max_action.append(action)

        next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
        print("the robot goes to " + str(next_state) + '.')
        state = next_state
        count += 1