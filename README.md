# ✈flight-fare-prediction
---
![alt text](img/interface.PNG)

**Link** : https://flight-fare-pred-application.herokuapp.com/home

### 📄Description
---
In this project our aim is to predict the `flight price` , the `duration` and the `travel time` using machine learning models. User has to input the name of the city(`source`) that they want to depart from and the destination.In addition to that user has to enter their `airline name` which is pretty important , their `departure time` and `departure date` and at last the user has to enter the total number of stoppages during flight. At the end, the model return three values; `price`, `travel time` and the `arrival time`.

### ⭕Challenges & Limitations
---
Although this project seems simple and straightforward, but you may face diverse challenges when you solve this problem. First of all the dataset contains about 10 features. In the first step you have to preprocess and analyse all of the features which is very time consuming. i.e the dataset contains the `date format` which is in a raw format and you have to split it into multiple comlumns(i.e. day, weekday, month, season, etc.) , in the next step you have to map some string to their corresponding values for further analysis(i.e. map the `summer` to the `3` or map `spring` to the `2` and etc.). In addition to that the dataset suffering from multiple issues and limitations. i.e. outliers and number of records that available in the dataset.

In terms of featuer engineering, this dataset contains various features from various formats. Some featuers are `continuous` and some of them are `categorical`  
