# PFHG.AI
Prefabricated Home Generator with Artificial Inteligence


This repository is intended to disseminate the content developed through the course of the Studio seminar Artificial Intelligence in Architecture for the MaCAD program of IaaC in 2021.

You can find in this repository:

The dataset developed in Grasshopper and encoded to be then trained as a neural network
The Python codes used to train the neural network for predicting the values
The Python codes used to connect the artificial intelligence model with the Grasshopper
The GH scripts for generating new houses from the predictions of the artificial intelligence model
The Human UI interface that allows for exploring the results of the developed Neural Network

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
The predicted values in output are directly related to the size of the house, thermal data and energy consumption. In the final test result, these values were a little higher than the trained values, although our model has a good MSE(mean loss error). We conclude that this situation occurs due to the large number of irregular samples generated from the random facade. For deeper development on the subject of this research, it is necessary that the dataset creation evolves in a direction of greater accuracy and clearer relationship, in order to enable the necessary feature correlation by the machine learning algorithm.
