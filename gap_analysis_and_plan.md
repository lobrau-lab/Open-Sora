# Gap Analysis and Phase 1 Plan

## Prioritized Gap Analysis

1.  **Architecture Gap:** The current repository tightly couples inference execution, configuration parsing, data loading, and model initialization into a single script (`scripts/diffusion/inference.py`).
2.  **API Gap:** There is no programmatic, typed API for submitting inference jobs; everything relies on `mmengine` configs and command-line arguments.
3.  **Hardware Abstraction Gap:** Hardware capabilities are hardcoded or implicitly handled by `colossalai` and basic `torch.cuda.is_available()` checks. There is no explicit memory budgeting or dynamic offloading strategy for constraints like an RTX 5070 (12GB VRAM usually, but need to check).
4.  **Job Lifecycle Gap:** Inference is a synchronous loop. There is no concept of a persistent job, cancellation, or recovery.

## Proposed Minimal-Change Architecture

Create a `runtime/` directory inside `opensora/` to establish the new modular boundary:

```text
opensora/
  runtime/
    api/         (GenerationRequest, Job Submission API)
    jobs/        (GenerationJob, State management)
    scheduler/   (Queueing and execution)
    memory/      (MemoryPolicy, Memory budgeting)
    hardware/    (HardwareBackend, Capability detection)
    adapters/    (ModelAdapter to wrap existing ckpt loading & mmdit/vae inference)
    media/       (Video assembly, metadata generation)
```

The existing `scripts/diffusion/inference.py` will be modified minimally to instantiate the new API and submit a job, acting as a compatibility wrapper to preserve existing CLI behavior.

## File-Level Implementation Plan

1.  **Phase 1 (Baseline):** Install dependencies, download a minimal checkpoint, run `scripts/diffusion/inference.py` to get baseline metrics.
2.  **Phase 2 (Architecture):**
    *   Create `opensora/runtime/api.py` defining `GenerationRequest`.
    *   Create `opensora/runtime/hardware.py` defining `HardwareBackend`.
    *   Create `opensora/runtime/adapters.py` defining `ModelAdapter`.
    *   Create `opensora/runtime/jobs.py` defining `GenerationJob`.
    *   Modify `scripts/diffusion/inference.py` to route through these abstractions while keeping original CLI args intact.
3.  **Phase 3 (Memory):** Implement memory detection and budget enforcement in `opensora/runtime/memory.py` and integrate it into the adapter.
4.  **Phase 4 (Recovery):** Expand `opensora/runtime/jobs.py` to serialize job states and handle interruptions.
5.  **Phase 5-8:** Further refinement and API hardening.

## Estimated Complexity and Technical Risks

*   **Complexity:** Medium-High. The logic in `inference.py` is deeply intertwined with `opensora.utils`. Unraveling it without breaking `train.py` or existing scripts requires precision.
*   **Risks:** Breaking distributed inference (ColossalAI) if we mismanage the booster or environment initialization.

## Required Approvals

1.  **Approval to install dependencies** (e.g., `pip install -r requirements.txt`).
2.  **Approval to download checkpoints** (a small or standard model to verify inference).
3.  **Approval to run GPU-intensive baseline benchmarks.**

## Recommendation for First Implementation Milestone

**Milestone 1:** Complete Phase 1 (Baseline). Authorize environment setup, checkpoint download, and running the original `inference.py` to capture metrics and ensure reproducibility before any refactoring begins.
