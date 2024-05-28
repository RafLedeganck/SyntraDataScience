# Highlights
### Goal
This program calculates churn risk based on employee data.  Features include organizational master data (e.g. site, department and employee type) but also <b>highly sensitive personal data</b> like handicap and <b>sensitive</b> personal financial data (bonus amounts).<br>
The program has 2 objectives:<ul>
<li>Explore how the feature set can be reduced so the predictions can be made on as few features as possible, thus (1) reducing the need for personal data, (2) making the model as transparant as possible, (3) making it as widely usable as possible and (4) maximizing efficiency.</li>
<li>Based on a minimal feature set search the prediction model that performs best.</li></ul>
In the process we will try to draw lessons from the data at hand and provide useful business insights.  These insights are presented via plots from different angles at the data.

### Me
[RafLedeganck on GitHub](https://github.com/RafLedeganck)<br>
The program was written in the context of the course 'Data Scientist' at Syntra AB over 2022-2024 .

### Principles and assumptions
<ul>
<li>Model training was done on anonymized data but for the predictions it is esteemed important to be able to act upon the conclusions of the data analysis. If the user doesn't know the person behind a churn risk calculation, the exercise does not make much sense. <b>It is left to the person executing the program to handle the outcome with the necessary caution.</b>  The plots that are output to the /Output folder are at a sufficiently high level to avoid direct identification but should nevertheless not be distributed innecessarily.
<li>The program was developed in a Tensorflow 2.11.0 Docker container.</li>
</ul><br>

# Folder structure
<ul><li>root</li><ul>
    this file
<li>\Docu: (o.a.) the business presentation (PPT)</li>
<li>\Notebooks<ul>
    latest version of the program (Jupyter notebook)
    <li>\Backup: archive for old versions</li>
    <li>\Data: input files</li>
    <li>\Output: plots in .jpg format</li></ul>
    </ul>
</ul></li><br>

# Program structure
### 1. Setting the stage
Package are installed and modules imported.<br>
Functions are defined.  More info in the docstring of each function.<br>
Most noteworthy, however, is § 1.2 which contains program switches that de-/activate the export of plots to the /Output folder or the grid searches to find the optimal parameters for the learning models.

### 2. Data loading
Training file: Data/Employee_Churn_train.csv

### 3. Data Exploration
Data preparation & cleaning.  NaN are filled with values from similar rows, replaced with 'None' or 0 depending on the feature.  Any NaN that could not resolved are dropped if in total less than 2% of the lines.

### 4. Feature reduction
The first main goal of the program.  Two approaches are explored:<ul>
<li>Filtering by checking for quasi-constant features, checking variance and correlations. Also Mutual Information is calculated.</li>
<li>Feature reduction embedded in learning models.  Random Forest, Gradient Boosting and Logistic Regression are explored.  For each model the result for the full and reduced feature set are compared.  It is also checked if dimension reduction via Principle Components Analysis sheds a useful light on which features are more/less relevant.</li>
</ul>

### 5. Learning models
The 2nd important goal of the program.  After checking whether the dataset is balanced, the performance of Random Forest, Support Vector Machines and Logistic Regression on the reduced feature set is compared with the full training set (and correction for imbalance) against training on the balanced subset of the training set.<br>
Also the performance of a Neural Network is checked, on the full feature set.<br>
Performance plots of the models are not exported because they have little business value.

### 6. Prediction on new dataset
New file: Data/Employee_Churn_apply.csv<br>
The best performing model is then re-trained on the full training data set (without train-test split) and applied to calculate predictions and probabilities on a new data set.

### 7. Further data analysis
To conclude, some further analysis is done on the data to see if we can draw any further conclusions.
