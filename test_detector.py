import os
import sys
from backend.detector import ImageForensicDetector

def run_tests():
    detector = ImageForensicDetector()
    samples_dir = os.path.join(os.path.dirname(__file__), "backend", "samples")
    
    ai_path = os.path.join(samples_dir, "sample_ai_diffusion.png")
    real_path = os.path.join(samples_dir, "sample_camera_photo.jpg")

    print(f"Testing AI Sample: {ai_path}")
    with open(ai_path, "rb") as f:
        ai_res = detector.analyze_bytes(f.read(), "sample_ai_diffusion.png")
    
    print(f" -> AI Probability: {ai_res['summary']['ai_probability']}%")
    print(f" -> Verdict: {ai_res['summary']['verdict']}")
    print(f" -> Findings count: {len(ai_res['key_findings'])}")
    assert ai_res['summary']['ai_probability'] > 60.0, f"Expected AI prob > 60%, got {ai_res['summary']['ai_probability']}%"

    print(f"\nTesting Real Camera Sample: {real_path}")
    with open(real_path, "rb") as f:
        real_res = detector.analyze_bytes(f.read(), "sample_camera_photo.jpg")
    
    print(f" -> AI Probability: {real_res['summary']['ai_probability']}%")
    print(f" -> Real Probability: {real_res['summary']['real_probability']}%")
    print(f" -> Verdict: {real_res['summary']['verdict']}")
    print(f" -> Findings count: {len(real_res['key_findings'])}")
    assert real_res['summary']['ai_probability'] < 40.0, f"Expected AI prob < 40%, got {real_res['summary']['ai_probability']}%"

    print("\n[SUCCESS] All forensic detection tests passed flawlessly!")

if __name__ == "__main__":
    run_tests()
