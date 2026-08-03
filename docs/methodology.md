# Methodology

## UCS Calculation

UCS is defined as the maximum axial stress recorded during the test.

The tool identifies:

- Peak stress (MPa)
- Corresponding strain

## Young’s Modulus Estimation

Young’s modulus (E) is estimated using a linear regression on the initial
elastic portion of the stress–strain curve.

By default, the first ~30% of data points are used. This is a simple and
transparent assumption suitable for most laboratory datasets.

## Assumptions

- Stress is provided in MPa.
- Strain is dimensionless.
- Data is monotonic until peak stress.
- No filtering or smoothing is applied.

## Limitations

- Elastic region detection is basic; advanced methods can be added.
- No correction for machine compliance.
- No handling of post-peak softening analysis.

## Future Improvements

- Configurable elastic region selection
- Automatic detection of linear elastic zone
- PDF report generation
- Batch processing of multiple specimens
