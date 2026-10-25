# Dependency Map
* Core: `torch==2.4.0`, `torchvision==0.19.0`
* Acceleration & distributed: `colossalai>=0.4.4`, `accelerate>=0.29.2`, `liger-kernel==0.5.2`
* Data & Config: `mmengine>=0.10.3`, `pandas>=2.0.3`, `pandarallel>=1.6.5`, `pyarrow`, `omegaconf>=2.3.0`
* Media: `av==13.1.0`
* Text/Tokens: `ftfy>=6.2.0`
* APIs/Tracking: `openai>=1.52.2`, `wandb>=0.17.0`, `tensorboard>=2.14.0`

## Dependencies constraints
Python >= 3.6 (from setup.py).
CUDA acceleration relies heavily on `colossalai` and `torch.distributed`.
