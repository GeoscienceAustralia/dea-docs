## Background

*This is a sub-product of [**DEA Surface Reflectance (Sentinel-2A MSI)**](https://cmi.ga.gov.au/data-products/dea/683/dea-surface-reflectance-sentinel-2a-msi). See the parent product for more information.*

Reflectance data at top of atmosphere (TOA) collected by Sentinel-2A MSI sensors can be affected by atmospheric conditions, sun position, sensor view angle, surface slope and surface aspect.

Surfaces with varying terrain can introduce inconsistencies to optical satellite images through irradiance and bidirectional reflectance distribution function (BRDF) effects. For example, slopes facing the sun appear brighter compared with those facing away from the sun. Likewise, many surfaces on Earth are anisotropic in nature, so the signal picked up by a satellite sensor may differ depending on the sensor’s position.

These inconsistencies need to be reduced or removed to ensure the data can be compared over time.

## What this product offers

This product takes Sentinel-2A MSI imagery captured over the Australian continent and corrects the inconsistencies across the land and coastal fringe. It achieves this using Nadir corrected Bi-directional reflectance distribution function Adjusted Reflectance (NBAR).

In addition, this product applies terrain illumination correction to correct for varying terrain.

The resolution is a 10/20/60 m grid based on the ESA level 1C archive.

% ## Data description

% ## Applications

## Technical information

#### Top of atmosphere reflectance measurements

Sentinel-2 series sensors measure top of atmospheric reflectance, which is a composite of:

* surface reflectance
* atmospheric condition
* interaction between surface land cover, solar radiation and sensor view angle (BRDF effect)
* land surface orientation relative to the imaging sensor (terrain illumination).

It has been traditionally assumed that satellite imagery displays negligible variation in sun and sensor view angles. However, these can vary significantly both within and between scenes, especially in different seasons and geographic regions (Li et al. 2010, 2012).

#### Surface reflectance correction models

This product represents standardised optical surface reflectance using robust physical models to correct for variations and inconsistencies in image radiance values.

It delivers modelled surface reflectance from Sentinel-2A MSI data using physical rather than empirical models. This ensures that the reflective value differences between imagery acquired at different times by different sensors will be primarily due to on-ground changes in biophysical parameters rather than artefacts of the imaging environment.

This product is created using a physics-based, coupled Bidirectional Reflectance Distribution Function (BRDF) and atmospheric correction model that can be applied to both flat and inclined surfaces (Li et al. 2012). The resulting surface reflectance values are comparable both within individual images and between images acquired at different times.

For more information on the BRDF/Albedo Model Parameters product, see [MCD43A1 Collection 6](/node/375). 

#### Sentinel-2 archive

To improve access to Australia’s archive of Sentinel-2 data, several collaborative projects have been undertaken in conjunction with industry, government and academic partners. These projects have enabled implementation of a more integrated approach to image data correction that incorporates normalising models to account for atmospheric effects, BRDF and topographic shading (Li et al. 2012). The approach has been applied to Sentinel-2 imagery to create baseline surface reflectance products.

The advanced supercomputing facilities provided by the National Computational Infrastructure (NCI) at the Australian National University (ANU) have been instrumental in handling the considerable data volumes and processing complexities involved with the production of this product.

#### Image format specifications

##### ***band01, band02, band03, band04, band05, band06, band07, band08, band8A, band11, band 12***

**Format** GeoTIFF

**Resolution** 10/20/60m based on Sentinel-2 original pixel resolution

**Datatype** Int16

**No data value** \-999

**Valid data range** \[1,10000\]

**Tiled with X and Y block sizes** 512x512

**Compression** Deflate, Level 6, Predictor 2

**Pyramids** Levels: \[8,16,32\]  
Compression: deflate  
Resampling: GDAL default (nearest)  
Overview X&Y block sizes: 512x512

**Contrast stretch** None

**Output CRS** As specified by source dataset; source is UTM with WGS84 as the datum

##### ***thumbnail***

**Format** JPEG

**RGB combination** 

Red: band 4  
Green: band 3  
Blue: band 2

**Resolution** X and Y directions each resampled to 10% of the original size

**Compression** JPEG, Quality 75 (GDAL default)  
PHOTOMETRIC colour model: YCBCR

**Contrast stretch** Linear  
Input minimum: 10  
Input maximum: 3500  
Output minimum: 0  
Output maximum: 255

**Output CRS** Geographics (Latitude/Longitude) WGS84

% ## Lineage

## Processing steps

1. Longitude and Latitude Calculation

1. Satellite and Solar Geometry Calculation

1. Aerosol Optical Thickness Retrieval

1. BRDF Shape Function Retrieval

1. Ozone Retrieval

1. Elevation Retrieval and Smoothing

1. Slope and Aspect Calculation

1. Incidence and Azimuthal Incident Angles Calculation

1. Exiting and Azimuthal Exiting Angles Calculation

1. Relative Slope Calculation

1. Terrain Occlusion Mask

1. MODTRAN

1. Atmospheric Correction Coefficients Calculation

1. Bilinear Interpolation of Atmospheric Correction Coefficients

1. Surface Reflectance Calculation (NBAR)

% ## Software

## References

1. F. Li, D. L.B. Jupp & M. Thankappan (2015) Issues in the application of Digital Surface Model data to correct the terrain illumination effects in Landsat images, International Journal of Digital Earth, 8:3, 235-257, DOI: [10.1080/17538947.2013.866701](https://doi.org/10.1080/17538947.2013.866701)

2. L. Wang, F. Li, I. Alam, D. Jupp, S. Oliver and M. Thankappan, "Analysis Ready Data Sensitivity Analyses," *IGARSS 2019 - 2019 IEEE International Geoscience and Remote Sensing Symposium*, 2019, pp. 5642-5645, [doi: 10.1109/IGARSS.2019.8898667](https://ieeexplore.ieee.org/abstract/document/8898667)
