import numpy as np
import matplotlib.pyplot as plt


class BernoulliBandit:
    """
    K: number of arms
    以概率p获得奖励1，以1-p获得奖励0
    """
    def __init__(self , K):
        self.probs = np.random.uniform(size=K)      # k个0~1的数字表示每根拉杆的获奖

        self.best_idx = np.argmax(self.probs)      #获奖概率最大的拉杆
        self.best_prob = self.probs[self.best_idx]
        self.K = K

    def step(self , k):
        if np.random.rand() < self.probs[k]:
            return 1
        else:
            return 0
        


np.random.seed(1)
K = 10
bandit_10_arm = BernoulliBandit(K)
print(bandit_10_arm.probs)
print("随机生成了一个%d臂伯努利老虎机" % K)
print("获奖概率最大的拉杆为%d号,其获奖概率为%.4f" %
      (bandit_10_arm.best_idx, bandit_10_arm.best_prob))



class Solver:
    def __init__(self , bandit):
        self.bandit = bandit
        self.counts = np.zeros(self.bandit.K)    #每根的尝试次数
        self.regret = 0  #累计懊悔
        self.action = [] 
        self.regrets = []

    def update_regret(self , k):
        self.regret += self.bandit.best_prob - self.bandit.probs[k]
        self.regrets.append(self.regret)

    def run_one_step(self):
        raise NotImplementedError

    def run(self , num_steps):
        for _ in range(num_steps):
            k = self.run_one_step()
            self.counts[k] += 1
            self.action.append(k)
            self.update_regret(k)

#epsilon-greedy

class EpsilonGreedy(Solver):
    def __init__(self, bandit , epsilon=0.1 , init_prob = 1.0):
        super(EpsilonGreedy , self).__init__(bandit)
        self.epsilon = epsilon
        self.estimates = np.array([init_prob] * self.bandit.K)     #初始化期望奖励估值
        print(self.estimates)
    
    def run_one_step(self):
        if np.random.random() < self.epsilon:
            k = np.random.randint(0 , self.bandit.K)    #随机拉动一根
        else:
            k = np.argmax(self.estimates)  # 选择期望奖励估值最大的拉杆
        r = self.bandit.step(k)    #本次动作的奖励
        self.estimates[k] += 1. /(self.counts[k] + 1) * (r - self.estimates[k])
        return k


#epsilon随时间衰减
class DecayingEpsilonGreedy(Solver):
    """ epsilon值随时间衰减的epsilon-贪婪算法,继承Solver类 """
    def __init__(self, bandit, init_prob=1.0):
        super(DecayingEpsilonGreedy, self).__init__(bandit)
        self.estimates = np.array([init_prob] * self.bandit.K)
        self.total_count = 0

    def run_one_step(self):
        self.total_count += 1
        if np.random.random() < 1 / self.total_count:  # epsilon值随时间衰减
            k = np.random.randint(0, self.bandit.K)
        else:
            k = np.argmax(self.estimates)

        r = self.bandit.step(k)
        self.estimates[k] += 1. / (self.counts[k] + 1) * (r - self.estimates[k])

        return k


def plot_results(solvers, solver_names):
    """生成累积懊悔随时间变化的图像。输入solvers是一个列表,列表中的每个元素是一种特定的策略。
    而solver_names也是一个列表,存储每个策略的名称"""
    for idx, solver in enumerate(solvers):
        time_list = range(len(solver.regrets))
        plt.plot(time_list, solver.regrets, label=solver_names[idx])
    plt.xlabel('Time steps')
    plt.ylabel('Cumulative regrets')
    plt.title('%d-armed bandit' % solvers[0].bandit.K)
    plt.legend()
    plt.show()


# np.random.seed(1)
# epsilon_greedy_solver = EpsilonGreedy(bandit_10_arm, epsilon=0.01)
# epsilon_greedy_solver.run(5000)
# print('epsilon-贪婪算法的累积懊悔为：', epsilon_greedy_solver.regret)
# plot_results([epsilon_greedy_solver], ["EpsilonGreedy"])


np.random.seed(1)
decaying_epsilon_greedy_solver = DecayingEpsilonGreedy(bandit_10_arm)
decaying_epsilon_greedy_solver.run(5000)
print('epsilon值衰减的贪婪算法的累积懊悔为：', decaying_epsilon_greedy_solver.regret)
plot_results([decaying_epsilon_greedy_solver], ["DecayingEpsilonGreedy"])