# [PY-02] NumPy and Pandas

## NumPy arrays

In mathematics, a **vector** is a sequence of numbers, and a **matrix** is a rectangular arrangement of numbers. Operations with vectors and matrices are the subject of a branch of mathematics called linear algebra. In Python (and in many other languages), vectors are called one-dimensional (1D) **arrays**, while matrices are called two-dimensional (2D) arrays. Arrays of more than two dimensions can be managed in Python without pain.

Python arrays are not necessarily numeric. Indeed, vectors of dates and strings appear frequently in data science. In principle, all the terms of an ordinary array must have the same type, so the array itself can have a type, though you can relax this constraint using mixed types (not used in this course). Arrays were already implemented in plain Python, but the functionality of the Python arrays was enlarged in **NumPy**, intended to be the fundamental library for scientific computing in Python.

The usual way to import NumPy is:

```
In [1]: import numpy as np
```

A 1D array can be created from a list with the NumPy function `array()`. If the items of the list have different type, they are converted to a common type when creating the array. A simple example follows.

```
In [2]: arr1 = np.array([2, 7, 14, 5, 9])
   ...: arr1
Out[2]: array([ 2,  7, 14,  5,  9])
```

A 2D array can be directly created from a list of lists of equal length. The terms are entered row-by-row:

```
In [3]: arr2 = np.array([[0, 7, 2, 3], [3, 9, -5, 1]])
   ...: arr2
Out[3]:
array([[ 0,  7,  2,  3],
       [ 3,  9, -5,  1]])
```

Although we visualize a vector as a column (or as a row) and a matrix as a rectangular arrangement, with rows and columns, it is not so in the computer. The 1D array is just a sequence of elements of the same type, neither horizontal nor vertical. It has one **axis**, which is the 0-axis.

In a similar way, a 2D array is a sequence of 1D arrays of the same length and type. It has two axes. When we visualize it as rows and columns, `axis=0` means *across rows*, while `axis=1` means *across columns*.

The number of terms stored along an axis is the **dimension** of that axis. The dimensions are collected in the attribute `.shape`.

```
In [4]: arr1.shape
Out[4]: (5,)
```

```
In [5]: arr2.shape
Out[5]: (2, 4)
```

## NumPy functions

NumPy incorporates vectorized forms of the **mathematical functions** of the package `math`. A **vectorized function** is one that, when applied to an array, returns an array with the same shape, whose terms are the values of the function on the corresponding terms of the original array.

For instance, NumPy the square root function `sqrt()` takes the square root of every term of a numeric array:

```
In [6]: np.sqrt(arr1)
Out[6]: array([1.41421356, 2.64575131, 3.74165739, 2.23606798, 3.        ])
```

The functions that are defined in terms of vectorized functions are automatically vectorized. For instance:

```
In [7]: def f(t): return 1/(1 + np.exp(t))
   ...: f(arr2)
Out[7]:
array([[5.00000000e-01, 9.11051194e-04, 1.19202922e-01, 4.74258732e-02],
       [4.74258732e-02, 1.23394576e-04, 9.93307149e-01, 2.68941421e-01]])
```
NumPy also provides common **statistical functions**, such as `mean()`, `max()`, `sum()`, etc.

## Subsetting arrays

**Subsetting** a 1D array is done as for a list:

```
In [8]: arr1[:3]
Out[8]: array([ 2,  7, 14])
```

The same applies to 2D arrays, but we need two indexes within the square brackets. The first index selects the rows (`axis=0`), and the second index the columns (`axis=1`):

```
In [9]: arr2[:1, 1:]
Out[9]: array([[7, 2, 3]])
```

When an expression involving an array is evaluated by the Python kernel, a Boolean array with the same shape is returned:

```
In [10]: arr1 > 3
Out[10]: array([False,  True,  True,  True,  True])
```

```
In [11]: arr2 > 2
Out[11]:
array([[False,  True, False,  True],
       [ True,  True, False, False]])
```

A subarray can be extracted by means of an expression. The expression is evaluated, returning a Boolean array called **Boolean mask**. The terms for which the mask is true are selected:

