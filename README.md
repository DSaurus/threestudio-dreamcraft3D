# threestudio-dreamcraft3D

The DreamCraft3D extension of threestudio. The original implementation can be found at https://github.com/deepseek-ai/DreamCraft3D. We thank them for their contribution to the 3D generation community. To use it, please install [threestudio](https://github.com/threestudio-project/threestudio) first and then install this extension in threestudio `custom` directory.

## Installation
```
cd custom
git clone https://github.com/DSaurus/threestudio-dreamcraft3D.git
```

## Quick Start
```
prompt="a delicious hamburger"
image_path="load/images/hamburger_rgba.png"

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
