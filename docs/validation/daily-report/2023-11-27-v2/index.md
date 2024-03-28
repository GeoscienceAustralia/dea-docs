# 2023-11-27: Mullion, Landsat 8 overpass

A Daily Validation Summary Report of the surface reflectance data collected on
the date of 2023-11-27 by Geoscience&nbsp;Australia. The full data collection is
contained in the [NSD database](https://www.dea.ga.gov.au/products/national-spectral-database).

:::{contents} In this report
:local:
:backlinks: none
:::

## Variables

The variables and other environmental factors that were present on the day the
data were collected.

:::{csv-table}
:class: validation-report-variables-table

"Instrument(s) used","ASD FR4 (18179/3)"
"Time of field site measurements (UTC)","2023-11-26 22:37:46 to 2023-11-26 23:37:06"
"Time of overpass (UTC)", 2023-11-27 00:45:46
"GPS quality","Good"
"Reference position","142.1036962E, 31.8135401S (WGS84)"
"Matchup quality","Good"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands.
This allows the data to be used to validate Geoscience Australia's other datasets
which use the same standardised bands.

```{eval-rst}
.. container:: validation-report-download

   :download:`Download as CSV <./DailyValidationResults-2023-11-27.csv>`
```

:::{csv-table}
:class: validation-report-results-table

"Band","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.0546","0.000435","0.0488","0.003"
"Blue","0.0659","0.00141","0.0638","0.00402"
"Green","0.102","0.00452","0.104","0.0104"
"Red","0.185","0.0141","0.188","0.0284"
"Re1","0.208","0.0142","0.209","0.0312"
"Re2","0.224","0.015","0.225","0.0331"
"Re3","0.234","0.015","0.237","0.0333"
"Nir_1","0.244","0.0151","0.246","0.0313"
"Nir_2","0.25","0.0125","0.251","0.03"
"Swir_2","0.387","0.011","0.395","0.0375"
"Swir_3","0.307","0.0117","0.322","0.039"
:::

## Figures

Click an image to view it at full size.

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2023-11-27.png

A satellite imagery tile of true colour (RGB) surface reflectance. It covers an
area of approximately 2&nbsp;km &times; 2&nbsp;km. The white box indicates the size and location
of the field site.
:::
::::
::::{grid-item}
:::{figure} ./DayComparison-2023-11-27.png

A band-by-band plot of surface reflectance for satellite and field data.
Satellite uncertainty error bars for each band are the standard deviation of
pixel values over and surrounding the field site. Field uncertainty error bars
are the standard deviation of values after averaging all spectra within the same
satellite pixels. 

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2023-11-27.png

A plot of Satellite Surface Reflectance versus Field Site Surface Reflectance on this day.
The solid line represents the one-to-one equality between field and satellite measurements.
The black dots are the values from all field site measurements prior to this date. 
The line of best fit is not shown, but its parameters are given in the bottom-right corner.
:::
::::
:::::

% :::{tags} validation, daily_validation, mullion_validation, landsat_8_validation
% :::
