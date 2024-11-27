---
editor_options: 
  markdown:
---

# Introduction

This is a comprehensive Exploratory Data Analysis for the BCG Virtual Internship Program Provided by [Forage](https://www.theforage.com/virtual-internships/prototype/Tcz8gTtprzAS4xSoK/Open-Access%20Data%20Science%20&%20Advanced%20Analytics%20Virtual%20Experience%20Program?ref=PFRxbADb5emG73ZYp) with Python and Data Visualization libraries such as matplotlib and seaborn.

The goal of this program challenge is to predict the probability of customers retention on one of BCG clients called PowerCo. PowerCo is a company that focus on supplying gas and electricity for SME( Small Medium Enterprises) and residential customers. They want to derive an effective decision to the declining customers lately by collaboration with BCG. One hypothesis that likely to happen of the customer churn is the price sensitiviy and the isssue of power-liberalization market in Europe. We, as consultant want to understand the data better and derive actionable insights through the hypothesis whether we should consider marketing strategy that PowerCo is trying to do by offering 20% discount to the customers churn. Is is an effective way to do or any other solutions that we can deliver to the client. Because this is a classification problem, we will be using one or more classification algorithms such as Logistic Regression, Decision tree, or Random Forest by always checking a few importants parts such as overfitting or underfitting model.

For these reasons, We will analyze three datasets that we will believe can support the insights by following data : 1. Historical customer data: Customer data such as usage, sign up date, forecasted usage etc 2. Historical pricing data: variable and fixed pricing data etc 3. Churn indicator: whether each customer has churned or not

We start the exploratory data analysis by loading the dataset using pandas, checking missing values, doing feature engineering,checking outliers and comparing between univariate and bivariate features,improving the model using ML Algorithms(Logistics regression, Decision Tree, Random Forest or Gradient Boosting) as classificication model.

## File descriptions

-   `ml_case_training_data.csv` - the training set (contains 16096 records)
-   `ml_case_training_hist_data.csv` - the testing set (contains 193002 records)
-   `ml_case_training_output.csv` - a sample of output whether the clients churned or not

## Data fields

### ml_case_training_data.csv

-   `id` client id
-   `activity_new` category of the company's activity
-   `campaign_disc_ele` code of the electricity campaign the customer last subscribed to
-   `channel_sales` code of the sales channel
-   `cons_12m` electricitym consumption of the past 12 months
-   `cons_gas_12m` gas consumption of the past 12 months
-   `cons_last_month` electricity consumption of the last month
-   `date_activ` date of activation of the contract
-   `date_end registered` date of the end of the contract
-   `date_first_activ` date of first contract of the client
-   `date_modif_prod` date of last modification of the product
-   `date_renewal` date of the next contract renewal
-   `forecast_base_bill_ele` forecasted electricity bill baseline for next month
-   `forecast_base_bill_year` forecasted electricity bill baseline for calendar year
-   `forecast_bill_12m` forecasted electricity bill baseline for 12 months
-   `forecast_cons` forecasted electricity consumption for next month
-   `forecast_cons_12m` forecasted electricity consumption for next 12 months
-   `forecast_cons_year` forecasted electricity consumption for next calendar year
-   `forecast_discount_energy` forecasted value of current discount
-   `forecast_meter_rent_12m` forecasted bill of meter rental for the next 12 months
-   `forecast_price_energy_p1` forecasted energy price for 1st period
-   `forecast_price_energy_p2` forecasted energy price for 2nd period
-   `forecast_price_pow_p1` forecasted power price for 1st period
-   `has_gas` indicated if client is also a gas client
-   `imp_cons` current paid consumption
-   `margin_gross_pow_ele` gross margin on power subscription
-   `margin_net_pow_ele` net margin on power subscription
-   `nb_prod_act` number of active products and services
-   `net_margin` total net margin
-   `num_years_antig` antiquity of the client (in number of years)
-   `origin_up` code of the electricity campaign the customer first subscribed to
-   `pow_max` subscribed power

### ml_case_training_hist_data.csv

-   `id` client id
-   `price_date` reference date
-   `price_p1_var` price of energy for the 1st period
-   `price_p2_var` price of energy for the 2nd period
-   `price_p3_var` price of energy for the 3rd period
-   `price_p1_fix` price of power for the 1st period
-   `price_p2_fix` price of power for the 2nd period
-   `price_p3_fix` price of power for the 3rd period

### ml_case_training_output.csv

-   `id` client id
-   `churn` has the client churned over the next 3 months
