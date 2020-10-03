# least-square-method
A simple simulation of Least Squares Method which I believe inspired modern day optimization methods in machine/deep learning.

Based on the book:
</br>[1] Avedyan, Eduard. Learning Systems. London: Springer, 1995.

<p align="center">
  <img src="https://github.com/AsyrafAzlan/least-square-method/blob/main/lsm-formula.PNG">
</p>

In this simulation, the program is trying to optimize 5 targeted weights with the values:
</br>0.2, 0.3, 0.4, 0.5, 0.6
</br>0.2 is  later changed to 0.2sin(2\*pi\*f)for illustration purposes.

This simulation also explores the effect of forgetting factor.
Forgetting factor, *q* is used because old information regarding estimation has less significance than new information when calculating the estimates of the system parameters.  It gives the algorithm a tracking capability. 0 < *q* < 1

![ScreenShot](https://github.com/AsyrafAzlan/least-square-method/blob/main/lsm-output1.PNG)


![ScreenShot](https://github.com/AsyrafAzlan/least-square-method/blob/main/lsm-output2.PNG)


![ScreenShot](https://github.com/AsyrafAzlan/least-square-method/blob/main/lsm-output3.PNG)


![ScreenShot](https://github.com/AsyrafAzlan/least-square-method/blob/main/lsm-output4.PNG)
