# Assignment 6: Text Analysis II

Create a new Word document in your assignments folder called ***assignment_6.docx***. In this document, document your answers to the questions below. Include output/figures from your analyses as needed to support your answers.

*Note: Ignore the module number in the Google Colab notebook title/subheadings. Several of these are drawn from materials I use for a different course.*

## Prerequisites

**If you have never used Google Colaboratory or are wholly unfamiliar with Python:** please work through this brief [tutorial](https://colab.research.google.com/github/amckenny/BUS-Z-798/blob/main/notebooks/welcome_to_python_and_colab.ipynb) before starting this assignment. You do not need to complete the 1.3 Practice Exercises or submit anything from this tutorial.

1. Work through the [Text Preprocessing](https://colab.research.google.com/github/amckenny/BUS-Z-798/blob/main/notebooks/text_preprocessing.ipynb) Colab notebook.
2. Copy the code from the big code cell in 5.8 Preprocessing our Corpus into a new code cell. Make the following modifications:
    * Replace the `# Load texts` section with the following:
        ```python
        # Load texts
        texts = [
            {'text_type': 'news', 'text_id': '1', 'text': 'This is a news article about a company.'},
            {'text_type': 'news', 'text_id': '2', 'text': 'This is another news article about a company.'},
            {'text_type': 'news', 'text_id': '3', 'text': 'This is a third news article about a company.'}
        ]
        ```
    * Replace the "text" column data with the first paragraph from each of three news articles of your chosing.
    * Add `display(corpus_df.head())` to the end of the code cell.
3. Before running the code cell, try to predict what the output will look like. Then run the code cell and compare the output to your prediction.
4. Work through the [Dictionary-based analysis](https://colab.research.google.com/github/amckenny/BUS-Z-798/blob/main/notebooks/dictionary_based_analyses.ipynb) Colab notebook for an introduction to dictionary-based analyses.
5. Complete the [dictionary-based analysis assignment workbook](https://colab.research.google.com/github/amckenny/BUS-Z-798/blob/main/notebooks/dictionary_assignment.ipynb). This workbook will guide you through the process of conducting a dictionary-based analysis on a corpus of texts and will be the focus of several questions below.

### Text Preprocessing and Dictionary Analysis Questions:

1. What is the purpose of text preprocessing? Are all text preprocessing steps needed for all analysis tasks? Why or why not?
2. Did the output from the text preprocessing code cell differ from your prediction? How so?
3. What is the purpose of the dictionary-based analysis? What are some of the limitations of this approach?
4. Reflect on the dictionary development process you completed as part of part 5 above. What were some of the challenges you encountered? What would you do differently if you were doing this 'for real'?
5. Take a look at the Excel file created in the dictionary-based analysis code cell at the end of part 5 above. What do these numbers 'mean'? How would you interpret these numbers to someone who is not familiar with the dictionary-based analysis process?
6. How might 'transformers' be used to improve upon what is possible with dictionary-based analyses?

### When finished and ready to submit:
1. Save your file
2. Commit and push it to your GitHub repository.
3. Verify that the file appears in your GitHub repository and looks correct.
4. Create an issue with the submitted label in your GitHub repository and assign it to me.

*If you do not recall how to do this, revisit the assignment from [week 1](./workflows_resources.md)*

### If concerned regarding privacy in putting your name in the GitHub-uploaded assignment: send me an email with the assignment attached with your name in the assignment so I can grade it.

[Home](../README.md)
