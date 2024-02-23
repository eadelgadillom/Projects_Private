install.packages("googletraffic")

devtools::install_github("dime-worldbank/googletraffic")

library(googletraffic)
library(ggplot2)
library(dplyr)
library(raster)

google_key <- "AIzaSyD_y-XJaFgPWp6PMGql7l_myAYOakW_Hv0"

r <- gt_make_raster(
    location = c(10.96854, -74.78132),
    height = 2000,
    width = 2000,
    zoom = 16,
    google_key = google_key
)
r
location()
location
height
gt_make_raster(
    location = c(10.96854, -74.78132),
    height = 2000,
    width = 2000,
    zoom = 16,
    google_key = google_key
)
location = c(10.96854, -74.78132)
height = 2000
width = 2000
zoom = 16
google_key = google_key
gt_make_png()
r <- gt_make_raster)
