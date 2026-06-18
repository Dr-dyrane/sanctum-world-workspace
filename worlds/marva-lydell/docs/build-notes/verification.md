# Verification Notes

Run the generic factory verifier after any build:

```bash
python3 tools/verify/verify_world_factory.py worlds/marva-lydell
```

Before upload, also run the task-specific gate after the task package exists:

```bash
python3 tools/verify/presubmit_task_gate.py worlds/marva-lydell/tasks/taskN/current
```
