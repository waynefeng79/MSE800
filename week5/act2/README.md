# Explain the below usecase diagram (figure 6.2)
The use case diagaram shows a sales system. It defines many actors who interacts with the system.
- 2 external users (Cashier, System Administrator)
- 5 external systems (Sales Activity System, Payment Authorization Service, Tax Calculator, Accounting System, HR System)
Main business use cases are defined as follows
- Process Sale
- Process Rental
- Cash In
- Handle return
Auxiliary use cases includes
- Analyze Activity
- Manage Security
- Manage Users

# Provide two recommendation to improve it
- Payment Authorization Service is not a real external user. Need to use same notation as other system actors.
- Too many use cases and actors are defined in same diagram. Better to separate in multiple diagrams.
- Combine "Cash in" and "Handle Returns" as a single "Process Cash" which should be included by "Process Sale" and "Process Rental"
