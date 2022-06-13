## Full documentation of the API

### Architecture diagram of the API [Here](https://www.figma.com/file/684S7kO4dPQbbZFZr6xZOn/Rego-builder?node-id=0%3A1)

![Screenshot 2022-06-13 at 09 55 43](https://user-images.githubusercontent.com/67229938/173343113-d51d72b4-84c8-4c3b-8555-af41e59cd2de.png)

### Detailed explanation of commands with examples: what they are and how to use them.

#### 1. input_props_equals
This command has different logic to handle series of equality checks.
- Handling '*' as the wildcard flag
This logic handles all the paths after a particular section. if /collections is supplied as the option, all the routes after it will be allowed e.g allow /collections/obs, allow /collections/test-data/obs, allow /collections/obs.
`allow {
   path = /collections/...
}`
If a particular path parameter is to be exempted, the command matches all other parameters aside the exempted one. e.g allow /collections/obs, allow /collections/test-data/obs, allow /collections/obs. deny /collections/lakes
`allow {
   path = /collections/...
}`
`deny {
   path = /collections/lakes
}`
-  Handling equality check between a property on the request object and a parameter