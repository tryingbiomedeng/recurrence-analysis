This repo contains code for creating recurrence plots and perform recurrence quantification analysis for a time series.

## To use
1. Load the code blocks in python
2. Import numpy, matplotlib and pandas
3. Load the time series dataset (e.g RR intervals from ecg sequences) using numpy
4. Call the functions on the dataset to get the recurrence plot and recurrence quantification analysis parameters

## Recurrence quantification analysis 

Recurrence rate: The proportion of recurrent points in a time series, measuring how often the system revisits a certain state.

Lmax: The longest diagonal line (recurrence) length in the recurrence plot, representing the maximum extent of repeated patterns in the data.

Lmin: The shortest diagonal line (recurrence) length in the recurrence plot, indicating the minimum extent of repeated patterns in the data.

Lmean: The average diagonal line (recurrence) length in the recurrence plot, providing a measure of the typical extent of repeated patterns in the data.

Determinism: The percentage of recurrent points that form diagonal lines in the recurrence plot, quantifying the degree of predictability or determinism in the time series.

Laminarity: The percentage of recurrent points that form vertical lines in the recurrence plot, indicating the frequency of periods of invariance or laminar phases in the data.

Trapping time: The average length of diagonal lines in the recurrence plot, representing the typical duration of recurrent patterns or trapping regions in the time series.

Shannon entropy: A measure of the uncertainty or complexity of the recurrence plot, reflecting the diversity of recurrent patterns in the time series.
