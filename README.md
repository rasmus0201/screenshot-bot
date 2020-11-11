# Webmatematik Screenshotter
Screenshot pages of Webmatematik.

## Get started

Make sure you have the chromedriver binary in place in the repo root directory.

#### Linux:
On linux it goes like this:
```
wget https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip
unzip chromedriver_linux64.zip && rm chromedriver_linux64.zip
```

Create a virual environment running Python 3.7 (or newer) and install the dependencies listed in `requirements.txt`
On linux the steps would be something along these lines:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### MacOS:
```
curl https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_mac64.zip -o chromedriver_mac64.zip
unzip chromedriver_mac64.zip && rm chromedriver_mac64.zip
```

Create a virual environment running Python 3.7 (or newer) and install the dependencies listed in `requirements.txt`
On mac the steps would be something along these lines. Notice that the line with "pkg-resources==0.0.0" is being removed:
```
python3 -m venv venv
source venv/bin/activate
sed -i '' "/pkg-resources==0.0.0/d" requirements.txt
pip install -r requirements.txt
```

## Running the tool
The tool can be tested by running the instructions in `instructions/links.json` and `instructions/screenshots.json`

To get all the necessary links, run this this command
```
python links.py instructions/links.json
```

Now an output file named `pages.json` will be made in the output folder. Copy the links into `screenshots.json` in the `pages` array. Then to capture screenshots, run:
```
python capture.py instructions/screenshots.json
```

```json
{
  "title": "webmatematik",
  "headless": true,
  "device": "imac21",
  "base_url": "https://www.webmatematik.dk",
  "pages": [
    "https://www.webmatematik.dk/lektioner/7-9-klasse/procenter/regn-med-procenter"
  ]
}
```
*Note: When you want to use the scripts you need to make sure the venv is activated*
