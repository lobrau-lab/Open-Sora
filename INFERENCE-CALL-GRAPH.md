# Inference Call Graph
1. `scripts/diffusion/inference.py:main()`
2. `parse_configs()` & `parse_alias()` -> setup device/dtype.
3. `init_inference_environment()` (from `opensora/utils/cai.py`) -> sets up colossalai if distributed.
4. `get_booster()` (from `opensora/utils/cai.py`) -> sets up model sharding/acceleration.
5. Dataset: `build_module(cfg.dataset, DATASETS)` and `prepare_dataloader(...)`
6. Model: `prepare_models(cfg, device, dtype, offload_model=...)` (from `opensora/utils/sampling.py`)
7. API Function: `prepare_api(model, model_ae, model_t5, model_clip, optional_models)`
8. Inference loop: iterates over prompts/dataloader, calls `refine_prompts` and processes chunks using `process_and_save(...)` (from `opensora/utils/inference.py`).
