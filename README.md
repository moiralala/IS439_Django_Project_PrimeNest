# PrimeNest -- Discover Your Ideal Apartment

## About Project

**PrimeNest** is a centralized platform that streamlines housing transactions between apartments near educational institutions and students. Currently, while each housing agency operates its own website, there's a notable lack of a unified portal that aggregates multiple apartment listings specifically tailored for students residing near Champaign. 

To address this gap, PrimeNest was developed to feature apartments from various agencies, enabling **tenants** to compare prices, locations, reviews, and ratings seamlessly. Additionally, the platform provides **agencies** with tools to display their profiles, post and manage listings, including the ability to adjust timings and pricing effectively.

## Prepare the Environment (Optional)

First, ensure that you have Python and pip installed on your system. Then, open your terminal or command prompt and run the following command:

```bash
pip install -r requirements.txt
```

## Run the project

This command will start the Django development server.

```bash
python manage.py runserver [Port Number]
```

## [Sample of User Interface](https://github.com/moiralala/IS439_Django_Project/tree/main/wang_chenzhao_final_project/doc/UI_PrimeNest.png)
![UI_PrimeNest.png](wang_chenzhao_final_project%2Fdoc%2FUI_PrimeNest.png)


## Authentication and Permissions

To support diverse user needs, PrimeNest implements a structured authentication and permission system. We categorize our users into several groups based on their roles and responsibilities within the platform:

1. **SuperUser**: Full access across all functions, capable of viewing and managing all aspects of the platform.
2. **ci_agency**: Agency staff can view, add, change, and delete their agency details and manage listings extensively including creating, updating, and deleting apartments, applications, and availability data.
3. **ci_user**: Typical tenants who can view agency, apartment, and application data. They can apply for apartments but cannot alter agency or apartment listings.
4. **ci_viewer**: Individuals who can view listings and details but cannot make changes or apply, suitable for users just browsing.
5. **tenant**: Similar to ci_user, tenants can view apartments, apply, and rate or review them based on their experience.
6. **agency**: Users belonging to an agency with rights to manage their listings and data.
7. **coworker**: An internal role for users assisting agencies in managing operations without full administrative rights.

This system ensures that each user interacts with PrimeNest in a way that respects their data access needs and security levels. Here is a detailed view of the permissions assigned to each group:

- **ci_user**: Primarily has view permissions.
- **ci_agency**: Can view, add, change, and delete entries related to agency operations and apartment management.
- **ci_viewer**: Restricted to viewing all data without any modification rights.


### [User Groups of PrimeNest](https://github.com/moiralala/IS439_Django_Project/tree/main/wang_chenzhao_final_project/doc/users_for_PrimeNest.png)
![users_for_PrimeNest.png](wang_chenzhao_final_project%2Fdoc%2Fusers_for_PrimeNest.png)

### [Permissions for user Groups of PrimeNest](https://github.com/moiralala/IS439_Django_Project/tree/main/wang_chenzhao_final_project/doc/users_and_user_permission_for_PrimeNest.jpg)
![users_and_user_permission_for_PrimeNest.jpg](wang_chenzhao_final_project%2Fdoc%2Fusers_and_user_permission_for_PrimeNest.jpg)


## Testing Instructions

The test data has been integrated into the project. For testing purposes, it is recommended to log in as the superuser, labeled as **'tester'.**

## Detail Information

For additional information, please refer to the ‘doc’ folder, which includes details on the UML diagrams and table designs.

### [Table Design](https://github.com/moiralala/IS439_Django_Project/tree/main/wang_chenzhao_final_project/doc/Tables_PrimeNest.pdf)
This pdf includes 9 tables of this project.


### [UML](https://github.com/moiralala/IS439_Django_Project/tree/main/wang_chenzhao_final_project/doc/UML_PrimeNest.png)
![UML_PrimeNest.png](wang_chenzhao_final_project%2Fdoc%2FUML_PrimeNest.png)

