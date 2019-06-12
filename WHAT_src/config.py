import argparse
import os
from distutils.util import strtobool

parser = argparse.ArgumentParser()

# Environment
parser.add_argument("--is_train", type=strtobool, default='true')
parser.add_argument("--tensorboard", type=strtobool, default='true')
parser.add_argument("--is_resume", action='store_true', help='resume')
parser.add_argument('--cpu', action='store_true', help='use cpu only')
parser.add_argument('--gpu', type=int, default=0)
parser.add_argument("--num_gpu", type=int, default=1)
parser.add_argument("--exp_dir", type=str, default="../WHAT_exp")
parser.add_argument("--exp_exp", type=str, default="")

# Data
parser.add_argument("--data_dir", type=str, default="/mnt/sda")
parser.add_argument("--data_name", type=str, default="fashion_mnist")
parser.add_argument('--batch_size', type=int, default=32)
parser.add_argument('--rgb_range', type=int, default=1)

# Model
parser.add_argument('--uncertainty', default='aleatoric',
                    choices=('normal', 'epistemic', 'aleatoric', 'combined'))
parser.add_argument('--in_channels', type=int, default=1)
parser.add_argument('--n_feats', type=int, default=32)
parser.add_argument('--var_weight', type=float, default=1e-4)

# Train
parser.add_argument("--epochs", type=int, default=200)
parser.add_argument("--lr", type=float, default=1e-3)
parser.add_argument("--decay", type=str, default='50-50-50-50')
parser.add_argument("--gamma", type=float, default=0.5)
parser.add_argument("--optimizer", type=str, default='adam')
parser.add_argument("--weight_decay", type=float, default=1e-4)
parser.add_argument("--momentum", type=float, default=0.9)
parser.add_argument("--betas", type=tuple, default=(0.9, 0.999))
parser.add_argument("--epsilon", type=float, default=1e-8)

# Test
parser.add_argument('--n_samples', type=int, default=25)


def save_args(obj, defaults, kwargs):
    for k,v in defaults.iteritems():
        if k in kwargs: v = kwargs[k]
        setattr(obj, k, v)


def get_config():
    config = parser.parse_args()
    config.data_dir = os.path.expanduser(config.data_dir)
    return config
