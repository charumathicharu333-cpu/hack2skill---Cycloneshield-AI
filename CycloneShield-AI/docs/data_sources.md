# Data Sources and Provenance

The shipped application uses only project sample data and labels it `DEMO`. No external source is queried by default.

Potential adapters for a future validated build:

- NOAA National Hurricane Center: https://www.nhc.noaa.gov/ - official US products for supported basins; follow product and reuse terms.
- IBTrACS historical best tracks: https://www.ncei.noaa.gov/products/international-best-track-archive - historical research dataset, not a live warning feed.
- India Meteorological Department: https://mausam.imd.gov.in/ - official Indian meteorological guidance; access and reuse conditions must be checked before integration.
- OpenStreetMap: https://www.openstreetmap.org/ - geographic context under the ODbL; do not infer shelter availability from map geometry.
- NASA Earthdata: https://www.earthdata.nasa.gov/ - potential environmental data source; credentials and product-specific terms may apply.

Fields used by the demo are cyclone position, wind, pressure, movement, regional coordinates, elevation proxy, coastal exposure proxy, rainfall exposure proxy, and population exposure proxy. The demo values are not retrieved from those sources and must not be represented as live data.
