# Transmembrane Region Finder

This script identifies potential transmembrane regions in protein sequences based on hydrophobicity values. It uses a sliding window approach to calculate the mean and median hydrophobicity of amino acid segments and flags regions that meet specified thresholds.

**Note:** This script was developed as part of a course project for the "Introduction to Programming" course in the Master's program in Applied Bioinformatics and Data Analysis. It is not an official tool.

## Features
- **Hydrophobicity Calculation:** Computes the mean and median hydrophobicity for each segment of the sequence.
- **Threshold-Based Detection:** Identifies segments that exceed the specified mean and median hydrophobicity thresholds.
- **Customizable Parameters:** Allows adjustment of window size and hydrophobicity thresholds.

## Usage

1.  **Input Sequence:** Provide the protein sequence as input.
2.  **Run the Script:** Execute the script to find potential transmembrane regions.

## Parameters


- `window_size`: The size of the sliding window (default: 25).
- `threshold_mean`: The mean hydrophobicity threshold (default: 0.65).
- `threshold_median`: The median hydrophobicity threshold (default: 0.75).

## Test Sequence
A test sequence file named `modified.seq` is included in the repository to help you verify the functionality of the script. You can use this sequence to see how the script identifies potential transmembrane regions.

## Installation

No special installation is required. Just ensure you have Python installed along with the `statistics` module.
