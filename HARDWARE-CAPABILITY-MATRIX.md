# Hardware Capability Matrix
* Current logic uses `torch.cuda.is_available()` to choose between "cuda" and "cpu".
* ColossalAI manages distributed capabilities and sequence/tensor parallelism (TP/SP) in `opensora.acceleration.parallel_states` and `set_group_size`.
* `offload_model` flag is extracted from config and passed to `prepare_models`.
* Memory tracking: `log_cuda_max_memory` used to print max allocated VRAM.
