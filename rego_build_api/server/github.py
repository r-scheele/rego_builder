from git import Repo

repo = Repo("/Users/Abdulrahman/code/opal-policy-example")


# write the file
# update the repo


repo.remotes.upstream.pull('master')