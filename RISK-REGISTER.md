# Risk Register
1. **Tight Coupling in Inference:** `inference.py` directly handles dataloading, model instantiation, prompt refinement, and saving. Separating it into `runtime/` requires careful decoupling without breaking expected inputs.
2. **Missing Dependencies/CUDA:** Currently, running `python -c "import torch"` fails because dependencies are not installed in the environment. Phase 1 smoke testing requires installing `requirements.txt`.
3. **ColossalAI Dependency:** Deeply integrated into `booster` and `distributed` env init. Creating a hardware abstraction must account for ColossalAI's initialization.
4. **Checkpoint Formats:** Multiple checkpoint formats and distributed sharded states are handled in `ckpt.py`. A generic `ModelAdapter` must wrap these seamlessly.
5. **Config System:** `mmengine.Config` allows arbitrary deep dictionary updates via CLI strings. The new API needs typed `GenerationRequest` which must interface correctly with the flexible legacy configurations.
