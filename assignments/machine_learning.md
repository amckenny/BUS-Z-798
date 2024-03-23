# Assignment 11: Machine Learning

Create a new Word document in your assignments folder called ***assignment_11.docx***. In this document, document your answers to the questions below. Include output/figures from your analyses as needed to support your answers.

# To prepare the assignment environment:
1. Place this file in your Quartz HPC folder.
    1. Preferably in a folder in your Slate drive (if you have one).
    2. In your home folder if you do not have a Slate drive.
2. Open a terminal window in the directory where you placed this file.
    1. Ideally the terminal window will be from the "Interactive Job" icon on Research Desktop (it will be faster).
    2. It's possible to do this from a normal terminal window, but it will be slower.
3. Type `bash prepare_ml_asst_environ` - This will set up your environment for the assignment.
    1. This will take a few minutes to run.
    2. It will create a subfolder called `z798_ml_assnmt` in the directory where you ran the command.
    3. It will download the necessary Python packages and files for the assignment.
    4. When it is done, it will print out a message saying it is done and give you next steps (which will be repeated below)
4. If you're in an "Interactive Job" terminal, type "exit" to relinquish the node.

# To get the assignment going:
1. Open a terminal window (preferably **not** from the "Interactive Job" icon on Research Desktop because we need a GPU node, not a compute node).
2. Navigate to the `z798_ml_assnmt` folder you created in the previous section.
3. Type `srun -p gpu -A c00697 --x11 --gpus-per-node v100:1 --cpus-per-task 16 --mem 32G --time 0-03:00:00 --pty bash` to get a GPU node.
    1. You may have to wait a bit for a GPU node to become available if they are all in use.
4. Once you have a new prompt, type `bash launch_assignment` to start the assignment.
    1. This will start a Jupyter notebook server.
    2. You'll see a lot of text show up, that's to be expected - it's the server starting up.
    3. When it's done, it will print out a URL that you can copy and paste into your web browser (if it doesn't automatically open for you).
5. In Jupyter Lab (within Firefox), you'll see a file on the left called "machine_learning.ipynb" - open it.
6. Follow the instructions in the notebook to complete the assignment.
    1. It works a lot like Google Colaboratory; however, it's running on Quartz HPC.
    2. You can run the cells in the notebook by clicking on them and pressing Shift+Enter OR by clicking the "Run" button at the top of the notebook (looks like a play/sideways triangle button).
    3. You can run *all* the cells at once by clicking the "Fast-Forward" button at the top of the notebook (looks like two triangles pointing right)... but I don't recommend that
    4. You may see some warnings pop up when you run the cells - that's okay... I wasn't able to resolve all of the HPC issues, but they shouldn't affect the assignment.
7. When you're done, close the tab in your web browser.
8. Go back to the terminal window where you launched the Jupyter notebook server and press Ctrl+C to stop the server.
9. Type `exit` to leave the GPU node.
10. You can now close the terminal window. You've just used the HPC to run machine learning models!


After completing the assignment, answer the following questions:

1. Compare the results from the dictionary-based approach to the supervised machine learning approaches. Which ones outperformed? Why do you think that is?
2. How did you do when you manually fine-tuned the rules-/dictionary-based and supervised machine learning models? How accurate were you able to get them? How did the grid search approach help you in fine-tuning the supervised machine learning models?
3. In organizational research, we examine multiple different forms of reliability and validity. How does this compare to the way machine learning models are evaluated? What are the implications of these differences for organizational research?
4. Were you able to find any topic model solutions that produced interpretable results? If so, what were they? If not, why do you think that is?

### When finished and ready to submit:
1. Save your file
2. Commit and push it to your GitHub repository.
3. Verify that the file appears in your GitHub repository and looks correct.
4. Create an issue with the submitted label in your GitHub repository and assign it to me.

*If you do not recall how to do this, revisit the assignment from [week 1](./workflows_resources.md)*

### If concerned regarding privacy in putting your name in the GitHub-uploaded assignment: send me an email with the assignment attached with your name in the assignment so I can grade it.

[Home](../README.md)
