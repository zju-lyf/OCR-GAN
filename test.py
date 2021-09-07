"""
TRAIN SKIP/GANOMALY

. Example: Run the following command from the terminal.
    run train.py                                    \
        --model <skipganomaly, ganomaly>            \
        --dataset cifar10                           \
        --abnormal_class airplane                   \
        --display                                   \
"""

##
# LIBRARIES

from options import Options
from lib.data.dataloader import load_data_lap_aug
from lib.models import load_model

##
def main():
    """ Testing
    """
    opt = Options().parse()
    data = load_data_lap_aug(opt)
    model = load_model(opt, data)
    model.test()

if __name__ == '__main__':
    main()
