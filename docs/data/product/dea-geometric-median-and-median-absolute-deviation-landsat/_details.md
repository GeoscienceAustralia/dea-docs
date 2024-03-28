## Background

Satellite imagery allows us to observe the Earth with significant accuracy and detail. However, missing data — such as gaps caused by cloud cover — can make it difficult to create a complete image. In order to produce a single, complete view of a certain area, satellite data must be consolidated by stacking measurements from different points in time to create a composite image. 

The Digital Earth Australia GeoMAD (Geometric Median and Median Absolute Deviation) data product is a cloud-free composite of satellite data compiled annually for each calendar year. 

Large-scale image composites are increasingly important for a variety of applications such as land cover mapping, change detection, and the generation of high-quality data to parameterise and validate bio-physical and geophysical models. A number of compositing methodologies are being used in remote sensing in general; however, challenges still exist. These challenges include  mitigating against boundary artifacts due to mosaicking scenes from different epochs ensuring spatial regularity across the mosaic image and maintaining the spectral relationship between bands. 

The creation of good composite images is especially important due to the opening of the [Landsat archive of the United States Geological Survey](https://www.usgs.gov/landsat-missions/landsat-collections). The greater availability of satellite imagery has resulted in demand to provide large regional mosaics that are representative of conditions over specific time periods while also being free of clouds and other unwanted visual noise. One approach is to ‘stitch together’ multiple selected high-quality images. Another is to create mosaics in which pixels from a time series of observations are combined (using an algorithm). This ‘pixel composite’ approach to mosaic generation provides more consistent results than with stitching high-quality images due to the improved colour balance created by combining one-by-one pixel-representative images. Another strength of pixel-based composites is their ability to be automated, hence enabling their use in large data collections and time series datasets. 

The DEA GeoMAD product can be used for seeing how an area of land usually looks rather than only viewing it at a single point in time. Hence you can assess the land cover and land use on a general basis rather than at a specific point in time. It can also be used to assess how much an area changes over time. It highlights areas like bare rock that are very stable in contrast to cropping areas that change dramatically.

This product combines the Geometric Median and the Median Absolute Deviation algorithms in a single package. The Geometric Median output provides information on the general conditions of the landscape for a given year. Meanwhile the Median Absolute Deviation output provides information on how the landscape is changing in the same year. 

::::{grid} 1 2 2 2
:::{grid-item}
<figure>
    <img src="/_static/geomedian/Geomedian_1988_2023_Canberra_ACT.gif" alt="Geomedian 1988-2023 Canberra, ACT" style="max-width: 600px;">
    <figcaption>Canberra, ACT 1988&ndash;2023</figcaption>
</figure>
:::
:::{grid-item}
<figure>
    <img src="/_static/geomedian/Geomedian_1988_2023_Lake_Argyle_WA.gif" alt="Geomedian 1988-2023 Lake Argyle, WA" style="max-width: 600px;">
    <figcaption>Lake Argyle, WA 1988&ndash;2023</figcaption>
</figure>
:::
:::{grid-item}
<figure>
    <img src="/_static/geomedian/Geomedian_1988_2023_Shepparton_Vic.gif" alt="Geomedian 1988-2023 Shepparton, VIC" style="max-width: 600px;">
    <figcaption>Shepparton, VIC 1988&ndash;2023</figcaption>
</figure>
:::
:::{grid-item}
<figure>
    <img src="/_static/geomedian/Geomedian_1988_2023_Lake_Dalrymple_Qld.gif" alt="Geomedian 1988-2023 Lake Dalrymple, Qld.zip" style="max-width: 600px;">
    <figcaption>Lake Dalrymple, Qld 1988&ndash;2023</figcaption>
</figure>
:::
::::

## What this product offers

This product provides statistical tools that utilise DEA’s Earth observation data to provide annual images of general conditions and how much an area changes in a given year. 

The geometric median part of the product provides an 'average' cloud-free image over the given year. The geometric median image is calculated with a multi-dimensional median, using all the spectral measurements from the satellite imagery at the same time in order to maintain the relationships between the measurements. 

The median absolute deviation part of the product uses three measures of variance, each of which provides a 'second order' high dimensional statistical composite for the given year. The three variance measures show how much an area varies from the 'average' in terms of 'distance' based on factors such as brightness and spectra. The three variance measures are: 

* Euclidean distance (EMAD) 
* Cosine (spectral) distance (SMAD) 
* Bray Curtis dissimilarity (BCMAD) 

Together, they provide information on variance in the landscape over the given year and are useful for change detection applications. 

The GeoMAD product is useful for the following.

* Land cover mapping.
* Change detection and classification (such as for burn-area mapping, crop mapping, and urban area mapping). 
* General variance and change, so it can be used in machine learning for change detection. 
* Environmental monitoring.

## Technical information

### Median Composites

Median composites are a method for creating large image mosaics using an algorithm that helps remove cloud and shadow noise by setting the value of each pixel of the composite to its consistent median values for each band. In this simple median method, the median of each band is independent of the other bands for any given pixel.

The benefit of using the median composite algorithm is that it is very fast to compute. The problem, however, is that satellite imagery pixels hold information for multiple bands and simple medians lose the relationships in this information, creating unnatural results. Therefore, a geometric median algorithm is used instead, since it can handle multi-dimensional data and maintain the relationships between bands for each pixel.

:::{figure} /_files/geomedian/geomedian-alg-composite_techspecs.jpg
:alt: Median compositing algorithm diagram

A simple median considers data from each band independently. This can be seen in Step 2 of the median compositing algorithm. (Source: [Digital Earth Africa &mdash; Introduction to the Digital Earth Africa Sandbox](https://learn.digitalearthafrica.org/courses/course-v1:digitalearthafrica+DEA101+2021/))
:::

:::{dropdown} Median Compositing Algorithm
As shown in the figure above, this algorithm is calculated as follows.

1. A median composite is applied individually to every given pixel stack
1. Spectral values like red, green, or blue are projected onto separate components. A median value is calculated on each component.
1. The medians calculated on each component are combined to form a single point in spectral space. This point may not be like previously observed pixels.
1. The generated pixel is added to the final composite product.
:::

### Geometric Median

Geomedian (or geometric median) composites are multi-band generalisations of median composites. A geomedian composite finds the median values of the bands for each pixel when considered together (as opposed to simple median composites which find a pixel’s median value for each band individually).

Geomedians are an appropriate choice of algorithm because they represent multiple bands of data. 

The **surface reflectance geomedian** uses high-dimensional statistical theory to deliver a spectrally consistent and reasonably artefact-free pixel composite product. 

The geomedian is a pixel-composite mosaic of a time series of earth observations. Essentially, the value of a pixel in a geomedian image is the statistical median of all observations for that pixel for a period of time. For example, the 2016 Landsat 8 geomedian image over an area will be the median of all Landsat 8 pixels recorded for that area in 2016. 

An **annual geometric median** is a high-dimensional median calculated from the reflectance values recorded over a one-year period. The annual geomedians are available for each full calendar year since 1986.

:::{figure} /_files/geomedian/geomedian-composite_techspecs.jpg
:alt: Geomedian algorithm diagram

Each band adds a dimension to the geomedian calculation. For a three-band dataset &mdash; such as the RGB dataset shown in this figure &mdash; each point can be represented on a three-dimensional scatter plot. The geomedian is the minimised ‘sum of distances’ between all of these points. (Source: [Digital Earth Africa &mdash; Introduction to the Digital Earth Africa Sandbox](https://learn.digitalearthafrica.org/courses/course-v1:digitalearthafrica+DEA101+2021/))
:::

:::{dropdown} Geometric Median Compositing Algorithm
As shown in the figure above, this algorithm is calculated as follows.

1. A geometric median composite is applied individually to every pixel stack.
1. Pixels are represented as vectors distributed in a high-dimensional space. Each value (like red, green, blue, or NIR) has a component in this space. (NIR means Near-Infra Red.)
1. By calculating a point that minimises the distance between it and all other points (pixels), this creates a representative pixel of all observations in the pixel stack.
1. The generated pixel is added to the final composite product.
:::

Multispectral satellite imagery (such as that provided by Landsat and Sentinel-2) consists of multiple measurements per pixel — one for each spectral band. In order to create a meaningful median, a median pixel must take all concurrent spectral measurements into account simultaneously as a multi-dimensional set (rather than each measurement independently as with a simple median). The geomedian is a high-dimensional statistic which calculates a multi-dimensional median from all the spectral measurements of the satellite imagery at the same time and maintains the relationships between the measurements. This provides a median of the physical conditions measured by the earth observations used to create it. It provides a good representation of a typical pixel observation devoid of outliers and has reduced spatial noise.

The annual geomedian provides an annual surface reflectance composite for any area of interest within the area covered by the DEA’s [Open Data Cube](https://www.dea.ga.gov.au/about/open-data-cube), up to the entire spatial extent available. It provides a cloud-free overview of the middle surface reflectance value for each year. It is equivariant, meaning that a linear algorithm applied to a geomedian image is equal to a geomedian applied to a set of images on which the same linear algorithm was applied. Therefore, it can be used in further analyses such as Tasseled Cap, Principal Components Analysis, and Normalised Difference Indices. It is useful in analyses requiring baseline conditions such as change detection.

Surface reflectance geometric median products are derived from the DEA Surface Reflectance (SR) products and provide a representation of the 'average' of surface reflectance over the time period. This is a synthetic representation of a time series rather than an actual observed pixel. 

The geomedian (Roberts et al. 2017) is used rather than the mean because the mean can be easily distorted by extrema whereas the median is less sensitive to outliers. The geomedian is used rather than the basic median because it preserves the physical relationship between spectral measurements. The geometric median is used rather than the medoid (Flood 2013) because a low noise composite cannot be provided. Note that where the provenance of each pixel in a composite is required, the medoid is the preferred method and the geomedian should not be used.

### Input Data

The input data used to calculate the geomedian are filtered to remove poor quality observations. The filter only accepts observations with a geometric quality assessment (GQA) of less than 1 and it applies a 3-pixel opening operation on clouds and a 6-pixel dilation operation on both cloud and shadows for pixels masked by the fmask algorithm.

The statistics are calculated over time periods based on the availability of the satellites and sensors.

* **ga_ls5t_gm_cyear_3** &mdash; Uses Landsat 5 data.
* **ga_ls7e_gm_cyear_3** &mdash; Uses Landsat 7 data.
* **ga_ls8cls9c_gm_cyear_3** &mdash; Uses Landsat 8 and 9 data.

Note that only Landsat 7 geomedian data is available between 2000 and 2002 because the Landsat 5 satellite was unavailable.

The primary uses of geomedian pixel composites are for change detection within baselines and for broad regional image composites (such as national and continental mosaics).

:::{figure} /_files/landsat/landsat-timeline-2024.jpg
:alt: Landsat geomedian time coverage diagram

Timeline of Landsat satellite and sensor availability.
:::

::::{dropdown} Timeline of Landsat availability
As shown in the figure above, the Landsat satellites have data available for the following time periods.

:::{list-table}

* - **Landsat 5**
  - 1986&ndash;2000 and 2002&ndash;2010
* - **Landsat 7**
  - 2000&ndash;2021
* - **Landsat 8**
  - 2013 onwards
* - **Landsat 9**
  - 2022 onwards
:::
::::

### Median Absolute Deviation

The ‘first order’ statistics of a dataset include the mean and the median. As opposed to the mean, for multi-dimensional datasets such as satellite imagery, the median provides a method to find general conditions for a time period while also maintaining the physical relationships between spectral measurements. 

A ‘second order’ statistic associated with a mean of a dataset is the standard deviation which provides a measure of data variance. The equivalent second order statistic associated with the median is the Median Absolute Deviation (MAD), which provides the associated variance measures for the median. 

The MAD is the median of absolute differences of the individual values in a set of data from their overall median. To calculate the MAD for a multi-dimensional dataset — such as the set of satellite images captured in a year — measures of ‘distance’ from each multi-dimensional measurement to the median are needed (these are the set of spectral measurements for a pixel through time:  blue, green, red, near-infra-red, and short-wave-infra-red). However, multi-dimensional distances can be calculated in different ways, providing different insights into the behaviour of pixels through time. The DEA GeoMAD product includes three MADs produced from different measures of distance.

* **Euclidean distance (EMAD)** — this is more sensitive to changes in target brightness.
* **Cosine (spectral) distance (SMAD)** —  this is more sensitive to changes in target spectral response.
* **Bray Curtis dissimilarity (BCMAD)** —  this is more sensitive to the distribution of the observation values through time.

Each MAD provides information on different land cover change features; this is useful for classification. 

The mathematical derivation of the three MADs can be found in Roberts et al. (2018).

### More technical information ...

::::{dropdown} Euclidean MAD (EMAD)
The most logical place to start thinking about any of the MADs is the Euclidean MAD (EMAD). This is because EMAD comes from Euclidean distance, and Euclidean distance can be explained with a physical analogy: it is how we measure straight-line distances between points. In our three-dimensional world, it may look like this:

:::{figure} /_files/geomedian/cartesian_euclidean.JPG
:alt: Euclidean distance in three dimensions

Euclidean distance in three dimensions.
:::

In the case of satellite data, we are measuring the Euclidean distance between a pixel’s geomedian value and a single multispectral measurement. The number of dimensions is equal to the number of bands in the data. In the illustration below, $m$ is the geomedian value and $\\mathbf{x}$ the measured value. In real data, there will be multiple measurements over a time period, so $t$ is the timestep number, otherwise noted in equations as superscript ($t$).

For example, if we had three bands of data (red, green, and blue), and three timesteps of data, then we can calculate the Euclidean distances as follows:

:::{figure} /_files/geomedian/bands_euclidean.JPG
:alt: Euclidean distance in three dimensions over three timesteps.

Euclidean distance in three dimensions over three timesteps.
:::

Each timestep gives a separate Euclidean distance result. Then EMAD is the median of all those distances.

In most real life conditions, there will be more than three timesteps and more than three bands. A general expression of Euclidean distance for $p$ bands is given as:

$$
\begin{align*}
&\text{Multispectral Euclidean distance for timestep }t \\
=& \sqrt{ \left( x^{(t)}_{\text{band 1}} - m_{\text{band 1}} \right)^2 + \left( x^{(t)}_{\text{band 2}} - m_{\text{band 2}} \right)^2  + \dots  + \left( x^{(t)}_{\text{band p}} - m_{\text{band p}} \right)^2 }\\
=& \lVert \mathbf{x}^{(t)} - m \rVert_{\mathbb{R}^p}
\end{align*}
$$

Then EMAD for $N$ timesteps is given by [Roberts et al, 2018](https://ieeexplore.ieee.org/abstract/document/8518312), as the median of the Euclidean distances from all the timesteps.

$$
\begin{align*}
\text{EMAD} = \text{median} \left( \left\{ \lVert \mathbf{x}^{(t)} - \mathbf{m} \rVert_{\mathbb{R}^p}, t = 1, \dots , N \right\}  \right)
\end{align*}
$$

In GeoMAD, the MADs are calculated from the same ten bands used in the geomedian, therefore $p=10$. The result of $\lVert \mathbf{x}^{(t)} - \mathbf{m} \rVert_{\mathbb{R}^p}$ is a positive scalar, so $\text{EMAD}_\text{GeoMAD}$ is a positive scalar number. As in the geomedian, $N$ is dependent on the number of satellite flyovers particular to that pixel.

$$
\begin{align*}
\text{EMAD}_\text{GeoMAD} = \text{median} \left( \left\{ \lVert \mathbf{x}^{(t)} - \mathbf{m} \rVert_{\mathbb{R}^{10}}, t = 1, \dots , N \right\}  \right)
\end{align*}
$$

The maximum possible value for EMAD depends on the value ranges for each of the bands in the dataset. In the case of GeoMAD, which uses at maximum annual timescales of ten bands of Sentinel-2 data, valid EMAD values range from 0 to 31623.

EMAD is useful for showing albedo shifts in satellite spectra.

(Source: [Digital Earth Africa &mdash; GeoMAD cloud-free composites](https://docs.digitalearthafrica.org/en/latest/data_specs/GeoMAD_specs.html))
::::

::::{dropdown} Spectral MAD (SMAD)
The spectral MAD (SMAD) is based on the median absolute deviations in the cosine distance between the geomedian and individual measurements.

In two dimensions, cosine distance can be graphically compared to Euclidean distance by the following figure:

:::{figure} /_files/geomedian/cosine_distance.JPG
:alt: Relative relationships between Euclidean and cosine distances.

Relative relationships between Euclidean and cosine distances.
:::

In a general sense, cosine distance is related to the angle between the two points $\theta$, while Euclidean distance is related to the straight-line distance between the two points $d$. Like Euclidean distance, points are more similar when the cosine distance between them is small. The value of the cosine distance is smaller when $\theta$ is small (i.e. close to 0) or when $\theta$ is close to 180 degrees.

Notice we could have a small cosine distance but a large Euclidean distance; for example, if the angle between the vectors is small, but one is much longer than the other. This is an important property of cosine distance (and thus SMAD) &mdash; unlike Euclidean distance, cosine distance is not skewed by the magnitude of the measurements.

Cosine distance is defined more formally as:

$$
\begin{align*}
\text{Cosine distance (two dimensions)} = 1 - \frac{x_1 y_1 + x_2 y_2}{ \left( \sqrt{ \left( x_1\right) ^2 + \left( x_2\right) ^2 } \right) \left( \sqrt{ \left( y_1\right) ^2 + \left( y_2\right) ^2 } \right)}
\end{align*}
$$

For more than two dimensions, we can generalise the cosine distance formula for a single pixel. For a multispectral measurement of $p$ bands at timestep $t$, $\mathbf{x}^{(t)}$, and the geomedian at the same point $\mathbf{m}$, the cosine distance is:

$$
\begin{align*}\small
&\text{Multispectral cosdist}\left( \mathbf{x}^{(t)}, m \right) \text{ for timestep } t  \\
&= 1 - \frac{ \mathbf{x}^{(t)} \cdot \mathbf{m} }{ \lVert \mathbf{x}^{(t)} \rVert \ \lVert \mathbf{m} \rVert} \ \text{ for }  \mathbf{x}^{(t)}, \mathbf{m} \in \mathbb{R}_{p}\\
&=  1 - \left( \frac{\left( x_{\text{band 1}}^{(t)} \right) \left(m_{\text{band 1}} \right) + \left( x_{\text{band 2}}^{(t)} \right) \left(m_{\text{band 2}} \right) + \cdots + \left( x_{\text{band p}}^{(t)} \right) \left(m_{\text{band p}} \right)}{ \left(\sqrt{\left( x_{\text{band 1}}^{(t)} \right)^2 + \cdots+ \left( x_{\text{band p}}^{(t)} \right)^2} \right) \left( \sqrt{\left( m_{\text{band 1}} \right)^2 + \cdots+ \left( m_{\text{band p}} \right)^2 } \right)} \right)
\end{align*}
$$

Then for $N$ timesteps, SMAD is the median of the cosine distances.

$$
\begin{align*}
\text{SMAD} = \text{median} \left( \left\{ \text{cosdist}\left( \mathbf{x}^{(t)}, \mathbf{m} \right), t = 1, \dots , N \right\}  \right)
\end{align*}
$$

As with the other distances and dissimilarities used in the MADs, this results in a positive scalar value, thus SMAD is a positive scalar. Valid values for SMAD fall between 0 and 1.

In applications of Earth observation data, SMAD is useful for showing areas of land cover change. One reason is that SMAD is less affected by cloud; unlike EMAD, it is invariant to albedo changes, such as that caused by the diffusion of solar radiation. SMAD can also be used to track water bodies, as water has high variation in reflectance.

(Source: [Digital Earth Africa &mdash; GeoMAD cloud-free composites](https://docs.digitalearthafrica.org/en/latest/data_specs/GeoMAD_specs.html))
::::

::::{dropdown} Bray-Curtis MAD (BCMAD)
The Bray-Curtis MAD (BCMAD) is calculated from the Bray-Curtis dissimilarity. The Bray-Curtis dissimilarity emphasises differences in each band between the measurement and the geomedian.

For a single band of satellite data, the Bray-Curtis dissimilarity looks remarkably like a normalised band index. For example, if we only had red band data, it might look something like this:

$$
\begin{align*}
\text{Single-band Bray-Curtis dissimilarity at timestep }t = \frac{\left| x_{\text{red}}^{(t)} - m_{\text{red}}\right|}{ \left| x_{\text{red}}^{(t)} + m_{\text{red}} \right| } 
\end{align*}
$$

It can be generalised to a multispectral dataset with $p$ bands:

$$
\begin{align*}
&\text{Multispectral Bray-Curtis dissimilarity for timestep }t\\
&= \frac{\left| x_{\text{band 1}}^{(t)} - m_{\text{band 1}}\right| + \left| x_{\text{band 2}}^{(t)} - m_{\text{band 2}} \right| + \dots + \left| x_{\text{band p}}^{(t)} - m_{\text{band p}} \right| }{ \left| x_{\text{band 1}}^{(t)} + m_{\text{band 1}} \right| + \left| x_{\text{band 2}}^{(t)} + m_{\text{band 2}} \right| + \dots + \left| x_{\text{band p}}^{(t)} + m_{\text{band p}} \right|} 
\end{align*}
$$

The Bray-Curtis dissimilarity will be maximised at a value of 1 when the measurements in each band are completely different. Conversely, the value of the dissimilarity will be small where each band observation is similar to the geomedian of that band.

As with the other MADs, the BCMAD is found by taking the median of all the Bray-Curtis dissimilarities from $N$ timesteps. For GeoMAD, $p=10$.

$$
\begin{align*}
\text{BCMAD} = \text{median} \left( \left\{ \frac{\left| \mathbf{x}^{(t)} - \mathbf{m}  \right|_{\mathbb{R}^p}}{\left| \mathbf{x}^{(t)} + \mathbf{m}  \right| _{\mathbb{R}^p}}, t = 1, \dots , N \right\}  \right)
\end{align*}
$$

BCMAD takes on values from 0 to 1.

(Source: [Digital Earth Africa &mdash; GeoMAD cloud-free composites](https://docs.digitalearthafrica.org/en/latest/data_specs/GeoMAD_specs.html))
::::

## Lineage

:::{figure} /_files/geomedian/lineage.svg
:alt: Lineage diagram.

Landsat 5, 7, 8, and 9 Surface Reflectance includes NBART and Observational Attributes products. GeoMAD stands for Geometric Median and Median Absolute Deviation.
:::

The GeoMAD is derived from Landsat surface reflectance data. The data are masked for clouds and shadows to increase clarity. 

The three MAD layers of the GeoMAD are calculated by computing the multidimensional distance between each observation in a time series of multispectral (or higher dimensionality such as hyperspectral) satellite imagery versus the multidimensional median of the time series. The median used for this calculation is the geometric median corresponding to the time series. 

The GeoMAD is calculated over annual time periods on Earth observations from a single sensor by default (such as the annual time series of Landsat 8 observations); however, it is applicable to multi-sensor time series of any length that computing resources can support. 

For the purposes of the default DEA product, GeoMADs are computed per calendar year and per sensor (Landsat 5, Landsat 7, Landsat 8, and Landsat 9) from terrain-illumination-corrected surface reflectance data (Analysis Ready Data).

Note that the constituent pixels in the GeoMAD pixel composite mosaics are synthetic. This means that the pixels have not been physically observed by the satellite; rather, they are the computed high-dimensional medians of a time series of pixels. 

## References

Roberts, D., Mueller, N., & Mcintyre, A. (2017). High-dimensional pixel composites from earth observation time series. *IEEE Transactions on Geoscience and Remote Sensing*, *55*(11), 6254–6264. [https://doi.org/10.1109/TGRS.2017.2723896](https://doi.org/10.1109/TGRS.2017.2723896)

Roberts, D., Dunn, B., & Mueller, N. (2018). Open data cube products using high-dimensional statistics of time series. *IGARSS 2018 - 2018 IEEE International Geoscience and Remote Sensing Symposium*, 8647–8650. [https://doi.org/10.1109/IGARSS.2018.8518312](https://doi.org/10.1109/IGARSS.2018.8518312)

