from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter(log_dir="log_dir") #日志的目录在 log_dir

x = range(100)
for i in x:
    writer.add_scalar('y=2x', i*2, i)
    print(i*2)

writer.close()