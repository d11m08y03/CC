# Git
Git is like a time-machine for your code. It lets you save snapshots, travel back in time 
and create alternate universes (branches). Perfect when the intern accidently deletes 
half the codebase.

## Git Installation
### Windows 
1. Download Git from [git-scm.com](https://git-scm.com/download/win).
2. Run the installer and follow the setup wizard.

### MacOS
1. Use Homebrew:  

   ```bash
   brew install git
2. Alternatively, install Xcode Command Line Tools:

   ```bash
    xcode-select --install
### Linux
1. Debian / Ubuntu:  

    ```bash
    sudo apt update
    sudo apt install git
2. Fedora / RHEL:

    ```bash
    sudo dnf install git
3. Arch:
    ```bash
    sudo pacman -S git 
## Basic Git Commands
1. **Initialise a Repository**

To create a new Git repository in your current folder:

```bash
git init .
```

Think of a repository as a directory or folder for your project. Git will track and record
every version of your code in that directory, allowing you to revisit past states,
collaborate with others and manage changes easily. Repositories can be 
local (on your computer) or remote (on platforms like GitHub).

2. **Check Status**

```bash
git status
```
This is like an audit report for your project. It shows which files you've changed,
which are ready to be committed, and if there are any new files Git hasn't noticed yet.

3. **Add or Stage Changes**
```bash
git add <file>
```
This stages changes, preparing them to be included in the next commit. 
It tells Git which files to track and save.

4. **Commit Changes**
```bash
git commmit -m "Your commit message"
```

This saves your staged changes with a message, creating creating a 
snapshot of your project at that point in time. It is generally
a good idea to briefly describe what you changes you made in the
commmit message.

5. **View History**

To display the commit history of the repository:

```bash
git log
```

6. **Create a branch**
```bash
git branch <branch-name>
```
A branch in Git is like a parallel version of your project. It lets you work on 
different features or fixes without affecting the main project, and you can merge
changes back later.

7. **Switch Branch**

To change to a different branch:

```bash
git checkout <branch-name>
```

8. **Clone a Repository**

To clone or download a git repo:

```bash
git clone <repository-url>
```

9. **Push changes**

To send your commits to a remote repository:

```bash
git push origin <branch-name>
```

10. **Pull changes**

To fetch and merge changes from the remote repository:

```bash
git pull
```

Hello World!