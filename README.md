
# Adelson's Checker-Shadow Illusion
The illusion can be seen on this [link](https://www.illusionsindex.org/ir/checkershadow)
## Programming 
The directory has this structure 
```
illusionApp
  ├── illusionApp
  │   ├── results
  │   └── static
  ├── results
      └── static
      └── background
  ├── threeSquaresIllusion.py
  ├── illusionTemplate.py
  ├── illusionTemplateAlt.py
  └── main.py
```
## Setup
Clone the repository in your desired folder e.g with:
`git clone git@github.com:steffenvan/AdelsonsCheckerIllusion.git`

#### How to test
As of now you can run the setup in the root of the repository with:
`bokeh serve --show illusionApp/`
This will open up the desired illusion on `http://localhost:5006/illusionApp`. 


#### Switch to another illusion
Switch which illusion to show in `localhost` by commenting out the specific line in `main.py`
```python
### here the specific illusion is imported 
import illusionTemplate as illusion
# import illusionTemplateAlt as illusion
# import threeSquaresIllusion as illusion
```
## Literature review
Currently working on the literature review. 
**Deadline** for the literature review is **4th of March**