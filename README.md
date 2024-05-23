# git Simplified 'Voorraad' link display in header for logged-in users.

pen_spark



# Improvements
# Wat moet er nog gebeuren? To do hieronder
## Notes
### views.py
- could be interesting to only return notes from the location of the login employee (not yet possible need to create the employee table first)
- create a new view to update a specific note
### model.py
- refactor the str method to use f-strings
- add a foreign key field for Employee

## Employee
- create an employee app

### models.py
- position should be a list of position, (choices for the Charfield), look at the sleeping bag models to see how to do it 

## Create Landing page
In wastraat create all the views use the url in Wasstraat to point to my view function for the landing page. Next create a html template this template should be put in notes/templates/notes

Create two templates one for registration one for the landing page. 
    Landing page should be protected 
    if not redirect to register view 
    given your authentication staus either directed to login passworpage (here you will be given the option to register instead) or to the landing page)


## Particpant
### models.py
- unicity check for date of birth, first_name and last_name combination
### views.py and participant_details
- write a custom jinja function to maange more thatn 2 sleeping bads and conditionnaly render the swap button
## Sleeeping Bag
## models.py
- last_washing_cycle should be updated only when is_washed go from false to true
## forms.py
- add last_washing_cycle as a read_only field




