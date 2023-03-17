#   Reinforcement Learning

##  Belman Equation

$$
V(s) = \max_{a} \left( R(s,a) + \gamma V(s') \right)
$$

##  Markov Decision Process, MDP


* Markov Stochastic Process
  * Markov Chain, 마르코프 연쇄라고도 한다.
  * 현재에 대한 조건부로 과거와 미래가 서로 독립인 확률 과정. 즉 미래의 상태에 대한 확률분포는 과거의 상태와 독립적이며 오로지 현재의 상태에 의해서만 결정된다.

discrete-time stochastic control process

$\left( S, \ A, \ P_a, \ R_a \right)$
