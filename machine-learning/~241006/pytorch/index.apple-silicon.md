# Pytorch in Apple Silicon

##  Using Pytorch with Metal (Apple Silicon)

텐서 생성 시 `device`를 mps(metal performance shader) 객체를 명시해주어야 한다.
또는 tensor 연산 전에 `.to` 메서드로 pytorch backend를 변경할 수는 있다.

```python
import torch
mps_device = torch.device("mps")
x = torch.ones(1, device=mps_device)
# or 
x = torch.ones(1)
x = x.to(mps_device)
```
* 출처
  * [Accelerated PyTorch training on Mac](https://developer.apple.com/metal/pytorch/)
  * [May 18, 2022 Introducing Accelerated PyTorch Training on Mac](https://pytorch.org/blog/introducing-accelerated-pytorch-training-on-mac/)

##  Troubleshooting using Jupyter Notebook in Apple Silicon Mac
```
Running cells with '/opt/homebrew/bin/python3.12' requires the ipykernel package.
Run the following command to install 'ipykernel' into the Python environment. 
Command: '/opt/homebrew/bin/python3.12 -m pip install ipykernel -U --user --force-reinstall'
```

```
# 위 커맨드 실행 시
$ /opt/homebrew/bin/python3.12 -m pip install ipykernel -U --user --force-reinstall
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try brew install
    xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-brew-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip.
    
    If you wish to install a non-brew packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

[notice] A new release of pip is available: 23.3.1 -> 23.3.2
[notice] To update, run: python3.12 -m pip install --upgrade pip
```