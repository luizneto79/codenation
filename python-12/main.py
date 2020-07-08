doc = '''
#%RAML 1.0
title: Desafio RESTful API
version: v1
mediaType: application/json

securitySchemes:
    JWT:
        description: Authenticv this to any method that needs a valid JWT to be set.
        type: x-{other}
        settings:
            signatures: ['HS256']
        describedBy:
            headers:
                Authorization:
                    Authorization:
                        description: X-AuthToken
                        type: string
                        required: true
            responses:
                401:
                    description: Authentication problem (JWT not set or expired)
                    body:
                    type: common.Error
            settings:
            roles: []

types:
    Auth:
        type: object
        discriminator: token
        properties:
            token: string
        example:
            token: asd3424352wdzda434234
  
    Agent:
        type: object
        discriminator: name
        properties:
            name: string
            status: boolean
            environment: string
            version: string
            address: string
            user_id: integer
        example:
            agent_id: 1
            name: Chrome
            status: True
            environment: PROD
            version: 1.0
            address: 200.10.1.1
            user_id: 1
            
    Event:
        type: object
        discriminator: level
        properties:
            level: string
            payload: boolean
            shelve: boolean
            shelved: boolean
            agent_id: integer
            date: datetime-only
            agent_id: integer
        example:
            event_id: 1
            level: CRITICAL
            payload: asdfgh asdfgh
            shelve: 1
            shelved: 1
            data: 2000-01-01 23:00:00
            agent_id: 1
            environment: PROD
            version: 1.0
            address: 200.10.1.1
            user_id: 1
            
    Group:
        type: object
        discriminator: name
        properties:
            id: integer
            name: string
        example:
            group_id: 1
            name: Admin
            
    User:
        type: object
        discriminator: name
        properties:
            user_id: integer
            name: string
            email: string
            group_id: integer
            last_login: date-only
        example:
            id: 1
            name: Luiz
            email: luizneto79@gmail.com
            last_login: 2000-01-01
            
/auth/token:
    post:
        description: validate token for system access
        body:
            application/json:
                username:
                    type: string
                token:
                    type: string
            
        responses:
            201: 
                body:
                    type: Auth
                    application/json:
                        properties:
                            username:
                                type: string
                            token:
                                type: string
            400:
                description: Bad request or expired an access token
                body: string
                    
/agents:
    get:
        securedBy: JWT
        description: return all agents
        responses:
            200:
                body:
                    type: Agent
    post:
        description: create new agent
        securedBy: JWT
        body:
            application/json:
                example: {
                    "name": "Chrome",
                    "status": True,
                    "environment": "PROD",
                    "version": "1.0",
                    "address": "192.168.13.1",
                    "user_id": 1 
                }
        responses:
            201:
                body:
                    application/json: 
                        type: Agent
            401:
                description: Unauthorized
                body:
                    string
                    
    /{id}:
        get:
            securedBy: JWT
            description: get agent
            responses:
                200:
                    description: get agent
                    body:
                        application/json:
                            type: Agent
                401:
                    description: Unauthorized
                    body:
                        string:
                            example: {
                                "Unauthorized"
                            }
                            
                404:
                    description: Not found
                    boby:
                        string:
                            example: {
                                "Not found"
                            }
                    
        put:
            description: uddate agent
            securedBy: JWT
            responses:
                200:
                401:
                    description: Unauthorized
                    body:
                        string
                404:
                    description: Not found
                    boby:
                        string:
                            example: {
                               "Not found"
                            }
        
        delete:
            description: delete agent
            securedBy: JWT
            responses:
                200:
                401:
                404:
                    description: Not found
                    boby:
                        string:
                            example: {
                               "Not found"
                            }
                
                    
    /{id}/events:           
        get:
            securedBy: JWT
            description: Get event
            responses:
                200:
                    body:
                        application/json: 
                            type: Agent[]
                401:
                    description: Unauthorized
                    body:
                        string
                404:
                    description: Not found
                    body:
                        string
        post:
            securedBy: JWT
            description: create event
            body:
                application/json:
                    type: Event
                201:
                    body:
                        application/json: 
                200:
                    description: OK
                401:
                    description: Unauthorized
                    body:
                        string
                404:
                    description: Not found
                    body:
                        string
        put:
            securedBy: JWT
            description: update event
            body:
                application/json:
                    type: Event
                200:
                    description: OK
                401:
                    description: Unauthorized
                    body:
                        string
                404:
                    description: Not found
                    body:
                        string
        delete:
            description: Delete Event
            securedBy: JWT
            body:
                application/json:
                    type: Event
                200:
                    body:
                        None
                401:
                    description: Unauthorized
                    body:
                        string
                404:
                    description: Not found
                    body:
                        string
                                
/users:
    get:
        securedBy: JWT
        description: get all users
        responses:
            200:
                body:
                    application/json:
                        type: User[]
            401:
                description: Unauthorized
                body:
                    string
            404:
                description: Not found
                body:
                    string
                        
    post:
        description: Create new user
        body:
            application/json:
                type: User
                properties:
                    name:
                        type: string
                    password:
                        type: string
                    email:
                        type: string
                    last_login:
                        type: datetime-only
        responses:
            200:
                body:
                    application/json:
                        type: User
            201:
                body:
                    application/json:
                        type: User
            401:
                description: Unauthorized
                body:
                    string
            404:
                description: Not found
                body:
                    string        
                        
    /{id}:
        get:
            securedBy: JWT
            description: Get User
            responses:
                200:
                    description: OK
                    body:
                        application/json:
                            type: User
                401:
                    description: Unauthorized
                    body:
                        string
                404:
                    description: Not found
                    body:
                        string
        put:
            securedBy: JWT
            description: Update User
            responses:
                200:
                    description: OK
                    boby:
                        null
                401:
                    description: Unauthorized
                    body:
                        string
                404:
                    description: Not found
                    body:
                        string
        delete:
            securedBy: JWT
            description: Delete a user
            responses:
                200:
                    description: OK
                    boby:
                        null
                401:
                    description: Unauthorized
                    body:
                        string
                404:
                    description: Not found
                    body:
                        string

/groups:
    get:
        responses:
            200:
                boby:
                    application/json:
                        type: User[]
                        
    post:
        responses:
            200:
                boby:
                    application/json:
                        type: Group
                        
/groups:
         
    post:
        description: Add new group
        securedBy: JWT 
        body:
            application/json:
                properties:
                    example: {
                        "group_id": 1,
                        "name": admin
                    }
                example: {
                    "group_id": 1,
                    "name": admin
                }
        responses:
            201: 
                body:
                    application/json:
                        properties:
                        example: {
                            "name": admin
                        }
            401:
                body:
                    
    get:
        description: get list all groups
        securedBy: JWT
        responses:
            200:
                body:
                    type: Group[]
            401:
                body:
                    application/json:
                        example: {
                            "message": "UnauthorizedError."
                        }
        
    /{id}:
        get:
            securedBy: JWT 
            description: get especific group
            responses:
                200:
                    description: OK
                    body:
                        application/json:
                            type: Group
                401:
                    description: Unauthorized
                    body:
                        string
                404:
                    description: Not found
                    body:
                        string
        delete:
            securedBy: JWT 
            description: delete especific group
            responses:
                200:
                    description: Delete a group
                    body:
                        null
        put:
            securedBy: JWT
            description: alter especific group
            responses:
                200:
                    description: Update OK
                    body:
                        string 
                401:
                    description: Bad request
                    body:
                        string 
                        
           
'''
