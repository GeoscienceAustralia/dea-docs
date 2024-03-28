# 2023-09-22: Mullion, Landsat 8 overpass

A Daily Validation Summary Report of the surface reflectance data collected on the date of 22 September 2023 by Geoscience&nbsp;Australia. The full data can be found in the [NSD database](https://www.dea.ga.gov.au/products/national-spectral-database).

:::{contents} In this report
:local:
:backlinks: none
:::

## Variables

The variables and other environmental factors that were present on the day the data was collected.

:::{csv-table}
:class: validation-report-variables-table

"Instrument(s) used","ASD FR4 (18179/3)"
"Time of field site measurements (UTC)","2023-09-21 23:56:14 to 2023-09-22 00:28:20"
"Time of overpass (UTC)","2023-09-21 23:50:46"
"GPS quality","Good"
"Reference position","148.862602E, 35.123138S (WGS84)"
"<a href='/guides/about/glossary/#pq' target='_blank'>Matchup quality</a>","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands. This allows the data to be used to validate our other datasets which use the same standardised bands.

```{eval-rst}
.. container:: validation-report-download

   :download:`Download as CSV <./Daily_Validation_Variables_2023_09_22.csv>`
```

:::{csv-table}
:class: validation-report-results-table

"<a href='/guides/about/glossary/#band' target='_blank'>Band</a>","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.0372","0.00146","0.0363","0.00667"
"Blue","0.043","0.00207","0.0429","0.00851"
"Green","0.074","0.00241","0.0772","0.013"
"Red","0.0654","0.00424","0.0685","0.0166"
"<a href='/guides/about/glossary/#nir' target='_blank'>NIR</a>","0.373","0.0215","0.39","0.0582"
"<a href='/guides/about/glossary/#swir' target='_blank'>SWIR1</a>","0.234","0.00781","0.251","0.0383"
"<a href='/guides/about/glossary/#swir' target='_blank'>SWIR2</a>","0.118","0.00442","0.128","0.0238"
:::

## Figures

Click each figure to view it at full size.

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./surface-reflectance-tile.png

A satellite imagery tile showing surface reflectance.
:::
::::
::::{grid-item}
:::{figure} ./band-chart.png

A chart showing bands.
:::
::::
::::{grid-item}
:::{figure} ./surface-reflectance-chart.png

A chart showing surface reflectance.
:::
::::
:::::

% :::{tags} validation, daily_validation, mullion_validation, landsat_8_validation
% :::

