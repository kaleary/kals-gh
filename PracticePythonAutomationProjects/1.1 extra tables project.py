import pandas as pd

gh_timeline = pd.read_html("https://en.wikipedia.org/wiki/Timeline_of_GitHub")

len1 = len(gh_timeline)
print(len1)