```
In [12]: arr1[arr1 > 3]
Out[12]: array([ 7, 14,  5,  9])
```

Note that this is the same as

```
In [13]: arr1[[False,  True,  True,  True,  True]]
Out[13]: array([ 7, 14,  5,  9])
```

Boolean masks can also be used to filter out rows or columns of a 2D array. 

## The package Pandas

**Pandas** provides a wide range of data wrangling tools. It is typically imported as

```
In [14]: import pandas as pd
```

Pandas provides two data container types, the series (one-dimensional) and the data frames (two-dimensional). A **series** can be understood as the combination of a 1D array containing the **values** and a list containing the names of the values, called the **index**. These components can be extracted as the attributes `.values` and `.index`.

A **data frame** can be seen as formed by one or several series with the same index (hence, with the same length). It can also be seen as a table for which the index provides the row names. In a Pandas data frame, each column has its own data type. The numeric types work as usual, but Pandas uses the data type `object` for many things, in particular for strings.

## Pandas series

Although we rarely do it in data science, where the data are imported from external data files, a Pandas series can be created directly, for instance from an array, with the Pandas function `Series()`:

```
In [15]: s1 = pd.Series(arr1)
    ...: s1
Out[15]:
0     2
1     7
2    14
3     5
4     9
dtype: int64
```

Now, the values of the series are extracted as:

```
In [16]: s1.values
Out[16]: array([ 2,  7, 14,  5,  9])
```

As shown above, when a series is printed, the index appears on the left. Since the index of `s1` has not been specified, a range of consecutive integers has been assigned as the index.

```
In [17]: s1.index
Out[17]: RangeIndex(start=0, stop=5, step=1)
```

Instead of an array, a list can be used to provide the values of a series. In the list, the items can have different type, but Pandas converts them to a common type, as shown in the following example. Here, instead of letting the Python kernel to create an index automatically, as a `RangeIndex`, we specify an index directly:

```
In [18]: s2 = pd.Series([1, 5, 'Messi'], index = ['a', 'b', 'c'])
    ...: s2
Out[18]:
a        1
b        5
c    Messi
dtype: object
```

Now the index is a plain `Index`:

```
In [19]: s2.index
Out[19]: Index(['a', 'b', 'c'], dtype='object')
```

Indexes are useful for combining, filtering and joining data sets. There are many types of indexes, which allow for specific operations. So, do not look at the index as an embarrassment, which is what it seems at first sight, but as a tool for data management.

## Pandas data frames

A Pandas **data frame** can be seen as a collection of series with the same index (hence, with the same length). Data frames can be built in many ways with the Pandas function `DataFrame()`, for instance from a dictionary of vector-like objects of the same length, as in

```
In [20]: df = pd.DataFrame({'v1': range(5),
    ...:     'v2': ['a', 'b', 'c', 'd', 'e'],
    ...:     'v3': np.repeat(-1.3, 5)})
    ...: df
Out[20]:
   v1 v2   v3
0   0  a -1.3
1   1  b -1.3
2   2  c -1.3
3   3  d -1.3
4   4  e -1.3
```

As the series, the data frames have the attributes `.values` and `.index`:

```
In [21]: df.values
Out[21]:
array([[0, 'a', -1.3],
       [1, 'b', -1.3],
       [2, 'c', -1.3],
       [3, 'd', -1.3],
       [4, 'e', -1.3]], dtype=object)
```

```
In [22]: df.index
Out[22]: RangeIndex(start=0, stop=5, step=1)
```

Without a explicit specification, the index is automatically created as a `RangeIndex`. In this example, since the columns have different data types, `df.values` takes type `object`. The third component of the data frame is a list with the column names, which can be extracted as the attribute `.columns`:

```
In [23]: df.columns
Out[23]: Index(['v1', 'v2', 'v3'], dtype='object')
```

A data frame has the same shape of the array of values. Having rows and columns, a data frame looks like a 2D array with row and column names. Indeed, we can also create data frames in this way:

```
In [24]: pd.DataFrame(arr2)
Out[24]:
   0  1  2  3
0  0  7  2  3
1  3  9 -5  1
```

