# Deploy feito em https://pcecilio.shinyapps.io/tlang_tp1/
if (!require('shiny')) install.packages('shiny')
library(shiny)

rm(list = ls())
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
#options(shiny.reactlog=TRUE)
runApp('app_tp1')
