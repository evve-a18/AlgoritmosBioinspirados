import random
import numpy as np

def generate_detectors(self_samples, num_detectors, min_range, max_range):
    detectors = []
    while len(detectors) < num_detectors:
        detector = random.uniform(min_range, max_range)
        
        is_valid = all([abs(detector - s) > 0.1 for s in self_samples])
        if is_valid:
            detectors.append(detector)
    return detectors
 
def classify(sample, self_samples, detectors):
    if any([abs(sample - s) <= 0.1001 for s in self_samples]): 
        return "Self"
   
    if any([abs(sample - d) <= 0.1 for d in detectors]):
        return "Non-self" 
    
    return "Unknown"

if __name__ == "__main__":

    self_samples = [1.0, 1.3, 2.0, 3.5, 4.4]
    
    num_detectors = 5
    detectors = generate_detectors(self_samples, num_detectors, 0.0, 5.0)

    print("Self samples: ", self_samples)
    print("Detectores Generados: ", detectors)
    
    test_samples = [0.9, 1.1, 2.5, 3.9, 4.7]
    for sample in test_samples:
        classification = classify(sample, self_samples, detectors)
        print(f"Sample {sample} clasificado como: {classification}")
