import statistics as stat

def find_transmembrane_regions(seq, window_size=25, threshold_mean=0.65, threshold_median=0.75):
    hydrophobicity = {
        'A': 0.616, 'C': 0.680, 'D': 0.028, 'E': 0.043, 'F': 1.000,
        'G': 0.501, 'H': 0.165, 'I': 0.943, 'K': 0.283, 'L': 0.943,
        'M': 0.738, 'N': 0.236, 'P': 0.711, 'Q': 0.251, 'R': 0.000,
        'S': 0.359, 'T': 0.450, 'V': 0.825, 'W': 0.878, 'Y': 0.880
    }

    region_end = -1

    for i in range(len(seq) - window_size + 1):
        structure = seq[i:i + window_size]

        hp_median = stat.median(hydrophobicity.get(aa, 0) for aa in structure)
        hp_mean = stat.mean(hydrophobicity.get(aa, 0) for aa in structure)

        if hp_mean >= threshold_mean and hp_median >= threshold_median:
            if i > region_end: 
                print(f"Possible transmembrane region found: {i}-{i + window_size}")
                region_end = i + window_size - 1

if __name__ == "__main__":
    seq = input()
    find_transmembrane_regions(seq)
