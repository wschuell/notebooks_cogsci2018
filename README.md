# CogSci 2018 article: Complexity Reduction in the Negotiation of New Lexical Conventions
Notebooks to reproduce results found in the CogSci 2018 article

The corresponding article will soon be available.

To launch the notebook server (inside a docker container, it should work on every platform):
```
python run.py
```

There are 2 notebooks:
* *1.Running.ipynb* to run the simulations. Several hours might be needed to execute everything, but you can change/narrow down the parameter ranges.
* *2.Plotting.ipynb* to plot the figures

Of course, you are encouraged to test other parameters, policies, or interaction scenarios. The code relies on a modular library for the Naming Game model, where many existing versions of the model have already been implemented: https://github.com/flowersteam/naminggamesal

Simpler notebooks to familiarize with the NG simulation framework are available at: https://github.com/wschuell/notebooks_edmi18

And an explanatory poster is available here: http://wschuell.github.io/resources/poster_edmi18.pdf

Dependencies:
* Python
* Docker: https://docs.docker.com/install/
* Docker-compose: `pip install docker-compose`