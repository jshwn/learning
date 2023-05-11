#   Functions about Deep Learning

* cost function
  * mse: $ \left( p - \hat{p} \right)^2  $
  * cross entropy: $  -1 \cdot \ln \left( \ \hat{p} \ \right) $

* activation funciton
  * 비선형 함수를 사용해야 모델의 레이어 층을 깊게 가져갈 수 있다.
  * 일람
    * linear
    * sigmoid
    * tanh
    * ReLU
    * leaky ReLU
    * PReLU
    * ELU
    * Maxout
    * ...
  * softmax: 확률값들을 정규화하며 출력 값들의 총합은 항상 1이 된다.
    * 수식: $$ f \left(  \vec{x}  \right)_{i} = {{e^{x_{i}}} \over {\sum_{k=1}^{K}{e^{x_{k}}}}} $$

* epoch
* learning rate
* batch_size

$$
X_{i} = X_{i-1} - \textrm{learning rate} \times \textrm{cost} \left( x,  \right)
$$

* $ x \in \mathbb{R} ^ {d \times 1} $: 모델에 입력되는 데이터

* $ W^{1} \in \mathbb{R} ^ {h \times d} $: 가중치 파라미터

* $ W^{1}x \in \mathbb{R}^{h} $:입력된 데이터를 모델의 가중치에 행렬곱한 결과. 즉 인공지능이 해당 입력에 대해 계산한 어떤 결과이다.

* $ \textrm{h} = \phi \left( W^{1}x \right)$: 인공지능이 계산한 결과를 활성화 함수에 대입하여 나온 값.
