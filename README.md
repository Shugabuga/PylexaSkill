# PylexaSkill
#### *An example Amazon Alexa skill using Python and Pylexa.*

Note: This is a modified fork of [heroku/alexa-heroku-info](https://github.com/heroku/alexa-heroku-info).

## Introduction
This example skill will, when prompted, get the response of information provided by environmental variables, making it easier to kickstart making an Alexa skill. Very similar code is used in skills such as [National Parks](https://www.amazon.com/ShugaBuga-Development-National-Parks/dp/B0734LBNYX) and [Bitcoin Value](https://www.amazon.com/dp/B0741N7SWN).

## Install to Heroku
To link the skill with Heroku, use the button below and fill out the variables:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Once you do this, go to your app, and note the app URL. You will need this later.

After this is done, you need to log in to your Amazon account and go  [here](https://developer.amazon.com/edw/home.html#/). After this is done, click `Get Started` under `Alexa Skills Kit`, click `Add a New Skill`, and fill in information under `Interaction Model` with info from the `/conf/` folder in this repository, then click Next.

After this is done, set the endpoint type to `HTTPS`, choose a location, and put in your endpoint URL from Heroku (should be like `https://given-name.herokuapp.com`), and click Next.

Then select the second option ("*My development endpoint is a sub-domain of a domain that has a wildcard certificate from a certificate authority*"), then click Next.

Finally, fill in the publishing information.

## License
Licensed under MIT, but a thank you somewhere would be appreciated (and required if you intend to make money, recieve benefits from Amazon, such as a t-shirt promition, and/or it is for a commercial project).
