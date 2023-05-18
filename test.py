import torch

dev = torch.cuda.current_device()

print("It worked!", torch.cuda.get_device_name(dev))