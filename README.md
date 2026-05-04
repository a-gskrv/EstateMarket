# Housing Rental Project

## Project Goal

To create a full-featured back-end application for a housing rental system, including property listing management, search functionality, and filtering by various parameters.

---

# Application Functionality Description

## Listing Management

### 1. Create a Listing

The user enters information about the property:

- Title
- Description
- Location
- Price
- Number of rooms
- Property type (apartment, house, etc.)

### 2. Edit a Listing

The user can modify any information in an existing listing.

### 3. Delete a Listing

The user can delete their listing from the database.

### 4. Manage Listing Availability

Switching the listing status (active/inactive) to temporarily hide or make the listing visible again.

---

## Search and Filtering

### 1. Keyword Search

The user enters keywords used to search through listing titles and descriptions.

### 2. Filtering by Parameters

- **Price** — ability to specify minimum and maximum price
- **Location** — ability to specify a city or district in Germany
- **Number of Rooms** — ability to specify a range for the number of rooms
- **Property Type** — ability to select the property type: apartment, house, studio, etc.

### 3. Sorting Results

- Ability to sort by price (ascending/descending)
- By date added (newest/oldest)

---

## User Authentication and Authorization

### 1. User Registration

The user enters their data to create an account:

- Name
- Email
- Password

### 2. Login

Entering email and password to access the account.

### 3. Access Rights Management

- **Tenant** — can view and filter listings
- **Landlord** — can create, edit, and delete their own listings

---

## Booking

### 1. Create a Booking

The user can book accommodation for specific dates.

### 2. View Bookings

The user can view their active and completed bookings.

### 3. Cancel a Booking

The user can cancel a booking before a certain date.

### 4. Booking Confirmation

The landlord can approve or reject booking requests.

---

## Ratings and Reviews

### 1. Leave a Review

A user who rented the property can leave a review and rating for a specific listing.

### 2. View Reviews

Ability to view all reviews for a specific listing.

---

## Additional Functionality

### 1. Popularity Sorting

Sorting by the number of views or reviews.

### 2. Search History

- Saving search keywords — storing keywords used by the user in a separate table
- Displaying popular queries — the most frequently used search queries are shown first

### 3. Listing View History

- Saving views — storing information about each listing viewed by the user
- Displaying popular listings — listings with the highest number of views are shown first

---

## Technical Requirements

- Django — used for developing the main application logic, database management, and API creation
- MySQL — main database for storing listings and user data

---

## Additional Technologies

- Docker — used for application containerization
- AWS — deploy the application in the AWS cloud using services such as:
  - EC2 (virtual servers)
  - and other required services