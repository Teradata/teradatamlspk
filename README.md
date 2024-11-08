## Teradata Python package for running Spark workloads on Vantage.

teradatamlspk is a Python module to run PySpark workloads on Vantage with minimal changes to the Python script.  

For community support, please visit the [Teradata Community](https://support.teradata.com/community?id=community_forum&sys_id=14fe131e1bf7f304682ca8233a4bcb1d).

For Teradata customer support, please visit [Teradata Support](https://support.teradata.com/csm).

Copyright 2024, Teradata. All Rights Reserved.

### Table of Contents
* [Release Notes](#release-notes)
* [Installation and Requirements](#installation-and-requirements)
* [Using the Teradata Python Package](#using-the-teradata-Python-package)
* [Documentation](#documentation)
* [License](#license)

## Release Notes:
#### teradatamlspk 20.00.00.02
* ##### New Features/Functionality
  * ###### teradatamlspk DataFrameReader
    * `table()` - Returns the specified table as a DataFrame.
  * ###### teradatamlspk DataFrameWriterV2
    * `partitionedBy` - Partition the output table created by create, createOrReplace, or replace using the given columns or transforms.
    * `option` - Add an output option while writing a DataFrame to a data source.
    * `options` - Adds output options while writing a DataFrame to a data source.
  * ###### teradatamlspk global functions
    * `years` - Partition transform function: A transform for timestamps and dates to partition data into years.
    * `days` - Partition transform function: A transform for timestamps and dates to partition data into days.
    * `months` - Partition transform function: A transform for timestamps and dates to partition data into months.
    * `hours` - Partition transform function: A transform for timestamps and dates to partition data into hours.
    * `udf` - Creates a user defined function (UDF).
    * `conv` - Convert a number in a string column from one base to another.
    * `log` - Returns the first argument-based logarithm of the second argument.
    * `log2` - Returns the base-2 logarithm of the argument.
    * `date_from_unix_date` - Create date from the number of days since 1970-01-01.
    * `extract` - Extracts a part of the date/timestamp or interval source.
    * `datepart` - Extracts a part of the date/timestamp or interval source.
    * `date_part` - Extracts a part of the date/timestamp or interval source.
    * `make_dt_interval` - Make DayTimeIntervalType duration from days, hours, mins and secs.
    * `make_timestamp` - Create timestamp from years, months, days, hours, mins, secs and timezone fields.
    * `make_timestamp_ltz` - Create the current timestamp with local time zone from years, months, days, hours, mins, secs and timezone fields.
    * `make_timestamp_ntz` - Create local date-time from years, months, days, hours, mins, secs fields
    * `make_ym_interval` - Make year-month interval from years, months.
    * `make_date` - Returns a column with a date built from the year, month and day columns.
    * `from_unixtime` - Converts the number of seconds from unix epoch (1970-01-01 00:00:00 UTC) to a string representing the timestamp.
    * `unix_timestamp` - Convert time string with given pattern to unix epoch.
    * `to_unix_timestamp` - Convert time string with given pattern to unix epoch.
    * `to_timestamp` - Converts a string column to timestamp.
    * `to_timestamp_ltz` - Converts a string column to timestamp.
    * `to_timestamp_ntz` - Converts a string column to timestamp.
    * `from_utc_timestamp` - Converts column to utc timestamp from different timezone columns.
    * `to_utc_timestamp` - Converts column to given timestamp from utc timezone columns.
    * `timestamp_micros` - Creates timestamp from the number of microseconds since UTC epoch.
    * `timestamp_millis` - Creates timestamp from the number of milliseconds since UTC epoch.
    * `timestamp_seconds` - Converts the number of seconds from the Unix epoch to a timestamp
    * `unix_micros` - Returns the number of microseconds since 1970-01-01 00:00:00 UTC.
    * `unix_millis` - Returns the number of milliseconds since 1970-01-01 00:00:00 UTC. 
    * `unix_seconds` - Returns the number of seconds since 1970-01-01 00:00:00 UTC. 
    * `base64` - Computes the BASE64 encoding of a binary column and returns it as a string column.
    * `current_timezone` - Returns the current session local timezone.
    * `format_string` - Formats the arguments in printf-style and returns the result as a string column.
    * `elt` - Returns the n-th input, e.g., returns input2 when n is 2. The function returns NULL if the index exceeds the
              length of the array.
    * `to_varchar` - Convert col to a string based on the format.
    * `current_catalog` - Returns the current catalog. 
    * `equal_null` - Returns same result as the EQUAL(=) operator for non-null operands, but returns true 
                    if both are null, false if one of the them is null.
    * `version` - Returns the teradatamlspk version.
    * `parse_url` - Extracts a part from a URL.
    * `reverse` - Returns a reversed string with reverse order of elements.
    * `convert_timezone` - Converts the timestamp without time zone sourceTs from the sourceTz time zone to targetTz.
    * `call_udf` - Register a user defined function (UDF).
  * ###### teradatamlspk UDFRegistration
    * `register()` - Call a registered user defined function (UDF).
  * ###### teradatamlspk DataFrameColumn a.k.a. ColumnExpression
    * `eqNullSafe()` - Equality test that is safe for null values.
  * ###### teradatamlspk MLlib Functions
    * `RegexTokenizer()` - Extracts tokens based on the pattern.
  * ###### pyspark2teradataml
    * `pyspark2teradataml` utility accepts directory containing Pyspark scripts as input.
    * `pyspark2teradataml` utility accepts Pyspark notebook as input.
* ##### Updates
  * `spark.conf.set` - Supports set time zone to session.
  * `spark.conf.unset` - Supports unset time zone to previous time zone set by user.
  *  `DataFrame.select()`, `DataFrame.withColumn()`, `DataFrame.withColumns()` function now accept functions `like`, `ilike`, `isNull`,`isNotNull`, `contains`, `startswith`, `endswith`, `booleanexpressions`, `binaryexpressions` without `when` clause.
  * `DataFrameColumn.cast()` and `DataFrameColumn.astype()` function supports `TimestampNTZType`, `DayTimeIntervalType`, `YearMonthIntervalType`.
  * `DataFrame.createTempView()` and `DataFrame.createOrReplaceTempView()` now drops view at the end of session.
  * `DataFrame.agg()` and `GroupedData.agg()` function supports aggregate functions generated using arthimetic operators.
* ##### Bug Fixes
  * `DataFrame.withColumnRenamed()` and `DataFrame.withColumnsRenamed()` will work if columns are renamed with same name of a column that is already present irrespective of case.
  * `DataFrame.join()` now works smiliar to pyspark if column name or list of column names are passed to `on` clause.
  
#### teradatamlspk 20.00.00.01
* ##### New Features/Functionality
  * ###### teradatamlspk DataFrame
    * `write()` - Supports writing the DataFrame to local file system or to Vantage or to cloud storage.
    * `writeTo()` - Supports writing the DataFrame to a Vantage table.
    * `rdd` - Returns the same DataFrame.
  * ###### teradatamlspk DataFrameColumn a.k.a. ColumnExpression
    * `desc_nulls_first()` - Returns a sort expression based on the descending order of the given column name, and null values appear before non-null values.
    * `desc_nulls_last()` - Returns a sort expression based on the descending order of the given column name, and null values appear after non-null values.
    * `asc_nulls_first()` - Returns a sort expression based on the ascending order of the given column name, and null values appear before non-null values.
    * `asc_nulls_last()` - Returns a sort expression based on the ascending order of the given column name, and null values appear after non-null values.
* ##### Updates
  * `DataFrame.fillna()` and `DataFrame.na.fill()` now supports input arguments of the same data type or their types must be compatible. 
  * `DataFrame.agg()` and `GroupedData.agg()` function supports Column as input and '*' for 'count'.
  * `DataFrameColumn.cast()` and `DataFrameColumn.astype()` now accepts string literal which are case insensitive.
  * Optimised performance for `DataFrame.show()`  
  * Classification Summary, TrainingSummary object and MulticlassClassificationEvaluator now supports `weightedTruePositiveRate` and `weightedFalsePositiveRate` metric.
  * Arithmetic operations can be performed on window aggregates.
* ##### Bug Fixes
  * `DataFrame.head()` returns a list when n is 1.
  * `DataFrame.union()` and `DataFrame.unionAll()` now performs union of rows based on columns position.
  * `DataFrame.groupBy()` and `DataFrame.groupby()` now accepts columns as positional arguments as well, for example `df.groupBy("col1", "col2")`.
  * MLlib Functions attribute `numClasses` and `intercept` now return value.
  * Appropriate error is raised if invalid file is passed to `pyspark2teradataml`.
  * `when` function accepts Column also along with literal for `value` argument. 

#### teradatamlspk 20.0.0.0
* `teradatamlspk 20.0.0.0` is the initial release version. Please refer to the teradatamlspk User Guide for the available API's and their functionality.

## Installation and Requirements

### Package Requirements:
* Python 3.9 or later

Note: 32-bit Python is not supported.

### Minimum System Requirements:
* Windows 7 (64Bit) or later
* macOS 10.9 (64Bit) or later
* Red Hat 7 or later versions
* Ubuntu 16.04 or later versions
* CentOS 7 or later versions
* SLES 12 or later versions
* Teradata Vantage Advanced SQL Engine:
    * Advanced SQL Engine 16.20 Feature Update 1 or later

### Installation

Use pip to install the teradatamlspk for running PySpark workloads.

Platform       | Command
-------------- | ---
macOS/Linux    | `pip install teradatamlspk`
Windows        | `py -3 -m pip install teradatamlspk`

When upgrading to a new version, you may need to use pip install's `--no-cache-dir` option to force the download of the new version.

Platform       | Command
-------------- | ---
macOS/Linux    | `pip install --no-cache-dir -U teradatamlspk`
Windows        | `py -3 -m pip install --no-cache-dir -U teradatamlspk`

## Usage the `teradatamlspk` Package

`teradatamlspk` has a utility `pyspark2teradataml` which accepts either PySpark script or PySpark notebook or a directory which has PySpark scripts, analyzes and generates 2 files as below:
  1. HTML file - Created in the same directory where users PySpark script or notebook resides with name as `<your pyspark script name>_tdmlspk.html`. This file contains the script conversion report. Based on the report user can take the action on the generated scripts or notebooks.
      - A single HTML file for directory which has PySpark scripts will be created with name `<your directory name>_tdmlspk.html`.
  2. Python script/notebook - Created in the same directory where users PySpark script/notebook resides with name as `<your pyspark script name>_tdmlspk.py` for PySpark script or `<your pyspark script name>_tdmlspk.ipynb` for notebook, that can be run on Vantage.
      - Refer to the HTML report to understand the changes done and required to be done in the script/notebook.
    
### Example to demostrate the usage of utility `pyspark2teradataml`

```
>>> from teradatamlspk import pyspark2teradataml
>>> pyspark2teradataml('/tmp/pyspark_script.py')
Python script '/tmp/pyspark_script.py' converted to '/tmp/pyspark_script_tdmlspk.py' successfully.
Script conversion report '/tmp/pyspark_script_tdmlspk.html' published successfully. 

```

### Example to demostrate the `teradatamlspk` DataFrame creation.
```
>>> from teradatamlspk.sql import TeradataSession.
>>> spark = TeradataSession.builder.getOrCreate(host=host, user = user, password=password)
>>> df = spark.createDataFrame("test_classification")
>>> df.show()
+----------------------+---------------------+---------------------+----------------------+-------+
|         col1         |         col2        |         col3        |         col4         | label |
+----------------------+---------------------+---------------------+----------------------+-------+
| -1.1305820619922704  | -0.0202959251414216 | -0.7102336334648424 | -1.4409910829920618  |   0   |
| -0.28692000017174224 | -0.7169529842687833 | -0.9865850877151031 |  -0.848214734984639  |   0   |
| -2.5604297516143286  |  0.4022323367243113 | -1.1007419820939435 | -2.9595882598466674  |   0   |
|  0.4223414406917685  | -2.0391144030275625 |  -2.053215806414584 | -0.8491230457662061  |   0   |
|  0.7216694959200303  | -1.1215566442946217 | -0.8318398647044646 | 0.15074209659533433  |   0   |
| -0.9861325665504175  |  1.7105310292848412 |  1.3382818041204743 | -0.08534109029742933 |   1   |
| -0.5097927128625588  |  0.4926589443964751 |  0.2482067293662461 | -0.3095907315896897  |   1   |
| 0.18332468205821462  |  -0.774610353732039 |  -0.766054694735782 | -0.29366863291253276 |   0   |
| -0.4032571038523639  |  2.0061840569850093 |  2.0275124771199318 |  0.8508919440196763  |   1   |
| -0.07156025619387396 |  0.2295539000122874 | 0.21654344712218576 | 0.06527397921673575  |   1   |
+----------------------+---------------------+---------------------+----------------------+-------+
```

## Documentation

General product information, including installation instructions, is available in the [Teradata Documentation website](#)

## License

Use of the Teradata Spark Package is governed by the *License Agreement for teradatamlspk and pyspark2teradataml*. 
After installation, the `LICENSE` and `LICENSE-3RD-PARTY` files are located in the `teradatamlspk` directory of the Python installation directory.
