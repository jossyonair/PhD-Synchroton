import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import describe

# 1. Intensity Distributions

def intensity_distribution(data):
    # Plot histogram
    plt.hist(data, bins=30, alpha=0.7, color='blue')
    plt.title('Intensity Distribution')
    plt.xlabel('Intensity')
    plt.ylabel('Frequency')
    plt.grid()
    plt.show()
    # Print statistics
    stats = describe(data)
    print('Statistics:', stats)

# 2. Centroid Calculations

def centroid_calculation(data):
    centroid = np.mean(data)
    displacement = np.abs(centroid - np.median(data))
    radial_distance = np.sqrt(np.sum((data - centroid) ** 2) / data.size)
    return centroid, displacement, radial_distance

# 3. Crystallographic Phase Analysis

def phase_analysis(d_spacing, miller_indices):
    # Example implementation for demonstration purposes
    for hkl in miller_indices:
        print(f'Miller Indices: {hkl}, d-spacing: {d_spacing}')

# 4. Batch Processing Capability

def batch_process(data_batches):
    results = []
    for data in data_batches:
        results.append(intensity_distribution(data))
    return results

# 5. Data Export to CSV and HDF5

def export_data(data, filename_csv, filename_hdf5):
    df = pd.DataFrame(data)
    df.to_csv(filename_csv, index=False)
    df.to_hdf(filename_hdf5, key='df', mode='w')

# 6. Synchrotron Beam Parameters
energy = 87.1  # keV
wavelength = 0.1426  # Å
def synchrotron_parameters():
    print(f'Synchrotron Energy: {energy} keV, Wavelength: {wavelength} Å')

# Example data
intensity_data = np.random.normal(loc=0, scale=1, size=1000)
centroid, displacement, radial_distance = centroid_calculation(intensity_data)
print(f'Centroid: {centroid}, Displacement: {displacement}, Radial Distance: {radial_distance}')

# Run demo functions
intensity_distribution(intensity_data)
phase_analysis(0.1, [(1, 0, 0), (1, 1, 0)]) # Example d-spacing and miller indices
synchrotron_parameters()

# Example of batch process
batch_results = batch_process([np.random.normal(loc=0, scale=1, size=500) for _ in range(5)])

# Export example data
export_data(intensity_data, 'intensity_data.csv', 'intensity_data.h5')