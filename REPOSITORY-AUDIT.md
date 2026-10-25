# Open-Sora Repository Audit
* Git Remote: https://github.com/lobrau-lab/Open-Sora (fetch and push)
* Branch: jules-15849827717734015394-02ee0b13
* Commit: 7ad6a96a135feb81f755c84fb391818718f6beb2 (Thu Apr 9 09:52:40 2026 +0800)
* Working tree: clean
* Version: Open-Sora 2.0.0 (from setup.py and README.md)

## Layout & Model Families
* Models: `opensora/models/` contains `mmdit`, `hunyuan_vae`, `dc_ae`, `vae`, and `text`. It supports Flux image generation and video generation.
* Configuration: `configs/` contains diffusion and vae subdirectories, specifying training and inference settings.
* Scripts: `scripts/` contains entry points: `diffusion/inference.py`, `diffusion/train.py`, `vae/inference.py`, etc.
* Datasets: `opensora/datasets/` contains dataloading, transforms, bucket, and sampler abstractions.

## Entry Points
* Inference: `scripts/diffusion/inference.py`
* Training: `scripts/diffusion/train.py`

## Checkpoint Loading
* Functionality found in `opensora/utils/ckpt.py` (e.g., `load_checkpoint`, `load_from_sharded_state_dict`).
* Supports Hugging Face safetensors, local .pt/.pth, and colossalai sharded checkpoints.

## Existing Inference Architecture
* `scripts/diffusion/inference.py` directly builds models, dataloaders, and runs loops over the dataset.
* Uses `build_module` with `MODELS` and `DATASETS` registries (from `opensora/registry.py`).
* Config parsing via `mmengine`'s `Config` in `opensora/utils/config.py`.
