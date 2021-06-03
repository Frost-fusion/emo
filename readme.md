<h1>Emo- Emotion Detection</h1>
<h4>How to create environment and python repository</h4>
<hr>
Download **anaconda manager** for host os from the
<a href="https://www.anaconda.com/products/individual">link </a>

Install anconda manager System-wide or as Admin(All users).

After finishing installation:<br>
Open anaconda prompt as administrator.<br>

run command to create a conda environment for the project.

`conda create --name <env> --file <this file>`<br> 
where `<env>` is name of conda env to create and `<this file>` 
is name of requirement file.

using git clone the repo into your ide (pycharm), load the conda env 
into ide and create configration file as
`emotions.py --train` to train on data and `emotions.py --display`
to identify live data.


