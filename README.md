# django-cms-model-in-plugin

2014-Jan-10

This is a simple proof-of-concept of using editable models inside a CMS-Plugin in django-cms version 3.0.0.beta3 and, in particular, to aide in the resolution of issues:

* https://github.com/divio/django-cms/issues/2432
* https://github.com/divio/django-cms/issues/2433

To work-around the issue #2432 (above), please apply the manual patch as outlined at the above issue url.


## Installation

To use, add this code base into your project and your settings file, then:

```` python
manage.py migrate path.to.poc
`

Run your project:

```` python
manage.py runserver
````


## Using the Software.

Using the software to aide the resolution of the above-mentioned issues.


### 1. Create some test data

In the administration sidebar, go to the POC app, and add a number of Persons.


### 2. Add the CMS Plugin

On any existing page (or create one first), edit the page in Structure mode and add the plugin "Proof of Concept: Person List".

When you go into Content Mode or into Live Mode, you should see a list of the people you created above.  Note that provided you applied the manual fix for issue #2432, you should be able to double-click on a person's name to edit that Person record, or double-click on the biography "Biography coming soon" to edit the bio.  All is good!


### 3. Modify the Person model

The code used above already includes a work-around for Issue #2433.  This work-around is insufficient because it dictates a specific plugin to be used in the PlaceholderField on the Person model.  In this case, we prepopulate the PHF with a Text Plugin, which is appropriate for a Bio, but in other applications, it would be more appropriate if the user could place any plugin they desire into the PHF.

1. Go to the Person model and comment out or delete the save() method.
1. Restart the server (it should do this automatically, of course)
1. Add a new Person record.
1. Go back to the page where you added the CMS Plugin.

Note that you should see the new person in your list. However, there will be no bio field displayed.  If you then go into content mode - where you would normally initially populate a PlaceholderField - there is nothing there you can use to create the biography.

*This is the issue (#2433).*
