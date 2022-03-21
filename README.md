# instagram-cleanup
Aim of the project is to write an automated script that unfollows every account that does not follow the main account. (The main account being the account the script is being run for)

### How it works?
- It navigates to the main accounts followers view (forgive me for a lack of better wording, will be updated in time) and creates a list of all accounts, storing them in a `followers` list.
- Moves to the main accounts following view, then checks to see if in the list of following accounts, each account is in the followers list. If it is not in that list, it clicks on the unfollow button.

At least that is how I would like it to work. That is the general usage application guide that I will be following throughout the building of the script untill it is complete.
