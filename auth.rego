package httpapi.authz
import input
default allow = false



allow {
  input.request_path[0] == 'v1' 
  input.request_path[1] == 'collections' 
  
  input.company == data.items[i].name
  input.request_method == "GET"
}

allow {
  input.request_path == ["v1", "collections"]
  input.request_path == ["v1", "collections", "lakes"]
}

allow {
  input.request_path[0] == 'v1' 
  input.request_path[1] == 'collections' 
  
  input.company == "geobeyond"
  some i 
  data.items[i].name == input.preferred_username 
  data.items[i].everyone == groupname
}

