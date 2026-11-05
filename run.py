import sys
import os
import uvicorn

# Ensure the project root is in python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "127.0.0.1")
    print("\n" + "="*60)
    print(" VERITAS.AI - Forensic AI Image Detector Server")
    print(f" Web UI running at: http://{host}:{port}")
    print(" Press Ctrl+C to stop.")
    print("="*60 + "\n")
    uvicorn.run("backend.app:app", host=host, port=port, reload=False)
