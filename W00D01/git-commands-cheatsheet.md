## Installing git
    - https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
## Commands
    - git -version
    - Initializing
        - git init
    - Staging files
        - git add file_name.py
        - git add file_name1.py file_name2.py
        - git add *.py
        - git add .
    - Status
        - git status
        - git status -s
    - Committing
        - git commit -m “message”
        - git commit
    - Removing files from working directory and/or staging
        - git rm file_name.py
        - git rm —cached file_name.py
    - History
        - git log
        - git log —oneline
        - git log —reverse
    - Unstaging
        - git restore --staged file.py (can also use multiple files, *.py, or .)
    - Viewing commits
        - git show 921a2ff # Shows the given commit
        - git show HEAD # Shows the last commit
        - git show HEAD~2 # Shows commit 2 steps before last commit
    - branches
        - git branch bugfix # Creates a new branch called bugfix
        - git checkout bugfix # Switches to the bugfix branch
        - git switch bugfix # Same as the above
        - git switch -C bugfix # Creates and switches
        - git branch -d bugfix # Deletes the bugfix branch
    - cloning
        - git clone url
    - syncing
        - git fetch origin master # Fetches master from origin
        - git fetch origin # Fetches all objects from origin
        - git fetch # Shortcut for “git fetch origin”
        - git pull # Fetch + merge
        - git push origin master # Pushes master to origin
        - git push # Shortcut for “git push origin master”
    - remote
        - git remote # Shows remote repos
        - git remote add upstream url # Adds a new remote called upstream
        - git remote rm upstream # Remotes upstream

## Setting up ssh login
    - https://www.youtube.com/watch?v=X40b9x9BFGo
    - more secure than pw