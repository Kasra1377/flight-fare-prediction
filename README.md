# ✈flight-fare-prediction
---
![alt text](img/interface.PNG)

**Link** : https://flight-fare-pred-application.herokuapp.com/home

### 📄Description
---
In this project our aim is to predict the `flight price` , the `duration` and the `travel time` using machine learning models. The user has to input the name of the city(`source`) that they want to depart from and the destination.In addition to that, user has to enter their `airline name` which is very important , their `departure time` and `departure date` and at last the user has to enter the total number of stoppages during flight. At the end, the model return three values; `price`, `travel time` and the `arrival time`.

### ⭕Challenges & Limitations
---
Although this project seems simple and straightforward, but you may face diverse challenges when you solve this problem. First of all the dataset contains about 10 features. In the first step you have to preprocess and analyse all of the features which is very time consuming. i.e the dataset contains a `date format` column which is  a raw format and you have to split it into multiple columns(i.e. day, weekday, month, season, etc.) , in the next step you have to map some strings to their corresponding values for further analysis(i.e. map the `summer` into `3` or map `spring` into `2` and etc.). In addition to this, the dataset suffering from multiple issues and limitations. i.e. outliers and the number of records that available in the dataset(~ `10000` records and all of them have been recorded between March and June 2019).

In terms of feature engineering, this dataset contains various features from various formats. Some featuers are `continuous` and some of them are `categorical`.For some of the categorical features that had very few values, `One-Hot-Encoding` was used and some of them which contains many more values `count/frequency` feature encoding was used(to prevent `the curse of dimensionality`). The new challenge we may face in this project is that we have to apply `cyclical` feature encoding to some features that have cyclical attribute.i.e `weekday` and `day` features have cyclical attribute(`Monday` and `Sunday` have the same distance as `Wednesday` and `Thursday`) so to improve the model performance it is better to apply cyclical feature encoding on these kind of features.

Another important thing to note is that, the `Arrival_Time` and `Duration` features are considered as output features in addition to `price` column. In spite of two features have high predictive power and their removal can affect on the model performance, but the user itself can not evaluate or guesse it properly. Because of that these two features removed from the input features.

### 📐Model Performance
---
For this project, Random Forest Regressor is used. In spite of good results that this algorithm can produce, its creation and validation was a little bit challenging. This is because many hyperparameters have to be defined to Random Forest to fits on them and this takes some time. After that Cross-Validation is applied and the best, worst, and the mean of mean squared error(mse) is calculated and reported.The more informations about the model's performance is available in the `Model Creation & Validation.ipynb`
The model is saved by pickle format and you can access it by `model` folder.

### 💻Installation
---
The Code is written in Python 3.7.5. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:
```
git clone git@github.com:Kasra1377/flight-fare-prediction.git
```
or
```
git clone https://github.com/Kasra1377/flight-fare-prediction.git
```
To install required libraries just type:
```
pip install -r requirements.txt
```

### ⚙Technologies Used
---
![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) [<img target="_blank" src="https://pandas.pydata.org/static/img/pandas.svg" width=200>](https://pandas.pydata.org/)[<img target="_blank" src="https://numpy.org/images/logos/numpy.svg" width=200>](https://numpy.org/) 

### ❌Bugs & Issues
If you ever encountered any bugs in this projects or any technical issues you can report it by `issues` section of this repository or you can contact me by my email address. 


### 👥Contributers
---
Kasra1377
