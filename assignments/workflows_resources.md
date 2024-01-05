# Assignment 1: Research Workflows and Resources

## Step 1 - Sign up for a GitHub account (if you don't already have one)

1. Create a GitHub Account:
    * If you want to use a public GitHub site, navigate to [https://www.github.com](https://www.github.com). It's less 'private' but it's easier for working with coauthors at multiple institutions and will be available to you after you graduate.
    * If you want to use IU's 'enterprise' GitHub site, navigate to [https://github.iu.edu](https://github.iu.edu/). (More difficult to work with coauthors at other institutions and you'll lose access to this once you graduate, but it's more private.)
2. If using github.com:
    * Click the sign up link and follow the instructions to create a GitHub account
3. If using github.iu.edu:
    * Click the "Sign in with IU Login" button
    * Log in with your IU credentials
    * Click the "Authorize" button
<br><br>
## Step 2 - Create your BUS-Z 798 GitHub repository and share it with me

[![Watch the video](https://img.youtube.com/vi/_AkJIH5MD_Y/maxresdefault.jpg)](https://youtu.be/_AkJIH5MD_Y)

*Note that I created this video for a different course, so the repository name is different. The steps are the same, though.*

1. Create a repository called ***BUS-Z-798***
2. Share the repository with me ***amckenny@iu.edu***
<br><br>

## Step 3 - Clone your new GitHub repository to your local machine and add a file

The way you do this will depend on your operating system and how 'technical' you want to get. If you like dragging-and-dropping things rather than using a terminal/command-line interface, you may prefer to use the [GitHub Desktop application](https://desktop.github.com/). Here is a video on how to clone a repository using GitHub Desktop:<br>
[![Watch the video](https://img.youtube.com/vi/PoZNIbs_wx8/maxresdefault.jpg)](https://www.youtube.com/watch?v=PoZNIbs_wx8)

*Note: if using IU's github, you'll need to specify "Github Enterprise" not "Github.com" when selecting a repository to clone.*

If you're comfortable with the terminal/command line interface, you can use the lighter-weight [git SCM](https://git-scm.com/downloads) instead. Here is a video on how to clone a repository using git SCM:<br>
[![Watch the video](https://img.youtube.com/vi/EhxPBMQFCaI/maxresdefault.jpg)](https://www.youtube.com/watch?v=EhxPBMQFCaI)

*Note: The exact procedure changes slightly from Windows/Mac/Linux. This video shows the Windows process.*

1. Clone your new BUS-Z-798 repository to your local machine.
    * Where you save it on your hard drive is up to you, but make sure to remember what folder you put it in!
2. Create a new folder in your local repository called ***assignments***
3. Place a new (empty, at the moment) Word Document in the assignments folder called ***assignment_1.docx***
<br><br>
## Step 4 - Populate your assignment_1.docx file with the assignment contents

1. Open the ***assignment_1.docx*** file in Word
2. Give the document a normal assignment heading including
    * Your name (if you are concerned with using your name on GitHub, leave your name off of the version submitted to GitHub and email me a copy of the document with your name in it so I can grade it)
    * "BUS-Z 798 - Assignment 1"
3. Add a section header entitled "Disease Stigma"
    * Visit: [This paper's github repository](https://github.com/arsena-k/disease_stigma)
    * include in this section the following information:
        * On what date did the authors create the repository? [Hint](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits#using-the-file-tree)
        * On what date was the last commit entitled 'v1' made? [Hint](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits#using-the-file-tree)
        * What changed in the commit entitled 'fixed typo'? [Hint](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits#using-the-file-tree)
4. Add a section header entitled "Kiley's CARMA repository"
    * Visit: [Jason Kiley's CARMA repository](https://github.com/jtkiley/carma_python)
    * include in this section the following information:
        * How many 'Releases' are there? [Hint](https://docs.github.com/en/repositories/releasing-projects-on-github/viewing-your-repositorys-releases-and-tags)
        * What was the title of the main README.md file for the v1.0.0 release? [Hint](https://docs.github.com/en/repositories/releasing-projects-on-github/viewing-your-repositorys-releases-and-tags)
        * How many files have changed between the v1.0.0 and v2.0.0 releases? [Hint](https://docs.github.com/en/repositories/releasing-projects-on-github/comparing-releases)
5. Save the file
<BR><BR>
## Step 6 - Upload the assignment to the github server

1. Commit the new folder and file to your local repository
    * If using GitHub Desktop, you can do this by:
        * Typing `Added assignment_1.docx` in the "Summary" box in the bottom left corner of the application, then
        * clicking the "Commit to main" button in the bottom left corner of the application
    * If using git SCM, you can do this by typing `git commit -m "Added assignment_1.docx"` in the terminal/command line interface.
    * *Note: you can replace the message with whatever you want, but it's good practice to make it descriptive of what you did.*
2. Push the new folder and file to the github server
    * If using GitHub Desktop, you can do this by clicking the "Push origin" button in the top right corner of the application
    * If using git SCM, you can do this by typing `git push` in the terminal/command line interface.
3. Check that the file is now on the github server by visiting your repository on the github website


## Step 6 - Create an 'Issue' with a 'submitted' label

[![Watch the video](https://img.youtube.com/vi/QqYxxX0nB6s/maxresdefault.jpg)](https://youtu.be/QqYxxX0nB6s)

*Note that I created this video for a different course, so the repository/file names are different. The steps are the same, though.*

1. In the Issues tab create the ***submitted*** label
2. Create a new issue called ***Assignment 1 Submission***
    * with the submitted label
    * with the commit containing your assignment linked in the body
    * assigned to me (***amckenny***)
3. That's it!

### If concerned regarding privacy in putting your name in the GitHub-uploaded assignment: send me an email with the assignment attached with your name in the assignment so I can grade it.