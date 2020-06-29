## Accuracy, Precision, and Bias ##

https://cals.arizona.edu/classes/rnr613/accuracy.html#:~:text=Bias%20is%20a%20measure%20of,two%20different%20components%20of%20Accuracy.

> We consider both bias and precision with respect to how well an estimator performs over many, many samples of the same size.  
> The average of these multiple samples is called the expected value of the estimator. 

> Bias is a measure of how far the expected value of the estimate is from the true value of the parameter being estimated. 

> Precision is a measure of how similar the multiple estimates are to each other, not how close they are to the true value (which is bias). 

> Precision and bias are two different components of Accuracy.

Say, a person's true weight is 100lb (we may never know or we are able to find a super scale which provides the true weight). Suppose we have two different scales (A and B) and use them to weigh the person. Scale A reads 100.5 lb and scale B read 98.5 lb. We would say neither A or B is accurate. 

**Accuracy** indicates if the measured/observed reflects the true value.  Here we also say scale A is more accurate than scale B since the measured value by A is closer to the actual value than that by scale B.
 
If we use scale A to weigh the person multiple times, each time the measured weight is consistently equal to or close to 100.5 , then we say scale A has high **precision**. If the measred weight varies "a lot", then we say scale A has low precision. The precision itself can be measured/calculated using *sample variance, standard deviation, or range*. 

If the measured values are consistently higher that the actual value, then we say the scale **over-estimates** the person's weight. If the measured values are consistently lower than the actual value, then we say the scale **under-estimates** the person's weight. The over-estimation and under-estimation are refered to as 
**bias**. Bias can be measured using *sample mean or median*. 
