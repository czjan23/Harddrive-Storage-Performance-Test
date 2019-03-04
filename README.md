# CSCE 678 Midterm Project
This repository is created for CSCE 678 Midterm Project. In this project, we focus on testing the writing & reading performance of 3 different cloud platforms - Microsoft Azure, AWS (EC2), Google Cloud Platform. 

## How to Run the Code
** Note: This program is developed with Python 3 in Linux environment.**

We accept 3 ways of running the test code:

<b>First</b>, you can simply run the default test by using the following command:

```
python storage_test.py
```

The program will run default test to write and read different file sizes. Each test result of writing speed and reading speed will be printed and the average speed will be shown as well in the final part.

<b>Second</b>, you can run the code with self-defined file sizes by following the following format:

```
python storage_test.py [file_size_number] [file_size_unit]
Example:
python storage_test.py 10 kb
```
This will trigger the test running with your specified file size. Both this method and the first method will only test once for each file size. 

<i>(Note: In our test, due to memory limitiatons, we have found AWS cannot handle write/read a file size of 1GB and Google Cloud Platform cannot deal with 2GB. Therefore, testing with larger files on these two platforms will lead to MemoryError or process being killed.)</i>

<b>Third</b>, you can run a file size for several iterations as many as you specified in the third argument:

```
python storage_test.py [file_size_number] [file_size_unit] [iteration_times]
Example:
python storage_test.py 10 kb 20
```
The above command will run the test for writing and reading a 10KB file 20 times. After the test finishes, mean, standard deviation, confident interval will be output for statistical use. 

## Implementation Method
In progress.

## Test Result

In this part, each test was run 20 times to collect two lists of writing speeds and reading speeds. From the lists, mean and standard variant were calculated. The test result of 3 cloud platforms are listed below. The file size we used were 1KB, 128KB, 256KB, 512KB, 1MB, 128MB, 256MB, 512MB. The reason for testing with different file sizes is to see how the performances change when the input file size increases.

### Microsoft Azure
| File size     | Mean of Writing Speed(byts/ms) | Mean of Reading Speed(byts/ms) | Confident Interval of Writing Speed(byts/ms) | Confident Interval of Reading Speed(byts/ms) |
| ------------- |:---------------------:| ---------------------:| -------------------------:| -----------------------------------:|
| 1KB           | 89.25 |  148676.55 | 89.25 +- 11.50 | 148676.55 +- 9952.61 | 
| 128KB         | 8242.77 | 4447949.25 | 8242.77 +- 841.76 | 4447949.25 +- 596143.12 |
| 256KB         | 14192.73 | 4837146.95 | 14192.73 +- 1676.44 | 4837146.95 +- 521044.48 |
| 512KB         | 22065.84 | 3876683.25 | 22065.84 +- 2283.16 | 4659265.17 +- 557134.27 |
| 1MB           | 31578.84 | 2142815.16 | 31578.84 +- 2469.03 | 3876683.25 +- 252671.60 |
| 128MB         | 104391.91 | 2729596.06 | 104391.91 +- 12877.35 | 2729596.06 +- 27581.31 |
| 256MB         | 96246.50 | 2574846.12 | 96246.50 +- 8728.29 | 2574846.12 +- 113126.31 |
| 512MB         | 94636.50 | 2392955.11 | 94636.50 +- 7959.86 | 2392955.11 +- 80651.24 |

---
### AWS EC2
| File size     | Mean of Writing Speed(byts/ms) | Mean of Reading Speed(byts/ms) | Confident Interval of Writing Speed(byts/ms) | Confident Interval of Reading Speed(byts/ms) |
| ------------- |:---------------------:| ---------------------:| -------------------------:| -----------------------------------:|
| 1KB           | 570.34  |  258596.73 | 570.34 +- 11.98 | 258596.73 +- 16686.27 | 
| 128KB         | 48525.97  | 8354828.74  | 48525.97 +- 932.68| 8354828.74 +- 489226.22 |
| 256KB         | 86767.82  | 8426935.64 | 86767.82 +- 1627.63 | 8426935.64 +- 765279.19 |
| 512KB         | 142221.96 | 9390529.41 | 142221.96 +- 1848.20 | 9390529.41 +- 772808.56 |
| 1MB           | 206290.47 | 9695203.59 | 206290.47 +- 8069.26 | 9695203.59 +- 831337.86 |
| 128MB         | 104956.20 | 1695898.81 | 104956.20 +- 1135.98 | 1695898.81 +- 6118.87 |
| 256MB         | 83016.06 | 1691595.90 | 83016.06 +- 6.67 | 1691595.90 +- 8854.06 |
| 512MB         | 72412.33 | 226373.14 | 72412.33 +- 2.13 | 226373.14 +- 14417.05 |

---
### Google Cloud Platform

| File size     | Mean of Writing Speed(byts/ms) | Mean of Reading Speed(byts/ms) | Confident Interval of Writing Speed(byts/ms) | Confident Interval of Reading Speed(byts/ms) |
| ------------- |:---------------------:| ---------------------:| -------------------------:| -----------------------------------:|
| 1KB           | 225.46   |  75407.66  |  225.46 +- 19.35    |   75407.66 +- 5420.52   | 
| 128KB         | 19343.65 | 1824200.55 | 19343.65 +- 1624.12 | 1824200.55 +- 119796.68 |
| 256KB         | 25077.60 | 2557286.42 | 25077.60 +- 4160.51 | 2557286.42 +- 140043.40 |
| 512KB         | 24989.17 | 2303295.95 | 24989.17 +- 5409.01 | 2303295.95 +- 150111.19 |
| 1MB           | 24128.69 | 2142815.16 | 24128.69 +- 6173.23 | 2142815.16 +- 105058.95 |
| 128MB         | 18565.70 | 1373328.15 | 18565.70 +- 24.70   | 1373328.15 +- 45172.09  |
| 256MB         | 18653.27 | 1333100.02 | 18653.27 +- 9.81    | 1333100.02 +- 38966.68  |
| 512MB         | 18685.80 | 459160.77 | 18685.80 +- 8.46 | 459160.77 +- 46548.56 |
---

## Graph and Analysis
In progress.