# Zomato-Restaurant-Rating-Prediction
![12](https://user-images.githubusercontent.com/108328448/186218145-885ac136-8b5d-43a0-b353-2db225568de1.PNG)
The main goal of this project is to perform extensive Exploratory Data Analysis(EDA) on the Zomato Dataset and build an appropriate Machine Learning Model that will help various Zomato Restaurants to predict their respective Ratings based on certain features.
# Dataset
![18](https://user-images.githubusercontent.com/108328448/186218542-e15ecbaf-0469-4f15-9c94-7180e1d7c353.PNG)
# Exploratory Data Analysis (EDA)
![22](https://user-images.githubusercontent.com/108328448/186218923-efcdc4c3-1cd5-43aa-8a1f-91ab0adba208.PNG)

count plot on online_order

![22](https://user-images.githubusercontent.com/108328448/186219100-afaa74da-8cfb-4550-801e-1b0463aedb5f.PNG)

count plot on book_table


![22](https://user-images.githubusercontent.com/108328448/186219242-f3139aee-a724-4842-b0df-2c3eb4112297.PNG)

online order vs Rating


![22](https://user-images.githubusercontent.com/108328448/186220186-61a9288d-3e5e-40c3-b09d-8d2383da510a.PNG)

Types of Restaurents vs Rate


![22](https://user-images.githubusercontent.com/108328448/186220401-0ef26709-ef72-4f77-8913-5b80cae934c6.PNG)

Cost2Plate Vs Rate


![22](https://user-images.githubusercontent.com/108328448/186220752-10d0ab41-37fa-4017-b57b-9734267d2ea1.PNG)


# Feature Engineering and Feature Selection
URL, Address, Name, phone, Rest_type, Dish_liked, Reviwe_list, Menu_item, and Listed_in(city) are not rerquired so we delete these columns.

# Model Training
We will use Supervised Machine Learning Regression Algorithums for the model building

Models Used :

1.Extra Tree Regressor (Accuracy 84%)

# Model Deployment


![13](https://user-images.githubusercontent.com/108328448/186226974-79d6ffcc-8be4-4263-8a17-03459a066a62.PNG)

Database Used for storing Data

1.MongoDB

Model is deployed on Amazon Web Services colud platform Tools used in deployment

1.Flask

2.Putty

3.Putty gen

4.API is designed in HTML

Online Link: http://ec2-13-232-229-129.ap-south-1.compute.amazonaws.com:8080


![23](https://user-images.githubusercontent.com/108328448/186227541-50933fb4-ede5-42a9-bbc8-fa71840347cd.PNG)
