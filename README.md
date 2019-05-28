# RedDust
This project presents the RedDust data resource
consisting of personal attribute labels for over 300k Reddit users across five predicates: profession, hobby, family status, age, and gender.

We construct RedDust using a diverse set of high-precision patterns 
and demonstrate its use as a resource for developing learning models 
to deal with implicit assertions.

RedDust consists of Reddit users ids, the corresponding users' personal attribute labels, and the users' post ids, which may be used to retrieve the posts from a publicly available crawl or from the Reddit API.

The link to the dataset itself:
https://zenodo.org/record/3234005#.XO2Cm6WxXRZ

In this repo we put the accompanying code used to extract RedDust data via Patterns

## Running
Use hadoop to run the scripts
For each attribute use 

`-mapper mapper_<att_name>.py - reducer joint_reducer.py`

Reducer is the same for all. For further details about the patterns refer to the pdf of the paper
