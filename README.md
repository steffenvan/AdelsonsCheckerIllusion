
# Adelson's Checker-Shadow Illusion
The illusion can be seen on this [link](https://www.illusionsindex.org/ir/checkershadow)
## Programming 
The directory has this structure 
```
illusionApp
  | 
  │── results
  │── static
        └── background
  |── variations
        └── variations_x.png
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
If this doesnt work because of the clossing socket issue, try:
`bokeh serve --websocket-max-message-size 10000000 --show illusionApp/`
This will open up the desired illusion on `http://localhost:5006/illusionApp`. 


#### Displaying the illusion
Switch which illusion to show in your `localhost` by commenting out the specific line in `main.py`
```python
### here the specific illusion is imported 
# import illusionTemplate as illusion
# import illusionTemplateAlt as illusion
# import threeSquaresIllusion as illusion
import adelsons as illusion
```
As of now we can display one variation of the illusion at a time. 

#### TODO 
Modify the draw function to be updated each time a new variation is chosen when the server is running. 

## Literature review
Currently working on the literature review. 
**Deadline** for the literature review is **4th of March**
