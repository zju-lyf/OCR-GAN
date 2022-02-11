## OCR-GAN &mdash; Official PyTorch Implementation

<!-- Official pytorch implementation of the paper "[APB2FACE: AUDIO-GUIDED FACE REENACTMENT WITH AUXILIARY POSE AND BLINK SIGNALS, ICASSP'20](https://arxiv.org/pdf/2004.14569.pdf)". -->

For any inquiries, please contact Yufei Liang at [yufeiliang@zju.edu.cn](mailto:yufeiliang@zju.edu.cn)

## Using the Code

### Requirements

This code has been developed under `Python3.7`, `PyTorch 1.2.0` and `CUDA 10.0` on `Ubuntu 16.04`. 


```shell
# Install python3 packages
pip install -r requirements.txt
```
## Datasets
Download  [MVTec](https://www.mvtec.com/company/research/datasets/mvtec-ad), and the dataset should be copied into `./data` directory, and should have the following directory & file structure:
```
data
├──metal_nut
│   ├── test
│   │   ├── good
│   │   │   └── 000.png
│   │   │   └── 001.png
│   │   │   ...
│   │   │   └── n.png
│   │   ├── bad
│   │   │   └── 000.png
│   │   │   └── 001.png
│   │   │   ...
│   │   │   └── m.png
│   ├── train
│   │   ├── good
│   │   │   └── 000.png
│   │   │   └── 001.png
│   │   │   ...
│   │   │   └── t.png

```
### Inference

- Download pretraind [NetG](https://drive.google.com/file/d/1Aoad_mlBwEsi2fI7KA3jb9l-O597pqa0/view?usp=sharing) for the class "metal_nut" in MVTec dataset to the path `output/ocr_gan_aug/metal_nut/train/weights/netG_best.pth`.
- Download pretraind [NetD](https://drive.google.com/file/d/1bVyQ3NXZrcBb3HG1KB7lOm8A3BnbQsmh/view?usp=sharing) for the class "metal_nut" in MVTec dataset to the path `output/ocr_gan_aug/metal_nut/train/weights/netD_best.pth`.

```shell
python test.py --dataset metal_nut --isize 256 --model ocr_gan_aug --load_weights
```

### Training

Train **OCR-GAN** model.
```shell
python train_all.py --dataset all --isize 256 --niter 200 --model ocr_gan_aug --batchsize 32
```
