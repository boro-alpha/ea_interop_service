# (Python) EA Interop Service

The (Python) EA Interop Service is a package developed by [BORO Solutions](https://borosolutions.net/) that exposes parts of the [Sparx EA object model](https://sparxsystems.com/enterprise_architect_user_guide/14.0/automation/theautomationinterface.html) interface.

**This project is currently in development. We are sharing it at this alpha stage to invite comments. We plan to further develop and test it in the future.**

We suggest people use this module as a utility component of bigger projects, since this merely provides an interface to .eap and .eapx files.

## Changes of the 0.1.0-alpha.1 Version

Code has been extended since the previous version.

## Installation

Either:

* Download ZIP code (Code > Download ZIP)
* Or simply add the package route into the Requirements.txt file of your Python project and install the Package
  * **Warning** - requires pywin32 Package to be installed
    * Include this too in your project's Requirements.txt file (See code snip below)

```bash
git+https://github.com/boro-alpha/ea_interop_service.git
pywin32
```

## Current Implementation
The implementation of the EA Automation Interface can be found in ea_interop_service_source.b_code.i_dual_objects.  It is a partial implementation that we add to as the need arises in our other code.  The current state at this alpha stage is as follows:
* [Repository Class](https://sparxsystems.com/enterprise_architect_user_guide/14.0/automation/repository3.html) - key components implemented
* [Project Class](https://sparxsystems.com/enterprise_architect_user_guide/14.0/automation/project_2.html) - key components implemented
* [Stereotype Class](https://sparxsystems.com/enterprise_architect_user_guide/14.0/automation/stereotype.html) - key components implemented
* [Collection Class](https://sparxsystems.com/enterprise_architect_user_guide/14.0/automation/collection.html) - key components implemented
* [Package Class](https://sparxsystems.com/enterprise_architect_user_guide/14.0/automation/package_2.html) - key components implemented
* [Element Class](https://sparxsystems.com/enterprise_architect_user_guide/14.0/automation/element2.html) - key components implemented
* [Connector Class](https://sparxsystems.com/enterprise_architect_user_guide/14.0/automation/connector2_2.html) - key components implemented
* [Diagram Class](https://sparxsystems.com/enterprise_architect_user_guide/14.0/automation/diagram2.html) - key components implemented
* [Attribute Class](https://sparxsystems.com/enterprise_architect_user_guide/14.0/automation/attribute.html) - key components implemented

## Usage Examples

Example code that lists out all stereotypes from a given EA model (.eap or .eapx file).

*Note: Replace the string **drive\folder\ea_model.eap** with the full path to your EA file.*

```python
from ea_interop_service_source.b_code.i_dual_objects.i_dual_repository import IDualRepository
from ea_interop_service_source.b_code.processes.i_dual_repository_creation_result_getter import \
    get_i_dual_repository_creation_result
from ea_interop_service_source.b_code.return_results.i_dual_repository_creation_result_types import \
    IDualRepositoryCreationResultTypes

ea_project_filename = \
    r'drive\folder\ea_model.eap'

i_dual_repository_creation_result = \
    get_i_dual_repository_creation_result(
        ea_project_filename=ea_project_filename)

print(
    i_dual_repository_creation_result.i_dual_repository_creation_result_type)

i_dual_repository_creation_failed = \
    i_dual_repository_creation_result.i_dual_repository_creation_result_type != \
    IDualRepositoryCreationResultTypes.SUCCEEDED

if i_dual_repository_creation_failed:
    exit(
        -1)

i_dual_repository: IDualRepository = \
    i_dual_repository_creation_result.i_dual_repository

count_of_stereotypes = \
    i_dual_repository.stereotypes.count

for index in range(0, count_of_stereotypes):
    stereotype = \
        i_dual_repository.stereotypes.get_at(
            index=index)

    print(
        stereotype.name)

i_dual_repository.exit()
```

## Documentation

#### Background

The Agile Manifesto prefers “working software over comprehensive documentation”. Robert C. Martin, one of the original authors of the Agile Manifesto, is also the author of the book Clean Code.  

In this book, he makes a strong case for code being self-documenting: saying things such as "always try to explain yourself in code." 

He suggests that the goal of every programmer should be to write code so clean and expressive that code comments are unnecessary. 

When a programmer writes a comment, it will usually mean that they have failed to write code that was expressive enough. At the extreme, he suggests, maybe a little rhetorically, that "comments are always failures".

#### The BORO documentation policy

To aim to write code so clean and expressive that code comments are unnecessary. 

## Contributing

This package doesn't allow external contributors.

## Liability and Warranty

This code is provided as-is and without warranty.

Under no circumstances will the developers be liable for any incidental, consequential, or indirect damages including but not limited to lost or damaged data, revenue loss, economic loss, or commercial loss arising out of the use of this code.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements

This work was carried out in collaboration with two projects.

Firstly, this work was supported by the UK National Digital Twin programme of the Digital Framework Task Group, which is, in turn, supported by the Department for Business, Energy & Industrial Strategy, the Construction Innovation Hub, and the Centre for Digital Built Britain.

And secondly, this work was supported in the project ‘Digital Twins in Construction: Towards an Ontological Model Development and Integration Framework’ carried out by the Centre for Digital Business Research (University of Westminster, UK) and funded via the Transforming Construction Network Plus. The Transforming Construction Network Plus is funded by UK Research and Innovation (UKRI), an investment supported by the Industrial Strategy Challenge Fund (ISCF).