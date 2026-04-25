# Example Analysis using SynchrotronAnalyzer

from SynchrotronAnalyzer import SynchrotronAnalyzer

# Example function to demonstrate parsing metadata

def parse_metadata(metadata_path):
    analyzer = SynchrotronAnalyzer(metadata_path)
    metadata = analyzer.get_metadata()
    return metadata

# Example function to analyze single images

def analyze_single_image(image_path):
    analyzer = SynchrotronAnalyzer(image_path)
    results = analyzer.analyze_single()
    return results

# Example function for batch processing

def batch_process(images_list):
    analyzer = SynchrotronAnalyzer()
    intensity_distributions = []
    centroids = []
    for image_path in images_list:
        results = analyzer.analyze_single(image_path)
        intensity_distributions.append(results['intensity_distribution'])
        centroids.append(results['centroid'])
    return intensity_distributions, centroids

# Example function for crystallographic phase analysis

def phase_analysis(image_path):
    analyzer = SynchrotronAnalyzer(image_path)
    phases = analyzer.analyze_phases()
    return phases

# Main function to demonstrate all features
if __name__ == '__main__':
    metadata_path = 'path/to/metadata.json'
    image_path = 'path/to/image.jpg'
    images_list = ['path/to/image1.jpg', 'path/to/image2.jpg']
    
    # Parse metadata
    metadata = parse_metadata(metadata_path)
    print('Metadata:', metadata)
    
    # Analyze single image
    single_image_results = analyze_single_image(image_path)
    print('Single Image Analysis Results:', single_image_results)
    
    # Batch processing
    distributions, centroids = batch_process(images_list)
    print('Batch Processing Results:', distributions, centroids)
    
    # Crystallographic phase analysis
    phases = phase_analysis(image_path)
    print('Phase Analysis Results:', phases)
