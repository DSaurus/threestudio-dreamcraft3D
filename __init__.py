import threestudio
from packaging.version import Version

if hasattr(threestudio, "__version__") and Version(threestudio.__version__) >= Version(
    "0.2.0"
):
    pass
else:
    if hasattr(threestudio, "__version__"):
        print(f"[INFO] threestudio version: {threestudio.__version__}")
    raise ValueError(
        "threestudio version must be >= 0.2.0, please update threestudio by pulling the latest version from github"
    )

from .data import image
from .guidance import stable_diffusion_bsd_guidance, stable_diffusion_bsd_lora_guidance
from .renderer import nvdiff_rasterizer_ref_mask
from .system import dreamcraft3d
