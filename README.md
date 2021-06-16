# PFHG.AI
Prefabricated Home Generator with Artificial Inteligence


This repository is intended to disseminate the content developed through the course of the Studio seminar Artificial Intelligence in Architecture for the MaCAD program of IaaC in 2021.

You can find in this repository:

1. The data set developed in Grasshopper and encoded to be then trained as a neural network

2. The Python codes used to train the neural network for predicting the values

3. The Python codes used to connect the artificial intelligence model with the Grasshopper

4. The GH scripts for generating new houses from the predictions of the artificial intelligence model

5. The Human UI interface that allows for exploring the results of the developed Neural Network

## What is this project about:

Our intent was to explore an AI-related generative design method for a simple house, made of SIP, and give the user of the plugin/code the possibility to quickly predict a house that fits the user’s inputs of cost and time of construction and orientation of the house, serving as a better informed start point for designing the house. 
 
## About the data set:

The house typology chosen has a SIP construction system - Structural Insulated Panels made of wood. The house changes sizes increasing or decreasing within the dimensions of a regular panel size (width: 1.22m, height: 2.44m). 
Based on this simple geometry, we developed a Grasshopper script to generate a representative population, and encoded a dataset of its dimensions, orientation, construction cost, construction time, brief annual energy consumption and daylight, either calculated from online construction reports, or simulated with Honeybee/Ladybug (considering the surroundings of Paris as location). 
The data set consists in XXXXX samples.
The GH scrip is….

## About the Artificial Intelligence approach: 

Our project started from the exploration and comparison of different machine learning methodologies applied to this architectural problem. What would be the best Neural Network architecture to predict a new house, from the developed data set, how well it would predict, and how to generate a new house from the predicted values were the challenges addressed.

The Artificial Neural Network developed consists in a Sequential Model with 6 Dense Layers ran with Keras, in the Google Colaboratory environment, and is .  
Through various experiments we could notice only a slight variation in the geometric results obtained while changing the model architecture by adding or reducing hidden layers in the neural network. Whereas, the variation in the number of epochs and batch sizes intensely affected the geometric result obtained.
The predicted values in output are directly related to the size of the house, thermal data and energy consumption. In the final test result, these values were a little higher than the trained values, although our model has a good MSE(mean loss error). We conclude that this situation occurs due to the large number of irregular samples generated from the random facade. 

## If you want to develope a similar Prefabricated House Generator for your own city 
<details>
           <summary> Learn how to here
            </summary>
           <p>


For accurate predictions, the most important thing is to have the best fit possible data. In case of energy consumption and Daylight, this means running a whole new data set for the city desired. The way to do it is through Grasshopper, with the script shared in this repository - DataSetCreator. 
Download the script, change the city climate file (you can find the one necessary here: https://www.ladybug.tools/epwmap/) and run the simulations until you have at least 2000 samples.

## Train your own PFHG.AI

With your data set prepared, you have to train it. You can download the Google Colab Notebook shared in this repository (Colab allows you to combine executable code and rich text in a single document).

Through Google Drive you can access the Notebook, call your data set, analise it and train the model. More information on how to train the model can be found inside the Notebook. It's important to be sure that there are no mistakes within the dataset such as uneven distributed numbers, missing information or unrepresentative numbers.
If you don't know how to analise and clean your dataset, a good place to start is here: https://colab.research.google.com/github/adelnehme/cleaning-data-in-python-live-training/blob/master/Cleaning_Data_in_Python_live_session.ipynb

After you clean your dataset, and train your model, you should save the predictor as an .h5 file, which you can do by following the steps on the notebook.
Download this .h5 file, and also the .pickle files created during the steps of training, to be used in the next steps. 

## Bringing the PFHG.AI back to Grasshopper 

#### The HOPS component
Hops is a component for Grasshopper in Rhino 7 for Windows. Hops adds external functions to Grasshopper, like other programming languages, in our case Python with some libraries.

In this repository you can find and download a folder to access directly from within Visual Studio Code, for example, or any other python interface, and build the Hops component for your own PFHD.AI.

Make sure you have the best fit python to deal with Hops by now (3.8), and also pip installed in your computer. Find it https://www.python.org/downloads/release/python-3810/ and https://pypi.org/project/pip/.

Before start, inside your Python interface, choose the Python 3.8 interpreter, and run these lines of code in the terminal to install the libraries necessary: 

* pip3.8 install flask
* pip3.8 install ghhops_server
* pip3.8 install rhino3dm
* pip3.8 install numpy
* pip3.8 install tensorflow
* pip3.8 install pickle
* pip3.8 install joblib
* pip3.8 install os
* pip3.8 install sys


This folder contains 3 files: 
##### 1. machinelearning.py
In this file you have to call your own .h5 file and .pickle files. Call it from your own computer by updating the path information.
Make sure you have everything connected, and press run.

##### 2. hops.py
In this file is where you will connect the PFHG.AI to the Hops component. For that we create the inputs and outputs expected to exist inside Grasshopper.  
You don't need to change anything here, just press run.

##### 3. Studio.gh
This file you open in Grasshopper, find the Hops component - should be the one with the little grape drawing - clic with the right button, add the Path (xxxxx/runML).
Make sure you uncheck the Cache options to always ensure the updated predictions.
Connect the inputs *Construction Cost*,*Construction Time* and *Rotation* to the Hops Component, and extract the outputs. 
Connect the ouputs to the prefabricated panels creator to see the final result.
</p>
</details>

## If you want to build upon this work 

For deeper development on the subject of this research, it is necessary that the data set creation evolves in a direction of greater accuracy and clearer relationship, in order to enable the necessary feature correlation by the machine learning algorithm. But also, we understand that high accuracy of prediction isn’t always guarantee of a good geometrical prediction. With that in mind, we beleive that next steps into this research could include:

* Different training architectures
* Different inputs and outputs

Other studies necessary are regarding the dissemination of this A.I. predictor.
We believe that the population with less access to computational knowledge and design tools would be the ones most benefited from the arrival of such a simplification of basic design generator.
Having the hability to make an informed decision with minimun inputs for a house made of SIP could allow the 85% of the population that don't hire architects or enginners today 
to have at decide on a prevalidated design and buy their own homes from a factory of pre fabricated houses.
