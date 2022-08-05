Project has 3 layers

1. Controller : Receives request from client,processes data and calls Service Layer
2. Service    : Implements business logic and call dao layer to perform db operations
3. DAO        : Interacts with Databse(postgrsql) and performs CRUD operations
