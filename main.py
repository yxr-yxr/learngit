import torch
t = torch.ones(5)
print(t)

n = t.numpy()
print(n)

t.add_(1)
print(t)