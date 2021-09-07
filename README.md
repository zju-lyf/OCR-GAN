## OCR-GAN &mdash; Official PyTorch Implementation

<!-- Official pytorch implementation of the paper "[APB2FACE: AUDIO-GUIDED FACE REENACTMENT WITH AUXILIARY POSE AND BLINK SIGNALS, ICASSP'20](https://arxiv.org/pdf/2004.14569.pdf)". -->

For any inquiries, please contact Yufei Liang at [yufeiliang@zju.edu.cn](mailto:yufeiliang@zju.edu.cn)

## Using the Code

### Requirements

This code has been developed under `Python3.7`, `PyTorch 1.2.0` and `CUDA 10.1` on `Ubuntu 16.04`. 


```shell
# Install python3 packages
pip install -r requirements.txt
```

### Inference

- Download pretraind [NetG](https://drive.google.com/) for the class "leather" in MVTec dataset to the path `output/ocr_gan_aug/leather/train/weights/netG_best.pth`.
- Download pretraind [NetD](https://drive.google.com/) for the class "leather" in MVTec dataset to the path `output/ocr_gan_aug/leather/train/weights/netD_best.pth`.

```shell
python test.py --dataset leather --isize 256 --model ocr_gan_aug --load_weights
```

### Training

Train **OCR-GAN** model.
For example, train the model for the class "leather" in MVTec dataset,
```shell
python train.py --dataset leather --isize 256 --niter 200 --model ocr_gan_aug --batchsize 32
```
## Datasets

```
leather
├── test
│   ├── good
│   │   └── 000.png
│   │   └── 001.png
│   │   ...
│   │   └── n.png
│   ├── bad
│   │   └── 000.png
│   │   └── 001.png
│   │   ...
│   │   └── m.png
├── train
│   ├── good
│   │   └── 000.png
│   │   └── 001.png
│   │   ...
│   │   └── t.png

```
### Citation

If you think this work is useful for your research, please consider citing:


### Acknowledgements