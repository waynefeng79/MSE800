# MSE800 Assessment2 Requirements
## Functional Requirements
### User account
- User can register to the system with email and password, and then login to the system with the email and password.
- After login, a unique access token for the user will be returned for other APIs access.
### User favourate routes
- User can configure his/her own favourate routes.
* Full list of routes can be retrieved from the server and user may filter them by keyword to ease the selection.
* User can also find nearby routes to opt. Those routes stop at nearby stops of user current position. 
- Once the route are selected, only transport information for those routes (stops and shapes) will be shown on the user interface.
- The selected favourate routes can be saved and retrieved back next time login.
### Realtime AT information
- User may see the Auckland map around his/her current position, zoom in/out the map or move it to other places.
- User may see the highlighted selected route in both directions on the map.
- User may see the running vehicles on selected route.
- User may click on the stop and see the estimated departure time for the coming 3 vehicles on the route.
- User may click on the vehicle to see detailed information of the vehicle.
- User may see other alert information on the selected routes in a status window beside the map.
## Non-functional Requirements
### Performance (network in low bandwidth < 10MBps)
- The UI response should be within 0.5 second to create and login a user account.
- The UI response should not freeze for more than 1 second during zoom in/out and stop info on click, applying to 
- The UI response should be within 1 second to show all the stops and shapes once route selected.
### Reliability
- The application must maintain a 99.9% uptime.
- AT GTFS feeds must be fetched in time to avoid service unavailable.
- All functions should contain unit tests and functional tests on real data. New release must pass all unit tests and functional tests before launch.
### Security
- All the API except user register and login should be accessed via an access token.
- Secret key for access token genenration should be updated regularly.
- No user privacy data should be stored in server including his/her current position to comply with protection principles of Te Tiriti.
### Usability
- The application user interface must adapt natively to mobile or desktop devices.
- The application must support characters for different languages to comply with partnership, participation principles of Te Tiriti.
### Maintainability
- The application should be scalable for various user amount. Frontend, backend, database, redis should be easily to deploy on a single server or multiple servers.
- Database model change should be easily migrated to existing database.
