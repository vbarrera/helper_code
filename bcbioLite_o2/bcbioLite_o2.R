
# Check if bcbioLite is installed. If not, install it with all upgrades.
if("remotes" %in% rownames(installed.packages())){
  library(remotes)
} else{
  install.packages("remotes")
  library(remotes)
}

if("bcbioLite" %in% rownames(installed.packages())){
  library(bcbioLite)
} else{
  remotes::install_github("vbarrera/bcbioLite", upgrade = "always")
  library(bcbioLite)
}

project_dir <- commandArgs(trailingOnly=T)[1]
output_dir <- commandArgs(trailingOnly=T)[1]
output_dir <- normalizePath(output_dir)

invisible(mapply(
  FUN = dir.create,
  list(output_dir),
  MoreArgs = list(recursive = TRUE, showWarnings = FALSE)
))

se <- bcbioLite::bcbreader(project_dir)

saveRDS(se, file = file.path(output_dir, paste0("se-",Sys.Date(),".rds")))