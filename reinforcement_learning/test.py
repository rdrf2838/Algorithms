import torch

dev = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
print(dev)


class LongList:
    def __init__(self):
        self.arr = [1, 2, 3, 4, 5]

    def __iter__(self):
        for v in self.arr:
            yield v


def func():
    for v in [1, 2, 3, 4, 5]:
        yield v


gen = func()
print(next(gen))
print(next(gen))
