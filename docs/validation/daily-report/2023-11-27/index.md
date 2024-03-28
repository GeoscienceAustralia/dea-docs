
A Daily Validation Summary Report of the surface reflectance data collected on the date of 2023-11-27 by Geoscience&nbsp;Australia. The full data can be found in the [NSD database](https://www.dea.ga.gov.au/products/national-spectral-database).

:::{contents} In this report
:local:
:backlinks: none
:::

## Variables

The variables and other environmental factors that were present on the day the data were collected.

:::{csv-table}
:class: validation-report-variables-table

"Instrument(s) used","ASD FR4 (18179/3)"
"Time of field site measurements (UTC)","2023-11-26 22:37:46 to 2023-11-26 23:37:06"
"Time of overpass (UTC)", 2023-11-27 00:45:46
"GPS quality","Good"
"Reference position","142.1036962E, 31.8135401S (WGS84)"
"<a href='/guides/about/glossary/#pq' target='_blank'>Matchup quality</a>","Good"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands. This allows the data to be used to validate our other datasets which use the same standardised bands.

```{eval-rst}
.. container:: validation-report-download

   :download:`Download as CSV <./DailyValidationResults-2023-11-27.csv>`
```

:::{csv-table}
:class: validation-report-results-table

"<a href='/guides/about/glossary/#band' target='_blank'>Band</a>","Sat Mean","Sat rms","Field mean","Field rms"
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

Click each figure to view it at full size.

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB-2023-11-27.png

A satellite imagery tile showing true colour (RGB) surface reflectance. The image is approximately 2km on a side, with the white box showing the location and the size of the field site.
:::
::::
::::{grid-item}
:::{figure} ./DayComparison-2023-11-27.png

A band-by-band plot of surface reflectance for satellite (blue) and field (red) data. Satellite uncertainty error bars for each band are the standard deviation of pixel values 
over and surrounding the field site. Field uncertainty error bars are the standard deviation of values after averaging all spectra within the same satellite pixels. 

:::
::::
::::{grid-item}
:::{figure} ./OverallComparison-2023-11-27.png

Satellite Surface Reflectance versus Field Site Surface Reflectance on this day are shown in coloured symbols, as per the insetted legend.
Black dots represent the values from all previous field site measurements prior to 2023-11-27. The solid line represents the one-to-one line
of equality between field and satellite measurements. Parameters for the line of best fit through all shown points are given in the lower right.
Note that the line of best fit is NOT shown here.
:::
::::
:::::

% :::{tags} validation, daily_validation, mullion_validation, landsat_8_validation
% :::
