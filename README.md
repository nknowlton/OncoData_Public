# OncoData
Preprocessing scripts to convert Dicoms to PNGs and extract relevant metadata.

# Introduction
This repo contains data preprocessing scripts for our Mammography projects.
For details on model development, see [OncoNet](https://github.com/yala/OncoNet_Public).
To use the models, see [OncoServe](https://github.com/yala/OncoServe_Public).

## Requirements
Required python pip packages are listed in `requirements.txt`. All required pip packages and command line tools can be installed by running `./requirements.sh`.

## DICOM to PNG conversion
DICOMs can be converted to PNGs using the script `dicom_to_png.py` located in the `scripts/dicom_to_png` folder. Conversion can use either the [dcmj2pnm](support.dcmtk.org/docs/dcmj2pnm.html) tool from the [dcmtk](http://dicom.offis.de/dcmtk.php.en) package or the Matlab [dicomread](https://www.mathworks.com/help/images/ref/dicomread.html) tool.

## DICOM metadata extraction
DICOM header metadata can be extracted using the scripts in the `scripts/dicom_metadata` folder. Use `dicom_metadata_to_json.py` to save metadata as JSON. The resulting JSON files can be summarized with `summarize.py` and visualized with `plot.py`.

## Parallel directory copying
A directory can be copied in parallel using `copy_dir_parallel.py` in the `scripts/utils` folder.