But not all data frames are so simple. While a NumPy 2D array has a data type, in a Pandas data frame every column has its own data type.

Data frames can also be extracted from a data source (local or remote), such as a CSV file, an Excel sheet, or a table from a relational database. As for the series, a range index is automatically created unless an alternative specification is provided. The same is true for column names, so, in the above example, `df.columns` returns a range of integers. It is recommended to choose a column name suggesting the content of the column.

## Exploring Pandas objects

The methods `.head()` and `.tail()` extract the first and the last rows of a data frame, respectively. The default number of rows extracted is 5, but you can pass a custom number.

```
In [25]: df.head(2)
Out[25]:
   v1 v2   v3
0   0  a -1.3
1   1  b -1.3
```

The content of a data frame can also be explored with the method `.info()`. It reports the dimensions, the data type and the number of non-missing values of every column of the data frame. Note that the data type of the second column, for which you would have expected `str`, is reported as `object`. Don't worry about this, you can apply the string methods to this column, as will be seen later in this course.

```
In [26]: df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   v1      5 non-null      int64  
 1   v2      5 non-null      object
 2   v3      5 non-null      float64
dtypes: float64(1), int64(1), object(1)
memory usage: 248.0+ bytes
```

The method `.describe()` extracts a conventional statistical summary of a Pandas object. The columns of type `object` are omitted, except when all the columns have that type. Then the report contains only counts. 

```
In [27]: df.describe()
Out[27]:
             v1   v3
count  5.000000  5.0
mean   2.000000 -1.3
std    1.581139  0.0
min    0.000000 -1.3
25%    1.000000 -1.3
50%    2.000000 -1.3
75%    3.000000 -1.3
max    4.000000 -1.3
```

## Subsetting data frames

Pandas offers multiple ways for subsetting data frames. First, you can extract a column, as a series:

```
In [28]: df['v2']
Out[28]:
0    a
1    b
2    c
3    d
4    e
Name: v2, dtype: object
```

Note that the syntax is the same as for extracting the value of a key from a dictionary (not by chance). You can also extract a **data subaframe** containing a subset of complete columns from a data frame. You can specify this with a list containing the names of those columns:

```
In [29]: df[['v1', 'v2']]
Out[29]:
   v1 v2
0   0  a
1   1  b
2   2  c
3   3  d
4   4  e
```

*Note*. You can extract a subframe with a single column. Beware that this is not the same as a series. `df['v2']`is a series with shape `(5,)`, and `df[['v2']]` is a data frame with shape `(5,1)`.

In data science, rows are typically filtered by expressions. Example:

```
In [30]: df[df['v1'] > 2]
Out[30]:
   v1 v2   v3
3   3  d -1.3
4   4  e -1.3
```

Combining a row filter and a column selection:

```
In [31]: df[df['v1'] > 2][['v1', 'v2']]
Out[31]:
   v1 v2
3   3  d
4   4  e
```

Besides this, there are two additional ways to carry out a selection, specifying rows and columns in one shot:

* **Selection by label** is specified by adding `.loc` after the name of the data frame. The selection of the rows is based on the index, and that of the columns is based on the column names.

* **Selection by position** uses `.iloc`. The selection of the rows is based on the row number and that of the columns on the column number.

In both cases, if you enter a single specification inside the brackets, it refers to the rows. If you enter two specifications, the first one refers to the rows and the second one to the columns.

## Importing data from CSV files

Data sets in tabular form can be imported as Pandas data frames from many file formats. In particular, data from a CSV file can be imported to a data frame with the Pandas function `read_csv`(). The (default) syntax is `dfname = pd.read_csv(fname)`. The data frame name is chosen by the user, and the file name has to contain the **path** of that file (either local or remote). `read_csv()` works the same way for CSV files and for **zipped ZIP files**.

Although defaults work in most cases satisfactorily, it is worth to comment a few things about some optional arguments of `read_csv()`. The list is not complete, but enough to give you an idea of the extent to which you can customize this function.

