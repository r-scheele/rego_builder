allow {
  input.request_method == "GET"
  input.request_path == ["v1", "collections", "obs"]
  input.preferred_username == "dev9ine"
  input.company == data[i].name
}

allow {
  input.request_path == ["v1"]
  input.groupname == "VIEWER"
}

allow {
  input.request_path == ["v1", "collections", ""]
  input.groupname == "GEOCITY_ADMINS"
}

