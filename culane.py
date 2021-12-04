# DATA
dataset='CULane'
data_root = 'D:/BaiduNetdiskDownload/CULane'# 'C:/Users/1.SK-20201217CFRW/Desktop/LT_Test'

# TRAIN
epoch = 80
batch_size = 16
optimizer = 'Adam'  #['SGD','Adam']
learning_rate = 0.0001 # 0.1
weight_decay = 1e-4
momentum = 0.9

scheduler = 'cos' #['multi', 'cos']
steps = [25,38]
gamma  = 0.1
warmup = 'linear'
warmup_iters = 695

# NETWORK
use_aux = True
griding_num = 150
backbone = '18'

# LOSS
sim_loss_w = 1
shp_loss_w = 1
cur_loss_w = 1

# EXP
note = '/train_ifo'

log_path = 'D:/train61'

# FINETUNE or RESUME MODEL PATH
finetune = None
resume = None

# TEST
test_model = None
test_work_dir = None

num_lanes = 4




