# Capstone Proposal

Create an app that lets each user track their hands on camera and practice sign language

## Overview

This app will be a SPA app with user login. User's will be able to get instant feedback on their hand gestures to learn certain sign language. New hand gestures should show more frequently and gestures that learned show up less frequently. The app will use Python, Flask, & Vue.js. The handtracking library is MediaPipe.

## Functionality

- User will be routed to login page if not logged in
- Home page will have a synopsis of gestures learned, learning, and having trouble with
- Each page will have a dashboard with logout, home, learn & admin links
- Admin page will have the ability to add or remove gestures from learning
- Admin page will allow changing password and editing profile
- Learn page will use user's camera to track hands, ask user to perform specific gesture, feedback area, skip button, & next button

## Data Model

- users: name, password
- cards: name, datapoints, image url, #attempts, #correct, #incorrect, time since last correct
- bins: {
    0: [cards],
    1: [cards],
    ...
}
-user m2m with cards
-user one2one with bins

## Timeline

- Week 1: Get framework working, setup database, diagram out API calls & wireframe, and build basic html layout
- Week 2 & 3: integrate MediaPipe. Start utilizing datapoints get feedback. Add 10 gestures to cards.
- Week 4: Create user login. Make front end look better. Implement user create cards. Ability to share cards with other users

