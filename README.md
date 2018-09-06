# CogSci 2018 article: Complexity Reduction in the Negotiation of New Lexical Conventions

[![Join the chat at https://gitter.im/wschuell_notebooks_cogsci2018/Lobby](https://badges.gitter.im/wschuell_notebooks_cogsci2018/Lobby.svg)](https://gitter.im/wschuell_notebooks_cogsci2018/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Notebooks to reproduce results found in the CogSci 2018 article: https://arxiv.org/abs/1805.05631  
The poster associated to the article can be found here: http://wschuell.github.io/resources/poster_cogsci2018.pdf

To launch the notebook server (which will be running inside a docker container, it should therefore work on every platform):
```
python run.py
```

There are 2 important files:
* **Experiment.ipynb** The notebook itself, to run simulations and replot figures. A few hours might be needed to run the simulations first (depending on your computer).
* **settings.py** where you can modify parameter values and other settings. To take changes into account, restart the kernel of the notebook.

Of course, you are encouraged to test other parameters, policies, or interaction scenarios. The code relies on a modular library for the Naming Game model, where many existing versions of the model have already been implemented: https://github.com/flowersteam/naminggamesal

Simpler notebooks to familiarize with the NG simulation framework are available at: https://github.com/wschuell/notebooks_edmi18

And an explanatory poster is available here: http://wschuell.github.io/resources/poster_edmi18.pdf

Dependencies:
* Python
* Docker: https://docs.docker.com/install/
* Docker-compose: `pip install docker-compose`
