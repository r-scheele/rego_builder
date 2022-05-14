allow {
  input.request_method == "GET"
  input.request_path == [""]
}

allow {
  input.request_method == "GET"
  input.request_path == ["static", "img"]
}

allow {
  input.request_method == "GET"
  input.request_path == ["static", "css"]
}

allow {
  input.request_method == "GET"
  input.request_path == ["collections"]
}

allow {
  input.request_method == "GET"
  input.request_path == ["collections", "obs"]
  input.company == "geobeyond"
  some i 
  data.items[i].name == input.preferred_username && data.items[i].groupname == everyone
}

