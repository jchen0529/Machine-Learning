# Catalog sales data analysis
A group project from Northwestern MSiA's Predictive Analytics class where I worked with a team of four 
and applied supervised learning methods to predict top revenue-generating customers. 

### Business situation:
The dataset comes from a retail company that sells upscale clothing on its website and via catalogs,
which help drive customers to the website. All customers were sent a catalog mailing on
Sep 1, 2012. On Dec 1, 2012 it was recorded whether or not they responded by making a
purchase. Each row represents a customer. The *targdol* is the response variable, which
is the purchase amount in response to receiving the catalog (*targdol* = 0 indicates that the
customer did not respond).

### Data:
There are a total 101,532 customers, who are randomly split into 50418 in the training
set and the remaining 51,114 in the test set. The variables definitions are displayed below:

* **targdol**: dollar purchase resulting from catalog mailing 
* **datead6**: date added to file
* **datelp6**: date of last purchase
* **lpuryear**: latest purchase year
* **slstyr**: sales ($) this year
* **slslyr**: sales ($) last year
* **sls2ago**: sales ($) 2 years ago
* **sls3ago**: sales ($) 3 years ago
* **slshist**: LTD dollars
* **ordtyr**: orders this year
* **ordlyr**: orders last year
* **ord2ago**: orders 2 years ago
* **ord3ago**: orders 3 years ago
* **ordhist**: LTD orders
* **falord**: LTD fall orders
* **sprord**: LTD spring orders
* **train**: training/test set indicator (1 = training, 0 = test)

### Goal: 
Build a predictive model for *targdol* based on the training set and then test it on the test set.
To do this, you need to first develop a binary logistic regression model for targdol > 0. Use this model to
estimate the probabilities of being responders for the test set.
Next develop a multiple regression model using data with targdol > 0 only.
Finally, for each observation, calculate E(targdol) by multiplying the
predicted targdol from the multiple regression model by the predicted probability from the
logistic regression model.

### Criteria for evaluating fitted models:
The final fitted regression model should meet the usual criteria such as:
* significant coefficients
* satisfactory residual plots
* good fit as measured by R2 or R2 adj
* parsimony and interpretability of the model etc.

Two numerical criteria will be used to evaluate the fitted models on the test set:
* Statistical Criterion : Mean square prediction error (MSPE) 
* Financial Criterion : Select the top 1000 customers (prospects) from the test set who have
the highest E(targdol). Then find their total actual purchases. This is the payoff and
should be as high as possible.