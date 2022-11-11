Feature: Create a new user

Scenario: Create a new user successfully
  Given A user navigates to the url 
  When A user enters the patient's firstName
  When A user enters the patient's middleName
  When A user enters the patient's lastName
  When A user enters  the patient's phoneNumber
  When A user enters  the patient's dob
  When A user enters the patient's address
  And A user clicks on the Add New User button
  Then A patient account should be created with the details provided.

