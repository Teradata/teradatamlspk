## Examples showcasing capabilities of pyspark2teradataml utility of teradatamlspk Python package.

teradatamlspk is a Python package that offers a utility function ‘pyspark2teradataml’ that enables conversion of PySpark scripts or notebooks to teradatamlspk scripts or notebooks that runs on Vantage ClearScape Analytics with minimal changes.
teradatamlspk has the capability to convert either a PySpark script or PySpark notebook or a directory which has PySpark scripts which are shown in examples. 

For community support, please visit the [Teradata Community](https://support.teradata.com/community?id=community_forum&sys_id=14fe131e1bf7f304682ca8233a4bcb1d).

For Teradata customer support, please visit [Teradata Support](https://support.teradata.com/csm).

Copyright 2024, Teradata. All Rights Reserved.

## Following examples in the folder are provided:

#### Script_conversion_with_pyspark2teradataml - contains Script conversion example
  * cal_housing.csv - Input data file.
  * Predicting_House_Prices_Pyspark.py - Input PySpark script.
  * Predicting_House_Prices_Pyspark_tdmlspk.html - HTML report generated from pyspark2teradataml utility.
  * Predicting_House_Prices_Pyspark_tdmlspk.py - Python script generated from pyspark2teradataml utility.
  * Updated_Predicting_House_Prices_Pyspark_tdmlspk.py - Modified script which is used to run on Vantage. 

#### Directory_conversion_with_pyspark2teradataml - contains Directory conversion example for directory which has PySpark scripts
  * Pyspark_scripts - Directory that contains Pyspark scripts.
      * cal_housing.csv - Input data file.
      * Predicting_House_Prices_Pyspark.py - Input PySpark script.
      * Spark_Session_PySpark.py - Input PySpark script but contains syntax error.
      * Predicting_House_Prices_Pyspark_tdmlspk.py - Python script generated from pyspark2teradataml utility.
      * Spark_Session_PySpark_tdmlspk - HTML report generated from pyspark2teradataml utility for PySpark script containing syntax error.
      * Updated_Predicting_House_Prices_Pyspark_tdmlspk.py - Modified script which is used to run on Vantage. 
  * Pyspark_scripts_tdmlspk - HTML report generated from pyspark2teradataml utility.

#### Notebook_conversion_with_pyspark2teradataml - contains Notebook conversion example
  * cal_housing.csv - Input data file.
  * Predicting_House_Prices_Pyspark.ipynb - Input PySpark notebook.
  * Predicting_House_Prices_Pyspark_tdmlspk.html - HTML report generated from pyspark2teradataml utility.
  * Predicting_House_Prices_Pyspark_tdmlspk.ipynb - Python notebook generated from pyspark2teradataml utility.
  * Updated_Predicting_House_Prices_Pyspark_tdmlspk.ipynb - Modified notebook which is used to run on Vantage. 

## Documentation

General product information, including installation instructions, is available in the [Teradata Documentation website](https://docs.teradata.com/r/Enterprise_IntelliFlex_VMware/Teradata-pyspark2teradataml-User-Guide)

## License

Use of the Teradata Spark Package is governed by the *License Agreement for teradatamlspk and pyspark2teradataml*. 
After installation, the `LICENSE` and `LICENSE-3RD-PARTY` files are located in the `teradatamlspk` directory of the Python installation directory.