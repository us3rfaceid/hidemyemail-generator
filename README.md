<p align="center"><img width=60% src="docs/header.png"></p>

> Automated generation of Apple's iCloud emails via HideMyEmail.

_You do need to have an active iCloud+ subscription to be able to generate iCloud emails..._

<p align="center"><img src="docs/example.png"></p>

## Usage

Follow the guide steps 1 & 2 below if you'd like to run it from source, otherwise you can skip to the 3rd step - set your cookie and run.

Apple allows you to create 5 * # of people in your iCloud familly emails every 30 mins or so. From my experience, they cap the amount of iCloud emails you can generate at ~700.

## Setup
> Python 3.12+ is required!

1. Clone this repository

```bash
git clone https://github.com/us3rfaceid/hidemyemail-generator
```

2. Install requirements

```bash
pip install -r requirements.txt
```

3. [Save your cookie string](#getting-icloud-cookie-string)

   > You only need to do this once 🙂

4. You can now run the gen with:


**on Mac:**

```bash
python3 main.py
```

**on Windows:**

```bash
python main.py
```

## CLI Commands

You can also use the CLI for more options:

### Generate emails

```bash
# Generate 5 emails (default)
python3 cli.py generate

# Generate a specific number of emails
python3 cli.py generate --count 10
```

### List emails

```bash
# List all active emails
python3 cli.py list

# List inactive emails
python3 cli.py list --inactive

# Search by label (supports regex)
python3 cli.py list --search "example.com"
```

### Export emails to CSV

You can export all your Hide My Email addresses to a CSV file:

```bash
# Export all active emails to a CSV file
python3 cli.py list --export my_emails.csv

# Export only inactive emails
python3 cli.py list --inactive --export inactive_emails.csv

# Combine with search
python3 cli.py list --search "example.com" --export filtered_emails.csv
```

The exported CSV file will contain the following columns:

| Column    | Description                              |
|-----------|------------------------------------------|
| Label     | The label/website associated with the email |
| Email     | The generated `@icloud.com` address      |
| Created   | Date and time the email was created      |
| IsActive  | Whether the email is currently active    |

**Example output:**

```csv
Label,Email,Created,IsActive
example.com,random-words.0x@icloud.com,2023-01-15 10:30:00,True
mysite.org,another-phrase.1a@icloud.com,2023-02-20 14:45:00,True
```

## Getting iCloud cookie string

> There is more than one way how you can get the required cookie string but this one is _imo_ the simplest...

1. Download [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg) Chrome extension

2. Go to [EditThisCookie settings page](chrome-extension://fngmhnnpilhplaeedifhccceomclgfbg/options_pages/user_preferences.html) and set the preferred export format to `Semicolon separated name=value pairs`

<p align="center"><img src="docs/cookie-settings.png" width=70%></p>

3. Navigate to [iCloud settings](https://www.icloud.com/settings/) in your browser and log in

4. Click on the EditThisCookie extension and export cookies

<p align="center"><img src="docs/export-cookies.png" width=70%></p>

5. Paste the exported cookies into a file named `cookie.txt`

# License

Licensed under the MIT License - see the [LICENSE file](./LICENSE) for more details.

Originally made by **[rtuna](https://twitter.com/rtunazzz)** — forked & enhanced by **[us3rfaceid](https://github.com/us3rfaceid)**.
