# CAPSTONE PROPOSAL
## Megan Cook
## 10/8/2021
_______________________________________________

- [ ] Python
- [ ] HTML
- [ ] CSS
- [ ] JavaScript
- [ ] Django

_______________________________________________
## 1. Project Overview

**Name: Coyote Cycle Tracker**

**Description:** An inclusive, evidence-based menstrual cycle tracking app for queer/trans/non-binary/gender-fluid or otherwise gender non-conforming individuals who want to get pregnant, prevent pregnancy, or gain a better understanding of their cycle. 

**What problem does this app solve?**

The menstrual cycle tracking apps that are currently on the market are targeted mostly to cis women and feel exlusive of non cis gendered people. Not everyone who menstruates and gives birth identifies as a woman, and certain individuals may be experiencing specific hormonal situations. Queer, trans, and NB folks have unique needs and challenges when it comes to conception and contraception that no app on the market currently addresses. 

**Major features:**
1. Color-coded calendar or circle representing each day of the cycle. 
2. Ability to log and track important events, signs, and symptoms (cycle begins/ends, encounter with sperm, basal body temp, mood swings, headaches, cramps, etc.).
3. User profile with personalized features (cycle length, flow length, goal).
4. In app notifications/reminders for phase of cycle (predicted mentstrual, follicular, ovulation, luteal phase dates), to take contraception, to take BBT.
5. Ability to predict and adjust cycle and flow length based on user input over time.

**Libraries:**
* [Django Scheduler](https://pypi.org/project/django-scheduler/)
* [Python Calendar](https://docs.python.org/3/library/calendar.html)

**Framesworks:**
* Django

**APIs:**
* [Moon phases](https://www.aerisweather.com/support/docs/api/reference/endpoints/sunmoon-moonphases/)


## 2. Functionality

**1. Create user page:**
* Prompt user to enter info:
    * Name (required)
    * Email address (required)
    * Goal (select):
        * Contraception
        * Conception
        * Cycle regulation
    * Cycle info:
        * Do you have regular cycles?
            * If yes: 
                * How many days does your cycle typically last?
                * How many days does menstruation usually last?
            * If no:
                * Set default to 28 days for cycle length and 5 days for menstruation
        * What symptoms do you typically experience, if any?
            * Symptom list

**2. Home page:** 
* Menu (collapsible):
    * Calendar/cycle view (Home)
    * Log symptom or event (select date)
    * Profile
    * How to use
    * Help
    * Contact/Feedback
* Logo
* Today's date  
* User's current cycle phase and day number
* Current moon phase (graphic)
* Quick add buttons (or just one generic add button):
    * Menstruation start date
    * Menstruation end date
    * Signs/symptoms
    * Event
* Notifications/reminders:
    * Upcoming dates (date of next):
        * Ovulation
        * Menstruation
    * Take contraception
    * Take BBT (alert)
* User's personalized calendar view (as calendar or cycle view; full cycle at a glance)

**3. User profile page:** 
* User's name
* User's goal (contraception, conception, cycle regulation)
* Stats about user's cycle:
    * Typical cycle length
    * Typical flow length
    * Frequently reported symptoms
* Notifications/reminders/date of next upcoming phase

**4. Day view (view a specific date):** 
* Show current date, moon phase
* Show current phase and cycle day number
    * Menstrual phase: day 0-5
    * Follicular phase: day 5-9
    * Ovulatory phase: day 10-16
        * Ovulation: day 14
    * Luteal phase: day 17-28
* Show date of next upcoming phase 
* User can log events, signs, and symptoms
    * Events: 
        * Encounter with sperm:
            * With or without protection (do not ask about protection if goal is conception)
        * Pregnancy test result
        * Basal Body Temperature (BBT)
        * Mid-cycle ovulation pain
        * Spotting/breakthrough bleeding
    * Signs/Symptoms:
        * Mood swings
        * Cramps
        * Headache
        * Bloating
        * Fatigue
        * Pimples
    * Scales (collect points of data then display on chart):
        * BBT chart (important feature!)
        * Flow (light, moderate, heavy)
        * Cramps (none, light, moderate, heavy)
        * Libido (low, moderate, high)
        * Mood (depressed, sad, numb, irritable, angry, sensitive, happy, excited, manic)
    * Notes (user can enter notes to themself)

**5. About:** 
* How to use
* Help (FAQs, search)
* Contact (help, feedback)


## 3. Data Model

1. Model 1: **User Info**
    * Fields:
        * Name
        * Email
        * Goal (select: contraception, conception, regulation)
        * Cycle length (number; default = 28 days)
        * Flow length (number; default = 5 days)

2. Model 2: **Cycle Info**
    * Fields:
        * Cycle start date
        * Menstruation end date
        * Events
        * Signs/symptoms
        * Scales
        * Notes
    * (ForeignKey that references Model 1)

**How to do predicted dates?**
* Menstrual Phase
* Follicular Phase
* Ovulation
* Luteal Phase
* 3 day warning before menstrual phase


## 4. Schedule

1. Milestone #1: 
    * Django and HTML with basic features

2. Milestone #2: 
    * CSS and Javascript

3. Milestone #3: 
    * Create users, testing, debug

4. Milestone #4: 
    * Finishing details, style and aesthetic

5. Milestone #5: 
    * Add features; improve user functionality

**Post-presentation:**    
* Test app on fertility course participants; eventually list in marketplace. 
* Gather feedback from users; make this a community created project; bring on skilled collaborators.
* Features to add: 
    * Guidance on how to manage symptoms and balance hormones (from licensed midwives/fertility experts)
    * Tell user how their cycle lines up with moon phases and explain what that means
    * Improve predictive features (moods, symptoms, charts, scales)
    * iCal/Google cal export/syncing
* Develop inclusive pregnancy app for queer/trans/NB people to track fetal development.


__________________________________________
## NOTES

**Cycle Tracker App:**
* Create user accounts
* Count
* Click on date
* Calendar or circle?
* Python/django libraries to display calendars
* Implement django rest

**Inspiration Apps:**
* Kindara
* Clue

**Community Feedback:**
* What features would you like to see in a cycle tracking app?
* What language or specific words do you want to see in the app?
* what type of language, specific words, colors, do you NOT want to see in the app?
* What types of notifications/alerts do you prefer? What do you not like? 