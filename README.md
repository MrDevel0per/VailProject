## Disclaimer
This project is intended for the sole purpose of education.

# JSON
This project scrapes data from [Vail Resorts](https://vail.com). Because Vail Resorts uses the same `JSON` format across their websites, this web scraper will work with any Vail Resorts-owned website. An example of the `JSON` for the chairlifts:
```json
{"Name":"Pete's Express #39","Status":"Open","Type":"quad","SortOrder":0,"Mountain":"Blue Sky Basin","WaitTimeInMinutes":3,"Capacity":4,"OpenTime":"10:00","CloseTime":"14:15"},
{"Name":"Earl's Express #38","Status":"Open","Type":"quad","SortOrder":1,"Mountain":"Blue Sky Basin","WaitTimeInMinutes":4,"Capacity":4,"OpenTime":"10:00","CloseTime":"14:30"},
{"Name":"Skyline Express #37","Status":"Open","Type":"quad","SortOrder":2,"Mountain":"Blue Sky Basin","WaitTimeInMinutes":1,"Capacity":4,"OpenTime":"10:00","CloseTime":"14:30"}
```

# Usage
First, clone the repository or download the files from the following URL: https://github.com/MrDevel0per/VailProject.git.
```bash
$ git clone https://github.com/MrDevel0per/VailProject
```
## Running
Run this command in your terminal to get the data:
```bash
python3 SkiRuns.py
```
## Parameter explaination
* `newUrl` - This is the URL of the website which you want to scrape. Ensure that you pass in the entire URL, such as: https://www.vail.com/the-mountain/mountain-conditions/terrain-and-lift-status.aspx. The given URL will be checked against the following `Regex`:
```python
r"https://www\.\w+\.com/the-mountain/mountain-conditions/terrain-and-lift-status.aspx"
```
* `fileName`: The name of the runs file. This does not have to include the extension `.csv`, as it will be added if necessary. Use `__name__` for the name of the mountain and `__num__` for the number of ski runs. This will be the name of the generated CSV file that is saved to your `Downloads`.
* `liftName`: The name of the lifts file. This does not have to include the extension `.csv`, as it will be added if necessary. Use `__name__` for the name of the mountain and `__num__` for the number of chairlifts.
* `difficulties`: A `Boolean` (`y/n` input) of whether or not the program should print the percentage difficulties for the runs of the mountain.
After giving the required parameters your data will be saved with your file names to your `Downloads` directory via the `csv` library.

