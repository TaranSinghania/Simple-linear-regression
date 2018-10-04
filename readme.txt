AN INTRODUCTION TO MACHINE LEARNING USING SIMPLE LINEAR REGRESSION


DATASET USED- CARBON DIOXIDE LEVELS RECORDED FROM 1958-2017.

The model used for this assignment tries to establish a linear relationship between the levels of carbon dioxide and the decimal dates.
 I)  The Zip Archive cotains the following-
        1.Python programs for -
          a)Splitting and exporting main dataset.
          b)Evaluation of coefficients, rmse and r^2 values, and also for plotting the resulting graph.  
        2. Datasets used.
        3. Programs in .txt format.

ll) Path taken to evaluate the model-
        1. Filtering out the null values from dataset to avoid NaN error.
        2. Importing the packages and the dataset.
        3. Splitting the dataset into training and testing datasets.
        4. Finding slope parameter and intercept [b1 and b0] using the training dataset.
        5. Using b1 and b0 to find the RMSE value on test dataset.
        6. RMSE value obtained here was 3.211.
        7. Verifying that the variables used were suitable by finding the R^2 value. Value obtained=0.985, signfying the model explains variance well and implying that the                model used is good.
        8. Using matplotlib to plot the relationship and scatterplot.(on test dataset)
        9. Using graph we can predict the CO2 levels.

lll) For conversion from date to decimal date-
       Attached here, are links for understanding conversion of dates to decimal dates and for converting them too(Microsoft Excel can also be used)-
          1. https://math.stackexchange.com/questions/1111207/converting-decimal-dates-to-calendar-dates
          2. http://sopac.ucsd.edu/convertDate.shtml
          3. https://stackoverflow.com/questions/6451655/python-how-to-convert-datetime-dates-to-decimal-years

lV) Sources-
        1. https://stackoverflow.com/
        2. https://github.com/
        3. http://machinelearningmastery.com/  
        4. https://mubaris.com/
        5. https://www.geeksforgeeks.org/ 
-----------------------------------------------------------------------------------xxx-THE END-xxx-----------------------------------------------------------------------------------------------