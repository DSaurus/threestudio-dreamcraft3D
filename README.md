# threestudio-dreamcraft3D
<img src="https://github.com/DSaurus/threestudio-dreamcraft3D/assets/24589363/d9ad81e9-1154-4b41-8cc9-2b7d558e0282" width="" height="128">
<img src="https://github.com/DSaurus/threestudio-dreamcraft3D/assets/24589363/6b27f858-8f88-47c3-98e9-c28401ab5e03" width="" height="128">
<img src="https://github.com/DSaurus/threestudio-dreamcraft3D/assets/24589363/81bdec2d-3be7-4df1-a47b-1bdef8e36186" width="" height="128">

The DreamCraft3D extension of threestudio. The original implementation can be found at https://github.com/deepseek-ai/DreamCraft3D. We thank them for their contribution to the 3D generation community. To use it, please install [threestudio](https://github.com/threestudio-project/threestudio) first and then install this extension in threestudio `custom` directory.

## Installation
```
cd custom
git clone https://github.com/DSaurus/threestudio-dreamcraft3D.git

# If you want to use your custom image, please install background remover
pip install backgroundremover
```

You also need to make sure that you have an access token from huggingface to use `DeepFloyd-IF`.
```
huggingface-cli login
```

To download stable-zero123, please go to the `load/zero123` directory and run `download.sh`.

## Quick Start
```
prompt="a delicious hamburger"
image_path="load/images/hamburger_rgba.png"

# All stages need ~22G GPU memory
# --------- Stage 1 (NeRF & NeuS) --------- #
python launch.py --config custom/threestudio-dreamcraft3D/configs/dreamcraft3d-coarse-nerf.yaml --train system.prompt_processor.prompt="$prompt" data.image_path="$image_path"

ckpt=outputs/dreamcraft3d-coarse-nerf/$prompt@LAST/ckpts/last.ckpt
python launch.py --config custom/threestudio-dreamcraft3D/configs/dreamcraft3d-coarse-neus.yaml --train system.prompt_processor.prompt="$prompt" data.image_path="$image_path" system.weights="$ckpt"

# --------- Stage 2 (Geometry Refinement) --------- #
ckpt=outputs/dreamcraft3d-coarse-neus/$prompt@LAST/ckpts/last.ckpt
python launch.py --config custom/threestudio-dreamcraft3D/configs/dreamcraft3d-geometry.yaml --train system.prompt_processor.prompt="$prompt" data.image_path="$image_path" system.geometry_convert_from="$ckpt"


# --------- Stage 3 (Texture Refinement) --------- #
ckpt=outputs/dreamcraft3d-geometry/$prompt@LAST/ckpts/last.ckpt
python launch.py --config custom/threestudio-dreamcraft3D/configs/dreamcraft3d-texture.yaml --train system.prompt_processor.prompt="$prompt" data.image_path="$image_path" system.geometry_convert_from="$ckpt"
```

## Run with your custom image

First preprocess images to remove background and get depth/normal maps. You can also get image caption with the following script.

```
# preprocess images
cd custom/threestudio-dreamcraft3D
python image_preprocess.py "examples/hamburger.png" --size 512 --border_ratio 0.0
# if you need image caption
# python image_preprocess.py "examples/hamburger.png" --size 512 --border_ratio 0.0 --need_caption
cd ../..
```

Then run dreamcraft3D using the following script.

```
prompt="a delicious hamburger"
image_path="custom/threestudio-dreamcraft3D/examples/hamburger_rgba.png"

# --------- Stage 1 (NeRF & NeuS) --------- #
python launch.py --config custom/threestudio-dreamcraft3D/configs/dreamcraft3d-coarse-nerf.yaml --train system.prompt_processor.prompt="$prompt" data.image_path="$image_path"

ckpt=outputs/dreamcraft3d-coarse-nerf/$prompt@LAST/ckpts/last.ckpt
python launch.py --config custom/threestudio-dreamcraft3D/configs/dreamcraft3d-coarse-neus.yaml --train system.prompt_processor.prompt="$prompt" data.image_path="$image_path" system.weights="$ckpt"

# --------- Stage 2 (Geometry Refinement) --------- #
ckpt=outputs/dreamcraft3d-coarse-neus/$prompt@LAST/ckpts/last.ckpt
python launch.py --config custom/threestudio-dreamcraft3D/configs/dreamcraft3d-geometry.yaml --train system.prompt_processor.prompt="$prompt" data.image_path="$image_path" system.geometry_convert_from="$ckpt"


# --------- Stage 3 (Texture Refinement) --------- #
ckpt=outputs/dreamcraft3d-geometry/$prompt@LAST/ckpts/last.ckpt
python launch.py --config custom/threestudio-dreamcraft3D/configs/dreamcraft3d-texture.yaml --train system.prompt_processor.prompt="$prompt" data.image_path="$image_path" system.geometry_convert_from="$ckpt"
```

## Citing

If you find DreamCraft3D helpful, please consider citing:

```
@article{sun2023dreamcraft3d,
  title={Dreamcraft3d: Hierarchical 3d generation with bootstrapped diffusion prior},
  author={Sun, Jingxiang and Zhang, Bo and Shao, Ruizhi and Wang, Lizhen and Liu, Wen and Xie, Zhenda and Liu, Yebin},
  journal={arXiv preprint arXiv:2310.16818},
  year={2023}
}
```