* The parameter `sep` specifies the column separator. The default is `sep=','`, but CSV files created with Excel may need `sep=';'`.

* The parameters `header` and `names` specify the row where the data to be imported start and the column names, respectively. The default is `header=0, names=None`, which makes Pandas start reading from the first row and take it as the column names. When the data come without names, you can use `header=None, names=namelist` to provide a list of names. With a positive value for `header`, you can skip some rows.

* The parameter `index_col` specifies a column that you wish to use as the index, if that is the case. The default is `index_col=None`. If the intended index comes in the first column, as it frequently happens, you will use `index_col=0`.

* The parameter `usecols` specifies the columns to be read. You can specify them in a list, either by name or by position. The default is `usecols=None`, which means that you wish to read all the columns.

* The parameter `dtype` specifies the data types of the columns of the data frame. This saves time with big data sets. The default is `dtype=None`, which means that Python will guess the data type, based on what it reads. When all the entries in a column are numbers, that column is imported as numeric. If there is, at least, one entry that is not numeric, all the entries are read as strings, and the data type `object` is assigned to that column.

* If the string data contained in a CSV file can contain special characters (such as ñ, or á), which can make trouble, you may need to control the parameter `encoding`. The default is `encoding='utf-8'`. So, if you are reading a CSV file created in Excel, you may need to set `encoding='latin'` to read the special characters in the right way.

## Plotting with Matplotlib

Matplotlib has an impressive range of graphical methods, including image processing. As many other libraries in the Python world, Matplotlib has several API's, which confounds the beginners. In this context, an application programmers interface (API) is like an idiom that you speak to call the functions of the library. It defines the kinds of requests that can be made and how to make them. 

Matplotlib offers you a choice between two API's, the pyplot API, used in this course, and the object-oriented API. This course uses the pyplot API. Beware that, if you use Google or similar ways to find information about plotting in Matplotlib, the solutions found can come in any of the two API's. So Matplotlib may look more difficult than it really is.

The subpackage `matplotlib.pyplot` is a collection of command style functions that make Matplotlib work like MATLAB. It is typically imported as:

```
In [32]: import matplotlib.pyplot as plt
```

Each `pyplot` function makes some change to a figure, such as changing the default size, adding a title, plotting lines, decorating the plot with labels, etc. This is illustrated by the following example. We plot here three curves together, a linear, a quadratic and a cubic curve. First, we fill a 1D array with linearly spaced values, tightly close, so I can create a smooth curve.

```
In [33]: t = np.linspace(0, 2, 100)
```

Next, I ask for the plot:

```
In [34]: plt.figure(figsize=(5,5))
    ...: plt.title('Figure. Three curves')
    ...: plt.plot(t, t, label='linear', color='black')
    ...: plt.plot(t, t**2, label='quadratic', color='black', linestyle='dashed')
    ...: plt.plot(t, t**3, label='cubic', color='black', linestyle='dotted')
    ...: plt.legend();
```

![](https://github.com/mikecinnamon/PythonRefresher/blob/main/Figure/figure.png)

Take care of running these lines of code together. The semicolon in the last line stops the Python output showing up. That output would correspond to plt.legend and would not say much to you. 

`figure()` allows to change some default specifications. Here, we have changed the size. If you are satisfied with the default size `figsize=(6,4)`, you do not need this line of code. Here, `figsize=(5,5)` has been set so that the figure looks fine on the screen. The units for the width and height and are inches.

`plot()` creates a line chart (which can be turned into a scatter plot, although it is better to use `scatter()` for that). If two vectors are entered, the first one is taken as $x$ (horizontal axis) and the second one as $y$ (vertical axis). If there is only one vector, it is taken as $y$, and the index is used as $x$. Here, we get a multiple line chart by calling `plot()` multiple times. Note that, even if you see the three components plotted here as three curves, they are really line plots without markers.

`plot()` admits other arguments, allowing a minute edition of your visualization, down to the smallest detail. As a default, it uses solid lines, with different colors for the different lines. The line style has been specified by the argument linestyle, and the color by the argument color. The default for the first line is `color='blue'`.

