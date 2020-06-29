##Task 4
Day-1
Q) HOW GITWORK FLOW WORKS
->It consists of four main elements:
Workspace [Working directory]
Index [Stage]
Local Repo.
Remote Repo

->Git --commit [URL] creates a local copy of repo in the workspace
-->Add (-u). This command is used to add a file which is in the workspace to index, now we can call that the file is 'staged'
-->Commit.This command will transfer all the staged files to the local repo.
\\ We can  use commit -a also, it will do both the works with a single command all at once
-->Push. This commands 'pushes' the content in the local repo to the remote remote. At this point all the changes all visible to whom soever has the access to the repo.
Now if we want to get the files to the repository instead of commiting.The workflow will be as follow-
-->Fetch.This command will fetch the content from remote repo to local repo.
-->Git merge.This command will be used to fetch the contents from local repo to the workspace, Thus all the changes made in remote repo will be visible in the workspace
\\ Pull command can be used to directly fetch the content from remote repo to local workspace

C Is it possible to do a git commit before git add . if you have made any changes? Explain why?
-->NO, as the git add command adds a change in the working directory to the staging area,changes are not actually recorded until you run git commit .

D Why is git diff used?
-->git diff is a multi-use Git command that when executed runs a diff function on Git data sources. These data sources can be commits, branches, files and more. ... The git diff command is often used along with git status and git log to analyze the current state of a Git repo.
E 
E
-->YES, newer versions of git do allow us to have an empty messages

Repo Link

https://github.com/kushagra-18/Football


TASK-2
Q1)
-->Git  is a distributed version-control system for tracking changes in source code during software development. It is designed for coordinating work among programmers, but it can be used to track changes in any set of files. Its goals include speed, data integrity, and support for distributed, non-linear workflows.

Git was created by Linus Torvalds in 2005 for development of the Linux kernel, with other kernel developers contributing to its initial development. Its current maintainer since 2005 is Junio Hamano. As with most other distributed version-control systems, and unlike most client–server systems, every Git directory on every computer is a full-fledged repository with complete history and full version-tracking abilities, independent of network access or a central server.

GITHUB-->GitHub is a for-profit company that offers a cloud-based Git repository hosting service. Essentially, it makes it a lot easier for individuals and teams to use Git for version control and collaboration.
GitHub’s interface is user-friendly enough so even novice coders can take advantage of Git. Without GitHub, using Git generally requires a bit more technical savvy and use of the command line.
GitHub is so user-friendly, though, that some people even use GitHub to manage other types of projects – like writing books.
Additionally, anyone can sign up and host a public code repository for free, which makes GitHub especially popular with open-source projects.
 Q2) Why github is so popular
-->Github has a very intuitive and user-friendly UI/UX, and integrations have been well implemented for many other productivity-enhancing services and version control software, in particular, GIT. 
-->Public APIs. These allowed others to build upon their work.
-->Open, clear communication. One of the things that set GitHub apart was its support. Even if they had some bigger issues they would communicate about those clearly

Q3)
-->Gitlab
-->BitBucket
-->SourceForge
-->AWS

Q4)
a)Fork-->A fork is a copy of a repository that allows you to freely experiment with changes without affecting the original project. A forked repository differs from a clone in that a connection exists between your fork and the original repository itself. In this way, your fork acts as a bridge between the original repository and your personal copy where you can contribute back to the original project using Pull Requests.
b)Cloning-->Cloning a GitHub repository creates a local copy of the remote repo. This allows you to make all of your edits locally rather than directly in the source files of the origin repo. Here’s how to clone a GitHub repository.

// The main difference is forking is done on github and cloning is done on git

b) Branches-->in layman's term we can say that git branches are individual projects within a git repository...all the branches are independant of each other. There is default 'Master' branch in git. Once we have made changes to a project we can merge that particular branch to the master branch. It is used mainly to reduce redundancy in the project
c) PR--> PR stands for pull request, A pull/merge request is submitted when you’ve worked on some code from a particular branch and want to inform the others of the changes you’ve made. A person/people can be assigned to review and subsequently approve the request before your changes can be incorporated into the branch. Users can give their contributions in the world of open source projects.

HOW TO PERFORM PULL REQUEST
Fork the Repository-->Clone the Repository-->Create a new branch [ master branch may also be used]-->commit ur changes localy-->Update ur local repo-->push the changes-->create the PR on github

d)Yes, we can actually delete the master branch but first we have to create a new branch and make it the default branch otherwise its not possible
e) Using Gitbash
    deleting locally--> git branch -d <branch>
    deleting remotely-->git push <remote> --delete <branch>
     
Links
Forked Repo-->https://github.com/deepak2431/gitseries/pull/1
PR from Branch-->https://github.com/kushagra-18/Online_intern/pull/1
