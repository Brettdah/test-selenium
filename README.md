# Selenium-test

## Getting your environnement Ready

### Create your virtual environment

You will need to set a few things before starting to test code
First thing first create a virutal environnement for your project

```bash
mkdir .venv
python3 -m venv .venv/selenium-test
source .venv/selenium-test/bin/activate
```

### Install seleniumbase

```bash
python -m pip install seleniumbase
# OR use the requierement file I have in the repos
python -m pip install -r pip-requirement.txt
```

### install chrome

Then get the latest chrome for test (if you are in WSL it's pretty good as it will keep behind the scene)

```bash
# Get and install chrome browser
meta_data=$(curl 'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json')
wget $(echo $meta_data | jq -r '.channels.Stable.downloads.chrome[0].url')

# Install chrome Dependencies
pkg_manager=nala #  you may want to install it or use your favorite or default for your distro
$pkg_manager install -y ca-certificates fonts-liberation \
    libappindicator3-1 libasound2 libatk-bridge2.0-0 libatk1.0-0 libc6 \
    libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgbm1 \
    libgcc1 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 \
    libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 \
    libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 \
    libxrandr2 libxrender1 libxss1 libxtst6 lsb-release wget xdg-utils

#Get the version of the chrome you installed
## exemple for me
echo $meta_data | jq -r '.channels.Stable.downloads.chrome[0].url'
https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.122/linux64/chrome-linux64.zip
# so I print the 5th collomn
echo $meta_data | jq -r '.channels.Stable.downloads.chrome[0].url' | awk -F"/" '{print $5}'
123.0.6312.122

# So now that I'm sure I can install the driver like so
# Install the chrome driver
seleniumbase get chromedriver $(echo $meta_data | jq -r '.channels.Stable.downloads.chrome[0].url' | awk -F"/" '{print $5}')
```

### Install Firefox

```bash
# install Mozilla Repo
## Be sure FF is not installed by snap
sudo snap remove firefox
## Get the Key
wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- > /etc/apt/trusted.gpg.d/mozilla.asc
## Create the repos file
echo "deb https://packages.mozilla.org/apt mozilla main" > /etc/apt/sources.list.d/mozilla.list
pkg_manager="nala"
$pkg_manager update
echo '
Package: *
Pin: origin packages.mozilla.org
Pin-Priority: 1000
' | sudo tee /etc/apt/preferences.d/mozilla
$pkg_manager update  # If needed
$pkg_manager install -y firefox

firefox --verion
124.0.1
## Install FF driver (gecko)
sbase get geckodriver 124.0.1
```

## execute a test

```bash
# Exec all tests
pytest

# Exec all tests and display the print you put in your codes
pytest -s

# Exec all test in test_cart.py
pytest -k test_cart -s

# Exec only 1 test (here from test_home.py)
pytest -k test_menu_links -s

# Exec all test and generate a dashboard
pytest --dashboard

# Exec all tests from test_contact.py and generate a dashborad
pytest -k test_upload --dashboard

# Test in a specifique browser
pytest --browser=firefox

# Display all browser available (for you to install them or not)
pytest --browser
```
